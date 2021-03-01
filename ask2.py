import random

t = input("Give a number >= 1:")
t = int(t)
def fibo(x):
        i = 1
        j = 1
        for k in range(x - 2):
            tmp = i
            i = i + j
            j = tmp
        return i

p = fibo(t)
print('Ο',t,"ος όρος της ακολουθίας Fibonacci ισούται με ", p, "και")

if p == 1:
    print("Δεν είναι πρώτος")
elif p == 2 :
    print("Είναι πρώτος")
else:
    metr = 0

    for d in range (20):
        orio = p-1
        a = (random.randint(2, orio))
        if (a**p)%p == (a%p) :
            metr = metr + 1
    if metr == 20:
        print("Είναι πρώτος")
    else:
        print("Δεν είναι πρώτος")
