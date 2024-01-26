
def manage_tasks(username):
    # Function allows the user to manage their tasks within a personal file
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
        print(3)
    elif action == '4':
        print(4)
    else: 
        print("Invalid command, try again")
        manage_tasks(username)

def login():
    print("Sign-in")
    user_n = input("Username: ")
    pass_w = input("Password: ")
    try:
        with open(f"{user_n} task.txt") as user_f:
            password = user_f.readlines(0)[0]
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
    name = input("Desired username: ")
    username_ = f"{username} task.txt"

    with open(username_, 'a') as f:
        f.write(password)
        f.write(f"\nName: {name}")
