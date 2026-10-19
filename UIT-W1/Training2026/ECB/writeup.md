# ECB
**Event: W1 Training2026 | Category: Cryptography | Date: 19/10/2026 | [Challenge](ecb.py)**

Đây là bài writeup đầu tiên của mình nên sẽ không thể tránh khỏi những thiếu sót, mong các bạn thông cảm!! Với lại mấy thử thách CTF của CLB là do mình hóng trên group Discord chứ mình không phải thành viên TeamT nha T-T.

### 1. Tổng quan
- Ta được cho 1 script python dùng để mã hóa plaintext thành ciphertext sử dụng thuật toán AES, chế độ ECB. Cuối script cho sẵn một ciphertex ở dạng hex.
- Mục tiêu: Tìm lại flag từ ciphertext đã cho.
- Kĩ thuật: Tấn công brute-force.

### 2. Quan sát ban đầu
Nhìn vào script, ta thấy module AES được dùng để mã hóa flag, và chế độ mã hóa ECB được dùng (mã hóa từng block riêng lẻ một cách độc lập, tai tiếng vì tính rủi ro bảo mật cao).

Ngoài ra, thứ đập vào mắt mình là dòng code chọn ngẫu nhiên key dùng để mã hóa: `key_int = secrets.randbelow(1_000_001)`. Đây chắc chắn là một lỗ hổng ta có thể exploit khi độ lớn key chỉ vỏn vẹn từ 0-1.000.000 (đâu đó khoảng 20 bits).

Sau khi suy nghĩ các hướng giải theo hướng exploit ECB, mình nhận ra trong module AES có hàm decrypt!!: `AES.new(key, AES.MODE_ECB).decrypt()`. 

Vì AES là thuật toán mã hóa đối xứng nên key mã hóa cũng chính là key phá khóa. Từ đó ta chỉ cần brute force tất cả các giá trị của key mã hóa ban nãy và bỏ vào hàm decrypt là sẽ ra được flag.

### 3. Lời giải
- Thử từng giá trị của key cho tới khi ra cờ.
- [Script](solution.py)

  <img width="656" height="255" alt="image" src="https://github.com/user-attachments/assets/c98d4ea9-9232-4971-ae0b-3ae3b30c88a2" />

### Bài học rút ra: Tạo key với độ lớn ít nhất 128 bits!!
