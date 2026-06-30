PRIMES =[2,3]
for i in range(3,2000000,2):
    k=50
    if i ==10001:
        print(i)
        print(PRIMES)
    elif i== 1000001:
        print(i)
        print(PRIMES)
    elif i == 100001:
        print(i)
        print(PRIMES)
    for j in range(len(PRIMES)):
        if PRIMES[j]<=i**0.5:
            if i%PRIMES[j]!=0:
                k=100
            else:
                k=0
                break
        else:

            break
    if k==100:
        PRIMES.append(i)
    elif k==0:
        continue
    else:
        print("error")
sums=0
for l in range(len(PRIMES)):
    sums =sums+PRIMES[l]

print(sums)

