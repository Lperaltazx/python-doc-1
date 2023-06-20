#in-class exercise 1#
#create a format statement that ask for color, year, make, model and print out the results#

name = input("what is thy name?: ")
color = input("what is the color of your steed?: ")
year = input("how old is your steed?: ")
model = input("what type of steed do you have?: ")
results = f"{name}, your {year} {model} color is {color}"

print(results)

#if statment#

num1 = 3
num2 = 9

if num2 == num1:
    print('Equal Values')
else:
    print("Not Equal")

if num2 >= num1:
    print("Num2 is greater")
elif num1 <= num2:
    print("Num1 is less than")

#is keywords#

num3 = 12

if num3 is 12:
    print("This is the exact number/object")

#in keyword

char_name = "link"

if "link" in char_name:
    print("the legendary warrior")

#not in keyword

nintendo_char = "link"

if 'a' not in nintendo_char:
    print("a is NOT here")

#in class exercise 2
#as user for input, check to see if the letter 'p' is in the input

game=input("what is your favorite game")
result_string = "{} this is the best character".format(game)
print(result_string)

if 'p' not in game:
    print("p is Not there")

#Using and/or with if ststements
num_11 = 12
num_12 = 1
num_13 = 10
num_14 = 1

if num_11 / 5 == num_12 and num_14:
    print("True and False")

if num_11 > num_12 or num_13 == num_14:
    print("True and False")

#Elif Statements
first_name = "link"

if first_name == 'zelda':
    print("ahh uga link")
elif first_name != 'link':
    print("ahh uhhgg NOT link")
else:
    print("aah ehhg link")

#for loops

name = "Cap Falco"

for letter in name:
    print(letter)

for i in range(len(name)):
    print(name[i])

#continue Statment

for i in range(30):
    if i == 3:
        continue
    print(i)


#Break Statement
for i in range(30):
    if i == 3:
        break
    print(i)

#Pass Statement

for i in game:
    pass

#Double for Loop

for i in range(4):
    for j in range(4):
        print("i = ", i, "j =", j)

#while loops

num = 0
while num < 10:
    print(num)
    num += 1

#Looping while true
game_over = False

while True:
    print("You Died")
    if game_over == False:
        break


#while & loops used Together

num = 0 

while num < 5:
    print("\n while loop Iteration: " + str(num))

    for i in range(2):
        print("For loop Iteration: ", str(i))
    
    num += 1

#Built in function

#range()

for i in range(2, 20, 2):
    print(i)

#len()

name = "link"

length = len(name)
print(length)

#help()

help(range)


#isinstane()


if isinstance(4.5,float):
    print("This number is a float type")

#abs()

print(abs(-5))

#Try and except

try:
    number_test = 0
    input_num = int(input('take a guess'))
    if input_num != number_test:
        input_num = input_num + number_test
        print("your number has been chosen: " + str(input_num))

except:
    print('oops it broke ERROR')

#list

l_1 = []

names = ['zelda','link','ganon', "luis",'mason']

print(names)

#indexing a list

print(names[0])
print(name[1:])
print(name[:2])
print(names[1::2])
print(names[::-1])

#.append()

names.append('goron')
print(name)

#.insert()
names.insert(2,'zack')
print(names)

#.pop()

print(names.pop(2))

#.remove()

while 'zack' in names:
    names.remove('zack')
print(names)

#del()

del(names[2])
print(names)

#concatenating two lists

l_2 = [0,1,2]
l_3 = [3,4,5]
large_list = l_2 + l_3
print(large_list)

#lists within list

names = ["link", "zelda", "goron"["ganon","fae","luis"]]

print(names)
print(names[3][1])

#looping through list

for i in range(len(names)):
    print(names[i])

for i in names:
    print(i)

#exorcise 1
cube = 1000
for i in range(1001):
    if i == 5:
        continue
    print(i)
#exercise 2

for Number in range (1, 102):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break
    if (count == 0 and Number != 1):
        print(" %d" %Number, end = ' ')

#exercise 3

age = int(input("how old are you"))
if age <= 17:
    print("kids")
elif age >17 and age <= 65:
    print("adult")
else:
    print("seniors")