# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from datetime import datetime

def create_ordered_list(list_length_request):
    """
    Function to create ordered list of numbers using a while loop based
    on users input
    """
    i = 1
    ordered_list = [] 
    while i < list_length_request + 1:
        ordered_list.append(i)
        i += 1
    return ordered_list

def welcome_user():
    """
    Function to run first on the console and welcome the user a quesiton is 
    asked if they want to learn more about binary search and the function 
    of this program and if the user wants to use the program. 
    """
    print('\n Hello welcome to Search Methods. \n')
    print('If this is your first time using Search Methods it is recommended that you read the instructions. \n')
    print('Would you like to read the instructions? y/n')
    learn_or_play = input()
    if learn_or_play == 'y':
        print('Loading Instructions...')
        return 'intructions'
    elif learn_or_play == 'n':
        print('Loading Program...')
        return 'program'
    else:
        while learn_or_play != 'y' or 'n':
            print('Please enter the character y and press enter if you would like to learn more about binary search or the character n if you would like to run the program')
            next_input = input()
            if next_input == 'y':
                print('Loading Instructions...')
                return 'intructions'
                
            elif next_input == 'n':
                print('Loading Program...')
                return 'program'


def program_type():
    """
    Function to ask the user what program type they would like to play
    """
    print('Enter the number 1 to use Search Methods on a single user selected list length. Enter the number 2 to use Search Methods to generate x and y data or type instructions if you would like to read the instructions.')
    program_type = input()
    if program_type == '1':
        return 'type_one'
    elif program_type == '2':
        return 'type_two'
    elif program_type == 'instructions':
        return 'instructions'
    else:
         while program_type != '1' or '2' or 'instructions':
            print('Please enter the number 1 to use Search Methods on a single user selected list length. Enter the number 2 to use Search Methods to generate x and y data or type instructions if you would like to read the instructions.')
            next_input = input()
            if program_type == '1':
                return 'type_one'
            elif program_type == '2':
                return 'type_two'
            elif program_type == 'instructions':
                return 'instructions'

def instructions():
    """
    Function to teach the user about bianry searches and the program itself 
    will lead the user onto running the program and direct them to the readme file 
    if they want to learn further
    """
    create_separation()
    print('Instructions')
    create_separation()
    print('Would you like to run this program y/n')
    run_program = input()
    if run_program == 'y':
        main()
    else:
        print('Closing program')
        exit()

def get_list_length():
    """
    Function used to obtain the users desired list length between 100 and 10000000
    will convert to int and assess if within the specified values
    """
    print('Please input a list length integer between 100 (one hundred) and 10000000 (10 million). Any floats will be rounded to the nearest whole number')
    list_request = input()
    list_request_num = int(round(float(list_request)))
    
    if list_request_num >= 100 and list_request_num <= 10000000:
        print(f'You entered {list_request_num}')
        print('Standby program may take some time if iterating through a very large list (greater than 1 million)')
        create_separation()
        return list_request_num
    else:
        while list_request_num < 100 or list_request_num > 10000000:
            print('Please enter a number between 100 (one hundred) and 10000000 (10 million)')
            second_list_request = input()
            second_list_request_num = int(round(float(second_list_request)))

            if second_list_request_num >= 100 and second_list_request_num <= 10000000:
                print(f'You entered {second_list_request_num}')
                return second_list_request_num
                break

def create_separation():
    """
    Function used to display 3 rows of full stops in the console
    Used to separate bulk pieces of text
    """
    i = 1
    while i < 4:
        print("...............................................................")
        i += 1

def select_random(x):
    start = x[0]
    end = x[-1]
    random_list_item = random.randint(start, end)
    print(f'program will be looking for {random_list_item}')
    create_separation()
    return random_list_item

def normal_iteration(created_list, random_selection):
    """
    Function to iterate through a list in the traditional fashion by looping from start to finish
    """
    print('Performing normal iteration \n')
    start = datetime.now().microsecond
    for list_item in created_list:
        if list_item == random_selection:
            end = datetime.now().microsecond
    time_delta = end - start
    print(f'The time taken to perform normal iteration is {time_delta} microseconds')
    create_separation()
    return time_delta

def binary_search_loop(list, low, high, random_item):
 
    if high >= low:
 
        mid = (high + low) // 2
 
        if list[mid] == random_item:
            return mid
        elif list[mid] > random_item:
            return binary_search_loop(list, low, mid - 1, random_item)
        else:
            return binary_search_loop(list, mid + 1, high, random_item)
    else:
        return -1
 
def binary_search(list, random_item):
    
    print('Performing binary search \n')
    start = datetime.now().microsecond
    binary_search_loop(list, 0, len(list)-1, random_item)
    end = datetime.now().microsecond
    time_delta = end - start
    print(f'The time taken to perform binary search is {time_delta} microseconds')
    create_separation()
    return time_delta


    
def program_one():
    list_length = get_list_length()
    list = create_ordered_list(list_length)
    random_item = select_random(list)
    time_delta_normal = normal_iteration(list, random_item)
    time_delta_binary = binary_search(list, random_item)
    print('program1 complete')

def program_two():
    print('program two is not available yet')
    main()

def main():
    """
    Main function used for the running of the program
    """
    direction = welcome_user()
    if direction == 'program':
        program_type_selection = program_type()
        if program_type_selection == 'type_one':
            type_selection = program_one()
        elif program_type_selection == 'type_two':
            type_selection = program_two()
        else:
            instructions()
    else:
        instructions()
        

main()


