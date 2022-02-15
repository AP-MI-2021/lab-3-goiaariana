def is_Prime(x):
    '''
       determina daca un numar este prim
       :param x: numar intreg
       :return: True daca x este prim sau False in caz contrar
    '''
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

def test_is_Prime():
    assert is_Prime(3) is True
    assert is_Prime(18) is False
    assert is_Prime(13) is True

def toateNrsuntPrime(l):
    '''
    determina daca toate numerele din lista sunt prime
    :param l: lista de numere intregi
    :return: True daca toate numerele din lista sunt prime, False in caz
    contrar
    '''
    for x in l:
        if is_Prime(x) is False :
            return False
    return True

def test_toateNrsuntPrime():
    assert toateNrsuntPrime([7,9]) is False
    assert toateNrsuntPrime([2,3]) is True

def get_longest_all_primes(lst: list[int]) -> list[int]:
    '''
    determina cea mai lunga subsecventa de numere prime
    :param lst: lista cu numere intregi
    :return: returneaza cea mai lunga subsecventa de numere prime din lista
    '''
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if toateNrsuntPrime(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax

def test_get_longest_all_primes():
    assert get_longest_all_primes([7,3,5,11,8,7,9]) == [7,3,5,11]
    assert get_longest_all_primes([11,6,3,5,7]) == [3,5,7]
    assert get_longest_all_primes([10,12,14,16]) == []

def nr_div(x):
    '''
    dtermina numarul de divizori al unui numar
    :param x: numar intreg
    :return: numarul de divizori al lui x
    '''
    nr=1
    for i in range (2, x//2):
        if x % i == 0:
            nr = nr+1
    return nr

def test_nrdiv():
    assert nr_div(12) == 4
    assert nr_div(25) == 2
    assert nr_div(10) == 2

def toateNrcuacelasiNrdiv(list):
    '''
    determina daca toate numerele dintr-o lista au acelasi numar de divizori
    :param list: lista cu numere intregi
    :return: True daca toate numerele din lista sunt au acelasi numar de
    divizori, False contrar
    '''
    div=nr_div(list[0])
    for x in list :
        if nr_div(x) != div:
            return False
    return True

def test_toateNrcuacelasiNrdiv():
    assert toateNrcuacelasiNrdiv([2,3,5,7]) is True
    assert toateNrcuacelasiNrdiv([6,2,8]) is False
    assert toateNrcuacelasiNrdiv([10,4]) is False

def get_longest_same_div_count(lst: list[int]) -> list[int]:
    '''
    determina cea mai lunga subsecventa de numere care au acelasi numar de
    divizor
    :param lst: lista cu nr intregi
    :return: returneaza cea mai lunga subsecventa de numere care respecta
    proprietatea din lista
    '''
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if toateNrcuacelasiNrdiv(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax

def test_get_longest_same_div_count():
  assert get_longest_same_div_count([16,20,12,7]) == [20,12]
  assert get_longest_same_div_count([16,11,13,15]) == [11,13]


def printMenu():
    print("1. Citire lista")
    print("Afisarea celei mai lungi secventa in care: ")
    print("2. Toate numerele sunt prime")
    print("3. Toate numerele au acelasi numar de divizori")
    print("x. Iesire")

def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def main():
    l = []
    while True:
        printMenu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
           print(get_longest_all_primes(l))
        elif optiune == "3":
            print(get_longest_same_div_count(l))
        elif optiune == "x":
            break
        else:
            print("Optiune invalida. Va rog sa incercati din nou")


if __name__ == "__main__":
    test_is_Prime()
    test_toateNrsuntPrime()
    test_get_longest_all_primes()
    test_nrdiv()
    test_toateNrcuacelasiNrdiv()
    test_get_longest_same_div_count()
    main()

