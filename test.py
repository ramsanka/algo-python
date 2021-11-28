from random import shuffle
from math import sqrt


msg = "Hello World"
print(msg)
msg.lower()
print('hello world')
print("I'm going on a run")
print(len('I am'))
mystring = 'abcdef'
print(mystring[3:5])
print(mystring[::-1]) 
print(mystring.upper())
print('2'+'3')
print(23)
print(mystring.split('d')) #breaking the string to list.
print('the {1} {0} {0}'.format('fox','quick','brown'))
print('the {f} {f} {f}'.format(f='fox',b='boy',c='cat'))
num_list = ['1','2','3','6','5']
print(num_list)
print(type(num_list.sort()))
print(num_list)

funny_list = ['ram','1','san','3']
funny_list.sort()
print(funny_list)  #sort data is based on number and characters


prices_lookup = {'apple':'1','banana':'2'}
print(prices_lookup['apple'])
#dictionary
d = {'k1':123,'k2':[0,1,2],'k3':{'ram':1,'dan':2}}
print(d['k3']['dan'])

d['k4']='NEW_VALUE'
print(d)

print(d.items())

#tuples
t = (1,2,3)
mylist = [1,2,3]

print(type(t))
print(type(mylist))
print(len(t))

#slicing and indexing.

t1 = ('a','b','a')
print(t1.count('a'))

#Sets
#unordered unique

myset = set()
myset.add(1)

print(myset)

myset.add(1)
myset.add(2)
mylist = [1,1,1,1,1,1,3,3,3]
#typecasting the list to set to get the list of
#the unique values.
print(mylist)
print(set(mylist))
print(myset)
myset.remove(1)
print(myset)

myfile = open('C:\\Users\\sankram\\Desktop\\GSTD.txt')
with open('C:\\Users\\sankram\\Desktop\\GSTD.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)



print('hello'=='hello')
print('hello'=='Hello')

print(1==1 and 1<3)
print(1<2<3)
print(1<2 and 2>3)
print(1<2 or 2>3)

print(not(1<2))

hungry = 2
if hungry == 1:
    print('fucking true')
elif hungry == 2:
    print('number 2')
else:
    print('feed me')



my_iterable = [1,2,3,4]
for item in my_iterable:
    print(item)

for jelly in my_iterable:
    print('python rocks')

for num in my_iterable:
    if num % 2 == 0:
        print(num)
    else:
        print(f'odd number: {num}') #fprints.. f {num}


for let in 'Hello World':
    print(let)


for _ in 'Hello World':
    print('cool')

tup = (1,2,3)

for item in tup:
    print(item)

d = {'k1':4,'k2':2,'k3':3}

for values in d.values():
    print(values)

while hungry:
    print('hungry')
    hungry = False
else:
    print('not hungry')

#while loop

#break continue pass

x = [1,2,3]

for item in x:
    pass

print('end of the for loop')

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)

x = 2
while x < 5:
    print(x)
    x += 1
        
index_count = 0

index = 0
word = 'abcdef'
for letter in word:
    print(word[index])
    index += 1
    
#from <lib> import <function>
#from random lib import shuffle function
ram_list  = [1,2,3,4,5]
shuffle(ram_list)

print(ram_list)

#typecast the input output -- always return a string.
result = input('Enter a number')
print(result)
print(type(result))

mylist = []
for letter in mystring:
    mylist.append(letter)

st = 'for the love of god, check and work on your future'
print(st)

for word in st.split():
    if word[0].lower() == 'f':
        print(word)

print(list(range(0,11,2)))

list = [x for x in range(1,51) if x%3 == 0]
print(list)
help(mylist.insert)


#Nov22nd Python class.

def hello_ram(name,num1,num2):
    print("hello" + name)
    return num1+num2


number = hello_ram('jose',1,2)
print(number)

print(hello_ram)

def check_list(list_num):
    #placeholder variable.
    even_numbers = []

    for number1 in list_num:
        print(number1)
        if number1 % 2 == 0:
            even_numbers.append(number1)
        else:
            pass #important change to ensure that for loop continues.
    return even_numbers

list1 = [5,5,5,5,5,5,2]
print(check_list(list1))


stock_prices = [('appl',200),('goog',400),('micro',500)]
for ticker,price in stock_prices:
    print(price+(0.1*price))

#nov23

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

example = [1,2,2,3,3,50]
result = shuffle_list(example)
print(result)


def player_guess():

    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number")

    return int(guess)

guess_return = player_guess()
print(guess_return)

#Nov 24
#arbitary number of args.

def myfunc(a,b):
    return sum((a,b)) * 0.5

#positional arguments.
#multiple positional arguments.

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)

myfunc(10,20,fruit='apple',vegetable='tomato')

#map function
#format of the map function.
#map(function_name, arguments)
#map will iterate through the list.

my_nums = [1,2,3,4]

for item in map(sqrt,my_nums):
    print(item)

#filter

mynums = [1,2,3,3,4]
def check_num(num):
    return num%2 == 0

print('filter function')
for n in filter(check_num, mynums):
    print(n)

print('lambda function')
#lambda
#anonymous function.
#format lambda argument:expression
#throwaway function.

names = ['Andy','Eve','Sandy']

for items in map(lambda name:name[1],names):
    print(items)

square = lambda num: num ** 2

result1 = map(lambda num:num**2,mynums)
for items in (result1):
    print(mynums)
    print(items)

x = 25
def printer():
    x =50
    return x

print(x)

def vol(rad):
    return (4/3) * (3.14) * (rad**3)

print('volume of the sphere')
print(vol(3))

def ran_check(num,low,high):
    if (low<num<high):
        return True
    return False


def ran_check_1(num,low,high):
    return(num in range(low,high+1))

print(ran_check_1(11,4,10))
num = 0
low = 190
print(f'{num} is in range of {low}')

#OBject oriented programming.
#classes and associated methods/functions.

class Sample():
    pass

my_sample = Sample()

print(type(my_sample))



