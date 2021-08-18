# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Moiz Vahora,8/16/2021,modified starter.py file):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# <Moiz Vahora>,<08.16.2021>,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data

        file = open(file_name, "r")
        # loop used to populate list_of_rows list
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        # TODO: Add Code Here!

        # appending list variable with user input using a dictionary
        dicRow = {"Task": task, "Priority": priority }
        list_of_rows.append(dicRow)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        # TODO: Add Code Here!

        # conditional statement used to remove from list, if user enters 0 nothing is deleted.
        if task == 0:
            # cancel deletion and return to menu
            print("No user input deleted")
        else:
            # Removing selected entry (subtract 1 since count starts at 0) and displaying entry number deleted
            list_of_rows.remove(list_of_rows[task - 1])
            print("Entry " + str(task) + " deleted!!!")
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # TODO: Add Code Here!
        # Opening file and overwriting my previous input, in case we deleted entries
        objfile_io = open(file_name, "w")

        for objrow in list_of_rows:
            # Writing entries in list to the file from each dictionary entry
            objfile_io.write(objrow["Task"] + ',' + objrow["Priority"] + '\n')
        objfile_io.close()  # close file
        print("User edits saved to file!!!")
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ asks the user to input a new task and priority

        :return:nothing
        """
        task = input("Enter a task: ")
        priority = input("Enter a priority: ")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        #pass  # TODO: Add Code Here!
        """ Asks the user which list item they would like deleted using a numerical list

        :return:
        """
        task = int(input("Which entry would you like to delete? 0 to cancel "))
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        I_task, I_priority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(I_task,I_priority,lstTable)

        IO.input_press_to_continue(strStatus)

        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here
        for i_entry, objRow in enumerate(lstTable):
            # displaying current data for user reference (copied from option 1)
            print("Entry ", i_entry + 1)
            print('Task: ' + objRow["Task"] + ' ' + 'Priority ' + objRow["Priority"])
        # Calling function to ask for user input for data deletion
        Delete = IO.input_task_to_remove()

        # calling function to remove data from list
        Processor.remove_data_from_list(Delete, lstTable)
        # Calling funtion to ask the user to press enter to continue
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File

        #calling function get user input if they would like to save
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        #conditional statement y to save, n to continue
        if strChoice.lower() == "y":
            # TODO: Add Code Here!
            # Opening file and overwriting my previous input, in case we deleted entries.

            Processor.write_data_to_file(strFileName,lstTable)

            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        # Ask user if they would like reload
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")

        #Conditional statement to detemrine, y to reload data, n to cancel and continue
        if strChoice.lower() == 'y':
            # TODO: Add Code Here!
            # Call function to re-read data, using the same function to load the data when the script was started
            Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
