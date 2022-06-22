###############################################################################
                            # Import dependencies #
###############################################################################
from security import person, employee
import os
import time
import turtle
###############################################################################
                # Password check for the security of the program #
###############################################################################
repeat = 1                     # repeat indicator for password attempts; 1 = repeat : 0 = dont repeat
retry = 'Y'                    # retry indicator for action after password attempt

while(repeat!=0):
    os.system('cls')           # clear screen
    print("# User Authentication, please enter your password #")
    password = input("password: ")            # Ask password for the program's access
    passwordinsert = person(password)         # object instantiation via the parent class
    if(passwordinsert.getpassword() == passwordinsert.defaultpassword()):
        permission = employee(passwordinsert) # give permission via child class
        result = permission.isemployee()      # Access grant
    else:
        result = passwordinsert.isemployee()  # Access Denied
    # Access Check
    if(result == True):                       # If access is granted
        print("\nLoading program...")
        time.sleep(2.0)
        repeat = 0
    else:                                     # Else access is denied, what actions should be done?
        print("\nWrong password")
        retry = str(input("Try again ? (Y or N): "))
        if(retry == "Y" or retry == "y"):     # retry
            print("\nResetting program...")
            repeat = 1
        elif(retry == "N" or retry == "n"):   # quit the program
            print("\nQuitting program...")
            repeat = 0
            time.sleep(2.0)
            os.system('cls')
            exit()
        else:                                 # retry (if user random type any unrelated things)
            print("\nI assume you want to try again...")
            repeat = 1
        time.sleep(2.0)
        continue

###############################################################################
                                    #File#
###############################################################################
print("\nReading file...")                      # Indicate the current action is reading file
time.sleep(1.0)                                 # Delay to let the user saw the statements
name_file = "stock.txt"                         # name of the file that used to save/write
createfile = open(name_file,"a")                # create a new file if it doesn't exist in the same directory
createfile.close()

item = dict()                                   # dictionary for storing data values in key:value pairs
readfile = open(name_file,"r")                  # open file in read mode
while True:                                     # loop to read file
    text = (readfile.readline()).rstrip("\n")   # read line by line
    lists = text.split(":")                     # split line by ':'
    if len(text) == 0:
        break
    else:
        key = lists[0]                          # key
        value = lists[1]                        # value
        item.update({key: value})               # key:value pair insertion
print("Done...")
if(item == {}):
    print("\nFile has nothing inside")
    item.update({'sample': 56})                 # the dictionary need to contain something to continue
readfile.close()
time.sleep(2.0)                                 # Delay to let the user saw the statements

##################################################################################
                        # Menu layout & description # (extra)
##################################################################################
# Description of the functions        (not the one print on terminal)            #
##################################################################################
# Add an item                         (Add item with their name and number)      #
# Remove an item                      (Remove item from the list)                #
# Update an item (+/-)                (update item by + or - on their number)    #
# Print all items in terminal         (print all item in list with word format)  #
# Print stock details (in turtle)     (print all item in bar chart/turtle)       #
# Quit the program                                                               #
##################################################################################

# Code labels that will be entered by user to perform the desired action
listcode = ["A","R","U","P","G","Q"]
# Description that tells what the labels does
description = ["Add an item","Remove an item","Update an item (+/-)", "Print all items in terminal", "Print all items in graphical","Quit the program"]
# Zip the listcode and description in a list
menu = list(zip(listcode,description))
#spacing ratio in format
menuformat = "{0}{1:<35}{2:<2}{3}"

##################################################################################
                                # define funtions #
##################################################################################

# 1. Add an item that doesn't exist in the data (add the data via the update from dictionary)
def add_item():
    print(" ")
    for key, value in item.items(): # Print all the item name
        print(key+",", end=" ")
    print(" ")
    item_name = input("\nEnter the name of the item (only lowercase): ").lower() # make sure every name is lowercase
    duplicate = 0                   # if name of item is found, this value will be 1 to indicate the duplicate
    for key, value in item.items():
        if (key == item_name):
            print("\nThe item name is duplicated")
            duplicate = 1           # item name is duplicated
            break
        else:
            continue
    if(duplicate == 0):             # new item name is found
        no_of_item = int(input("Enter the number of the items: "))
        item.update({item_name: no_of_item})    # Add a new item name
        print("\n"+item_name+" is successfully added to the stock")
    else:
        print("Error is found... back to menu")

# 2. Remove an item entirely from the data (remove the data via the pop from dictionary)
def delete_item(delete_target):     # delete_target is the parameter that bring value to this function
    existence = 0                   # if name of item is found, this value will be 1 to indicate its existence
    for key, value in item.items():
        if (key == delete_target):
            print ("The item, "+ delete_target + " has been deleted")
            item.pop(delete_target) # Delete the item
            existence = 1
            break
        else:
            continue
    if existence == 0:              # Deletion is fail due to non-existence of the input data
        print("The name of the item cannot be found")

