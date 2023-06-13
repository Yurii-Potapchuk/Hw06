import sys
import shutil
from pathlib import Path
from normalize import normalize



CATEDORIES = {"Audio": [".mp3", ".aiff", ".wav"],
              "Video": [".mkv", ".mov"],
              "Documents": [".docx", ".pptx", ".doc", ".txt", ".pdf", ".xlsx"],
              "Images": [".jpeg", ".png", ".svg"],
              "Archives": [".zip", ".rar", ".tar"],
              "Others": [".csv"],
              "Python": [".py", ".json"]}




def move_file(path: Path, root_dir: Path,  categories: str):
    target_dir = root_dir.joinpath(categories)
    if not target_dir.exists():
        print(f"Make {target_dir}")
        target_dir.mkdir()
    #print(target_dir.joinpath(f"{normalize(path.stem)}{path.suffix}"))
    path.replace(target_dir.joinpath(f"{normalize(path.stem)}{path.suffix}"))


def unpack_archive(path: Path):
    archive_folder = "Archives"
    ext = [".zip", ".rar", ".tar"]

    for el in path.glob(f"**/*"):  # Обираю цей варіант суто для розширення охоплення пошуку, якщо наприклад якийсь архів не було відсортовано в папку Архів. Логічно що ми передаємо такі само розширення в функцію, але наприклад тут вже можна додати більше розширень задля охоплення більше файлів.
        if el.suffix in ext:
            filename = el.stem
            arch_dir = path.joinpath(path/archive_folder/filename)
            arch_dir.mkdir()
            shutil.unpack_archive(el, arch_dir)
       


def delete_empty_folder(path: Path):

    folders_to_delete = [f for f in path.glob("**")]
    for folder in folders_to_delete[::-1]:
        try:
            folder.rmdir()
        except OSError:
            continue
        


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
        path = Path(sys.argv[1]) #do not forget to change path lib
    except IndexError:
        return "No path to folder"
    
    if not path.exists():
        return "Folder with path {path} don't exist."
        
    sort_folder(path)
    delete_empty_folder(path)
    unpack_archive(path)
    return "Your files are done!"


if __name__== "__main__":
    print(main())



