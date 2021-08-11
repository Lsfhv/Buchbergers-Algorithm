import re


# Everything is done with the lexicographic ordering x > y > z > ...



# separates polynomials into a list
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


def tuplelength(input):

    tupledimension = 0
    set = {}


    lst = list(input)

    for i in range(0, len(lst)):
        if lst[i] == '(' or lst[i] == ')' or lst[i] == '+' or lst[i] == '-' or lst[i] == ',' or lst[i] == '^' or lst[i] == ' ' or lst[i] == '2' or lst[i] == '3':
            continue
            # ignore
        else:
            print(lst[i])

    return len(set)



def S(polynomial1, polynomial2):
    # 1 < 2
    print(polynomial1)
    print(polynomial2)

    # search for the leading term

    if polynomial1[0] != '-' and polynomial1[0] != '+':
        leading_term_1 = polynomial1[0]
    else:
        leading_term_1 = polynomial1[1]

    if polynomial2[0] != '-' and polynomial2[0] != '+':
        leading_term_2 = polynomial2[0]
    else:
        leading_term_2 = polynomial2[1]

    print(leading_term_1)
    print(leading_term_2)

    # find powers in terms of tuples




def computation(monomial_list):
    for i in range(0, len(monomial_list) - 1):
        for j in range(i + 1, len(monomial_list)):
            S(monomial_list[i], monomial_list[j])

    return 10


input = '(x - y^3 , -x^2 + xy^2)'

polynomiallist = polynomial(input)
monomiallist = monomial(polynomiallist)
computation(monomiallist)

print()
print("Monomials: ")
print(monomiallist)

print(tuplelength(input))
