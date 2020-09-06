#Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
#Make sure that you write up the algorithm before starting to code.
#Then implement the algorithm in Python. Put your algorihmic description as a comment in the program file.
allar_tolur =[1, 2, 3,]
n = int(input("Enter the length of the sequence: "))

if n >3:
    for i in range(n-3):
        summa = 0
        for i in range(3):
            summa += allar_tolur[-(i+1)]
        allar_tolur.append(summa) 
if n==1:
    print(allar_tolur[0])
elif n==2:
    print(allar_tolur[0])
    print(allar_tolur[1])
elif n==3:
    print(allar_tolur[0])
    print(allar_tolur[1])
    print(allar_tolur[2])
else:
    for i in range(len(allar_tolur)):
        print(allar_tolur[i])
