# RSA
**Event: W1 Training2026 | Category: Cryptography | Date: 19/10/2026 | Challenge: [script](johan_335f59b72545e3e27e60453719d50288.py), [output](output_0ef6d6343784e59e2f44f61d2d29896f.txt)**

Ban đầu không biết độ khó nên mình làm bài này trước cả bài ECB, và đây là *MỘT SAI LẦM TAI HẠI*. Mình dành cả ngày để đọc và hiểu hướng giải, sau đó là 2-3 ngày liên tiếp để tự tạo và debug script exploit. Nhưng mà bù lại thì mình đã học được khá nhiều thứ về RSA và phép toán modulo=))

Các bạn nên xem qua [cách thuật toán RSA mã hóa](https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/) để hiểu rõ bài này.

### 1. Tổng quan
- Có 2 file: script mã hóa dùng thuật toán RSA và file output chứa nhiều ciphertext dưới dạng số + số mũ e và số chia N dùng trong mã hóa RSA.
- Mục tiêu: Tìm flag từ các số N, e, c đã cho.
- Kĩ thuật: **Hastad's Broadcast Attack**.

### 2. Quan sát ban đầu
Khi đọc script, có 2 thứ mà mình để ý:
- Số nguyên tố p và q được chọn ngẫu nhiên với **kích thước rất lớn** là 1024 bits, do đó tấn công brute-force đơn thuần là điều không thể. Ngoài ra theo mình tìm hiểu thì hàm getPrime() cũng không có lỗ hỏng trong việc chọn ngẫu nhiên SNT nên các exploit liên quan đến phân tích N ra thừa số nguyên tố cũng không khả thi.
<div align="center"><img width="152" height="40" alt="image" src="https://github.com/user-attachments/assets/1b3b77ce-aab1-49ca-a928-0b909da68915" /></div>

- Tuy nhiên thì số mũ e có giá trị rát nhỏ là 3. Mình chắc chắn là sẽ có một exploit khai thác điều này, và sau khi tra cứu thì đúng là như vậy: Hastad's Broadcast Attack. 
