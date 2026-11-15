# Check It Out

**Event: brotherctf.com | Category: Web | Difficulty: Easy | Date: 15/11/2026 | [Challenge](https://brotherctf.com/practice/check-it-out)**

Hôm bữa mình thử đủ thể loại kĩ thuật tấn công nâng cao cho bài này (overthinking chúa) mà không ra nên bỏ. Hôm nay thử làm lại thì ai ngờ flag được giấu trong file CSS mà mình còn không thèm check =))

## Quá trình giải

Vào trang web thì giao diện trông có vẻ bình thường, và trong HTML cũng không có gì khả nghi. Mình có thử nhập vào các tên thư mục phổ biến thì _/.env_ trả lại kết quả này:

<div align="center"><img width="1041" height="211" alt="image" src="https://github.com/user-attachments/assets/121dc9e1-007b-45fa-99d0-bfa0bab30e13" /></div>

Mình thử nhập flag ở cuối nhưng mà không đúng, tìm hiểu sâu hơn thì bài CTF nào cũng có thư mục này. Mình cũng thử nhiều hướng tấn công khác mà không thành nên bỏ cuộc suốt mấy ngày T-T. Nay giải lại thử thì mình mới nhận ra có file _style.css_ mà mình chưa kiểm tra (đần thiệt chứ =)) ). Lướt tới cuối file thì xuất hiện phần comment có chứa 1 chuỗi kí tự rất khả nghi, trông có vẻ là số thập lục phân.

<div align="center"><img width="1046" height="537" alt="image" src="https://github.com/user-attachments/assets/7e4985d4-f8c0-422a-86b5-ce3d2503e20f" /></div>

Mình thử đổi số đó về bytes trong Python và đã ra được flag :D

<div align="center"><img width="747" height="207" alt="image" src="https://github.com/user-attachments/assets/29a24324-3f9c-4cf3-a325-9a147836abdb" /></div>

**Flag:** `HUTECHCTF{w4rmup_w3b_f0r_y0u}`
