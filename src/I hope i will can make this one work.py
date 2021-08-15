import re


# polynomials broken down into monomials with respect to the signs
def polynomial(input):
    # parse for polynomials
    polynomials = []

    x = re.split('\(|\)|,', input)
    x = removeblankss(x)
    for i in x:
        polynomials.append(i.strip())
    return polynomials


def removeblankss(input):
    lst = []
    for i in input:
        if i != '':
            lst.append(i)

    return lst


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


def find_least_common_monic_term(monomial1, monomial2, polynomail1, polynomail2):
    # which variables show up?

    # print(monomial1,monomial2,polynomail1, polynomail2)

    first = {}
    second = {}

    # autpmatically infer it to be exponent of 1 if now power shows up
    for i in monomial1:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            first.update({i: 1})

    for i in monomial2:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            second.update({i: 1})

    for i in range(0, len(monomial1)):
        if monomial1[i] == '^':
            first.update({monomial1[i - 1]: int(monomial1[i + 1])})

    for i in range(0, len(monomial2)):
        if monomial2[i] == '^':
            second.update({monomial2[i - 1]: monomial2[i + 1]})

    # compare powers? find leasrt common monic??

    key_list = list(first.keys())
    least_common_monic = {}

    for i in key_list:

        if first[i] == second[i]:
            least_common_monic.update({i: first[i]})
        else:
            if int(first[i]) > int(second[i]):
                least_common_monic.update({i: first[i]})
            else:
                least_common_monic.update({i: second[i]})

    # the S function call M the least common monic
    # M/M1(M!)

    # print(first,second, least_common_monic)

    Sfucntion(least_common_monic, polynomail1, polynomail2)


def Sfucntion(LCM, polynomial1, polynomial2):
    print("Least Common Monic: ", LCM, "Polynomail 1:", polynomial1, "Polynomial 2: ", polynomial2)

    leadingterm1 = LT(polynomial1)
    leadingterm2 = LT(polynomial2)

    # prob wanna format into S function then compute

    # S(P1,P2) = (M/LT1)P1 - (M/LT2)P2



# find the leading term
def LT(p1):
    for j in p1:
        for i in j:
            if 'a' <= i <= 'z':
                return j

def addition(summand1, summand2):
    
    return True



# monomial1 = 'x^2y^5'
# monomial2 = 'x^3y^3'
#
# find_least_common_monic_term(monomial1,monomial2)


input = '(x^2y^5 - y^3 , -x^3y^3 + xy^2)'
monomial_list = monomial(polynomial(input))
find_least_common_monic_term( ( monomial_list[0])[0],(monomial_list[1])[1] ,monomial_list[0], monomial_list[1])

