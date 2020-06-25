import os


dir = ""

with open("subdir_size.properties") as properties:
    lines = properties.readlines()
    for line in lines:
        if line.rstrip(" ").split("=")[0] == "base_dir_name":
            dir = line.split("=")[1].rstrip("\n")
            print(dir)

dir_list = os.listdir(dir)
with open("subdir_size.csv", 'w') as result:
    result.write("Dir name , size-MB \n")
for subdir in dir_list:

    subdir_path = os.path.join(dir, subdir)
    # print(subdir_path)
    if os.path.isdir(subdir_path):
        # print(subdir_path + " is a directory")
        subdir_size = 0
        # with open("subdir_size.txt", 'w') as result:
        #     result.write("Dire name , size")
        for l, m, n in os.walk(top=subdir_path):
            # print(l, m, n)
            for file in n:
                file_path = os.path.join(l, file)
                # print(os.path.getsize(file_path))
                subdir_size += os.path.getsize(file_path)
                # print("inside loop")
        subdir_size = "{0:.3f}".format( subdir_size/1048576)
        with open("subdir_size.csv", 'a') as result:
            result.write("{} , {} \n".format(subdir_path, subdir_size))
            # print("Size of {} , {}".format(subdir_path, subdir_size), file="result")

