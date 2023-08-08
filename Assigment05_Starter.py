# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Patrick Regan,8/8/23,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
objFile = None

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, 'r')
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:  # for loop examines each row in the table
            print(row["task"] + ' -- ' + row["priority"])  # print each rows value for task and priority
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        todo = input("Enter a new task >>>")  # create variable for new task
        intensity = input("Now enter its priority.  High or Low. >>>")  # create variable for the new task priority
        dicRow = {"task": todo, "priority": intensity}  # variable for new dictionary entry to list
        objFile = open(strFile, 'w')  # open file with write permission
        lstTable.append(dicRow)  # add new dictionary to list
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print()
        entry = input("which task would you like to remove?  Use the name of the task.")  # input for which to remove
        for row in lstTable:  # loop through each dictionary in list
            print(row["task"] + ' -- ' + row["priority"])  # print to screen each dictionary in easy to read format
        for row in lstTable:  # loop through each dictionary in list
            if row["task"].lower() == entry.lower():  # determine if the input 'entry' is located in a dictionary
                lstTable.remove(row)  # if entry equals a found entry, remove row
        print()  # add line for looks
        print("Updated List: \n")
        for row in lstTable:  # loop through each dictionary in li
            print(row["task"] + ' -- ' + row["priority"])  # reprint the new list
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, 'w')  # open file with write permission
        for row in lstTable:  # loop through each dictionary in list
            objFile.write(row["task"] + "," + row["priority"] + "\n")  # write new dictionaries to file
        objFile.close()  # close file
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # No additional code needed.
        break  # and Exit the program
