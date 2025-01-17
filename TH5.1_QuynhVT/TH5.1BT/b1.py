import numpy as np

# Tạo vector gồm 30 phần tử tăng dần từ 1 đến 30
a = np.arange(1, 31)

a_reshaped = a.reshape(6, 5, order ='C') 
#1 2 3 4 5 6
#7 8 9 10 11 12

# 1 2 3 4 5 6 7 8 9 10 11 12
a_flattened = a_reshaped.ravel()

# tach a_flattened thanh 3 nhom 
split_vectors = np.split(a_flattened, 3)

# Tách các vector con 
a_lẻ = np.array([x for x in a_flattened if x % 2 != 0]).reshape(-1) #so chan
a_chan = np.array([x for x in a_flattened if x % 2 == 0]).reshape(-1) #so le
a_3 = np.array([x for x in a_flattened if x % 3 == 0]).reshape(-1) # chi het cho 3 

print("Vector a:", a)
print("a_lẻ:", a_lẻ)
print("a_chẵn:", a_chan)
print("a_3:", a_3)
