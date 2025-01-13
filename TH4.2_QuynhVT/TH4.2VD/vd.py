# VD40

#Max Min: Xác định giá trị lớn nhất, nhỏ nhất:
#1) Hiển thị điểm cao nhất, thấp nhất của lớp 2A
print('Điểm cao nhất của lớp:', diem_2a.max())
print('Điểm thấp nhất của lớp:', diem_2a.min())

#2) Liệt kê điểm cao nhất và thấp nhất theo môn học
for i in range(0,diem_2a.shape[0]):
    print('Môn', i,': Điểm Max:', diem_2a[i,:].max(),
          'Điểm Min:', diem_2a[i:].min())

#3) Liệt kê điểm cao nhất và thấp nhất của mỗi học sinh
for i in range(0,diem_2a.shape[1]):
    print('Học sinh', i,': Điểm Max:', diem_2a[:,i].max(),
          'Điểm Min:', diem_2a[:,i].min())
    
# VD41
diem_2a.sum()
print('Tổng tất cả điểm trong của lớp 2A:', 
      diem_2a.sum())

for i in range(diem_2a.shape[1]):
    print('Tổng điểm các môn của học sinh', i,':', 
          diem_2a[:,i].sum())

# VD43
diem_2a.mean()
print('Điểm trung bình của cả lớp 2A:', 
      diem_2a.mean())

for i in range(diem_2a.shape[1]):
    print('Điểm trung bình của học sinh', i,':', 
          diem_2a[:,i].mean())

mean_2a = diem_2a.mean(axis=0)
for i in range(mean_2a.size):
    print('Điểm trung bình của học sinh', i,':', mean_2a[i])

# VD44
a=diem_2a[1,:15]
print('Mảng a ban đầu: \n', a)
print('Số phần tử trong mảng a: ', a.size)
print('Mảng a đã sắp xếp: \n', np.sort(a))
print('Giá trị trung bình mean:', np.mean(a))
print('Giá trị trung vị median:', np.median(a))

# VD45
from scipy import stats as sp
for i in range(0,diem_2a.shape[0]):
    a = sp.mode(diem_2a[i,:])
    print('Môn', i,': Điểm xuất hiện nhiều nhất: ', a[0], ' số lần: ', a[1])
    print(type(a))

# VD46
for i in range(0,diem_2a.shape[1]):
    print('Độ chênh của học sinh', i,':',
           diem_2a[:,i].max() - diem_2a[:,i].min())

# VD47
a = np.array([10, 1, 1, 9, 12, 1, 9, 12, 10])
print('Phần tử của mảng a:', a)
print('Giá trị trung bình:', a.mean())
print('Độ lệch chuẩn:', a.std())

b = np.array([7, 7, 8, 7, 8, 7, 7, 7, 7])
print('Phần tử của mảng b:', b)
print('Giá trị trung bình:', b.mean())
print('Độ lệch chuẩn:', b.std())

# VD53
a_giohoc = np.array([4, 7, 1, 2, 8, 0, 3, 8, 6])
b_diem = np.array([7, 9, 3, 4, 9, 0, 5, 10, 8])
co = np.corrcoef(a_giohoc, b_diem)
print(type(co))
print('Hệ số tương quan: \n', co)