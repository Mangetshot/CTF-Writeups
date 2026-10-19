# RSA
**Event: W1 Training2026 | Category: Cryptography | Date: 19/10/2026 | Challenge: [script](johan_335f59b72545e3e27e60453719d50288.py), [output](output_0ef6d6343784e59e2f44f61d2d29896f.txt)**

Ban đầu không biết độ khó nên mình làm bài này trước cả bài ECB, và đây là *MỘT SAI LẦM TAI HẠI*. Mình dành cả ngày để đọc và hiểu hướng giải, sau đó là 2-3 ngày liên tiếp để tự tạo và debug script exploit. Nhưng mà bù lại thì mình đã học được khá nhiều thứ về RSA và phép toán modulo=))

Các bạn nên xem qua [cách thuật toán RSA mã hóa](https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/) để hiểu rõ bài này.

### 1. Tổng quan
- Có 2 file: script mã hóa dùng thuật toán RSA và file output chứa nhiều ciphertext dưới dạng số + số mũ e và số mô-đun N dùng trong mã hóa RSA.
- Mục tiêu: Tìm flag từ các số N, e, c đã cho.
- Kĩ thuật: **Hastad's Broadcast Attack**.

### 2. Quan sát ban đầu
Nhìn sơ qua script, quá trình mã hóa tương tự như RSA:
- Chuyển plaintext m từ dạng bytes sang integer.
- Chọn 2 số nguyên tố siêu to p và q, tính số mô-đun N = pq.
- Chọn số mũ e (thường là 65537).
- Ta có ciphertext: c = m<sup>e</sup> mod N.
- Cuối cùng, hàm trả về N, e, c.
<div align="center"><img width="418" height="169" alt="image" src="https://github.com/user-attachments/assets/117a2074-a220-4040-b7ab-4d86207ac41c" /></div>


Ở đây có vài thứ mình để ý:
- SNT p và q được chọn ngẫu nhiên với **kích thước rất lớn** là 1024 bits, do đó tấn công brute-force đơn thuần là điều không thể. Ngoài ra theo mình tìm hiểu thì hàm getPrime() cũng không có lỗ hổng trong việc chọn ngẫu nhiên SNT nên các exploit liên quan đến việc phân tích N ra thừa số nguyên tố cũng không khả thi.
<div align="center"><img width="152" height="40" alt="image" src="https://github.com/user-attachments/assets/1b3b77ce-aab1-49ca-a928-0b909da68915" /></div>

- Tuy nhiên thì số mũ e có giá trị rát nhỏ là 3. Mình chắc chắn là sẽ có một exploit khai thác điều này (đọc tiếp sẽ biết =)) ).
- Ở đoạn cuối, từng plaintext m được lấy ra từ *messages* trong module *secret* bí ẩn nào đó để mã hóa. Theo mình đoán thì *messages* là 1 list chứa nhiều plaintext khác nhau, và 1 trong số chúng là flag ta cần tìm.
<div align="center"><img width="421" height="111" alt="image" src="https://github.com/user-attachments/assets/85794f60-4f6f-43b7-8dbf-e773648b0198" /></div>

Nhìn sang file output.txt, ta thấy tổng cộng có 7 bộ ba (n, e, c) tương ứng với 7 plaintext m trong list *messages* hồi nãy. Có thể thấy, mọi giá trị n và c **RẤT LỚN**, nhưng e luôn luôn bằng 3.
<img width="1919" height="847" alt="image" src="https://github.com/user-attachments/assets/60be2d46-b3fe-45bc-9cd8-2615b4c53472" />

Điều đầu tiên mình làm là thử tính căn bậc e (= 3) của từng c: **trong vài trường hợp, m<sup>e</sup> < n => c = m<sup>e</sup> (mod n) = m<sup>e</sup>**. Từ đó, chỉ cần lấy căn 3 của c là sẽ ra lại m...
<img width="1779" height="190" alt="image" src="https://github.com/user-attachments/assets/cad02b3a-ea56-42de-9832-dfabc4b86680" />
...và cả 7 kết quả đều ra căn 3 không hoàn thiện T-T. Từ đó ta có thể kết luận rằng **m<sup>e</sup> > n với mọi n**.

Sau khi thất bại, mình bắt đầu theo hướng exploit số mũ e nhỏ được dùng nhiều lần. Mình tra cứu một lúc thì tìm ra **Hastad's Broadcast Attack**.

Về cơ bản, kĩ thuật tấn công này lợi dụng việc gửi 1 plaintext nhiều lần, và với mỗi cặp (c, n) mới sẽ moi thêm thông tin về plaintext gốc:
- Giả sử Alice gửi cùng 1 tin nhắn cho nhiều người khác nhau sử dụng RSA. Alice chỉ chọn đúng 1 số mũ e nhỏ nhưng vẫn chọn các số mô-đun n khác nhau để cho ra các ciphertext c khác nhau cho từng lần gửi.
- **Nếu e đủ nhỏ**, Eve muốn tìm ra tin nhắn ban đầu thì chỉ cần biết **ít nhất e cặp (c, n)** mà không cần đến private key.
