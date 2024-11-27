import os
def check_directory(user_directory):
    while os.path.isdir(user_directory) == False:
        try:
            if os.path.isdir(user_directory) == False:
                print(f"Error: That folder '{user_directory}' was not found. Please try again")
                user_directory = input("Enter the folder path you would like to search:\n")
        except:
            print(f"An unexpected error occured. Please enter a different folder name:\n")