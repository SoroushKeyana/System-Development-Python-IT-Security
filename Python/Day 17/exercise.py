"""
s = 'Python'

print(s[4])
print(s[:4])
print(s[1:4])
print(s[::-1])

l = [3,7,[1,4,'hello']]

l[2][2] = "goodbye"
print(l)
d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

list = ["soroush", "barsam", "someyeh"]

name = input("What is your name? ")
name = name.lower()

if name in list:
    print('hej', name.capitalize())
else:
    print("nej", name)

for item in list:
    print(item)
age = 4
name = "Sammy"

print("Hello my dog's name is {} and he is {} years old" .format(name,age))

def arrayCheck(list):
    if 1 in list and 2 in list and 3 in list:
        print(True)
    else:
        print(False)

arrayCheck([1, 1, 2, 3, 1]) 
arrayCheck([1, 1, 2, 4, 1]) 
arrayCheck([1, 1, 2, 1, 2, 3])
def stringBits(string):
    text = ""

    for i in range(0,len(string),2):
        text = text + string[i]
    print(text)


stringBits('Hello')
stringBits('Hi') 
stringBits('Heeololeo')
stringBits('Soroush')
def doubleChar(string):
    newString = ''
    for i in range(0,len(string)):
        newString += string[i] + string[i]
    print(newString)

doubleChar('The')
doubleChar('AAbb') 
doubleChar('Hi-There')
"""
def count_evens(list):
    count = 0
    for item in list:
        if item % 2 == 0:
            count = count + 1
    print(count)

count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5])


