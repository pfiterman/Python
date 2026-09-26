import os
import sys

from azure.identity import DefaultAzureCredential

def get_required_env(name: str) -> str:
    """
    Get a required environment variable.

    If it doesn't exist, ask the user to enter it.
    """
    value = os.getenv(name)

    if not value:
        value = input(f"Enter your {name}: ").strip()

        if not value:
            print(f"Error: {name} is required.")
            sys.exit(1)

    return value
