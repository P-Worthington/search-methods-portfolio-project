#random module to select random number from list length
import random
#date time module to calculate time deltas between searches
from datetime import datetime

#creates list of integers based on inputs
def create_ordered_list(list_length_request):
    """
    Function to create ordered list of numbers using a while loop based
    on users input
    """
    i = 1
    ordered_list = [] 
    while i < list_length_request + 1:
        ordered_list.append(i) # add to ordered lsit
        i += 1 # increases list length by 1 integer
    return ordered_list

# Welcomes user and allows selection of program or instructions
def welcome_user():
    """
    Function to run first on the console and welcome the user a quesiton is 
    asked if they want to learn more about binary search and the function 
    of this program and if the user wants to use the program. 
    """
    create_separation()
    print('Hello welcome to Search Methods. \n')
    print('If this is your first time using Search Methods it is recommended that you read the instructions. \n')
    create_separation()
    print('Would you like to read the instructions? y/n')
    learn_or_play = input('\n')
    if learn_or_play == 'y':
        print('Loading Instructions...')
        return 'intructions'
    elif learn_or_play == 'n':
        print('Loading Program...')
        return 'program'
    else:
        while learn_or_play != 'y' or 'n': #loops if user inputs unknown entry into console
            print('Please enter the character y and press enter if you would like to learn more about binary search or the character n if you would like to run the program')
            next_input = input('\n')
            if next_input == 'y':
                print('Loading Instructions...')
                return 'intructions'
                
            elif next_input == 'n':
                print('Loading Program...')
                return 'program'

# runs following the welcome_user() function and allos selection of program type 
def program_type():
    """
    Function to ask the user what program type they would like to play.
    Program 1 is using search methods to iterate through a user specified list length for a random number
    and provides the time delta between the two methods.

    Program 2 takes a user specified list lengh and iterates through it normally and using binary search 
    for each of the items within the list. It provides the user with x and y data to plot the result on a graph

    Program3 takes a user specifiec list length and searches the -1 index item of 50 shorter list lengths and provides
    the user with the results in a format that can be graphed 
    """
    print('Enter the number 1 to use Search Methods on a single user selected list length.\n')
    print('Enter the number 2 to use Search Methods to generate x and y data on a single specified list length.\n') 
    print('enter the number 3 to use search methods to search for an item across multiple list lengths or:\n') 
    print('type instructions if you would like to read the instructions.\n')
    program_type = input('\n')
    if program_type == '1':
        return 'type_one'
    elif program_type == '2':
        return 'type_two'
    elif program_type == '3':
        return 'type_three'
    elif program_type == 'instructions':
        return 'instructions'
    else:
         while program_type != '1' or '2' or 'instructions': #loops if user inputs unknown entry to console
            print('Enter the number 1 to use Search Methods on a single user selected list length.\n')
            print('Enter the number 2 to use Search Methods to generate x and y data on a single specified list length.\n') 
            print('enter the number 3 to use search methods to search for an item across multiple list lengths or:\n') 
            print('type instructions if you would like to read the instructions.\n')
            next_input = input('\n')
            if program_type == '1':
                return 'type_one'
            elif program_type == '2':
                return 'type_two'
            elif user_selection == '3':
                return 'type_three'
            elif program_type == 'instructions':
                return 'instructions'

