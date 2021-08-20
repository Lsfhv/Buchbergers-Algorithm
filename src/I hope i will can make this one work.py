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
        print(i.split())
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


def Sfucntion(polynomial1, polynomial2):
    set1 = {"sign": "+", "LT": "x^2y^5"}
    set2 = {"sign": "-", "LT": "y^3"}

    ply1 = [set1, set2]
    set1 = {"sign": "-", "LT": "x^3y^3"}
    set2 = {"sign": "+", "LT": "xy^2"}
    ply2 = [set1, set2]

    polynomial1 = restore_order(polynomial1)
    polynomial2 = restore_order(polynomial2)
    print("Polynomial 1:", polynomial1, "Polynomial 2: ", polynomial2)
    leadingterm1 = LT(polynomial1)
    leadingterm2 = LT(polynomial2)
    lt1 = leadingterm1["LT"]
    lt2 = leadingterm2["LT"]
    lcm = LCM(lt1, lt2)

    print("Leading term 1: ", lt1, "Leading term 2: ", lt2, "LCM: ", lcm)

    # do all computation here? push evertyhign above out lter
    # and LT needs to support sign

    x1 = division(lcm, lt1)
    x2 = division(lcm, lt2)
    print(x1,x2)
    result = []

    for i in ply1:
        for j in ply2:
            result.append(multiplication(i,j))

    multiplication(leadingterm1, leadingterm2)

    # The SFunction, cartesian product, ideal would collect like terms first

    # i thin yes

    # S(P1,P2) = (M/LT1)P1 - (M/LT2)P2


# make divison respt sgn
def division(dividend, divisor):
    x1 = find_power(dividend)
    x2 = find_power(divisor)

    resultstr = ""
    result = {}
    for i in x1:
        if x1[i] >= x2[i]:
            tmp = x1[i] - x2[i]
            result.update({i: tmp})
    for i in result:
        if result[i] == 0:
            continue
        else:
            resultstr = resultstr + str(i)
            resultstr = resultstr + "^"
            resultstr = resultstr + str(result[i])
    return resultstr


# multiplcation working?
def multiplication(term1, term2):
    result = {}
    returndict = {}
    x1 = find_power(term1["LT"])
    x2 = find_power(term2["LT"])

    if term1["sign"] == term2["sign"]:
        result.update({"sign": '+'})
    else:
        result.update({"sign": '-'})
    returndict = {"sign": result["sign"]}
    oeafyayd = ""
    for i in x1:
        result.update({i: x1[i] + x2[i]})
        oeafyayd = oeafyayd + str(i)
        oeafyayd = oeafyayd + "^"
        oeafyayd = oeafyayd + str(x1[i] + x2[i])
    # so result holds signs and powers
    returndict.update({"mT": oeafyayd})
    return returndict


def LCM(LT1, LT2):
    LCM = {}
    LCMstr = ""
    x1 = find_power(LT1)
    x2 = find_power(LT2)
    x1key = list(x1.keys())
    for i in x1key:
        if x1[i] > x2[i]:
            LCM.update({i: x1[i]})
        else:
            LCM.update({i: x2[i]})
    for i in LCM:
        LCMstr = LCMstr + str(i)
        LCMstr = LCMstr + '^'
        LCMstr = LCMstr + str(LCM[i])
    return LCMstr


# find the leading term
def LT(p1):
    sign = ""
    for j in p1:
        for i in j:
            if 'a' <= i <= 'z':
                return {"sign": sign, "LT": j}
            else:
                sign = i


# will assume order is respected
def addition(summand1, summand2):
    return True


# we want to restore the ordering on the monomials, assume no two monomials have same multidegree as we shall collect
# like terms before doing this. we assume usual lexicographic ordering x > y > z etc. - not grlex or grevlex

def restore_order(polynomial):
    powers = []
    ordered = []
    signs = {}
    # for i in polynomial:
    #     if i == '+' or i == '-':
    #         signs.update({i:})
    #         continue
    #     else:
    #         powers.append(find_power(i))

    for i in range(0, len(polynomial)):
        if polynomial[i] == '+' or polynomial[i] == '-':
            signs.update({polynomial[i + 1]: polynomial[i]})
            continue
        else:

            powers.append(find_power(polynomial[i]))

    lenx = len(powers)
    for i in range(0, lenx):
        max = powers[0]['x']
        counter = 0
        for j in powers:

            if max < j['x']:

                max = j['x']
                counter = counter + 1
                # pop the resulting max here somewhere and append it
            else:
                continue

        ordered.append(powers.pop(counter))

    polyordered = []

    # matching powers

    for i in polynomial:
        if i == '+' or i == '-':
            continue
        else:
            for j in range(0, len(ordered)):
                if find_power(i) == ordered[j]:
                    polyordered.insert(j, i)

    polyorderedre = []

    lenx = len(polyordered)
    for i in range(0, lenx):
        try:
            polyorderedre.append(signs[polyordered[i]])
            polyorderedre.append(polyordered[i])
        except:
            polyorderedre.append(polyordered[i])
    # print("Input: ", polynomial, "output: ",polyorderedre)
    return polyorderedre


# finds power of terms as a dictionary
def find_power(monomial):
    first = {}
    first.update({'x': 0})
    first.update({'y': 0})
    for i in monomial:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            first.update({i: 1})

    for i in range(0, len(monomial)):
        if monomial[i] == '^':
            first.update({monomial[i - 1]: int(monomial[i + 1])})

    return first


# monomial1 = 'x^2y^5'
# monomial2 = 'x^3y^3'
#
# find_least_common_monic_term(monomial1,monomial2)

input = '(+x^2y^5 - y^3 , -x^3y^3 + xy^2)'
monomial_list = monomial(polynomial(input))
# find_least_common_monic_term((monomial_list[0])[0], (monomial_list[1])[1], monomial_list[0], monomial_list[1])

x = ['-', 'x^2y^3', '+', 'x^5y^4', '-', 'x^4y^2']

Sfucntion(monomial_list[0], monomial_list[1])
