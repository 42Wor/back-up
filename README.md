# Backup and Folder Management Script

This Python script automates the process of backing up files and managing backup directories. It performs two main tasks:

1. **Copying Files**: Copies files from a source directory to a backup destination, appending a timestamp to the backup directory name.
2. **Managing Folders**: Ensures that only the most recent 3 backups are retained in the destination folder, deleting any older backups.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Functions](#functions)
  - [copytree](#copytree)
  - [manage_folders](#manage_folders)
- [Requirements](#requirements)
- [License](#license)

## Installation

To use the script, you need to have Python 3 installed on your machine. Additionally, the script uses custom functions from a module (`_11.py`), which must be located on your machine.

1. Clone or download the repository.
2. Ensure that the `_11.py` file is located in the specified path in the script (e.g., `/home/maaz/Desktop/backup_make`).

```bash
git clone https://github.com/yourusername/backup-management-script.git
cd backup-management-script
Usage
Running the Script
You can run the script by executing the following command in your terminal:

bash
Copy code
python3 backup_script.py
Make sure to replace the source and destination paths in the script to match your desired backup locations.

The script will:

Copy the contents of the source directory to the destination directory with a timestamped folder.
Delete any backup folders older than the 3 most recent ones.
Customization
Source Directory: Modify the source variable to specify the directory you want to back up.

python
Copy code
source = "/home/maaz/Desktop"
Destination Directory: Modify the destination variable to specify where the backup should be stored.

python
Copy code
destination = "/media/maaz/maaz1/projects_back_up"
How it Works
Copying Files:

The script copies the contents of the source directory to a backup folder in the destination directory.
A timestamp in the format YYYY-DD-Mon-HH-MM-SS is appended to the folder name, ensuring unique backups.
Managing Folders:

The manage_folders function checks the destination directory for subfolders.
It keeps the 3 most recent backup folders and deletes any older ones, ensuring that only the latest backups are kept.
Functions
copytree(src, dst, symlinks=False, ignore=None)
Copies an entire directory tree from the source (src) to the destination (dst), appending a timestamp to the destination directory name.

Arguments:

src: The source directory path.
dst: The destination directory path.
symlinks: Optional flag to include symbolic links (default: False).
ignore: Optional function that can be used to specify files or directories to ignore.
Behavior:

The function creates a backup folder in the destination directory with a timestamp.
It copies files and directories from the source to the new backup folder.
In case of any error (e.g., permission issues), it prints an error message.
manage_folders(directory)
Manages the subfolders in the destination directory by deleting older backups, leaving only the 3 most recent ones.

Arguments:

directory: The directory where backups are stored.
Behavior:

Sorts the subfolders based on creation time.
Deletes any subfolders older than the 3 most recent ones.
If there are 2 or fewer subfolders, no deletion is performed.
