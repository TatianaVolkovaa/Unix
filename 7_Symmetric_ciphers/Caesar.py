def encrypt(key, str):
    s1=[]
    s2=[]
    for i in str:
        s1.append((ord(i)+key)%256) 
    for i in range(len(s1)):
        s2.append(chr(s1[i]))
    cipher=''.join(s2)   
    return cipher 

def decrypt(key, cipher):
    s1=[]
    s2=[]
    for i in cipher:
        s1.append((ord(i)-key)%256) 
    for i in range(len(s1)):
        s2.append(chr(s1[i]))
    str=''.join(s2)   
    return str

def hack(cipher):
    number =[]
    for i in range(len(cipher)):
        number.append([cipher.count(cipher[i]),cipher[i]])
        max=0
        for j in range(len(number)):
            if number[j][0] > max:
                max=number[j][0]
                elmax=number[j][1]
    key=ord(elmax)-ord(' ')%256
    s1=[]
    s2=[]
    for i in cipher:
        s1.append((ord(i)-key)%256) 
    for i in range(len(s1)):
        s2.append(chr(s1[i]))
    str=''.join(s2)   
    return str

text = "I love you"
key = int(input("Введите ключ --> "))
rez = encrypt(key,text)
tran = decrypt(key,rez)
print(text, " <-- Исходное")
print(rez, " <-- Зашифрованное")
print(tran, " <-- Раскодированное")


cip = input("Введите зашифрованное предложение --> ")
r = hack(cip)
print("Расшифровка предложения --> ", r)
