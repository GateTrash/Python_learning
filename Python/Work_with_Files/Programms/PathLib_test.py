from pathlib import Path
file_path = Path("/Users/a0000/Developer/Git_Repositories/Python_learning/Python/Work_with_Files/files/Article.txt")
directory = Path("test")
directory.mkdir(parents=True, exist_ok=True)
try:
    if directory.dir():
        print(f"{directory} this directory")
except:
    print(f"Error; {directory} This isn't directory")
if file_path.exists():
    if file_path.is_file: print("this is file")
    print(f"{file_path}file found!")
else: print(f"{file_path}File not found")
    