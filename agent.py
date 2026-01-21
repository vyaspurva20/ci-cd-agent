import subprocess
import sys
from pathlib import Path

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
    print("▶ Running tests")
    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    return result.returncode == 0


if __name__ == "__main__":
    changed = auto_fix_simple_issue()

    if not run_tests():
        print("❌ Tests failed")
        sys.exit(1)

    print("✅ Tests passed")

    if changed:
        print("📌 Code was changed by agent")
