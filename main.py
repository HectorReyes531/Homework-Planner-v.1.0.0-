# Homework Planner Bot designed for students!

# Import the prettytable module from the Python library to display our to-do list in visually appealing ASCII table format
from prettytable import PrettyTable
# Import the itertools module to iterate over multiple lists in our program
import itertools

# Declare empty list to store general information about our assignment
course_list = []
assignment_list = []
deadline_list = []

x = PrettyTable()


# This method returns the user's action they'd like to perform
def action():
    print('What would you like to do?')
    # Prompt the user to enter the desired action
    print('1) Enter $Add to add a new assignment')
    print('2) Enter $Delete to delete an assignment')
    print('3) Enter $Update to update an assignment')
    print('4) Enter $Dis to disconnect the bot')
    print('5) Enter $List-View to view your assignments as a list')

    selection = input('Selection: ')
    # Set the input to all lower keys to accept both upper and lower key characters(simplify our code)
    selection.lower()
    # return user selection
    return selection


def add_assignment(new_course, new_assignment, new_deadline):
    # Add elements to our current list
    course_list.append(new_course)
    assignment_list.append(new_assignment)
    deadline_list.append(new_deadline)

def delete_assignment(delete_assignment_name):
    # Remove assignment specified from our current list
    assignment_list.remove(delete_assignment_name)

def update_course_name(original_course, updated_course):
    # Retrieve the index of the original course in our current list
    get_index = course_list.index(original_course)
    # Replace original course name with updated course name
    course_list[get_index] = updated_course

def update_list_name(original_name, updated_name):
    # Index() method returns the position of the assignment to-be updated
    get_index = assignment_list.index(original_name)
    # Replace original assignment with the updated assignment name
    assignment_list[get_index] = updated_name

def update_list_deadline(original_deadline, updated_deadline):
    # Retrieve the index of the original assignment
    get_index = deadline_list.index(original_deadline)
    # Replace original deadline with the updated one
    deadline_list[get_index] = updated_deadline

# Output a visual representation of the to-do list
def display_list():
    x.field_names = ['Course Name', 'Assignment', 'Due Date']
    # Iterate over every item in the list to add a new assignment
    for (i, j, y) in itertools.zip_longest(course_list, assignment_list, deadline_list):
        # Add each item to our table by row
        x.add_row([i, j, y])

    # Title our table
    print(x.get_string(title='Homework Planner'))

    # Deletes all the rows in the table and updates it with new content each time it's run
    x.clear_rows()


