import os
import sys

def deploy():
    print("🚀 Starting deployment...")

    # Create deploy folder if not exists
    os.makedirs("deploy", exist_ok=True)

    # Simulate deployment
    with open("deploy/deployed.txt", "w") as f:
        f.write("Application deployed successfully")

    print("✅ Deployment completed")

def verify():
    print("🔍 Verifying deployment...")

    if not os.path.exists("deploy/deployed.txt"):
        print("❌ Deployment verification failed")
        sys.exit(1)

    print("✅ Deployment verified")

if __name__ == "__main__":
    deploy()
    verify()
