import getpass
def get_pwd():
    username = input('Enter username : ')
    password = getpass.getpass()
    print(username, password)


get_pwd()

#revisit this later for ssh/telnet logins


