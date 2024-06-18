# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#random module to select random number from list length
import random
#date time module to calculate time deltas between searches
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
        while learn_or_play != 'y' or 'n': #loops if user inputs unknown entry into console
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
    Function to ask the user what program type they would like to play.
    Program 1 is using search methods to iterate through a user specified list length for a random number
    and provides the time delta between the two methods.

    Program 2 takes a user specified list lengh and iterates through it normally and using binary search 
    for each of the items within the list. It provides the user with x and y data to plot the result on a graph
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
         while program_type != '1' or '2' or 'instructions': #loops if user inputs unknown entry to console
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
    print('Instructions') #to be completed
    create_separation()
    print('If you would like use Search Methods on a single user selected list length enter 1.')
    print('If you would like to use use search methods to generate x and y data enter the number 2.') 
    print('Finally, if you would like to end this program type end into the console')
    user_selection = input()
    if user_selection == '1':
        program_one()
    elif user_selection == '2':
        program_two()
    elif user_selection == 'end':
        exit()
    else:
        while user_selection != '1' or '2' or 'instructions' or 'end': #loops if user provides unknown input
            print('It seems like you have not entered a correct input. Please enter the number 1 to If you would like use Search Methods on a single user selected list length enter 1, if you would like to use use search methods to generate x and y data enter the number 2. Finally, if you would like to end this program type end into the console')
            second_user_input = input()
            if second_user_input == '1':
                program_one()
            elif second_user_input == '2':
                program_two()
            elif second_user_input == 'end':
                exit()

def get_list_length():
    """
    Function used to obtain the users desired list length between 100 and 10000000
    will convert to int and assess if within the specified values

    10 million selected as a reasonable list length for program to run in a short time frame
    but also provide reaonable output
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
        while list_request_num < 100 or list_request_num > 10000000: #prevents user from inputing list length greater than or shorter than intended
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

def compare_time_delta (normal, binary):
    """
    Function to calculate the time difference between normal iteration and binary search 
    """
    time_taken = normal - binary
    return time_taken

def time_delta_realisation(time, list_length, random_item):
    """
    Function used to take the time delta data and provide the user with feedback. 
    This function also coverts the microseconds into seconds and minutes to further demostrate the differences 
    in search methods
    """
    print(f'The time difference between binary search and normal iteration is {time} when searching a list made up of {list_length} items and a randomly selected search item of {random_item}')
    create_separation()
    time_over_hnths = time * 100000
    time_seconds = time_over_hnths * 0.0000001
    time_min = time_seconds / 60
    print(f'Over 100000 iterations through the same list this would equate to {round(time_seconds, 2)} seconds or {round(time_min, 2)} minutes. Rounded to two decimal places')
    create_separation()

def graph_interval(length):
    """
    Function used to calculate the most appropriate interval for x and y axis such that there are 
    50 values on each axis 
    """
    interval = int(length) // 50
    return interval

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

def x_axis_generation(list, interval):
    """
    Function to generate the the x axis data values
    """
    x_axis = list[0: -1: interval]
    return x_axis

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

def program_two_results(normal, binary, length):
    """
    Function taking the two results from the search data and displaying them such that the user can read
    tabulate the data
    """
    print(f'The below list contains 50 data points of the time it has taken to search for 50 different (but evenly) spaced index items within a list length of {length} by normal iteration through the list')
    print('In shorter list lengths you should see the time taken is fairly steady but for long list lengths the time timen increases at roughly equal intervals.')
    create_separation()
    print(normal)
    create_separation()
    print(f'The below list contains 50 data points of the time it has taken to search for 50 different (but evenly) spaced index items within a list length of {length} using binary search')
    print('Regardless of list length you should see the time taken remaining stetady regardless of the item searched for. In longer list lengths this should be significantly shorter than normal iteration')
    create_separation()
    print(binary)

def program_complete():
    """
    Followingf the completion of program 1 and program 2 this function provides the user with options on
    running program1 or 2 again, reading the instructions or ending the program
    """
    print('Thank you for using search methods. I hope you found the result interesting and informative.')
    create_separation()
    print('If you would like use Search Methods on a single user selected list length enter 1.')
    print('If you would like to use use search methods to generate x and y data enter the number 2.')
    print('If you would like to read the again type instructions into the console.') 
    print('Finally, if you would like to end this program type end into the console')
    user_selection = input()
    if user_selection == '1':
        program_one()
    elif user_selection == '2':
        program_two()
    elif user_selection == 'instructions':
        instructions()
    elif user_selection == 'end':
        exit()
    else:
        while user_selection != '1' or '2' or 'instructions' or 'end':
            print('It seems like you have not entered a correct input. Please enter the number 1 to If you would like use Search Methods on a single user selected list length enter 1, if you would like to use use search methods to generate x and y data enter the number 2. If you would like to read the instructions type instructions into the console. Finally, if you would like to end this program type end into the console')
            second_user_input = input()
            if second_user_input == '1':
                program_one()
            elif second_user_input == '2':
                program_two()
            elif second_user_input == 'instructions':
                instructions()
            elif second_user_input == 'end':
                exit()

    
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



