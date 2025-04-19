import os

folder = "files"  # The folder where your files are located
files = os.listdir(folder)  # Get a list of all files in the folder

for index, file in enumerate(files):
    extension = os.path.splitext(file)[1]  # Get the file extension (e.g., .jpg, .txt)
    new_name = f"renamed_file_{index+1}{extension}"  # Create a new name for the file
    old_path = os.path.join(folder, file)  # Full path of the original file
    new_path = os.path.join(folder, new_name)  # Full path with the new name
    os.rename(old_path, new_path)  # Rename the file

print("✅ All files renamed successfully!")
