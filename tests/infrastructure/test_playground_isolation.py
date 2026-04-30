import os
import re
import pytest

def test_src_never_imports_from_playground():
    """
    RED TEST: Enforce that the production core (src/) never imports from the experimental playground.
    This protects the Domain integrity from 'dirty' experimentation leaks.
    """
    src_dir = "src"
    playground_dir = "playground"
    
    # Pattern to match 'import playground' or 'from playground import ...'
    import_pattern = re.compile(r"^\s*(?:import|from)\s+" + playground_dir, re.MULTILINE)
    
    violations = []
    
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if import_pattern.search(content):
                        violations.append(path)
    
    assert not violations, f"Architectural Violation: Production files import from playground: {violations}"
