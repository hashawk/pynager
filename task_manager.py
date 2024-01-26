
def manage_tasks(username):
    print("\
        1 -- View Data\n\
        2 -- Add Task\n\
        3 -- Update Task\n\
        4 -- View Task Status"
    )
    action = input(':')

    if action == '1':
        print(1)
    elif action == '2':
        print(2)
    elif action == '3':
        print(2)
    elif action == '4':
        print(2)
    else: 
        print("Invalid command, try again")
        manage_tasks(username)

def login():
    print("Sign-in")
    user_n = input("Username: ")
    pass_w = input("Password: ")
    try:
        username = f"{user_n} task.txt"
        user_f = open(username, 'r')
        password = user_f.readlines(0)[0]
        user_f.close()

        if pass_w == password:
            print(f"Hello {username}!")
            manage_tasks(username)
        else:
            print("Try, again please.")
            login()
    except Exception as e:
        print(e)
        login()


def signup():
    print("Sign-up")
    username = input("Enter a desired username: ")
    password = input("Enter a password: ")
    user_info(username, password)
    print("Please sign in to your account")
    login()

def user_info(username, password):
    name = input("Name: ")
    username_ = f"{username} task.txt"

    f = open(username_, 'a')
    f.write(password)
    f.write(f"\nName: {name}")
    f.close()
