from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()


def update_env_variable(key: str, value: str, env_file_path: str = None) -> bool:
    """
    Update or add an environment variable in the .env file.
    
    Args:
        key (str): The environment variable name
        value (str): The value to set
        env_file_path (str): Path to the .env file (defaults to project root .env)
    
    Returns:
        bool: True if the operation was successful
    """
    # Default to project root .env file if no path specified
    if env_file_path is None:
        # Get the project root (2 levels up from src/auth/auth_manager.py)
        project_root = Path(__file__).parent.parent.parent
        env_file_path = project_root / ".env"
    
    variable_line = f"{key}={value.strip()}\n"

    # Read existing .env file content
    existing_lines = []
    if os.path.exists(env_file_path):
        with open(env_file_path, 'r') as file:
            existing_lines = file.readlines()

    # Check if the variable already exists and update it
    variable_found = False
    for i, line in enumerate(existing_lines):
        if line.startswith(f"{key}="):
            existing_lines[i] = variable_line
            variable_found = True
            break

    # If variable line doesn't exist, add it
    if not variable_found:
        existing_lines.append(variable_line)

    # Write back to .env file
    with open(env_file_path, 'w') as file:
        file.writelines(existing_lines)

    return True


def save_token(token: str) -> str:
    """
    Persist the Upstox access token to both environment variables and .env file.
    
    This function saves the provided token to the UPSTOX_ACCESS_TOKEN environment 
    variable for immediate use and writes it to the .env file for persistence 
    across sessions. If the token already exists in the .env file, it will be 
    updated; otherwise, a new entry will be created.
    
    Args:
        token (str): The Upstox access token to be saved. Leading/trailing 
                    whitespace will be automatically stripped.
    
    Returns:
        str: A success message confirming the token has been saved to both 
             the environment variable and .env file.
    
    Note:
        - Creates .env file if it doesn't exist
        - Automatically strips whitespace from the token
        - Overwrites existing UPSTOX_ACCESS_TOKEN if present
    """
    # Save to environment variable
    os.environ["UPSTOX_ACCESS_TOKEN"] = token.strip()

    # Save to .env file using the generic function
    update_env_variable("UPSTOX_ACCESS_TOKEN", token)

    return "Token saved successfully to environment and .env file"


if __name__ == "__main__":
    save_token("nitesh-nandan")
    print(os.getenv("UPSTOX_ACCESS_TOKEN"))
