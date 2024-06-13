# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


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
    print('Search Methods takes a sorted string and iterates through it in two ways. A traditional looping method and binary search. It times the program during the iteration and returns the result and difference in time \n')
    print('Would you like to learn more about binary search? y/n')
    print('*Recommended if this is your first time using the program* \n')
    learn_or_play = input()
    if learn_or_play == 'y':
        print('Loading Instructions...')
        instructions()
    elif learn_or_play == 'n':
        print('Loading Program...')
    else:
        while learn_or_play != 'y' or 'n':
            print('Please enter the character y and press enter if you would like to learn more about binary search or the character n if you would like to run the program')
            next_input = input()
            if next_input == 'y':
                print('Loading Instructions...')
                instructions()
                break
            elif next_input == 'n':
                print('Loading Program...')
                break

def instructions():
    """
    Function to teach the user about bianry searches and the program itself 
    will lead the user onto running the program and direct them to the readme file 
    if they want to learn further
    """
    i = 1
    while i < 4:
        print("...............................................................")
        i += 1
    print('Instructions')

welcome_user()
