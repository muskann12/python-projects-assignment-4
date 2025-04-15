import os

folder = "files"  # Jis folder me files hain
files = os.listdir(folder)  # Folder ke andar ke files ki list

for index, file in enumerate(files):
    extension = os.path.splitext(file)[1]  # File ka extension (.jpg, .txt)
    new_name = f"renamed_file_{index+1}{extension}"  # Naya naam banao
    old_path = os.path.join(folder, file)  # Purana path
    new_path = os.path.join(folder, new_name)  # Naya path
    os.rename(old_path, new_path)  # Naam change karo

print("✅ All files renamed successfully!")
