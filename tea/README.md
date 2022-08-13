# [WRITE_UP] ShellCTF_Tea

### Đề

![Imgur](https://i.imgur.com/YZNhZpw.png)

# Sơ bộ

Đề cho file **tea** chạy bằng kali được kết quả như này: 

![Imgur](https://i.imgur.com/mSWh9cq.png)

Vẫn là dạng tìm mật khẩu phù hợp, ném vào IDA xe, sourceCode thì thấy, đầu tiên chương trình kiểm tra coi đoạn text nhập vào có dài đủ 32 ký tự không, nếu sai sẽ in ra chuỗi *wrong length*:

![Imgur](https://i.imgur.com/j3jsGd5.png)

Khi đã kiểm tra xong kết quả ta thấy chuơng trình chạy qua 3 func **addSugar**, **addTea**, **addMilk** để sửa xâu nhập vào, sau đó gọi func **strainAndServe** để so sánh 
xâu nhận được với đoạn text dưới đây, nếu đúng sẽ in ra flag:

```
R;crc75ihl`cNYe`]m%50gYhugow~34i
```

![Imgur](https://i.imgur.com/PcIfv9n.png)

# Xử lý
Ta xem xét hàm **addMilk** chương trình sẽ lấy đoạn từ đầu đến trước ký tự *'R'* điền vào cuối của xâu được trả về của hai hàm trên:

![Imgur](https://i.imgur.com/F56bgFZ.png)

Đối với hàm **addTea** chương trình chia đôi str nhận vào, lấy từng ký tự của nửa đầu **+ 3 * (vitri / -2)** lưu vào **dest**, lấy từng ký tự của 
nửa cuối **+ vitri / 6** lưu vào **src**, sau đó *str* ban đầu được gán bằng **src + dest**:

![Imgur](https://i.imgur.com/hu6AzZW.png)

Còn đối với hàm **addSugar** chuơng trình sẽ lấy ký tự có index lẻ lưu vào **v2**, ký tự có index chẵn lưu vào **dest** sau đó *str* ban đầu được gán bằng **v2 + dest**:


![Imgur](https://i.imgur.com/mCBGVCI.png)

Tóm tắt lại:Chương trình sẽ nhận vào flag sau đó viết ký tự vị trí lẻ vào nửa đầu, chẵn vào nửa sau, sau đó lấy mã ascii của từng ký tự trong nửa đầu **+ 3 * (vitri / -2)**
lấy từng ký tự trong nửa sau ** + vitri / 6** và đổi vị trí hai nửa, sau đó cắt đoạn từ đầu đến 'R' gắn vào cuối để nhận được *R;crc75ihl`cNYe`]m%50gYhugow~34i*, Trên nguyên
lý đó ta viết script bằng python

# Script brute force flag

```
output = 'R;crc75ihl`cNYe`]m%50gYhugow~34i'

a = ''
count = 0
while count<32:
    v14 = output[count:]
    v14 += output[0:count]
    dest = ''
    src = ''
    for i in range(16,32):
        dest += chr(ord(v14[i]) - 3*((i-17)//(-2)))
    for i in range(16):
        src += chr(ord(v14[i]) - (i+16)//6)
    flag = ''
    for i in range(16):
        flag+=src[i]
        flag+=dest[i]
    count+=1
    print(flag)
```

Kết quả chạy ra là :
![Imgur](https://i.imgur.com/V5MfA6Y.png)

Done !!!

**Flag: shellctf{T0_1nfiNi7y_4nD_B3y0nd}**
