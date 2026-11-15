from Crypto.Util.number import getPrime, bytes_to_long


bits = 150
p = getPrime(bits)
q = getPrime(bits)
e = 65537
N = p*q


with open('flag.txt', 'rb') as f:
    m = bytes_to_long(f.read())

c = pow(m, e, N)

p = p * 2

print('p=', p)
print('e=', e)
print('N=', N)
print('c=', c)
