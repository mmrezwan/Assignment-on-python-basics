#1. Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

input_string = input('Please input the String: ')

cnt = dict()


for a in input_string:
    if a in cnt.keys():
        cnt[a] +=1 
    else :
        cnt[a] = 1 


cnt = dict(sorted(cnt.items(), key=lambda x: (-x[1], x[0])))

print(cnt)


#2. Write a Python program to check if a given key already exists in a dictionary.

input_keys = input('Please input the keys of the dictionary seperated by comma: ')

input_values = input('Please input the values of the dictionary seperated by comma: ')

Dict = dict(zip(input_keys.split(','), input_values.split(',')))


check = input('Please input the checking string: ')

print('Exists' if check in Dict else 'Not Existis')


#3. Write a Python program that accepts a sequence of comma-separated numbers from the
#user and generates a list and a tuple of those numbers.
#Sample data : 1, 5, 7, 23
#Expected Output :
#List : ['1', ' 5', ' 7', ' 23']
#Tuple : ('1', ' 5', ' 7', ' 23')

input_values = input('Please input the values of the list/tuple seperated by comma: ')

print("List :" , input_values.split(','))
print("Tuple :" , tuple(input_values.split(',')))


#4. Write a Python program to calculate the number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days

from datetime import datetime

_1 = input('Please input the first date in year,month,day format: ')

_2 = input('Please input the 2nd date in year,month,day format: ')


Date1_list = [int(x) for x in _1.split(',')]

Date2_list = [int(x) for x in _2.split(',')]

dt1 = datetime(*Date1_list)
dt2 = datetime(*Date2_list)

print((dt2 - dt1).days, 'days')


#5. Write a Python program to solve (x + y) * (x + y).
#Test Data : x = 4, y = 3
#Expected Output : (4 + 3) ^ 2) = 49

x = int(input('Please input x: '))
y = int(input('Please input y: '))

print("(" + str(x), " + " + str(y) + ") ^ 2 = " , (x+y) * (x+y))


#6. Write a Python program to compute the future value of a specified principal amount,
#rate of interest, and number of years.
#Test Data : amt = 10000, int = 3.5, years = 7
#Expected Output : 12722.79

input_values = input('Please input P, r, t in comma seperated values: ')

P, r, t = [float(x) for x in input_values.split(',')]

FV = P*((1+(0.01*r)) ** t)

print(round(FV,2))


#7. Write a Python program that removes duplicate elements from a given array of numbers so
#that each element appears only once and returns the new length of the array.
#Sample Input: [0,0,1,1,2,2,3,3,4,4,4]
#Sample Output:
#The list of unique numbers: [0,1,2,3,4]
#length of the unique list : 5

input_values = input('Please input list elements in comma seperated values: ')

new_list = list(set([int(x) for x in input_values.split(',')]))

print("The list of unique numbers :", new_list)
print("length of the unique list :", len(new_list))


#8. Write a Python program to sort (ascending and descending) a dictionary by key value.

input_keys = input('Please input the keys of the dictionary seperated by comma: ')

input_values = input('Please input the values of the dictionary seperated by comma: ')

Dict = dict(zip(input_keys.split(','), [int(x) for x in input_values.split(',')]))


print("Ascending : ", dict(sorted(Dict.items(), key=lambda x: x[1])))

print("Descending : ", dict(sorted(Dict.items(), key=lambda x: x[1], reverse = True)))


#9. Write a Python program to add key to a dictionary. Go to the editor
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

Dict = {0: 10, 1: 20}
Dict[2] = 30

print(Dict)


#10. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
#Sample Python dictionary data and list labels:
#exam_data = {'name': ['Arif', 'Asir', 'Arik', 'Anis', 'Anil', 'Ashish', 'Anahi', 'Alia', 'Alvin', 'Asim'],
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
import numpy as np

exam_data = {
            'name': ['Arif', 'Asir', 'Arik', 'Anis', 'Anil', 'Ashish', 'Anahi', 'Alia', 'Alvin', 'Asim'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
            }


labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame.from_dict(exam_data)

df.index = labels
df
