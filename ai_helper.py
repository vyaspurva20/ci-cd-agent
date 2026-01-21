from pathlib import Path

def apply_ai_fix(error_log: str) -> bool:
    """
    Simulated AI auto-fix logic.
    Returns True if a fix was applied.
    """

    print("🤖 AI analyzing error...")

    # Example case: wrong expected value in test
    if "assert" in error_log and "test_add" in error_log:
        test_file = Path("tests/test_app.py")

        if test_file.exists():
            content = test_file.read_text()

            # Fix common mistake: expected 6 -> expected 5
            fixed = content.replace("assert add(2, 3) == 6", "assert add(2, 3) == 5")

            if content != fixed:
                test_file.write_text(fixed)
                print("🛠 AI fixed test expectation")
                return True

    print("⚠️ AI could not apply fix")
    return False
