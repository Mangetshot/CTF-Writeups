# INDEXING

**Event: brotherctf.com | Category: Web | Difficulty: Easy | Date: 10/11/2026 | [Challenge](https://brotherctf.com/practice/indexing)**

Đây là bài Web đầu tiên mình giải được trên brotherctf.com và cũng khá là dễ (Ban đầu mình làm bài Check It Out nhưng không giải ra nên mới qua bài này =)) ).

## Quá trình giải
Khi mới vào địa chỉ web thì nó chẳng hiện ra gì cả: 

<div align="center"><img width="1915" height="996" alt="image" src="https://github.com/user-attachments/assets/3bc675a2-6c1b-4837-8729-9330b23409f0" /></div>

Nếu chú ý đến phần description thì sẽ có 1 hint để giải bài này:

<div align="center"><img width="1421" height="316" alt="image" src="https://github.com/user-attachments/assets/ec93cba5-1735-4d84-89aa-b186b2bccbb0" /></div>

**"Crawl it to win it"** - đọc xong mình nghĩ ngay đến file [robots.txt](https://en.wikipedia.org/wiki/Robots.txt) dùng để cho phép/không cho phép các con [web crawler](https://en.wikipedia.org/wiki/Web_crawler) crawl các thư mục nào. Như vậy ta sẽ xem coi trang web này có file ấy hay không và trong đó có gì:

<div align="center"><img width="820" height="365" alt="image" src="https://github.com/user-attachments/assets/c1b71e0f-f194-4486-ae73-ce7646e0b1d1" /></div>

File robots.txt này sẽ hiện các thư mục có trên trang web, kèm theo file _sitemap.xml_ chứa các đường dẫn URL mà chủ web thấy cần thiết và khuyến khích cho các con web crawler vào crawl.

Mình đã thử truy cập vào các thư mục nêu trên nhưng toàn ra lỗi 404 nên mình tiếp tục xem file sitemap.xml có gì:

<div align="center"><img width="801" height="692" alt="image" src="https://github.com/user-attachments/assets/4b6a76fc-66e1-4c51-a700-57fbb6776864" /></div>

Trong file chứa những đường dẫn đến các thư mục mà mình đã thử truy cập hồi nãy. NHƯNG ở cuối có thêm một file thú vị là _secret.xml_.

<div align="center"><img width="792" height="295" alt="image" src="https://github.com/user-attachments/assets/4db0dc61-05f3-4959-8df8-da63289e7860" /></div>

File này hiện ra một đoạn HTML có chứa chuỗi kí tự nhìn rất giống đã được mã hóa Base64 nên mình thử chuyển ngược lại và ra được flag :D

<div align="center"><img width="982" height="687" alt="image" src="https://github.com/user-attachments/assets/f5ae0f50-079c-4924-b08b-337ed29b6cb1" /></div>

**Flag: `HUTECHCTF{4r3_y0u_r0b0ts??}`**
