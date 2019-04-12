import os

dir = "D:\\D_drive_BACKUP\\MENTOR"
dir_list = os.listdir(dir)

for subdir in dir_list:

    subdir_path = os.path.join(dir, subdir)
    # print(subdir_path)
    if os.path.isdir(subdir_path):
        # print(subdir_path + " is a directory")
        subdir_size = 0
        for l, m, n in os.walk(top=subdir_path):
            # print(l, m, n)
            for file in n:
                file_path = os.path.join(l, file)
                # print(os.path.getsize(file_path))
                subdir_size += os.path.getsize(file_path)
                # print("inside loop")
        print("Size of {} = {}".format(subdir_path, subdir_size))

