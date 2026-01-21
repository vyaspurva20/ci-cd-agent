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

def git_commit_and_push():
    try:
        print("🔄 Pulling latest changes before commit...")
        subprocess.run(
            ["git", "pull", "--rebase"],
            check=True,
            capture_output=True,
            text=True
        )

        subprocess.run(["git", "status"], check=True)
        subprocess.run(["git", "add", "."], check=True)

        subprocess.run(
            ["git", "commit", "-m", "ci(agent): auto-fix test failure"],
            check=True
        )

        subprocess.run(
            ["git", "push"],
            check=True,
            capture_output=True,
            text=True
        )

        print("✅ Auto-fix committed and pushed successfully")

    except subprocess.CalledProcessError as e:
        print("❌ Git operation failed")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        raise

