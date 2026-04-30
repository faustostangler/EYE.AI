import re
from typing import Final


class PIIScrubber:
    """
    Domain service responsible for masking PHI/PII from clinical records.

    This component acts as an Anti-Corruption Layer (ACL) safeguard, ensuring
    that sensitive data never leaks into vector databases or LLM prompts.
    """

    # Brazilian CPF Pattern (000.000.000-00 or 00000000000)
    IDENTIFIER_PATTERN: Final[re.Pattern] = re.compile(
        r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"
    )

    # Patient Name Heuristic: Capitalized words following 'paciente' or 'paciente:'
    # Handles common Brazilian name connectors (da, de, do, dos, das)
    NAME_HEURISTIC: Final[re.Pattern] = re.compile(
        r"(?i)(paciente:?\s+)([A-ZÀ-Ú][a-zà-ú]+\s+(?:da\s+|de\s+|do\s+|dos\s+|das\s+)?(?:[A-ZÀ-Ú][a-zà-ú]+\s*)+)"
    )

    def clean(self, text: str) -> str:
        """
        Anonymizes text by replacing PII with standardized placeholders.

        Args:
            text: The raw clinical text potentially containing sensitive data.

        Returns:
            The sanitized text with [PATIENT_NAME] and [IDENTIFIER] placeholders.
        """
        if not text:
            return ""

        # 1. Mask Identifiers (CPF)
        text = self.IDENTIFIER_PATTERN.sub("[IDENTIFIER]", text)

        # 2. Mask Patient Names via Heuristic
        # We preserve the 'paciente' keyword to maintain clinical context
        text = self.NAME_HEURISTIC.sub(r"\1[PATIENT_NAME]", text)

        return text
