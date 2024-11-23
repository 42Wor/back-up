import os
import shutil
import time

def copytree(src, dst, symlinks=False, ignore=None):
    date_format = time.strftime("%Y-%d-%b-%H-%M-%S")
    s = src
    d = os.path.join(dst, date_format)
    if  not os.path.exists(d) and os.path.isdir(s):
        print("exists")
        try:
            if os.path.isdir(s):
                print("tree")
                shutil.copytree(s, d, symlinks, ignore)
            else:
                print("copy2")
                shutil.copy2(s, d+date_format)
        except Exception as e:
            print(f"Error copying {s} to {d}: {e}")
    else:
        print("not exists")


def manage_folders(directory):

    subfolders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]


    subfolders.sort(key=lambda folder: os.path.getctime(os.path.join(directory, folder)))


    if len(subfolders) > 3:
        extra_folders = subfolders[:len(subfolders) - 3]
        for folder in extra_folders:
            folder_path = os.path.join(directory, folder)
            try:

                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder}")
            except Exception as e:
                print(f"Error deleting {folder}: {e}")
    else:
        print("There are 2 or fewer folders, no deletion necessary.")


if __name__ == "__main__":

    source = "/home/maaz/Desktop/backup_make/s"
    destination = "/home/maaz/Desktop/backup_make/b"#end add '/ '  , k_up/
    copytree(source, destination)
    manage_folders(destination)
