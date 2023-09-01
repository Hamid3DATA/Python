import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hamid",
    database="nintendo games"
)

print("With this program you are able to search any game made by Nintendo which were officially released in the US")
user_input = input("Search by: ID, Name, Console Name or Year: ")
user_input2 = input("Which is: ")

user_input = user_input.lower()
user_input = user_input.replace(" ", "")

my_cursor = mydb.cursor()

if user_input == "id":
    my_cursor.execute("SELECT * FROM Games WHERE GameID = " + user_input2)
    my_result = my_cursor.fetchall()
    for x in my_result:
        print(x)
    if not my_result:
        print("There is only 630 games in our list check if you didn't go above (or under) it :)")

elif user_input == "name":
    my_cursor.execute("SELECT * FROM Games WHERE GameName LIKE '%" + user_input2 + "%'")
    my_result = my_cursor.fetchall()
    for x in my_result:
        print(x)
    if not my_result:
        print("Check if you spelled the game name (or a part of it) correctly :)")

elif user_input == "consolename":
    my_cursor.execute("SELECT * FROM Games WHERE ConsoleName LIKE '%" + user_input2 + "%'")
    my_result = my_cursor.fetchall()
    for x in my_result:
        print(x)
    if not my_result:
        print("Check if you spelled the console name correctly :)")

elif user_input == "year":
    my_cursor.execute("SELECT * FROM Games WHERE GameDate = " + user_input2)
    my_result = my_cursor.fetchall()
    for x in my_result:
        print(x)
    if not my_result:
        print("Check that you didn't type a year where they didn't make any games")
