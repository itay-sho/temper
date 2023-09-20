import datetime
import pathlib
import os

BASE_TEMP_DIR = pathlib.Path.home() / "temp"

def main():
    current_dir = datetime.datetime.now().strftime("%Y-%m-%d")
    temp_dir_path = pathlib.Path(BASE_TEMP_DIR) / current_dir

    created = True
    if temp_dir_path.exists():
        created = False

    temp_dir_path.mkdir(parents=True, exist_ok=True)

    os.chdir(temp_dir_path)
    if created:
        print(f"Created a new temp directory at {temp_dir_path}")
    else:
        print(f"Using existing temp directory at {temp_dir_path}")
    
    print("To enter run the following command:")
    print(f"cd {temp_dir_path}")

if __name__ == "__main__":
    main()