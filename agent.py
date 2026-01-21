import subprocess
import sys
from pathlib import Path
from ai_helper import ask_ai

def auto_fix_simple_issue():
    """
    Example automatic change:
    Ensure a VERSION file exists.
    """
    version_file = Path("VERSION")

    if not version_file.exists():
        print("🛠 Creating VERSION file")
        version_file.write_text("1.0.0\n")
        return True

    print("ℹ️ No auto changes needed")
    return False


def run_tests():
    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        fix = ask_ai(result.stdout + result.stderr)
        print("AI suggestion:", fix)
        return False

    return True
