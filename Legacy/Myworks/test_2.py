import csv
import os


def IsPalindrone(s):
    ns = [letter.lower() for letter in s if letter.isalnum()]

    if ns[::-1] == ns:
        return 'Y'
    else:
        return 'N'


def CombineString(a, b):
    l = max(len(a), len(b))

    res = ''

    for i in range(l):
        try:
            l1 = a[i]
        except IndexError:
            l1 = ''
        try:
            l2 = b[i]
        except:
            l2 = ''

        res = res + l1 + l2

    return (res)


with open('/Users/mbheri/PycharmProjects/cbdev/pyworks/00-Python Object and Data Structure Basics/hello.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    writeCSVRow = []
    col2 = []
    for row in readCSV:
        row_3 = CombineString(row[0], row[1])
        print(row[0], row[1], row_3, IsPalindrone(row_3))
