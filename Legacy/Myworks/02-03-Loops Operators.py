import math
list1 = [32,234,1,4,23,53,1,231,1]

print('Elements in the list\n',list1)

print('\n-----For loop elements\-----')
for item in list1:
    print (item)

#sum elemenmts in a string for each iteration
print('\n---------Sum for each elements----------')

prev = 0
for item in list1:
    #print (type(item))
    #if type(item) == "<class 'int'>":
    prev = item + prev
    print(prev)
#


# string iteration
print('\n-------------Iterate letters in string---------')
Str = 'This is str'
for letter in Str:
    print(letter)


# tupple iteration

print('\n--------- Tupples---------')
tup = (1,2,3,5,5,5)

for t in tup:
    print(t)


# dictionaries
print ('\n------Dictionaries -------')
d ={'k1':1, 'k2':3,'k3':2}

print('keys in dict')
for key in d:
    print (key)

print('items in dict')

print(d.items())

for k,v in d.items():
    print (k,v)

print (list(d.keys()))

print(sorted(d.values()))



###While loop

#list all even numbers up to 100
print('\n--------While loop statements for even and odd-----')
x = 0
e =[]
o=[]

while (x<=100):
    if (x>0 and x%2==0):
        e.append(x)
    elif (x>0 and x%2==1):
        o.append(x)
        #l = l.append(x)
    x = x + 1

print('Even list', e)
print('Odd list ', o)


######## Range
print (range(0,11))
l = list(range(0,12,2))

print(l)


for i in range(0,11):
    print(i)


#### enumerate contents in file
print('----------Print by enumerations\n')
file_test= open('test.txt','w')

file_test.write('Adress-7077 alvern st, a213\n'
        'City-Los angeles\n'
        'State-CA\n')

file_test = open('test.txt','a')
file_test.write('Country-USA')

file_test = open('test.txt','r')

for i,line in enumerate(file_test.readlines()):
    print(i+1, line)

file_test.seek(0)

for i , letter in enumerate(file_test.readline()):
    print(i+1, letter)


print (enumerate('1fqwe3'))