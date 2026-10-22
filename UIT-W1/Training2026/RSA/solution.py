from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot #Hàm lấy căn của số siêu to

n_list = []
c_list = []
n, e, c = 0, 0, 0

with open('/media/mangetshot/304E07574E0714EE/STUDY MATERIAL/Cybersecurity/Cryptography/Challenges/Training2026/RSA/output_0ef6d6343784e59e2f44f61d2d29896f.txt', 'r') as f: #Thu thập các giá trị n, e, c từ file output.txt
    for line in f.readlines():
        first = line[0]
        stripped = line.strip()[4:]

        if first == 'n':
            n = int(stripped)
        elif first == 'e':
            e = int(stripped)
        elif first == 'c':
            c = int(stripped)

        if n != 0 and c != 0:
            n_list.append(n)
            c_list.append(c)
            n, c = 0, 0


def hastad_broadcast_attack(n0: int, c0: int, n1: int, c1: int, n2: int, c2: int):
    N = n0 * n1 * n2
    N0 = n1 * n2
    N1 = n0 * n2
    N2 = n0 * n1

    u0 = pow(N0, -1, n0)
    u1 = pow(N1, -1, n1)
    u2 = pow(N2, -1, n2)

    x = c0*N0*u0 + c1*N1*u1 + c2*N2*u2

    a = x % N

    return a

for i in range(5):
    for j in range(i+1, 6):
        for k in range(j+1, 7): #Lấy tổ hợp chập 3 của 7 cặp (n, c)
            m_cubed = hastad_broadcast_attack(n_list[i], c_list[i], n_list[j], c_list[j], n_list[k], c_list[k])
            m, complete_root = iroot(m_cubed, 3)

            if complete_root: #True nếu lấy căn 3 ra số nguyên
                flag = long_to_bytes(m)
                print(f"Flag retrieved: {flag}")
                quit()
