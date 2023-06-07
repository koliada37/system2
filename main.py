import users
import command as cm

root_list = []

user_list = []

admin1 = users.User("admin", "1", "1111111")
user1 = users.User("user1", "1", "0000000")
user2 = users.User("user2", "1", "0000000")

user_list.append(admin1)
user_list.append(user1)
user_list.append(user2)


while True:
    login = input("loggin ")
    password = input("pasword ")
    for w in user_list:
        if w.login == login and w.password == password:

            role = list(w.root)

            tf = True
            while tf:
                name = input()
                if "mkdir" in name:
                    name = name.split(' ')
                    cm.mkdir(name[1], int(w.root[0]))

                if "rm" in name:
                    name = name.split(' ')
                    cm.rm(name[1], int(w.root[1]))

                if name == "ls":
                    cm.ls()

                if name == "pwd":
                    cm.pwd()

                if "cd" in name:
                    cm.cd(name, int(w.root[2]), int(w.root[3]), int(w.root[4]))

                if "vi" in name:
                    cm.vi(name, int(w.root[5]), int(w.root[6]), int(w.root[7]))
                if "exit" == name:
                    cm.exit()
                    tf = False
