from src.domain.compliance.pii_scrubber import PIIScrubber


def test_scrubber_masks_patient_names_and_cpf() -> None:
    """
    REQ: LGPD Compliance.
    Ensures that sensitive patient data is redacted using placeholders.
    """
    raw_text = (
        "O paciente João da Silva, CPF 123.456.789-00, apresenta quadro de cefaleia."
    )

    scrubber = PIIScrubber()
    clean_text = scrubber.clean(raw_text)

    # Assertions to guarantee data protection
    assert "João da Silva" not in clean_text
    assert "123.456.789-00" not in clean_text
    assert "[PATIENT_NAME]" in clean_text
    assert "[IDENTIFIER]" in clean_text
    assert (
        "apresenta quadro de cefaleia" in clean_text
    )  # Clinical context must be preserved


def test_scrubber_is_idempotent() -> None:
    """
    Ensures that multiple passes do not degrade the masked information.
    """
    raw_text = "Paciente: Maria Souza."
    scrubber = PIIScrubber()

    first_pass = scrubber.clean(raw_text)
    second_pass = scrubber.clean(first_pass)

    assert first_pass == second_pass