#instructions for program type 
def instructions():
    """
    Function to teach the user about bianry searches and the program itself 
    will lead the user onto running the program and direct them to the readme file 
    if they want to learn further
    """
    create_separation()
    print('Search Methods is a learning program which demonstrates the differences between normal iteration through a list and binary search. \n')
    print('Normal iteration through a list starts at the first index item and moves through the list in order. \n')
    print('Binary search splits the list an half and half again until the result is found. \n')
    print('This python project uses the datetime module at its core to time the computer \n performing normal iteration and binary search. \n')
    print('If you would like to learn more about this program please read the README.md \n file attached to the repositiory. ')
    create_separation()
    print('Search Methods utilises three program types to search and provides the results. \n')
    print('Program 1 - Takes a specified list and finds a random number within. \n')
    print('Program 2 - Takes a specified list and searches for 50 numbers within that \n specific list. \n')
    print('Program 3 - Takes a user specified list and searches for the last item in that \n list and 49 other list length. \n')
    create_separation()
    print('Enter the number 1 to use Search Methods on a single user selected list length.\n')
    print('Enter the number 2 to use Search Methods to generate x and y data on a single \n specified list length.\n') 
    print('enter the number 3 to use search methods to search for an item across multiple \n list lengths or:\n') 
    print('If you would like to end this program type end into the console')
    user_selection = input('\n')
    if user_selection == '1':
        program_one()
    elif user_selection == '2':
        program_two()
    elif user_selection == '3':
        program_three()
    elif user_selection == 'end':
        exit()
    else:
        while user_selection != '1' or '2' or '3' or 'instructions' or 'end': #loops if user provides unknown input
            print('It seems like you have not entered a correct input.\n')
            print('Enter the number 1 to use Search Methods on a single user selected list length.\n')
            print('Enter the number 2 to use Search Methods to generate x and y data on a \n single specified list length.\n') 
            print('enter the number 3 to use search methods to search for an item across \n multiple list lengths or:\n') 
            second_user_input = input('\n')
            if second_user_input == '1':
                program_one()
            elif second_user_input == '2':
                program_two()
            elif user_selection == '3':
                program_three()
            elif second_user_input == 'end':
                exit()

#asks user for the list length then would like th eprogram to run 
def get_list_length():
    """
    Function used to obtain the users desired list length between 100 and 10000000
    will convert to int and assess if within the specified values

    10 million selected as a reasonable list length for program to run in a short time frame
    but also provide reaonable output
    """
    print('Please input a list length integer between 100 (one hundred) and 10000000 \n (10 million).\n') 
    print('Any floats will be rounded to the nearest whole number')
    list_request = input('\n')
    while True:
        try:
            print('Please input a list length integer between 100 (one hundred) and 10000000 \n (10 million).\n') 
            print('Any floats will be rounded to the nearest whole number')
            list_request = input('\n')
            list_request_num = int(round(float(list_request)))
            break      
        except ValueError:
            print("Not an integer! Try again.")
            continue



    
    if list_request_num >= 100 and list_request_num <= 10000000:
        print(f'You entered {list_request_num}')
        print('Standby program may take some time if iterating through a very large list \n (greater than 1 million)')
        create_separation()
        return list_request_num
    else:
        while list_request_num < 100 or list_request_num > 10000000: #prevents user from inputing list length greater than or shorter than intended
            print('Please enter a number between 100 (one hundred) and 10000000 (10 million)')
            second_list_request = input('\n')
            second_list_request_num = int(round(float(second_list_request)))

            if second_list_request_num >= 100 and second_list_request_num <= 10000000:
                print(f'You entered {second_list_request_num}')
                return second_list_request_num
                break
   
#separation between prints 
def create_separation():
    """
    Function used to display 3 rows of full stops in the console
    Used to separate bulk pieces of text
    """
    print("................................................................................")


#uses random module to select item
def select_random(x):
    """
    Function used to select a random list index number within the user specified list length. 
    Uses random module imported from above
    """
    start = x[0]
    end = x[-1]
    random_list_item = random.randint(start, end)
    print(f'program will be looking for {random_list_item}')
    create_separation()
    return random_list_item

#searches a list one by one 
def normal_iteration(created_list, random_selection):
    """
    Function to iterate through a list in the traditional fashion by looping from start to finish
    """
    print('Performing normal iteration \n')
    start = datetime.now().microsecond
    for list_item in created_list:
        if list_item == random_selection:
            break
        end = datetime.now().microsecond
    end = datetime.now().microsecond
    if start > end:
        time_delta = start - end
    else:
        time_delta = end - start
    print(f'The time taken to perform normal iteration is {time_delta} microseconds')
    create_separation()
    return abs(time_delta)

#searches a list in binary fashion
def binary_search_loop(list, low, high, random_item):
    """
    Function to loop through the list and identify the searched for item
    """
 
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

#provides the binary search with the 4 inputs reaquired
def binary_search(list, random_item):
    """
    Function to set up binary_search_loops (above) and provide it with the 4 statments required
    """
    
    print('Performing binary search \n')
    start = datetime.now().microsecond
    binary_search_loop(list, 0, len(list)-1, random_item)
    end = datetime.now().microsecond
    if start > end:
        time_delta = start - end
    else:
        time_delta = end - start
    print(f'The time taken to perform binary search is {time_delta} microseconds')
    create_separation()
    return abs(time_delta)

