import re
import numpy


def plyformat(ideal):
    """Takes an Ideal and seperates by polynomial stored with sign
    [p1,p2,p3] pi = [{"sign": ,}, {"mT": }]

    """
    polynomials = []
    x = re.split('\(|\)|,', ideal)
    lst = []
    for i in x:
        if i != '':
            lst.append(i)
    noply = len(lst)
    x.clear()
    for i in lst:
        x.append(i.split())
    for i in x:
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
    templst = []
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            if (x[i])[j] == '+' or (x[i])[j] == '-':
                tempdict = {"sign": str((x[i])[j]), "mT": str((x[i])[j + 1])}
                j = j + 1
                templst.append(tempdict)
            else:
                continue

        polynomials.append(templst)
        templst = []
    return polynomials


def find_power(monomial):
    """Finds the powers in an accessible form"""
    first = {}
    first.update({'c': 1})
    first.update({'x': 0})
    first.update({'y': 0})
    counter = 0
    for i in monomial:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            counter = counter + 1
            first.update({i: 1})
        elif 50 <= ord(i) <= 57 and counter == 0:
            first.update({'c': int(i)})
    for i in range(0, len(monomial)):

        if monomial[i] == '^':
            first.update({monomial[i - 1]: int(monomial[i + 1])})
    return first


def generalDivision(dividend, divisors):
    """GENERAL POLYNOMIAL DIVISION IN TWO VARIABLES"""
    r1 = []
    remainders = []
    while len(dividend) != 0:
        flag = False
        lt = dividend[0]

        for i in divisors:
            if find_power(lt["mT"])['x'] >= find_power(i[0]["mT"])['x'] and find_power(lt["mT"])['y'] >= \
                    find_power(i[0]["mT"])['y']:

                df = (difference(dividend, i))

                for j in dividend:
                    r1.append(j)

                for v in i:
                    r1.append(multiplication(df, v))

                r1 = collectliketerms(r1)
                r1 = restore_order(r1)

                dividend = r1.copy()

                r1 = []
                flag = True
                break
        if not flag:
            remainders.append(lt.copy())
            dividend.pop(0)

    return remainders


def multiplication(term1, term2):
    """Multiplication"""
    result = {}
    x1 = find_power(term1["mT"])
    x2 = find_power(term2["mT"])
    if term1["sign"] == term2["sign"]:
        result.update({"sign": '+'})
    else:
        result.update({"sign": '-'})
    returndict = {"sign": result["sign"]}
    rtnstr = ""
    for i in x1:
        if i == 'c':
            if x1[i] == 1:
                continue
            else:
                rtnstr = rtnstr + str(x1[i] + x2[i])
        else:
            rtnstr = rtnstr + str(i)
            rtnstr = rtnstr + "^"
            rtnstr = rtnstr + str(x1[i] + x2[i])
    returndict.update({"mT": rtnstr})
    return returndict


def difference(p1, p2):
    """Calculates the difference so we can divide"""
    xs = find_power(p1[0]["mT"])['x'] - find_power(p2[0]["mT"])['x']
    ys = find_power(p1[0]["mT"])['y'] - find_power(p2[0]["mT"])['y']
    cs = find_power(p1[0]["mT"])['c'] - find_power(p2[0]["mT"])['c']
    rtnstr = ""
    if xs == 0 == cs == 0 == ys:
        if p1[0]["sign"] == '-' and p2[0]["sign"] == '-':
            return {"sign": '-', "mT": '1'}
        elif p1[0]["sign"] == '-' and p2[0]["sign"] == '+':
            return {"sign": '+', "mT": '1'}
        elif p1[0]["sign"] == '+' and p2[0]["sign"] == '-':
            return {"sign": '+', "mT": '1'}
        elif p1[0]["sign"] == '+' and p2[0]["sign"] == '+':
            return {"sign": '-', "mT": '1'}
    if xs != 0:
        rtnstr = rtnstr + 'x'
        rtnstr = rtnstr + '^'
        rtnstr = rtnstr + str(xs)
    if ys != 0:
        rtnstr = rtnstr + 'y'
        rtnstr = rtnstr + '^'
        rtnstr = rtnstr + str(ys)
    if p1[0]["sign"] == '-' and p2[0]["sign"] == '-':
        return {"sign": '-', "mT": rtnstr}
    elif p1[0]["sign"] == '-' and p2[0]["sign"] == '+':
        return {"sign": '+', "mT": rtnstr}
    elif p1[0]["sign"] == '+' and p2[0]["sign"] == '-':
        return {"sign": '+', "mT": rtnstr}
    elif p1[0]["sign"] == '+' and p2[0]["sign"] == '+':
        return {"sign": '-', "mT": rtnstr}


