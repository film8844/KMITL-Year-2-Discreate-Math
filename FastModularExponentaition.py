
def FME(b, n, m):
    x = 1
    power = b % m
    bi = bin(n)[2::][::-1]
    for i in range(len(bi)):
        if(bi[i] == '1'):
            x = (x * power) % m
        power = (power**2)%m
        print("i = ", i, "| a = ", bi[i], "| x =", x, "| power =", power)
    return x


print(FME(8, 500, 99))
