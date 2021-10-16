def str2int(c):
    az = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return az.find(c)

def int2str(c):
    az = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return az[c]

def ShiftCipherEn(s:str,k:int):
    li = list(map(str2int,s))
    li = list(map(lambda x:(x+k)%26,li))
    li = list(map(int2str,li))
    return li

def ShiftCipherUn(s:str,k:int):
    li = list(map(str2int,s))
    li = list(map(lambda x:(x-k)%26,li))
    li = list(map(int2str,li))
    return li


print(*ShiftCipherUn("ECGUPSMYQ" ,k=12))