#compares time taken differences. 
def compare_time_delta (normal, binary):
    """
    Function to calculate the time difference between normal iteration and binary search 
    """
    time_taken = normal - binary
    return time_taken

#used in conjuction with program 1 to put the data into perspective
def time_delta_realisation(time, list_length, random_item):
    """
    Function used to take the time delta data and provide the user with feedback. 
    This function also coverts the microseconds into seconds and minutes to further demostrate the differences 
    in search methods
    """
    print(f'The time difference between binary search and normal iteration is {time}') 
    print(f'when searching a list made up of {list_length} items')
    print(f'and a randomly selected search item of {random_item}')
    create_separation()
    time_over_hnths = time * 100000
    time_seconds = time_over_hnths * 0.0000001
    time_min = time_seconds / 60
    print(f'Over 100000 iterations through the same list this would equate to \n {round(time_seconds, 2)} seconds') 
    print(f'or {round(time_min, 2)} minutes. Rounded to two decimal places')
    create_separation()

#identifies interval size such that there are 50 data points
def graph_interval(length):
    """
    Function used to calculate the most appropriate interval for x and y axis such that there are 
    50 values on each axis 
    """
    interval = int(length) // 50
    return interval

#iterates through a list length normally for program 2 
def normal_iteration_for_graph(list, list_length, interval):
    """
    Function to control the operation of the normal iteration across the 50 intervals. 
    """
    time_delta_normal = []
    i = 1
    time_taken = []
    while i < list_length:
        start = datetime.now().microsecond
        for item in list:
            if item == i:
                break    
        end = datetime.now().microsecond
        if start > end:
            time_delta = start - end
        else:
            time_delta = end - start
        time_taken.append(time_delta)
        i += interval
    print("Normal search complete")
    create_separation()
    return time_taken

# generates data for the x axis in program 2
def x_axis_generation(list, interval):
    """
    Function to generate the the x axis data values
    """
    x_axis = list[0: -1: interval]
    return x_axis

# searches in binary fashion for program 2 
def binary_search_for_graph(list, list_length, interval):
    result = []
    i = 1
    while i < list_length:
        start = datetime.now().microsecond
        binary_search_loop(list, 0, len(list)-1, i)
        end = datetime.now().microsecond
        if start > end:
            time_delta = start - end
        else:
            time_delta = end - start
        result.append(time_delta)
        i += interval
    print("Binary search complete")
    create_separation()
    return result

# presents the reuslt from program 2 to the user 
def program_two_results(normal, binary, length):
    """
    Function taking the two results from the search data and displaying them such that the user can read
    tabulate the data
    """
    print(f'The below list contains 50 data points of the time it has taken to search \n for 50 items') 
    print(f'within a list length of {length} by normal iteration through the list')
    create_separation()
    print(normal)
    create_separation()
    print(f'The below list contains 50 data points of the time it has taken to search \n for 50 items')
    print(f'within a list length of {length} using binary search')
    create_separation()
    print(binary)

#searches in normal fashion in conjuction with program 3 
def normal_iteration_prog_3(created_list, end_index):
    """
    Function to iterate through a list in the traditional fashion by looping from start to finish
    """
    start = datetime.now().microsecond
    for list_item in created_list:
        if list_item == end_index:
            break
        end = datetime.now().microsecond
    end = datetime.now().microsecond
    if start > end:
        time_delta = start - end
    else:
        time_delta = end - start
    return abs(time_delta)

# loops through normal_interation_prog_3() 
def prog_3_search_normal(list_length):
    """
    Loops through normal iteration program 3 (above function) using the interval size
    """
    interval = graph_interval(list_length)
    time_taken = [0]
    i = interval
    while i < list_length:
        list = create_ordered_list(i)
        end_index = list[-1:]
        time_delta = normal_iteration_prog_3(list, end_index)
        time_taken.append(time_delta)
        i += interval
    print(f'Below is the time taken to iterate through differeing list lengths from')
    print(f'{interval} to {list_length} in intervals of {interval} using normal search')
    create_separation()
    print(time_taken)
    return time_taken

