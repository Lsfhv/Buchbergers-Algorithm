import re


def plyformat(ideal):
    '''Takes an Ideal and seperates by polynomial stored with sign
    [p1,p2,p3] pi = [{"sign": ,}, {"mT": }]

    '''
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
    # store terms with sign
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


def buchbergersAlgorithm(polys):
    length = len(polys)
    generalDivision(Spolynomial(polys[0], polys[1]), polys.copy())

    # if lenght chages we call it again but appended list


def generalDivision(dividend, divisors):
    remainder = []
    print(dividend)
    print(divisors)
    print()
    m1 = []
    while len(dividend) != 0:
        flag = False
        lt = dividend[0]

        # check for divisibility
        for i in divisors:

            if decompose(lt["mT"])['x'] >= decompose(i[0]['mT'])['x'] and decompose(lt["mT"])['y'] >= decompose(
                    i[0]['mT'])['y']:

                d = difference(dividend, i)
                for j in i:
                    dividend.append(multiplication(d, j))
                print(dividend)
                # addition(dividend)
                # print("dividend",dividend)
                flag = True
        if not flag:
            remainder.append(lt)
            dividend.pop(0)

    return remainder


def difference(p1, p2):
    """Calculates the difference so we can divide"""
    xs = decompose(p1[0]["mT"])['x'] - decompose(p2[0]["mT"])['x']
    ys = decompose(p1[0]["mT"])['y'] - decompose(p2[0]["mT"])['y']
    rtnstr = ""
    if xs != 0:
        rtnstr = rtnstr + 'x'
        rtnstr = rtnstr + '^'
        rtnstr = rtnstr + str(xs)

    if ys != 0:
        rtnstr = rtnstr + 'y'
        rtnstr = rtnstr + '^'
        rtnstr = rtnstr + str(ys)

    return {"sign": '-', "mT": rtnstr}


def Spolynomial(ply1, ply2):
    r1 = []
    lcm = LCM(ply1[0], ply2[0])
    m1 = division(lcm, ply1[0])
    m2 = division(lcm, ply2[0])

    for i in ply2:
        if i["sign"] == '+':
            i["sign"] = '-'
        else:
            i["sign"] = '+'
    for i in ply1:
        r1.append(multiplication(m1, i))
    for i in ply2:
        r1.append(multiplication(m2, i))

    result = addition(r1)
    return restore_order(result)


def division(dividend, divisor):
    x1 = decompose(dividend["mT"])
    x2 = decompose(divisor["mT"])

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


def multiplication(term1, term2):
    """Multiplication"""
    result = {}
    x1 = decompose(term1["mT"])
    x2 = decompose(term2["mT"])

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
    returndict.update({"mT": oeafyayd})
    return returndict


def addition(r1) -> list:
    """Collects like terms
    :return {sign: },{mT: }"""
    lst = []
    flag = []
    lenx = len(r1)
    for i in range(0, len(r1)):
        for j in range(0, len(r1)):
            if i != j:
                if decompose(r1[i]["mT"]) == decompose(r1[j]["mT"]):

                    if r1[i]["mT"][0].isdigit():
                        # coeffs is not 1 support coefficients, might not actually work
                        p1 = r1[i]["mT"][0]
                        if r1[j]["mT"][0].isdigit():
                            p2 = r1[j]["mT"][0]
                        else:
                            p2 = 1

                        max = 0
                        if r1[i]["sign"] == "-":
                            p1 = - int(p1)
                        if r1[j]["sign"] == "-":
                            p2 = - int(p2)

                        rst = p1 + p2
                        if rst > 0:
                            sign = '+'
                        else:
                            sign = '-'
                            rst = rst * -1
                        lst.append({"sign": sign, "mT": str(rst) + r1[i]["mT"][1:]})
                    else:
                        # coeffs are 1, so check sign, if differ, delete tm
                        if r1[i]["sign"] != r1[j]["sign"]:
                            flag.append(i)
                            flag.append(j)
    for i in range(0, len(r1)):
        if i in flag:
            continue
        else:
            lst.append(r1[i])
    return lst


def LCM(lt1, lt2):
    """Finds lowest common monic of two monomials
    :return {"sign": + or -}, {"mT": x^iy^j}"""
    LCM = {}
    LCMstr = ""
    x1 = decompose(lt1["mT"])
    x2 = decompose(lt2["mT"])
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


def decompose(monomial):
    """Finds the powers in an accessible form
    :return {variable: exponent}"""
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


def restore_order(x):
    rtn = []
    for i in range(0, len(x) - 1):
        if decompose(x[i]["mT"])['x'] > decompose(x[i + 1]["mT"])['x']:
            x[i], x[i + 1] = x[i + 1], x[i]
    for i in reversed(x):
        rtn.append(i)
    return rtn


def collectliketerms(r1):
    for i in range(0, len(r1)):
        for j in range(0, len(r1)):
            if i != j:
                if same(i["mT"], j["mT"]):
                    # finnd power for c and use sign to add em
                    return 0


def same(t1, t2):
    x1 = decompose(t1)
    x2 = decompose(t2)
    if x1['x'] == x2['x'] and x1['y'] == x1['y']:
        return True
    else:
        return False


ideal = '(+x^2y^5 - y^3 , -x^3y^3 + xy^2)'
polynomials = plyformat(ideal)
# buchbergersAlgorithm(polynomials.copy())
generalDivision(([{'sign': '+', 'mT': 'x^2y^4'}, {'sign': '-', 'mT': 'x^0y^3'}]),
                [[{'sign': '+', 'mT': 'x^2y^5'}, {'sign': '-', 'mT': 'y^3'}],
                 [{'sign': '+', 'mT': 'x^3y^3'}, {'sign': '-', 'mT': 'xy^2'}],
                 [{'sign': '+', 'mT': 'x^1y^4'}, {'sign': '-', 'mT': 'x^1y^3'}]])
