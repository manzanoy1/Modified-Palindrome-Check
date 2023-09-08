#Yanira Manzano
#4/7/2020
#Modified Palindrome Check

import time

def menu():
    print("""
    Please enter a word or sentence and 
    we'll check if the string you input
    it's an actual palindrome or not.""")
    usrstring = str(input(">>>"))
    p_check(usrstring)
    time.sleep(3)
    next()
    
def true():
    print("It's Palindrome.")

def false():
    print("It's not Palindrome.")
    
def punc(string):
    return ''.join(i for i in string if i.isalnum())
   
#This was a pain to make it work
def p_check(string):
    string.strip()
    string = punc(string)
    string = string.lower().replace(" ", "")
    print(string)
    time.sleep(1)
    if len(string) < 1:
        true()
    elif string[0] == string[-1]:
        return p_check(string[1:-1])
    else:
        false()
        
def next():
    print("What's your choice?")
    choice = int(input("""
        1. Repeat
        2. Quit
        >"""))
    if choice == 1:
        menu()
    elif choice == 2:
        exit()
    else:
        print("Yikes, that's not an option. Sadly. :')")
        time.sleep(1)
        next()
