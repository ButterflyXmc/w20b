import mariadb
import dbcreds
# import db
# connecting to the db
# conn = db.connect_to_db()
conn = mariadb.connect(
                        user = dbcreds.user,
                        password = dbcreds.password,
                        host = dbcreds.host,
                        port = dbcreds.port,
                        database = dbcreds.database,
                        )
cursor = conn.cursor()

# & LOGIN
def login():
    alias = input("Enter yout Alias : ")
    password = input("Enter your Password : ")
    cursor.execute("SELECT id FROM hackers WHERE alias = ? AND password = ?", [alias, password])
    result = cursor.fetchone()
    # Setting ID as a global variable so I can use it outside of this function as well
    global user_id
    user_id = result[0]
    if result != None:
        print("Hello User ID :", result[0])
        user_options()
    else:
        print("__!Incorrect alias or password!__")
        cursor.close()
        conn.close()


# & 1.ENTER A NEW POST
def create_exploit():
    content = input("Enter content : ")
    user_id = input("Enter YOUR ID : ")
    cursor.execute("CALL new_post(?,?)",[content, user_id])
    conn.commit()
    print("Post created!")

# & 2.ONLY SHOW MY POSTS
def my_exploits():
    user_input = user_id
    cursor.execute("CALL my_exploits(?)", [user_input])
    results = cursor.fetchall()
    for i in results:
        print(i[0])

# & 3.SHOW EVERYONES POSTS EXCEPT MINE
def all_exploits():
    user_input = user_id
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
            
login()
