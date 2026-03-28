import os
import shutil

path=input("Enter the path:")
files=os.listdir(path)

for file in files:
    full_path=os.path.join(path,file)

    if os.path.isfile(full_path):
        filename, extension=os.path.splitext(file)

        if not extension:
            continue
        extension=extension[1:]

        folder_path=os.path.join(path,extension)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        shutil.move(full_path,os.path.join(folder_path,file))

        print(f"{file} has been moved to a foler with extension {extension}")

    print("program successful!!")