# 3. Update value of an item that from the data (addition/subtraction on the data)
def update_item():
    # Asking input from user
    item_name = input("Enter the name of the item that need to be updated (only lowercase): ").lower() # make sure every name is lowercase
    operation = str(input("Enter the operation ('+' or '-'): "))
    no_of_item = int(input("Enter the number of the items (only in integer): "))

    # Checking on the inputs and updating the item with the inputs
    existence = 0   # if name of item is found, this value will be 1 to indicate its existence
    for key, value in item.items():
        if (key == item_name):
            existence = 1
            if(operation == '+'):     # addition operation
                item[item_name] = int(value) + no_of_item
                print("The item, "+ item_name + " has been updated")
                break
            elif(operation == '-'):   # subtraction operation
                total = int(value) - no_of_item
                if (total > -1):
                    item[item_name] = total
                    print("The item, "+ item_name + " has been updated")
                    break
                else:                 # the final value shouldn't be negative as there is not negative quantity
                    print("The final value shouldn't be negative value! no changes is made...")
                    break
            else:                     # if wrong input is found
                print("Invalid operation, back to menu...")
                break
        else:
            continue
    if existence == 0:
        print("The name of the item cannot be found")

# 4.1 Print all the existing data in terminal (String formatting + kwarg)
def print_all(**dictionary):
    print(" ")
    print_all_format = "{0:<20}{1}{2}"
    title = ["Item name","Quantity"]
    print(print_all_format.format(title[0]," ",title[1]))
    for key, value in dictionary.items():   # print all the key:value pair
        print(print_all_format.format(key," ",value))

# 4.2 Print all the existing data in barchart (Turtle + kwarg + import function from other file)
def print_turtle(**data):
    turtle.TurtleScreen._RUNNING = True         # To make sure turtle always running
    wn = turtle.Screen()                        # settings for the turtle/windows
    wn.bgcolor("black")
    wn.title("Chart of the current stocks (Click on screen to close)")
    chart = turtle.Turtle()
    chart.shape("triangle")
    chart.color("yellow")
    chart.pensize(3)
    chart.penup()                               # set a starting point for the drawing
    chart.goto(-350,-250)                       # start at (-200,-200) position
    chart.pendown()

    from barchart import draw_bar               # import draw_Bar function for drawing the barchart

    for key in data:
        draw_bar(chart,str(key),int(data[key])) # Function call from other module
    turtle.exitonclick()                        # Exit by clicking on the screen of Turtle display windows

##################################################################################
                                      # Main #
##################################################################################
user_input = 'Y'                                    # initialize user_input to allow user to choose operation
choice = 'N'                                        # initialize choice to allow user to continue after any operation
while(user_input != 'Q'):
    os.system("cls") # clear screen
    print('#'*40+"\n Welcome to Inventory Management System \n"+'#'*40+'\n') # print the border also
    for listcode,description in menu:               # for loop to print the menu
        print(menuformat.format(' ',description,'-',listcode))
    print('\n'+'#'*40)                              # print the border by using multiplication

    # selections of the user input
    user_input = input("Enter the code: ")
    if (user_input == "A" or user_input == "a"):    # Add an item
        add_item()

    elif(user_input=='R' or user_input=='r'):       # Delete an item
        print(" ")
        for key, value in item.items():             # Print all the item name
            print(key+",", end=" ")
        print(" ")
        item_name = input("\nEnter the name of the item that will be removed (only lowercase): ").lower() # make sure every name is lowercase
        delete_item(item_name)                      # Argument - the value will passed to the function

    elif(user_input=='U' or user_input=='u'):       # Update a value of an item
        printingdoc = item.copy()
        print_all(**printingdoc)
        print(" ")
        update_item()

    elif(user_input=='P' or user_input=='p'):       # Print data in terminal
        printingdoc = item.copy()
        print_all(**printingdoc)

    elif(user_input=='G' or user_input=='g'):       # Print data in bar chart using Turtle
        printinggra = item.copy()
        print_turtle(**printinggra)

    elif(user_input == "Q" or user_input == "q"):   # Quit the program
        break

    else:                                           # Indicate wrong code is entered
        print("Wrong input, please try again")
        user_input = 'Y'                            # Make user to enter the code again

    choice = input('\nContinue? (Any input): ')     # short delay to wait user enter any input
    if(choice == 'Y'):
        continue
    else:
        continue

##################################################################################
                                # Closing program #
##################################################################################
# Saving file # After enter Q, save the file (only if the user quit the program "properly") #
writefile = open(name_file, "w")
for key, value in item.items():
    writefile.write(key + ":" + str(value) + "\n")  # write the key:value pair into file
writefile.close()

os.system("cls")                                    # clear the screen and show the closing statements to user
print("Saving...")
time.sleep(2.0)
print("Completed")
print("\nThank you for using the program")
print("and Goodbye <3")
time.sleep(2.0)
os.system("cls")
