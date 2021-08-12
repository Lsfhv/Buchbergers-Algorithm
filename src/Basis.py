import re
import numpy

# Everything is done with the lexicographic ordering x > y > z > ...


# separates polynomials into a list
import numpy as np


def polynomial(input):
    # parse for polynomials
    polynomials = []

    x = re.split('\(|\)|,', input)
    x = removeblankss(x)
    for i in x:
        polynomials.append(i.strip())
    return polynomials


# separates polynomial into monomials with signs
def monomial(input):
    monomials = []

    for i in input:
        monomials.append(i.split())

    for i in monomials:
        for j in range(0, len(i)):
            if (i[j])[0] == '-' or (i[j])[0] == '+':
                try:
                    (i[j])[1]
                    if (i[j])[0] == '-':
                        (i[j]) = (i[j]).replace('-', '', 1)
                        i.insert(0, '-')
                    else:
                        (i[j]) = (i[j]).replace('+', '', 1)
                        i.insert(0, '+')
                except:
                    continue

    return monomials


# removes '' entries from a list
def removeblankss(input):
    lst = []
    for i in input:
        if i != '':
            lst.append(i)

    return lst


# how many variables are we in?
def dimension(input):
    global s
    s = set()

    lst = list(input)

    for i in range(0, len(lst)):
        if lst[i] == '(' or lst[i] == ')' or lst[i] == '+' or lst[i] == '-' or lst[i] == ',' or lst[i] == '^' or lst[
            i] == ' ' or lst[i] == '2' or lst[i] == '3':
            continue
            # ignore
        else:
            s.add(lst[i])

    return len(s)


def S(polynomial1, polynomial2):
    # 1 <

    # print(polynomial1)
    # print(polynomial2)

    # search for the leading term

    if polynomial1[0] != '-' and polynomial1[0] != '+':
        leading_term_1 = polynomial1[0]
    else:
        leading_term_1 = polynomial1[1]

    if polynomial2[0] != '-' and polynomial2[0] != '+':
        leading_term_2 = polynomial2[0]
    else:
        leading_term_2 = polynomial2[1]

    # find powers in terms of tuples
    tupledimension

    find_power(leading_term_1, leading_term_2)


def find_power(leading_term_1, leading_term_2):
    lst1 = list(leading_term_1)
    lst2 = list(leading_term_2)

    filtered1 = {}
    filtered2 = {}

    for i in lst1:
        if i == 'x' or i =='y':
            filtered1[i] = 1

    for i in lst2:
        if i == 'x' or i =='y':
            filtered2[i] = 1



    #

    counter = 0
    while counter < len(lst2):
        try:
            lst2[counter+1]
            if lst2[counter+1] == '^':
                filtered2.update({lst2[counter], filtered2[lst2[counter]] + lst2[counter+2]-1})
                print(filtered2['x'])
                counter = counter+2
        except:
            continue

        counter = counter+1

    print(filtered1)
    print(filtered2)




def computation(monomial_list):
    for i in range(0, len(monomial_list) - 1):
        for j in range(i + 1, len(monomial_list)):
            S(monomial_list[i], monomial_list[j])

    return 10


input = '(x - y^3 , -x^2 + xy^2)'
tupledimension = dimension(input)

polynomiallist = polynomial(input)
monomiallist = monomial(polynomiallist)
computation(monomiallist)

# print()
# print("Monomials: ")
# print(monomiallist)
