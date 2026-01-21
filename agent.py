import subprocess
import sys
from pathlib import Path
from ai_helper import apply_ai_fix

def run_tests():
    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )
    return result.returncode, result.stdout + result.stderr

def commit_and_push():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "ci(agent): auto-fix test failure"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    print("▶ Running tests")

    code, logs = run_tests()

    if code == 0:
        print("✅ Tests passed")
        sys.exit(0)

    print("❌ Tests failed")

    fixed = apply_ai_fix(logs)

    if fixed:
        print("🔁 AI applied fix, committing changes")
        commit_and_push()
        sys.exit(1)  # Fail this run, next run will re-test

    print("🚫 No fix applied, stopping pipeline")
    sys.exit(1)
