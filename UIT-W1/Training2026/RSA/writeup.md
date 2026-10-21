# RSA
**Event: W1 Training2026 | Category: Cryptography | Date: 19/10/2026 | Challenge: [script](johan_335f59b72545e3e27e60453719d50288.py), [output](output_0ef6d6343784e59e2f44f61d2d29896f.txt)**

Ban đầu không biết độ khó nên mình làm bài này trước cả bài ECB, và đây là *MỘT SAI LẦM TAI HẠI*. Mình dành cả ngày để đọc và hiểu hướng giải, sau đó là 2-3 ngày liên tiếp để tự tạo và debug script exploit. Nhưng mà bù lại thì mình đã học được khá nhiều thứ về RSA và số học mô đun=))

Các bạn nên xem qua [cách thuật toán RSA mã hóa](https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/), và căn bản về [số học mô đun](https://www.geeksforgeeks.org/engineering-mathematics/modular-arithmetic/) để hiểu rõ hơn về bài này.

### 1. Tổng quan
- Có 2 file: script mã hóa dùng thuật toán RSA và file output chứa nhiều ciphertext dưới dạng số + số mũ e và số mô đun N dùng trong mã hóa RSA.
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
- SNT p và q được chọn ngẫu nhiên với **kích thước rất lớn** là 1024 bits, do đó tấn công brute-force đơn thuần là điều không thể. Ngoài ra theo mình tìm hiểu thì hàm getPrime() cũng không có lỗ hổng trong việc chọn ngẫu nhiên SNT nên các exploit liên quan đến Prime Factorization cũng không khả thi.

<div align="center"><img width="152" height="40" alt="image" src="https://github.com/user-attachments/assets/1b3b77ce-aab1-49ca-a928-0b909da68915" /></div>

- Tuy nhiên thì số mũ e có giá trị rất nhỏ là 3. Mình chắc chắn là sẽ có một exploit khai thác điều này (đọc tiếp sẽ biết =)) ).
- Ở đoạn cuối, từng plaintext m được lấy ra từ *messages* trong module *secret* bí ẩn nào đó để mã hóa. Theo mình đoán thì *messages* là 1 list chứa nhiều plaintext khác nhau, và 1 trong số chúng là flag ta cần tìm.

<div align="center"><img width="421" height="111" alt="image" src="https://github.com/user-attachments/assets/85794f60-4f6f-43b7-8dbf-e773648b0198" /></div>

Nhìn sang file output.txt, ta thấy tổng cộng có 7 bộ ba (n, e, c) tương ứng với 7 plaintext m trong list *messages* hồi nãy. Có thể thấy, mọi giá trị n và c **RẤT LỚN**, nhưng e luôn luôn bằng 3.

<img width="1919" height="847" alt="image" src="https://github.com/user-attachments/assets/60be2d46-b3fe-45bc-9cd8-2615b4c53472" />

Điều đầu tiên mình làm là thử tính căn bậc e (= 3) của từng c: **trong vài trường hợp, m<sup>e</sup> < n => c = m<sup>e</sup> mod n = m<sup>e</sup>**. Từ đó, chỉ cần lấy căn 3 của c là sẽ ra lại m...

<img width="1779" height="190" alt="image" src="https://github.com/user-attachments/assets/cad02b3a-ea56-42de-9832-dfabc4b86680" />

...và cả 7 kết quả đều ra căn 3 xấu T-T. Từ đó ta có thể kết luận rằng **m<sup>e</sup> > n với mọi n**.

Sau khi thất bại, mình bắt đầu theo hướng exploit số mũ e nhỏ được dùng nhiều lần. Mình tra cứu một lúc thì tìm ra **Hastad's Broadcast Attack**.

