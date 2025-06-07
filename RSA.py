import math

def powMod(a, b, m):
    #Biến đổi số mũ thành dạng bit
    bit = list()
    while b != 0:
        bit.append(b & 1)
        b = b >> 1
    bit.reverse()

    x = [a%m]
    for i in range(1,len(bit)):
        p = (x[i-1]*x[i-1])%m
        if bit[i] != 0:
            p*=x[0]
            p%=m
        x.append(p)
    return x[len(bit) - 1]
def multiplicate_inverse(a, b):
    A, B = a, b
    T1, T2 = 0, 1
    while B != 0:
        Q = A//B
        R = A%B
        T = T1 - (T2 *Q)
        A = B
        B = R
        T1 = T2
        T2 = T
    if T1 < 0:
        T1 += a
    return T1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def getE(phi):
    e = 65537
    while True:
        if gcd(e,phi) == 1:
            break
        e+=2
    return e

def getD(phi, e):
    d = multiplicate_inverse(phi, e)
    return d




dig ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-+ "
def encrypt(e, n, plaintext):
    global dig
    x = list()
    for i in plaintext:
        x.append(dig.index(i))

    result = list()
    for i in x:
        result.append(powMod(i,e,n))
    return result




def decrypt(d,n, ciphertext):
    global dig
    result = list()
    for i in ciphertext:
        result.append(dig[powMod(int(i),d,n)])
    return "".join(result)








p = 176806666083199943810624708480637063441019137307351346530442902586095101027807450308489430154868555187855233695844119297432514344216398567416882797430985826624138101999668852216965417105636463229951158749390261472422042538433049079476291257122724120029539790722982595167248456369653582145725131334036008548393
q = 141411464463783054650268982180185945836966573611357894821255638848462106259192583525424049201378883771451574057351113185130783591143005697595289546828206583108058298323992467722226887614778586624894771429388377371347868855553901545786120859331852251331257627029475436366990435357465721473729728694765959581807
n = p*q
phi = (p-1)*(q-1)
e = getE(phi)
d = getD(phi, e)
message = "I am B21DCAT119"
encode = encrypt(e,n,message)
decode = decrypt(d,n,encode)





print("p: ", p)
print("q: ", q)
print("n: ", n)
print("d: ", d)
print("e: ", e)
print("phi: ", phi)
print("Message: ", message)
print("Encode: ", encode)
print("Decode: ", decode)
