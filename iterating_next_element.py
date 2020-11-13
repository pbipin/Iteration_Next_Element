"""
Author: Bipin P. (mailto: bipinp2013@gmail.com)
http://iambipin.com
101010101    10  101010101    10  101     10    101010101
1010101010   10  1010101010   10  1010    10    1010101010
10      101  10  10      101  10  10 01   10    10      101
10      101  10  10      101  10  10  10  10    10      101
1010101010   10  1010101010   10  10   01 10    1010101010
1010101010   10  101010101    10  10    1010    101010101
10      101  10  10           10  10     010    10
10      101  10  10           10  10      10    10
1010101010   10  10           10  10      10    10
101010101    10  10           10  10      10    10  10
Python Program to access the next element while iterating
"""
list1 = [1, 8, 3, 4, 9, 6]

print(f'The elements of list: ')
for index, elem in enumerate(list1):
    if(index<(len(list1)-1)):
        current_elem = elem
        next_elem = list1[index+1]        
        print(current_elem, end=' ')
    else:
        print(elem)
