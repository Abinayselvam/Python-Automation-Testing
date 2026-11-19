from pathlib import Path

# Current working directory
current_directory = Path.cwd()

print("Current directory:", current_directory)

# Create a path
file_path = Path("test_data") / "users.json"

print("File path:", file_path)

# File name
print("File name:", file_path.name)

# Extension
print("Extension:", file_path.suffix)

# Parent directory
print("Parent:", file_path.parent)