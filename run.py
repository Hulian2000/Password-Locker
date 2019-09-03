#!/usr/bin/env python3.6
from user import User
from credential import Credentials


# creating an acount


def create_user(fname, sname, password):
    ''' 
    function to create a new user account

    '''
    new_user = User(fname, sname, password)
    return new_user


def create_app(app, app_password):
    '''
    Function to create new app and password
    '''
    new_app = Credentials(app, app_password)
    return new_app


# saving user and app
def save_user(user):
    '''
    Function to save our user details
    '''
    user.save_user()


def save_app(credentials):
    '''
    Function to save new app details
    '''
    credentials.save_app()


# delete user
def del_account(user):
    '''
    Function that deletes a user acoount
    '''
    user.delete_account()


def del_app(credentials):
    '''
    Function that deletes app logged
    '''
    credentials.delete_app()

# finding a user by first name


def find_user(first_name):
    '''
    Function that finds user by their first name and returns their first name
    '''
    return User.find_by_fname(first_name)


def find_app(app):
    '''
    Function that finds an app
    '''
    return Credentials.find_app(app)

# checking if a user exists


def user_existance(first_name):
    '''
    Function that checks if a user exist and returns a boolean
    '''
    return User.user_exist(first_name)


def app_existance(app):
    '''
    Function that checks if an app exists and returns a boolean
    '''
    return Credentials.app_exist(app)

# displaying users


def display_users():
    '''
    Function that does actual display of users
    '''
    return User.display_user()


def display_app():
    '''
    Function that displays a list of apps saved
    '''
    return Credentials.display_app()


def generate_password():
    '''
    Function that generates random passwords
    '''
    generate_password = Credentials.gen_password()
    return generate_password

# main function


def main():
    print("Welcome to passlock, to login please enter your name")
    user_name = input().upper()

    print("Password:")
    password = input()

    print(f"Welcome {user_name}!")

    while True:
        print("Use this short codes: NC - to name new account credentials VC - to view credentials DEL - to delete credentials EXIT to leave app")

        short_code = input().upper()

        if short_code == 'NC':
            print("*"*100)
            print("New app:\n")
            app = input()

            # print("App password")
            # app_password = input()

            while True:
                print("-"*10)
                print("App password:\n use short codes:'mine' to use your own password\n 'generate' to use generated password\n 'ex'to exit")

                password = input().lower().strip()

                if password == 'mine':
                    print("Enter your password")
                    app_password = input().strip()
                    break
                elif password == 'generate':
                    app_password = generate_password()
                    break
                elif password == 'x':
                    break
                else:
                    print("Please enter a valid password")

            # create and save new app and password
            save_app(create_app(app, app_password))

            print(f"New {app} account created\n")
            print(f"Password: {app_password}")

        elif short_code == 'VC':
            if display_app():
                print("Here is a list of all your apps their respective passwords")

                for credentials in display_app():
                    print(
                        f"{credentials.app} - Password: {credentials.app_password}")
                else:
                    print(
                        "Save a list of apps with their passwords inorder to have them displayed")

        elif short_code == 'DEL':
            '''
            Delete app credentials
            '''
            print("Please tell me which app you want to delete")
            app = input()

            print("Confirm password")
            app_password = input()

            return credentials.delete_app()

        elif short_code == 'EXIT':
            print("You're now leaving pass-lock")
            break
        else:
            print("Could you please use the short codes?")


if __name__ == '__main__':

    main()
