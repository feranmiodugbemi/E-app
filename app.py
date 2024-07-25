import os
import sys

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)

def create_serverless_structure():
    base_dir = "food_delivery_app-2"
    create_directory(base_dir)

    # Create app structure
    app_dirs = [
        "app/api/v1/endpoints",
        "app/core",
        "app/db",
        "app/models",
        "app/schemas",
        "app/crud",
        "app/services",
        "app/utils",
    ]
    for dir in app_dirs:
        create_directory(os.path.join(base_dir, dir))

    # Create test structure
    test_dirs = [
        "tests/api/v1",
        "tests/crud",
    ]
    for dir in test_dirs:
        create_directory(os.path.join(base_dir, dir))

    # Create main files
    main_files = [
        "app/__init__.py",
        "app/main.py",
        "app/api/v1/router.py",
        "app/core/config.py",
        "app/core/security.py",
        "app/db/session.py",
        "tests/__init__.py",
        "tests/conftest.py",
        ".env",
        ".env.example",
        ".gitignore",
        "requirements.txt",
        "serverless.yml",
        "README.md",
    ]
    for file in main_files:
        create_file(os.path.join(base_dir, file))

    print("Serverless project structure created successfully!")

def create_basic_structure():
    base_dir = "food_delivery_app_basic"
    create_directory(base_dir)

    # Create app structure
    app_dirs = [
        "app/models",
        "app/schemas",
        "app/api/endpoints",
        "app/core",
        "app/services",
    ]
    for dir in app_dirs:
        create_directory(os.path.join(base_dir, dir))

    # Create other directories
    other_dirs = [
        "alembic/versions",
        "tests",
    ]
    for dir in other_dirs:
        create_directory(os.path.join(base_dir, dir))

    # Create main files
    main_files = [
        "app/main.py",
        "app/database.py",
        "celery_worker.py",
        "requirements.txt",
        "Dockerfile",
        "docker-compose.yml",
    ]
    for file in main_files:
        create_file(os.path.join(base_dir, file))

    print("Basic project structure created successfully!")

if __name__ == "__main__":
    choice = input("Which structure do you want to create? (serverless/basic): ").lower()
    if choice == "serverless":
        create_serverless_structure()
    elif choice == "basic":
        create_basic_structure()
    else:
        print("Invalid choice. Please choose 'serverless' or 'basic'.")