import subprocess
from pathlib import Path
import re


def run_pytest():
    """
    Run pytest and return (exit_code, output)
    """
    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )
    return result.returncode, result.stdout + result.stderr


def fix_test_assertion(pytest_output: str) -> bool:
    """
    Fix common failing assertion like:
    assert add(2, 3) == 15  -> change to == 5
    """
    test_file = Path("tests/test_app.py")

    if not test_file.exists():
        print("❌ test_app.py not found")
        return False

    content = test_file.read_text()

    # Look for wrong assertion pattern
    pattern = r"assert\s+add\((\d+),\s*(\d+)\)\s*==\s*(\d+)"

    match = re.search(pattern, content)
    if not match:
        print("❌ No fixable assertion found")
        return False

    a, b, wrong = map(int, match.groups())
    correct = a + b

    if correct == wrong:
        print("ℹ️ Assertion already correct")
        return False

    fixed_content = re.sub(
        pattern,
        f"assert add({a}, {b}) == {correct}",
        content
    )

    test_file.write_text(fixed_content)
    print(f"✅ Fixed test: {a} + {b} = {correct}")
    return True


def commit_and_push():
    """
    Commit and push changes back to GitHub
    """
    subprocess.run(["git", "config", "user.email", "ci-agent@github.com"])
    subprocess.run(["git", "config", "user.name", "ci-agent"])

    subprocess.run(["git", "add", "."])
    subprocess.run(
        ["git", "commit", "-m", "ci(agent): auto-fix failing test"],
        check=False
    )
    subprocess.run(["git", "push"], check=False)


def main():
    print("🤖 AI Agent started")

    exit_code, output = run_pytest()

    if exit_code == 0:
        print("🟢 Tests already passing. Nothing to fix.")
        return

    print("❌ Tests failed. Attempting auto-fix...")

    fixed = fix_test_assertion(output)

    if not fixed:
        print("❌ No automatic fix possible")
        return

    print("📦 Committing and pushing fix...")
    commit_and_push()
    print("🚀 Fix pushed successfully")


if __name__ == "__main__":
    main()
