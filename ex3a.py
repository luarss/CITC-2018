# CITC Python A
# Done by:
# Luar Shui Song

# Requirements
# Write a python program that generates a list containing ints
# of random values.

# Input: List length and range
# Output List, length, largest, smallest, sum of int, average of ints

from random import randint

def print_statements (rand_list, length, big, small, sum_list, avg_list):
    # print all statements given results
    print('Sequence: ' + str(rand_list))
    print('\nList length: %d' % list_length)
    print('Largest integer: %d' % big)
    print('Smallest integer: %d' % small)
    print('Sum :' + str(sum_list))
    print('Average: ' + str(avg_list))

    
def rand_gen (length, smallest, biggest):
    global rand_list
    # generates random number list
    temp = randint(smallest, biggest)
    big = temp
    small = temp
    
    for i in range (0,length):
        rand_list.append(temp)
        temp = randint(smallest, biggest)
        if temp > big: big = temp
        if temp < small: small = temp

    return big, small

#Error checking for inputs (int only)
while True:
    try: 
        list_length = int(input('Please enter the length for the list'))
        lower_bound = int(input('Please enter the lower bound for the list'))
        upper_bound = int(input('Please enter the upper bound for the list'))
        break
    except ValueError:
        print('Please enter an integer')

rand_list = []
big, small = rand_gen(list_length, lower_bound, upper_bound)
sum_list = sum(rand_list)
avg_list = sum_list / list_length

print_statements(rand_list, list_length, big, small, sum_list, avg_list)
