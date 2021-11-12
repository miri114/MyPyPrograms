import os

path = "D:\PythonBookProjects\Advance_Core_Python_Programming"

os.chdir(path)

my_dir_path = os.getcwd()
my_files_list = []

for file in os.listdir(my_dir_path):
    if os.path.isfile(file):
        my_files_list.append(file)


def files_stats_dict():
    my_dict = {el: 0 for el in my_files_list}
    for file in my_dict.keys():
        my_dict[file] = os.stat(file).st_size
    return my_dict


print(files_stats_dict())
