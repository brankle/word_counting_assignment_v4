#create a program that can calculate a count of 
# how many times a word occurs in a text file.

#import os, sys and functions
import os
import sys

import directory_checker

#checking the amount of command line arguments
if len(sys.argv) <3:
    print("Error: too few command line arguments provided.")
    sys.exit

# welcome message
print("Welcome to my word counting program!\n")

#user provides one or two-word phrase at command line
word_being_counted = sys.argv [1]


#case sensitivity provided at command line
case_sensitive_string = sys.argv[2]

#printing system arguments 
print(f"These are your arguments: {sys.argv}")


#printing out the current working directory
#and contents of that directory
print (f"Here is your Current Working Directory: {os.getcwd()}")
print (f"Here's what's in that directory: {os.listdir()}")


#ask user for a path to a directory 
user_directory = input("Enter the folder path you would like to search:\n")



#checking user directory with function

directory_checker.check_directory(user_directory)

#changing to desired user directory
os.chdir(user_directory)
print (f"Here's what's in'{user_directory}':", os.listdir())

# executing case-sensitive or case-insensitive count

if case_sensitive_string.lower() == "yes":
    case_sensitive = True
elif case_sensitive_string.lower() == "no":
    case_sensitive = False
else:
    print("I didn't understand that response, so I will run a case-insensitive search by default.")
    case_sensitive = False

#performing the word count and printing results to a file called wordcount_results.txt
dir_list = os.listdir()

#initializing list to store results
results = []

#iterating over each file in the folder
for filename in dir_list:
        if os.path.isfile(filename):  
            try:
                with open(filename, 'r') as file_connection:  # Open the file
                    file_contents = file_connection.read() 
                    words = file_contents.split()
                    if case_sensitive:
                        word_count = words.count(word_being_counted)
                        result = f"The word/phrase '{word_being_counted}' was found {word_count} times in this file: {filename}\n"
                        print(result)
                        results.append(result)
                    else:
                        word_count = file_contents.casefold().count(word_being_counted.casefold())
                        result = f"The word/phrase '{word_being_counted}' was found {word_count} times in this file: {filename}\n"
                        print(result)
                        results.append(result)
            except:
                print(f"An unexpected error occured. Exitting program:")

#creating results file
with open("wordcount_results.txt", "w") as results_file:
    results_file.write("\n".join(results))