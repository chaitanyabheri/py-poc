#x = 5
#s = 'hello world'
#y = [1,2,3]
#
#print(type(x))
#
#print (type(s))
#
#print(type(y))
#
#
#
#o1 = type('X', (object,), dict(a='Foo', b=12))
#
#print (type(o1))
#print(vars(o1))
#
i1 = 'hello'
i2 = 'foobar'
#
#
v1 = i2
l = len(v1)
v2 =''
letter1 =''
pos1 =0

letter2 = ''
pos2 = 0

#
#print(l)
#

#find first oval and position

i=0

while i<l:
    #print ( v1[i] )
    if v1[i] in ('a','e','i','o','u'):
        letter1 = v1[i]
        pos1 = i
        break

    #v2 = v2+ v1[i]
    #print (v2)
    i= i+1

#2nd oval
i=-1

while i>-l:
    #print ( v1[i] )
    if v1[i] in ('a','e','i','o','u'):
        letter2 = v1[i]
        pos2 = i
        break

    #v2 = v2+ v1[i]
    #print (v2)
    i= i-1

pos2 = l + pos2

#print ('\n1st oval details ', letter1, pos1)
#print ('\n2nd oval details ', letter2, pos2)


#replace values

i=-1

v2=''
i=0

while i<l:
    #print ( v1[i] )
    if i ==pos1:
        v2 = v2+letter2
    elif i ==pos2:
        v2 = v2+ letter1
    else:
        v2 = v2  +v1[i]
    #print (v2, i, pos1,pos2)

    #v2 = v2+ v1[i]
    #print (v2)
    i= i+1

print ('\n1st oval details ', letter1, pos1)
print ('\n2nd oval details ', letter2, pos2)
print ('\n1st letter ', v1)
print ('\n2nd letter ', v2)

myTuple = ("John", "Peter", "Vicky")

x = ",".join(myTuple)

print(x)

print (v1)



strlist = list(v1)

strlist[pos1],strlist[pos2] =strlist[pos2], strlist[pos1]

print(strlist)
print("".join(strlist))


