import re


def plyformat(ideal):
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


def buchbergersAlgorithm(polynomials):
    Spolynomial(polynomials[0], polynomials[1])


def Spolynomial(ply1, ply2):
    r1 = []
    lcm = LCM(ply1[0], ply2[0])

    m1 = division(lcm, ply1[0])
    m2 = division(lcm, ply2[0])
    print("polynomial 1", ply1, "polynomial 2", ply2, "m1", m1, "m2", m2)
    for i in ply1:
        r1.append(multiplication(m1, i))
    for i in ply2:
        r1.append(multiplication(m2, i))

    result = addition(r1)

    # division now
    generalDivision(result, polynomials)
    return 0


def generalDivision(dividend, polynomials):
    print("Dividend: ", dividend)
    print("Polynomials:", polynomials)
    remainder = []
    quotients = []
    for i in dividend:
        i
        for j in polynomials:
            # division(i,j[0])
    return 0

def division(dividend, divisor):
    x1 = find_power(dividend["mT"])
    x2 = find_power(divisor["mT"])

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

    resltt = {"sign": '+', "mT": resultstr}
    return resltt


def multiplication(term1, term2):
    # print(term1,term2)
    result = {}
    returndict = {}
    x1 = find_power(term1["mT"])
    x2 = find_power(term2["mT"])

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


def addition(r1) -> list:
    lst = []
    flag = []
    lenx = len(r1)
    for i in range(0, len(r1)):
        for j in range(0, len(r1)):
            if i != j:
                if find_power(r1[i]["mT"]) == find_power(r1[j]["mT"]):

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
    LCM = {}
    LCMstr = ""
    x1 = find_power(lt1["mT"])
    x2 = find_power(lt2["mT"])
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
    LCM = {"sign": '+', "mT": LCMstr}

    return LCM


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


ideal = '(+x^2y^5 - y^3 , -x^3y^3 + xy^2)'
polynomials = plyformat(ideal)
buchbergersAlgorithm(polynomials)
