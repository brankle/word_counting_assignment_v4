Hello and welcome to my word counting 4.0 program!
In this program you will be able to count the occurrences of a specific word or phrase in all files in a specified directory. The program also allows for case-sensitive and case-insensitive searches. The results are then printed  directly to the terminal and also saved to a text file called `wordcount_results.txt`.

**Requirements**
This program uses a custom Python module called `directory_checker` which is used to verify that the user provided directory exists. This must be in the same directory as the main `word_counting_4.py'.

In order to run this program open a terminal window and navigate to the directory containing the word_counting_4.py Python program. Once you have done that, at the command line you must first write python word_counting_4 and proceed to write the word/phrase you would like to search and whether or not you want case sensitivity (yes/no).

Example: python word_counting_4 spam no
The above provided example written at the command line will run the word_counting_4 program and search for the word spam in each file within the directory you provide without case sensitivity.

If you want to search for more than one word, that phrase should be put in quotes "".
Example: python word_counting_4 "egg and" yes
The above provided example written at the command line will run the word_counting_4 program and search for the phrase "egg and" in each file within the directory you provide with case sensitivity.

The program will ask you to provide the path to the directory you would like to count words within. The path provided should look like the following example: /Users/brenda/Documents/UMD/INST126/word_counting_assignment_v4/monty_python_sketches


**Why this is helpful**

My README is helpful to users becuase it  provides clear instructions on how to set up and run the program. The README explains that the module should also be in the same directory as the program in order for the program to run correctly. The README explains how to correctly provide the command-line arguments, with examples showing how to run the program using a word or phrase and specifying whether the search should be case-sensitive or case-insensitive. The README also provides users with an example of how to correctly provide the path to their directory. 

Without the README, users might struggle with providing the correct command-line arguments, especially when trying to search for multi-word phrases or choosing case-sensitivity. They could also encounter issues when specifying the directory path or if the custom module (directory_checker) is missing from the working directory. The README clarifies this to prevent confusion when running the program.