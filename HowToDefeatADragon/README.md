# [WRITE_UP] ShellCTF_HowToDefeatDragon

### Đề bài 
![Imgur](https://i.imgur.com/LPmx6rK.png)

Đề cho file *vault*, vứt vào kali để chạy cho kết quả như này: 

![Imgur](https://i.imgur.com/qmOdwJ0.png)

Vứt vào ida Vào String view search *wron..aaaaaahhhhhhhh* dẫn đến đây:

![Imgur](https://i.imgur.com/I9mHsOs.png)

Chuyển sang chế độ xem pseudocode ta nhận được đoạn text sau với mật khẩu *69420*:

![Imgur](https://i.imgur.com/E69SjMb.png)

```
SHELLCTF{5348454c4c4354467b31355f523376337235316e675f333473793f7d}
```

Test thử trên kali :

![Imgur](https://i.imgur.com/fRPHyaj.png)

Có vẻ vẫn chưa đúng, đoạn text bên trong *SHELLCTF{}* giống giống một đoạn hex, copy ra rồi vào kt.gy convert:

![Imgur](https://i.imgur.com/DEzdu61.png)

#Done

**Flag: SHELLCTF{15_R3v3r51ng_34sy?}**
