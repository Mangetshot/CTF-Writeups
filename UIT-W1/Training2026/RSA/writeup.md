# RSA
**Event: W1 Training2026 | Category: Cryptography | Date: 19/10/2026 | Challenge: [script](johan_335f59b72545e3e27e60453719d50288.py), [output](output_0ef6d6343784e59e2f44f61d2d29896f.txt)**

Ban đầu không biết độ khó nên mình làm bài này trước cả bài ECB, và đây là *MỘT SAI LẦM TAI HẠI*. Mình dành cả ngày để đọc và hiểu hướng giải, sau đó là 2-3 ngày liên tiếp để tự tạo và debug script exploit. Nhưng mà bù lại thì mình đã học được khá nhiều thứ về RSA và phép toán modulo=))

### 1. Tổng quan
- Có 2 file: script mã hóa dùng thuật toán RSA và file output chứa nhiều ciphertext dưới dạng số + số mũ e và số chia N dùng trong mã hóa RSA.
- Mục tiêu: Tìm flag từ các số N, e, c đã cho.
- Kĩ thuật: Hastad's Broadcast Attack.

### 2. Quan sát ban đầu

