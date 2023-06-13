import sys
from pathlib import Path
from normalize import normalize



CATEDORIES = {"Audio": [".mp3", ".aiff", ".wav"],
              "Video": [".mkv", ".mov"],
              "Documents": [".docx", ".pptx", ".doc", ".txt", ".pdf", ".xlxs"],
              "Images": [".jpeg", ".png", ".svg"],
              "Archives": [".zip", ".rar", ".tar"],
              "Others": [".csv"],
              "Python": [".py", ".json"]}




def move_file(path: Path, root_dir: Path,  categories: str) -> None:
    target_dir = root_dir.joinpath(categories)
    if not target_dir.exists():
        print(f"Make {target_dir}")
        target_dir.mkdir()
    #print(target_dir.joinpath(f"{normalize(path.stem)}{path.suffix}"))
    path.replace(target_dir.joinpath(f"{normalize(path.stem)}{path.suffix}"))





def get_categories(path: Path) -> str:
    ext = path.suffix.lower()
    for cat, exts in CATEDORIES.items():
        if ext in exts:
            return cat
    return "Other"




def sort_folder(path: Path):
    for item in path.glob("**/*"):
        # print(item.is_dir(), item.is_file())
        if item.is_file():
            cat = get_categories(item)
            move_file(item, path, cat)


def main():
    try:
        path = Path("c:/Testfolder")
    except IndexError:
        return "No path to folder"
    
    if not path.exists():
        return "Folder with path {path} don't exist."
    
    sort_folder(path)


if __name__== "__main__":
    print(main())


# parent_folder = Path('C:\\Users\\potap\\Desktop\\Garbage')
# Path.is_dir(parent_folder)
# print(Path.is_dir(parent_folder))
