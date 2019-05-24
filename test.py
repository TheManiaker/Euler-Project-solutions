from math import sqrt
from abc import *

def f3():
    n = 600851475143
    lim = int(sqrt(n))
    lst = []
    for i in range(2, lim):
        for l in lst:
            if l > int(sqrt(i) + 1):
                lst.append(i)
                if n % i == 0:
                    x = i
                break
            if i % l == 0:
                break
        else:
            lst.append(i)
            if n % i == 0:
                x = i
    print(x)


def f4():
    ans = 0
    for x in range(999, 99, -1):
        for y in range(x, 99, -1):
            n = str(x * y)
            for l in range(len(n) // 2):
                if n[l] != n[-1 - l]:
                    break
            else:
                if int(n) > ans:
                    ans = int(n)
    print(ans)


def f5():
    d = {}
    tmp = {}
    for i in range(2, 31):
        n = i
        tmp.clear()
        for l in range(2, i):
            while n % l == 0:
                n /= l
                if l not in tmp.keys():
                    tmp[l] = 1
                else:
                    tmp[l] += 1
            if n < l:
                break
        else:
            if i not in tmp.keys():
                tmp[i] = 1
            else:
                tmp[i] += 1
        for key in tmp.keys():
            if key not in d.keys():
                d[key] = tmp[key]
            else:
                if d[key] < tmp[key]:
                    d[key] = tmp[key]
    ans = 1
    for key in d.keys():
        for l in range(d[key]):
            ans *= key
    print(ans)


def binary_search(lst, n):
    min = 0
    top = len(lst) - 1
    mid = lst[min + (top - min) // 2]
    while min <= top:
        if mid > n:
            top = min + (top - min) // 2 - 1
            mid = lst[min + (top - min) // 2]
        else:
            min = min + (top - min) // 2 + 1
            mid = lst[min + (top - min) // 2]
    print(lst.index(mid) + 1)


def f6():
    s1 = 0
    s2 = 0
    for i in range(1, 101):
        s1 += i ** 2
        s2 += i
    print(s2 ** 2 - s1)


def f7():
    i = 2
    lst = []
    while len(lst) < 10001:
        for l in lst:
            if l > int(sqrt(i) + 1):
                lst.append(i)
                break
            if i % l == 0:
                break
        else:
            lst.append(i)
        i += 1
    print(lst[10000])


def f8():
    series = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    ans = 1
    i = 0
    while i < len(series) - 12:
        tmp = 1
        for l in range(13):
            if series[i + l] == '0':
                i = i + l
                break
            tmp *= int(series[i + l])
        else:
            if tmp > ans:
                ans = tmp
        i += 1
    print(ans)


def yandex_5():
    n, m, k = [int(i) for i in input().split()]
    lst = [int(i) for i in input().split()]
    ans = [0 for i in range(k)]
    solution(lst, ans, k, n, 1, m)
    for i in range(k):
        print(ans[i] + 1, end=' ')


def solution(lst, ans, k, n, lvl, m):
    product = 1
    if lvl == k+1:
        for i in range(k):
            product *= lst[ans[i]]
        if product > m:
            return False
        elif product == m:
            return True
    else:
        if lvl == 1:
            for i in range(n-k):
                ans[0] = i
                if solution(lst, ans, k, n, lvl + 1, m):
                    return True
        else:
            i = ans[lvl - 2] + 1
            while i < n - (k - lvl):
                ans[lvl - 1] = i
                if solution(lst, ans, k, n, lvl + 1, m):
                    return True
                i += 1
    return False


def f9():
    a = 1
    b = 1
    while True:
        c = sqrt(a ** 2 + b ** 2)
        if a + b + c > 1000:
            a = 1
            b += 1
        elif a + b + c == 1000:
            break
        a += 1
    print(a, b, c)
    print(a * b * c)


def f10():
    i = 2
    lst = []
    s = 0
    while True:
        for l in lst:
            if l > int(sqrt(i) + 1):
                lst.append(i)
                s += lst[-1]
                break
            if i % l == 0:
                break
        else:
            lst.append(i)
            s += lst[-1]
        if lst[-1] >= 2000000:
            s -= lst[-1]
            print(s)
            break
        i += 1


class Decor(metaclass=ABCMeta):
    __count = 0

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.__count += 1

    def __del__(self):
        self.__count -= 1

    @abstractmethod
    def info(self):
        print(self.name, self.size)


class Table(Decor):
    def __init__(self, model, color, name, size):
        Decor.__init__(self, name, size)
        self.model = model
        self.color = color

    def info(self):
        print(self.name, self.size, self.model, self.color)

