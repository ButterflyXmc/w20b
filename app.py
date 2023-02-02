
# !Importing 3 functions from db.py
from db import connect_to_db, close_conn, close_cursor

#!"""
# LOGIN() :-
# - User's ID will print when they're logged in.
# - Choosing ID to get printed instead of the name so I can use the ID later.
# - Will save the result(ID) into a global variable for later use.
# - If the login is successful, print the option, else close the application.
#!"""
# & LOGIN
def login():
    cursor = connect_to_db()
    alias = input("Enter yout Alias : ")
    password = input("Enter your Password : ")
    cursor.execute("SELECT id FROM hackers WHERE alias = ? AND password = ?", [alias, password])
    result = cursor.fetchone()
#*  Setting the result as a global variable so I can use it outside of this function as well
    global user_id
    user_id = result[0]
    if result != None:
        print("Hello User ID :", result[0])
        user_options()
    else:
        print("__!Incorrect alias or password!__")
        close_conn()
        close_cursor()

#!"""
# create_exploit() :-
# - Lets user input their ID and any content
# - Calls a stored procedure that takes in user's input and creates a new post
#!"""
# & 1.ENTER A NEW POST
def create_exploit():
    cursor = connect_to_db()
    content = input("Enter content : ")
    user_id = input("Enter YOUR ID : ")
    cursor.execute("CALL new_post(?,?)",[content, user_id])
#^  INSERT INTO exploits (content,user_id) VALUES(content_input,user_id_input)
    print("__!POST CREATED!__")


#!"""
# my_exploits() :-
# - Putting the global variable in a (variable) to get the logged in user's ID
# - Calling a procedure that takes in the (user's ID) to show the logged in user ONLY their posts 
# - Using a for loop to display the results nicely
#!"""
# & 2.ONLY SHOW MY POSTS
def my_exploits():
    cursor = connect_to_db()
    user_input = user_id
    cursor.execute("CALL my_exploits(?)", [user_input])
#^  SELECT content FROM exploits WHERE user_id = user_id_input = TRUE;
    results = cursor.fetchall()
    for i in results:
        print(i[0])

#!"""
# all_exploits():-
# - Putting the global variable in a (variable) to get the logged in user's ID
# - Calling a procedure that takes in the (user's ID) to show the users everyone's post except theirs
# - Using a for loop to display the results nicely
#!"""
# & 3.SHOW EVERYONES POSTS EXCEPT WHOEVER'S LOGGED IN
def all_exploits():
    cursor = connect_to_db()
    user_input = user_id
#^  SELECT content FROM exploits WHERE user_id = user_id_input = FALSE;
    cursor.execute("CALL all_exploits(?)",[user_input])
    results = cursor.fetchall()
    for i in results:
        print(i[0])


# & 4.EXIT APPLICATION
def exit():
    print("__!GOODBYE!__")


# & USER OPTIONS
def user_options():
        print(" 1. Enter a NEW exploits")
        print(" 2. See all YOUR exploits")
        print(" 3. See EVERYONES exploits")
        print(" 4. EXIT the application")
        while True:
            user_input = int(input("Please enter your selection : "))
            if user_input == 1:
                create_exploit()
            if user_input == 2:
                my_exploits()
            if user_input == 3:
                all_exploits()
            if user_input == 4:
                exit()
                break

#! THE FUNCTION THAT'S RUNNING!
login()