Về cơ bản, kĩ thuật tấn công này lợi dụng việc gửi 1 plaintext nhiều lần, và với mỗi cặp (c, n) mới sẽ moi thêm thông tin về plaintext gốc:
- Giả sử Alice gửi cùng 1 tin nhắn cho nhiều người khác nhau sử dụng RSA. Alice chỉ chọn đúng 1 số mũ e nhỏ nhưng vẫn chọn các số mô đun n khác nhau để cho ra các ciphertext c khác nhau cho từng lần gửi.
- **Nếu e đủ nhỏ**, Eve muốn tìm ra tin nhắn ban đầu thì chỉ cần biết **ít nhất e cặp (c, n)** mà không cần đến private key.

  <div align="center"><img width="744" height="501" alt="image" src="https://github.com/user-attachments/assets/dab48259-3112-4bf1-bd58-b6f9855c0c70" /></div>

**Mà khoan**, để dùng được exploit thì _chỉ duy nhất 1 plaintext m_ được gửi nhiều lần. Chẳng phải điều này trái lại với giả thuyết mình đề ra rằng nhiều m khác nhau đã được đưa vô hàm RSA_ecnrypt() trong file output.txt sao??

Ban đầu mình nghĩ ngay cả hướng này cũng không đúng nên đã lục lọi thêm nhiều exploit khác nữa nhưng mà cũng không khả thi. Cuối cùng thì mình đã xem bài writeup [này](https://github.com/KranBoring/CTF-Solutions/blob/main/Others-Events/2026/W1n.game_Training/RSA/write-up.md) được gửi trên group Discord của CLB (fun fact: bài writeup này cũng là động lực thúc đẩy mình tự viết writeup riêng cho mình =)) thế nên mình cảm ơn bạn/anh/chị nhéee).

Và đúng thật là trong bài writeup đã sử dụng hướng tấn công Hastad!! Nhưng mà kì lạ là người viết đã giải bằng cách _thử tất cả tổ hợp bộ 3 cặp (c, n) từ 7 cặp_ trong file output.txt cho tới khi ra được flag, đồng nghĩa là có vài plaintext m _thực sự giống nhau_. Người viết đã đưa ra 1 giả thuyết mình thấy khá là hợp lý: **trong 7 plaintext m được lấy ra từ _messages_, 3 trong số chúng là flag được lặp lại, còn lại là plaintext rác nhằm đánh lạc hướng**.

Như vậy, giờ ta sẽ bắt đầu đào sâu hơn vào cách mà Hastad's Broadcast Attack hoạt động (ai chỉ thích áp dụng liền vào script thì đi tới phần [lời giải](#solution) nha).

### 3. Hastad's Broadcast Attack
Kĩ thuật tấn công này có nguyên lí dựa trên [Định lí Thặng dư Trung Hoa (Chinese Remainder Theorem hay CRT)](https://www.scribd.com/document/892783382/%C4%90%E1%BB%8Bnh-L%C3%BD-Th%E1%BA%B7ng-D%C6%B0-Trung-Hoa). Định lý về căn bản phát biểu như sau: 
<div align="center"><img width="1218" height="355" alt="image" src="https://github.com/user-attachments/assets/5b82bbe1-375e-473f-a835-8e2f760a05c9" /></div>

Mấu chốt ở đây là **đôi một nguyên tố cùng nhau (pairwise-coprime)** và **có nghiệm duy nhất mô đun tích các số mô đun**:
- Hai số a, b là nguyên tố cùng nhau khi ƯCLN(a, b) = 1.

`VD: 6 và 7 nguyên tố cùng nhau do ƯCLN(6, 7) = 1; 6 và 8 không nguyên tố cùng nhau do ƯCLN(6, 8) = 2` 

- Một hệ đồng dư 'có nghiệm duy nhất mô đun N' tức là hệ đó chỉ có duy nhất 1 tập hợp các nghiệm đồng dư với nhau qua mô đun N (chứ không phải chỉ có 1 nghiệm!!). Tập hợp nghiệm đó được gọi là lớp đồng dư (congruence class), và để cho ngắn gọn thì được đại diện chỉ bởi 1 nghiệm trong khoảng (0, N).
- 
`VD: x 

<div align="center"><img width="522" height="332" alt="image" src="https://github.com/user-attachments/assets/9fd8bb92-4ad6-4db4-8f8f-98d1c2104939" /></div>

Nhưng mà ta cần tính m chứ đâu cần tính x chi đâu??

**Trừ khi x cũng chính là m<sup>3</sup>!!**. Điều này xảy ra khi **m<sup>3</sup> < n<sub>0</sub>n<sub>1</sub>n<sub>2</sub>**. Điều kiện này gần như là luôn đúng đối với thuật toán RSA thông thường, trong đó độ lớn plaintext m (khi đã chuyển về integer) được đảm bào nhỏ hơn số mô đun n cho quá trình mã hóa và giải mã.

Thật ra để áp dụng CRT thì vẫn cần một điều kiện quan trọng nữa: **cả 3 số mô đun n<sub>0</sub>, n<sub>1</sub>, n<sub>2</sub> phải [đôi một nguyên tố cùng nhau (pairwise-coprime)](https://vi.wikipedia.org/wiki/S%E1%BB%91_nguy%C3%AAn_t%E1%BB%91_c%C3%B9ng_nhau)**. Hiểu đơn giản là không được chọn trùng lặp các số SNT để cấu thành nên các số mô đun n khác nhau. Để kiểm tra thì mình đã lần lượt bỏ 2 trong 7 số mô đun vào hàm gcd() mà mình tự code để tìm ra ƯCLN (Nếu điều kiện không thỏa thì đây sẽ càng là một lỗ hổng nghiêm trọng mà ta có thể exploit).

```
n_list = []
c_list = []
n, e, c = 0, 0, 0

with open('output_0ef6d6343784e59e2f44f61d2d29896f.txt', 'r') as f: #Thu thập các giá trị n, e, c từ file output.txt
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

def gcd(a: int, b: int) -> int: #Xem thuật toán Euclid để hiểu rõ hon
    while b != 0:
        a, b = b, a % b
    return a

n_len = len(n_list)
for i in range(n_len-1):
    for j in range(i+1, n_len):
        res = gcd(n_list[i], n_list[j])
        if res != 1:
            print(f"Moduli {i} and {j} have a common factor: {res}")
```
Khi chạy thì terminal không in ra gì cả, nghĩa là điều kiện đã được thỏa.

Sau khi xét hết điều kiện và chứng minh _x = m<sup>3</sup>_ thì tiếp đến là bước quan trọng nhất: **Làm như thế nào để tính x??**

Ở đây ta sẽ trải qua vài bước tính toán dù code không khó nhưng mới nhìn qua chắc chắn sẽ khó mà hiểu một cách trực quan được:
1. Đặt **N = n<sub>0</sub>n<sub>1</sub>n<sub>2</sub>**. Lần luợt tính: **N<sub>i</sub> = N / n<sub>i</sub>**
2. Lần lượt tính [nghịch đảo nhân (Modular Multiplicative Inverse)](https://nhannguyen95.wordpress.com/2017/03/16/modular-multiplicative-inverse-tinh-nghich-dao-theo-phep-nhan-modulo/), đặt là _u<sub>i</sub>_, của từng N<sub>i</sub> theo mô đun n<sub>i</sub>. Nghĩa là tính _u<sub>i</sub>_ sao cho:
**<div align="center">u<sub>i</sub>N<sub>i</sub> mod n<sub>i</sub> = 1</div>**
3. Tính tổng **S = c<sub>1</sub>N<sub>1</sub>u<sub>1</sub> + c<sub>2</sub>N<sub>2</sub>u<sub>2</sub> + c<sub>3</sub>N<sub>3</sub>u<sub>3</sub>**
4. Cuối cùng, tính **x = S mod N**

<a id="solution"></a>
### 4. Lời giải 

$$
x^2 + y^2 = z^2
$$