def main():
    print('Homework Planner v.1.0\n')
    # Declare variable as true to keep our main loop running
    running = True

    while running:
        # Prompt user to input the action they'd like to perform
        user_choice = action().lower()

        # Add item to our list
        if user_choice == '$add':
            add_course = input('Course name: ')
            add_assignment_name = input('Name of assignment: ')
            add_deadline = input('Due date(dd-mm-yyyy): ')

            print(f'New assignment added - {add_assignment_name}')
            # Append new element/assignment to our list

            add_assignment(add_course, add_assignment_name, add_deadline)
            display_list()
            print()

        # Delete item from our list
        elif user_choice == '$delete':
            # Continue executing the loop until the user has entered a valid entry
            while True:
                # Ask the user to enter the name of assignment
                delete_assignment_name = input('Enter the name of the assignment you\'d like to delete: ')
                # Try clause is executed
                try:
                    # Check if the assignment is in the list initially created by the user
                    if delete_assignment_name in assignment_list:
                        validate_addition = input(f'Are you sure you\'d like to remove {delete_assignment} from your list? (y/n): ').lower()
                        if validate_addition == 'y':
                            # Delete the assignment from our list
                            delete_assignment(delete_assignment_name)
                            print('List updated!')
                            # Call on the update_list() function to display a table of our newly updated list
                            display_list()
                            print()
                            # Exit out of the while loop
                            break

                        elif validate_addition == 'n':
                            break
                    else:
                        print('Assignment not found')
                # Catch any exceptions
                except Exception:
                    print('Invalid entry.')


        # Make changes to our list
        elif user_choice == '$update':
            # Declare variable as true to keep while loop running
            update = True
            # Continue executing the value until valid entries are entered
            while update:
                assignment_to_be_updated = input('Enter the name of the assignment you\'d like to modify: ')
                # Try clause is executed
                try:
                    # Check if the assignment is in our current list
                    if assignment_to_be_updated in assignment_list:
                        validate_update = input(f'Are you sure you\'d like to update {assignment_to_be_updated} from your list? (y/n): ').lower()
                        if validate_update == 'y':

                            # Check if the user would like to update the name
                            validate_update_name = input('Would you like to update the name (y/n): ')
                            if validate_update_name == 'y':
                                updated_name = input(f'What would you like to update {assignment_to_be_updated} with: ')
                                # Update list with new assignment name
                                update_list_name(assignment_to_be_updated, updated_name)
                                print('Assignment updated!')
                                display_list()
                                # Restart program
                                update = False
                                print()

                            elif validate_update_name == 'n':
                                print()
                                break


                            # Check if the user would like to update the due date
                            validate_update_deadline = input(f'Would you like to update the due date for {assignment_to_be_updated}? (y/n) ').lower()

                            if validate_update_deadline == 'y':
                                # Prompt the user to input the original due date to validate it
                                deadline_to_be_updated = input(f'Enter the original due date for {assignment_to_be_updated}: ')

                                try:
                                    # Check if the deadline entered by the user matches with the one in the current list
                                    if deadline_to_be_updated in deadline_list:
                                        # Retrieve updated due date
                                        new_deadline = input(f'Enter the updated deadline for assignment - {assignment_to_be_updated}\nNew deadline(dd-mm-yyyy): ')
                                        update_list_deadline(deadline_to_be_updated, new_deadline)
                                        print('Deadline updated!')
                                        display_list()
                                        # Restart program
                                        update = False
                                        print()

                                    else:
                                        print('Deadline not found!')

                                except Exception:
                                    print('Invalid entry, try again')
                                    print()


                            elif validate_update_name == 'n':
                                print()
                                break

                            # Check if the user would like to update a course name
                            validate_update_course_name = input(f'Would you like to update the course name for {assignment_to_be_updated}? (y/n) ').lower()

                            if validate_update_course_name == 'y':
                                # Prompt user to input the original course name for validation
                                course_name_to_be_updated = input(f'Enter the original course name for {assignment_to_be_updated}: ')

                                try:
                                    # Check if the course name entered by the user is stored in the original course list
                                    if course_name_to_be_updated in course_list:
                                        # Obtain updated course name
                                        updated_course_name = input(f'Enter the updated course name for {assignment_to_be_updated}\nUpdated course name: ')
                                        update_course_name(course_name_to_be_updated, updated_course_name)
                                        print('Course name updated!')
                                        display_list()
                                        print()
                                        update = False

                                    else:
                                        print('Course name not found, try again')

                                except Exception:
                                    print('Invalid entry, try again')
                                    print()

                            elif validate_update_course_name == 'n':
                                print()
                                break



                        # Terminate the loop if the user does not want to update an assignment name
                        elif validate_update == 'n':
                            print()
                            update = False

                    # If assignment specified is not in the list, output an error message
                    else:
                        print('Assignment not found\n')

                # Catch any exceptions
                except Exception:
                    print('Invalid entry\n')


        # Disable the bot from the server
        elif user_choice == '$dis':
            validate_exit = input('Are you sure you want to disconnect the bot? (y/n): ').lower()
            if validate_exit == 'y':
                running = False
            elif validate_exit == 'n':
                running = True

        # Output a table containing a list of the assignments registered
        elif user_choice == '$list-view':
            display_list()
            print()

        else:
            print('Invalid entry, please try again.')
            print()

main()