# loops different list lengths and provides them to the binary search function 
def binary_search_prog_3(list, random_item):
    """
    Function to set up binary_search_loops (above) and provide it with the 4 statments required
    used in conjuction with program 3 
    """
    
    start = datetime.now().microsecond
    binary_search_loop(list, 0, len(list)-1, random_item)
    end = datetime.now().microsecond
    if start > end:
        time_delta = start - end
    else:
        time_delta = end - start
    return abs(time_delta)

# preps the data types for the above function such that binary search can be performed
def prog_3_search_binary(list_length):
    """
    Function to set up the correct data types on each list length to perform binary search
    """
    interval = graph_interval(list_length)
    time_taken = [0]
    i = interval
    while i < list_length:
        list = create_ordered_list(i)
        end_index = list[-1:]
        string = str(end_index)
        new_string = string.replace("[", "")
        new_string_2 = new_string.replace("]", "")
        integer = int(new_string_2)
        time_delta = binary_search_prog_3(list, integer)
        time_taken.append(time_delta)
        i += interval
    create_separation()
    print(f'Below is the time taken to iterate through differeing list lengths from') 
    print(f'{interval} to {list_length} in intervals of {interval} using binary search')
    create_separation()
    print(time_taken)
    return time_taken

# function to run when users chosen program is complete and allows user to continue running results or end program
def program_complete():
    """
    Followingf the completion of program 1 and program 2 this function provides the user with options on
    running program1 or 2 again, reading the instructions or ending the program
    """
    print('Thank you for using search methods. I hope you found the result interesting and informative.')
    create_separation()
    print('Enter the number 1 to use Search Methods on a single user selected list length.\n')
    print('Enter the number 2 to use Search Methods to generate x and y data on a single \n specified list length.\n') 
    print('enter the number 3 to use search methods to search for an item across multiple \n list lengths or:\n')
    print('Finally, if you would like to end this program type end into the console')
    user_selection = input('\n')
    if user_selection == '1':
        program_one()
    elif user_selection == '2':
        program_two()
    elif user_selection == '3':
        program_three()
    elif user_selection == 'instructions':
        instructions()
    elif user_selection == 'end':
        exit()
    else:
        while user_selection != '1' or '2' or 'instructions' or 'end':
            print('It seems like you have not entered a correct input.')
            print('Enter the number 1 to use Search Methods on a single user selected list length.\n')
            print('Enter the number 2 to use Search Methods to generate x and y data on a single specified list length.\n') 
            print('enter the number 3 to use search methods to search for an item across multiple list lengths or:\n')
            second_user_input = input('\n')
            if second_user_input == '1':
                program_one()
            elif second_user_input == '2':
                program_two()
            elif user_selection == '3':
                program_three()
            elif second_user_input == 'instructions':
                instructions()
            elif second_user_input == 'end':
                exit()


 # main function to run the operation of program 1    
def program_one():
    """
    This function runs the operation of program 1 containing all of the functions required to provide the user with the
    intended output
    """
    list_length = get_list_length()
    list = create_ordered_list(list_length)
    random_item = select_random(list)
    time_delta_normal = normal_iteration(list, random_item)
    time_delta_binary = binary_search(list, random_item)
    time_taken = compare_time_delta(time_delta_normal, time_delta_binary)
    result = time_delta_realisation(time_taken, list_length, random_item)
    program_complete()

#main function to run the operation of program 2 
def program_two():
    """
    This function runs the operation of program 2 containing all of the functions required to provide the user with the
    intended output
    """
    list_length = get_list_length()
    list = create_ordered_list(list_length)
    interval = graph_interval(list_length)
    graph_result_normal = normal_iteration_for_graph(list, list_length, interval)
    x_axis_normal = x_axis_generation(list, interval)
    graph_result_binary = binary_search_for_graph(list, list_length, interval)
    program_two_results(graph_result_normal, graph_result_binary, list_length)
    program_complete()

#main program to run the function of program 3 
def program_three():
    list_length = get_list_length()
    time_dela_noraml = prog_3_search_normal(list_length)
    time_delta_binary = prog_3_search_binary(list_length)
    create_separation()
    program_complete()

#,main function for running of program 
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
        elif program_type_selection == 'type_three':
            type_selection = program_three()
        else:
            instructions()
    else:
        instructions()
        
#function call for main program
main()


