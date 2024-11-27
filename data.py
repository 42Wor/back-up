import os

def print_tree(startpath, depth=0):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level + depth)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1 + depth)
        for f in files:
            print(f'{subindent}{f}')
source = "/home/maaz/Desktop/backup_make"
#print_tree(source)