def collectliketerms(r1):
    prvlenth = 0
    while prvlenth != len(r1):
        flag = False
        prvlenth = len(r1)
        for i in range(0, len(r1)):
            for j in range(0, len(r1)):
                if i != j:
                    if same(r1[i]["mT"], r1[j]["mT"]):
                        x = int(r1[i]["sign"] + str(find_power(r1[i]["mT"])['c'])) + int(
                            r1[j]["sign"] + str(find_power(r1[j]["mT"])['c']))
                        if x == 0:
                            x1 = r1[i]
                            x2 = r1[j]
                            r1.remove(x1)
                            r1.remove(x2)
                        else:
                            r1[i] = {"sign": str(numpy.sign(x)),
                                     "mT": str(abs(x)) + "x^" + str(find_power(r1[i]["mT"])['x']) + "y^" + str(
                                         find_power(r1[i]["mT"])['y'])}
                            r1.remove(r1[j])
                        flag = True
                        break
            if flag:
                break
    return r1


def same(t1, t2):
    x1 = find_power(t1)
    x2 = find_power(t2)
    if x1['x'] == x2['x'] and x1['y'] == x2['y']:
        return True
    else:
        return False


def LCM(lt1, lt2):
    """Finds lowest common monic of two monomials
    :return {"sign": + or -}, {"mT": x^iy^j}"""
    LCM = {}
    LCMstr = ""
    x1 = find_power(lt1["mT"])
    x2 = find_power(lt2["mT"])
    x1key = list(x1.keys())
    x1key.remove('c')
    for i in x1key:
        if x1[i] > x2[i]:
            LCM.update({i: x1[i]})
        else:
            LCM.update({i: x2[i]})
    for i in LCM:
        LCMstr = LCMstr + str(i)
        LCMstr = LCMstr + '^'
        LCMstr = LCMstr + str(LCM[i])
    LCM = {"sign": '+', "mT": LCMstr}
    return LCM


def restore_order(r1):
    """RESTORE ORDER WITH LEXICOGRAPHIC ORDERING X > Y > Z"""
    flag = False
    while not flag:
        flag = True
        for i in range(0, len(r1) - 1):
            if find_power(r1[i]["mT"])['x'] < find_power(r1[i + 1]["mT"])['x']:
                x1 = r1[i]
                x2 = r1[i + 1]
                r1[i + 1] = x1
                r1[i] = x2
                flag = False
            elif find_power(r1[i]["mT"])['x'] == find_power(r1[i + 1]["mT"])['x']:
                if find_power(r1[i]["mT"])['y'] < find_power(r1[i + 1]["mT"])['y']:
                    x1 = r1[i]
                    x2 = r1[i + 1]
                    r1[i + 1] = x1
                    r1[i] = x2
                    flag = False
    return r1


def division(dividend, divisor):
    x1 = find_power(dividend["mT"])
    x2 = find_power(divisor["mT"])
    x1.pop('c')
    x2.pop('c')
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
    if dividend["sign"] == divisor["sign"]:
        resltt = {"sign": '+', "mT": resultstr}
    else:
        resltt = {"sign": '-', "mT": resultstr}
    return resltt


def Spolynomial(ply1, ply2):
    r1 = []
    lcm = LCM(ply1[0], ply2[0])
    m1 = division(lcm, ply1[0])
    m2 = division(lcm, ply2[0])

    if ply1[0]["sign"] == '+' and ply2[0]["sign"] == '-':
        m2["sign"] = '+'
    elif ply1[0]["sign"] == '+' and ply2[0]["sign"] == '+':
        m2["sign"] = '-'
    elif ply1[0]["sign"] == '-' and ply2[0]["sign"] == '+':
        m2["sign"] = '-'
    elif ply1[0]["sign"] == '-' and ply2[0]["sign"] == '-':
        m2["sign"] = '+'
    for i in ply1:
        r1.append(multiplication(m1, i))
    for i in ply2:
        r1.append(multiplication(m2, i))
    return restore_order(collectliketerms(r1))


def buchbergersAlgorithm(polys):
    cartesianproducts = []
    flag = False
    while not flag:
        flag = True
        for i in range(0, len(polys)):
            for j in range(0, len(polys)):
                if i != j and ([i,j] not in cartesianproducts):
                    sp = Spolynomial(polys[i].copy(), polys[j].copy())
                    d = generalDivision(sp.copy(), polys.copy())
                    if len(d) != 0:
                        polys.append(d)
                        flag = False
                        break
            cartesianproducts.append([i, j])
            if not flag:
                break
    return polys

print("*****Find the Gröbner Basis of an ideal in a polynomail ring in two variables*****")
print(">>", end= '')
x = input()
y = buchbergersAlgorithm(plyformat(x).copy())
print("Gröbner Basis: ", y)
print("Reduced Gröbner Basis: ")
