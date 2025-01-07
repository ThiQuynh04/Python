# 1 xây dựng hàm trong python
def hello_MDC(str):

 print('Hi', str,', How are you?')

#5
 print('Have a nice day!')
 print('Have a nice day!')
 hello_MDC('Tùng Dương')

#2
# Xây dựng hàm tính n!
# 1) Hàm này dùng để làm gì? - Để tính n!
# 2) Hàm này nhận dữ liệu vào là gì? - Một số nguyên dương
# 3) Hàm trả kết quả là gì? - Một số nguyên dương là tích của các số từ 1 đến n

def giai_thua(n):
    # Nhóm câu lệnh xử lý bên trong hàm
    tich = 1
    for i in range(1, n+1):
        tich = tich * i
    # Kết quả trả về cho hàm
    return tich

n = int(input("Nhập vào một số nguyên N: "))
print(n, "! =", giai_thua(n))

#3
n = int(input('Nhập vào một số nguyên N: '))
print(n, '! =', giai_thua(n))
print('12! = ', giai_thua(12))

#4
#xây dựng hàm trong python
def hello_MDC(str):

 #Hiển thị câu chào
    print('Hi', str,', How are you?')
    print('Have a nice day!')

# Xây dựng hàm tính n!
def giai_thua(n):
    tich = 1
    for i in range(1, n+1):
        tich = tich * i
    return tich

#5
#Hàm tính tổng, hiệu, tích, thương:
def all_ab(a,b):
    add = a+b
    sub = a-b
    multi = a*b
    div = a/b
    #hàm trả về kết quả là 4 giá trị
    return add, sub, multi, div
#----
a = 10
b = 6

# Lấy kết quả trả về khi thực hiện hàm
tong, hieu, tich, thuong = all_ab(a, b)

# Lưu ý: Thứ tự trả về theo đúng thứ tự đã viết trong câu lệnh return

print('Tổng', a, '+', b, '=', tong)
print('Hiệu', a, '-', b, '=', hieu)
print('Tích', a, '*', b, '=', tich)
print('Thương', a, '/', b, '=', thuong)

#6
# Xây dựng hàm tính n!
# Hàm giai_thua có 1 tham số bắt buộc
def giai_thua(n):
    tich = 1
    for i in range(1, n+1):
        tich = tich * i
    return tich

# Gọi hàm giai_thua đã xây dựng
print('12! = ', giai_thua(12))

# Gọi hàm giai_thua đã xây dựng
# Khi không truyền vào tham số
print('12! = ', giai_thua())

#7

# Hàm tính tổng
def sum_ab(a=5, b=7):
    total = a + b
    return total

# Gọi hàm sum_ab() truyền vào 2 tham số
print(sum_ab(8, 13))

# Gọi hàm sum_ab() không truyền vào tham số
# Sử dụng tham số mặc định
print(sum_ab())

#8
# Xây dựng hàm tính tổng các số dựa vào
def get_sum(*num):
    tmp = 0
    # duyệt các tham số
    for i in num:
        tmp = tmp + i
    return tmp

# Gọi hàm và truyền các tham số cho hàm
result = get_sum(1,2,3,4,5)
print('Kết quả:', result)

#9
x = 300  # Biến toàn cục, có tác dụng trong toàn bộ chương trình
y = 800

def myfunc():
    # Biến địa phương, chỉ có tác dụng trong thân hàm
    x = 200
    total = x + y
    print("(Local) x:", x)
    print("total:", total)

# Gọi hàm
myfunc()

print("----------------")
print("(global) x:", x)

#10
def myfunc():
    global k  # Thiết lập biến k là biến toàn cục
    k = 300