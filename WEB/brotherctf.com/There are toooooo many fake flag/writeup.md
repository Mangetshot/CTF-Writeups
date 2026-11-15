# There are toooooo many fake flag

**Event: brotherctf.com | Category: Web | Difficulty: Easy | Date: 13/11/2026 | [Challenge](https://brotherctf.com/practice/there-are-toooooo-many-fake-flag)**

Như cái tên thì bài này chứa rất nhiều flag giả =)) Mấu chốt bài này là tìm ra và đổi giá trị của _cookie_.

## Quá trình giải

Mới vào thì trên trang web đã hiện ra một cái flag mà mình cá 100% là giả. Mình mở DevTool để xem HTML của trang thì cũng chứa 1 flag giả giống vậy ở cuối.

<div align="center"><img width="998" height="157" alt="image" src="https://github.com/user-attachments/assets/e49fbe0a-c21f-499b-8224-d11da384aea2" /></div>
<div align="center"><img width="770" height="285" alt="image" src="https://github.com/user-attachments/assets/6169de87-d068-42df-b3bf-de001b9572a4" /></div>

Mình thử vào file robots.txt có gì không và nó hiện ra đống flag giả khác, nhưng cùng với đó là các thư mục ẩn có vẻ quan trọng:

<div align="center"><img width="1072" height="238" alt="image" src="https://github.com/user-attachments/assets/87a81b99-dcf8-4581-a37c-25d7c74622bf" /></div>

Ở thư mục /admin thì cũng chỉ hiện ra 1 flag giả, còn ở /s3cr3t thì nó lại hiện ra cái này:

<div align="center"><img width="1826" height="1258" alt="image" src="https://github.com/user-attachments/assets/e2d8360d-17ca-4f5d-8b97-069ada137335" /></div>

Bro thật sự bị rickroll vào năm 2026 lớn =))

Còn lại thư mục /backup thì trông có vẻ khả quan hơn vì nó hiện một chuỗi kí tự rất giống đã được mã hóa Base64 (dấu hiện dễ nhận biết nhất là có dấu = ở cuối xuất phát từ việc padding khi mã hóa Base64). Mình đã chuyển ngược lại thử và nhận lại một chuỗi có vẻ là vẫn đang ở dạng Base64 nên mình decode lần 2 tiếp, và đã nhận được flag thật...

<div align="center"><img width="1054" height="143" alt="image" src="https://github.com/user-attachments/assets/c898e122-c12a-471b-9bf1-2db7bacda69f" /></div>
<div align="center"><img width="986" height="513" alt="image" src="https://github.com/user-attachments/assets/37476183-0977-4c3d-a34b-9d9ec278dfc0" /></div>
<div align="center"><img width="984" height="538" alt="image" src="https://github.com/user-attachments/assets/40b12892-bcf6-48a9-9761-c60a67305e25" /></div>

...ngoại trừ đây vẫn là flag giả!! T-T Khúc này mình nhập vào sai nên tuyệt vọng đến nỗi thử luôn cả mấy cái flag kia nhưng đương nhiên là sai hết rồi =))

Sau đó mình bắt đầu đi theo hướng khác là kiểm tra _cookie_ của web (cookie là dữ liệu dạng {tên:giá trị} chứa các thông tin về phiên làm việc như ID, setting,... và được lưu trữ trên trình duyệt). Để xem các cookie thì bạn chỉ cần mở DevTool lên và vô phần Application là sẽ thấy. Ở đây có 2 cái cookie, và ngoài hutech_guard ra (mình để ý là bài CTF nào cũng có nó nên chắc cũng không quan trọng mấy) thì có cái tên _flavour_ với giá trị là `Z3Vlc3Q%3D`.

<div align="center"><img width="1061" height="385" alt="image" src="https://github.com/user-attachments/assets/2bdfce79-1470-44a2-8326-6cf448e515a5" /></div>

Giá trị này có vẻ đang ở dạng URL encoding (hay percent encoding, xem thêm tại [đây](https://www.geeksforgeeks.org/html/html-url-encoding/)). Trình duyệt mình có tính năng decode sẵn luôn và ra `Z3Vlc3Q=`, đang ở dạng Base64. Khi decode thì nó ra `guest`, và lúc này mình nghĩ ra hướng là thế `admin` vô để xem coi web cho mình thêm quyền hạn gì.

Trước đó thì ta cần Base64 nó trước, sau đó URL encode ra `YWRtaW4%3D` rồi mới bỏ vào cookie và tải lại trang (nhớ quay về thư mục root của web):

<div align="center"><img width="1057" height="350" alt="image" src="https://github.com/user-attachments/assets/a5adf469-56aa-4023-b3b5-5f59d5c7d251" /></div>
<div align="center"><img width="1108" height="193" alt="image" src="https://github.com/user-attachments/assets/061fe76c-a84b-4ee4-acfd-abc7cba6692c" /></div>

Và ta đã có flag :D

**Flag:** `HUTECHCTF{H3ll0_r34l_4dm1n.}`
