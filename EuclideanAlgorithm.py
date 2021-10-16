def gcd(x:int, y:int):
    if x<y: x,y = y,x
    if (x%y == 0): return y
    else: 
        print("gcd(%d,%d) > %d = (%d x %d) + %d"%(y,x%y,y,x%y,int(x/y),(y%(x%y))))
        return gcd(y,x%y)


for i in range(1,10):
    print(i,"======> gcd =",gcd(27, i))
