from sympy import Symbol

def jorip(poly, mok):
    result = []
    trys = 1
    multi = 0
    plus = 0
    for i in range(len(poly)):
        if trys == 1:
            plus = poly[i]
            result.append(plus)
            trys += 1
        else:
            multi = mok * result[-1]
            plus = poly[i] + multi
            result.append(plus)


            trys += 1
    return result

def yaksu(a):
    result = []
    a = abs(int(a))
    for i in range(1,a+1):
        if a%i==0:
            result.append(i)
    return result

def daeip(i,j,poly):
    x = j/i
    n = len(poly)
    result = 0
    for k in range(n):
        result += poly[k]*(x ** (n-k-1))
    return result

def insubunhae(poly):
    bunmo = yaksu(poly[0])
    bunja = yaksu(poly[-1])
    mok_flag = False
    for i in bunmo:
        for j in bunja:
            if daeip(i, j, poly) == 0:
                mok = j / i
                mok_flag = True
            elif daeip(-1 * i, j, poly) == 0:
                mok = j / i * -1
                mok_flag = True
    if not mok_flag:
        # print("더이상 인됨분해 안됨")
        new_poly = poly[:-1]
        n = len(new_poly)
        x = Symbol('x')
        result = ""
        for i in range(len(new_poly)):
            result += str(int(new_poly[i])* (x**(n-i-1)))

        print("인수  :",result + " ")
    else:
        print("인수"," : x-%d"%mok)
        new_poly = jorip(poly, mok)[:-1]
        if(len(new_poly)>2):
            insubunhae(new_poly)
        else:
            n = len(new_poly)
            x = Symbol('x')
            result = ""
            for i in range(len(new_poly)):
                result += str(int(new_poly[i]) * (x ** (n - i - 1)))

            print("인수  :", result + " ")

chasu = int(input("차수를 입력하세요: "))
poly = []
for i in range(chasu + 1):
    msg = "%d 차항의 계수를 입력하세요: " % (chasu - i)
    poly.append(int(input(msg)))
# mok = int(input("몫을 입력하세요: "))
bunmo = yaksu(poly[0])
bunja = yaksu(poly[-1])
mok_flag = False
for i in bunmo:
    for j in bunja:
        if daeip(i,j,poly) == 0:
            mok = j/i
            mok_flag=True
        elif daeip(-1*i,j,poly)==0:
            mok = j/i * -1
            mok_flag = True
if not mok_flag :
    print("인수분해 안됨")

else:
    print("인수", " : x-%d" % mok)
    new_poly = jorip(poly,mok)[:-1]
    if(len(new_poly)>2):
        insubunhae(new_poly)
    else:
        n = len(new_poly)
        x = Symbol('x')
        result = ""
        for i in range(len(new_poly)):
            result += str(int(new_poly[i])* (x**(n-i-1)))

        print("인수  :",result + " ")

print("end!!")