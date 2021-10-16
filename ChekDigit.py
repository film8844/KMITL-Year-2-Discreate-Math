def CheckDigit(s: str):
    n = list(map(int, s))
    sum = 0

    for i in range(len(n)):
        if(i % 2 == 1):sum += (n[i]*3)
        sum += n[i]

    if sum % 10 == 0:return True
    else:return False


# print(CheckDigit("3978269097341"))

def checkIDcard(id:str):
    id = list(map(int, id))
    s = 0 
    for i in range(12):
        s+= ((14-i+1)*id[i])
        s=s%11

    
    print(11-s)


checkIDcard("011532498092")
