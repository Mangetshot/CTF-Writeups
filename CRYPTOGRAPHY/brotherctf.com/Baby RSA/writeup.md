# Baby RSA
**Event: brotherctf.com | Category: Cryptography | Date: 15/11/2026 | Challenge: [script](Challenge/chall.py), [output](Challenge/output.txt)**

Bài này khá dễ vì đã cho sẵn tất cả giá trị cần thiết để tình ra khóa riêng tư :v Để hiểu rõ hơn thì bạn xem [cách thuật toán RSA hoạt động](https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/).

### 1. Tổng quan
- Có 2 file: file chương trình mã hóa dùng thuật toán RSA và file output khi cho giá trị flag vào chương trình
- Mục tiêu: Tìm flag từ các thông số đã cho.
- Kĩ thuật: **Tính khóa riêng tư.**

### 2 Quan sát ban đầu

Nhìn sơ qua script thì đây là thuật toán RSA thông thường, và qua file output.txt ta biết giá trị của số nguyên tố p, số mũ e, số mô đun N, và số ciphertext c. Từ đó, ta có thể tính số nguyên tố q còn lại => tính được giá trị hàm phi Euler => tính được khóa riêng tư d = giải ra được flag.

<div align="center"><img width="1024" height="572" alt="image" src="https://github.com/user-attachments/assets/31d9d943-deae-4830-b4dc-9da26c5f3c09" /></div>

### 3. Lời giải
- Tính SNT q = N / p
- Tính phi = (p-1)(q-1)
- Tính khóa riêng tư d là nghịch đảo nhân của e mod phi, nghĩa là d*e $\equiv$ 1 (mod phi)
- Tính plaintext m = c<sup>d</sup> mod N
- Giải ra flag bằng cách đổi plaintext ở dạng số về bytes.
- [Script](solution.py)

`b'HUTECHCTF{th15_15_s0_cut3}'`
