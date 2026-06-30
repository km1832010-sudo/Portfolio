a=1
b=1
c=1

while True:
    a=a+1
    if a + b + c ==1000 and c > b > a:
        print("XXXXXX "+str(c)+ "," +str(b) +"," +str(a))
        if a**2 + b**2 == c**2:
            print("This is it:" + str(a) + "," + str(b) +"," +str(c) )
            break
    elif a>b:
        a=1
        b=b+1
    elif b>c:
        a=1
        b=1
        c=c+1
    else:
        continue

#if b < c - 1 and a < c - 1:
    #b = b + 1
#elif b >= c - 1:
   # b = 1
   # a = a + 1
#elif a >= c - 1:
  #  break
#else:
    #print("error")
