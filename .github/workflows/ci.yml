import subprocess
import sys

def run_tests():
    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    if result.returncode != 0:
        print("❌ Tests failed")
        sys.exit(1)

    print("✅ Tests passed")

if __name__ == "__main__":
    run_tests()
