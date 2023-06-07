import os
import shutil

path_core = "C:/Users/User/Desktop/pythonProject4/pythonProject4/lab1(2)"

os.chdir(path_core)


def path(some_path):
    return os.getcwd() + '/' + some_path


def check(r):
    if r == 1:
        return True

def mkdir(new_folder, root):
    if check(root):
        if not os.path.exists(path(new_folder)):
            os.mkdir(path(new_folder))

    else:
        print("The folder already exists")


def rm(del_item, root):
    if check(root):
        if os.path.exists(path(del_item)):
            if ".txt" in del_item:
                os.remove(path(del_item))
            else:
                shutil.rmtree(path(del_item))
        else:
            print("The folder does not exist")


def ls():
    contents = os.listdir(os.getcwd())
    for item in contents:
        print(item)


def pwd():
    current_directory = os.getcwd()
    print(current_directory)


def vi(name, root_w, root_a, root_r):
    comm = name.split(' ')
    if check(root_w):
        if comm[-1] == 'w':
            with open(comm[1] + '.txt', 'w') as file:
                file.write(comm[2])

    if check(root_a):
        if comm[-1] == 'a':
            with open(comm[1] + '.txt', 'a') as file:
                file.write(comm[2])
    if check(root_r):
        if comm[-1] == 'r':
            with open(comm[1] + '.txt', 'r') as file:
                content = file.read()
        print(content)


def cd(new_dir, root_cd, root_prev_cd, root_core):

    if check(root_cd):
        if "cd" in new_dir and len(new_dir.split(' ')) > 1:
            new_dir = new_dir.split(' ')
            if os.path.exists(path(new_dir[1])):
                os.chdir(path(new_dir[1]))
            else:
                print("The folder does not exist")
    if check(root_core):
        if new_dir == "cd":
            os.chdir(path_core + '/')
    if check(root_prev_cd):
        if new_dir == "cd/":
            current_dir = os.getcwd()
            parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
            os.chdir(parent_dir)


def exit():
    os.chdir(path_core + '/')

