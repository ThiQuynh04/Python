#VD11 
import pandas as pd

path = 'csv_Data_Loan.csv'

# Sử dụng phương thức read_csv
data = pd.read_csv(path)

# Hiển thị thông tin biến Data
data.info()
# VD13 
import pandas as pd

path = 'csv_Data_Loan.csv'

# Sử dụng phương thức read_csv()
# Tham số: Thiết lập cột index là cột Personal
data1 = pd.read_csv(path, index_col=0)

data1.info()

# Hiển thị dữ liệu 5 dòng đầu tiên
data1.head()
# VD14
import pandas as pd

path = 'csv_Data_Loan.csv'

# Sử dụng phương thức read_csv()
# Thiết lập số hàng, cột muốn đọc dữ liệu
data2 = pd.read_csv(path,
                    nrows=100, 
                    usecols=['Height_cm', 'Weight_kg'])

data2.info()

# Hiển thị dữ liệu 5 dòng đầu tiên
data2.head()
# VD15 
import pandas as pd

path = 'Data_Excel.xlsx'

# Thiết lập tham số đọc dữ liệu từ dòng thứ 5 trong file
# và đặt lại tên của các cột dữ liệu
data3 = pd.read_csv(path,
                    names=['ID', 'Sex', 'H(cm)', 'W(kg)'],
                    skiprows=5)

data3.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data3.head()
#  VD21 
import pandas as pd

path_excel = 'Data_Excel.xlsx'

# Đọc dữ liệu từ file excel
data_ex = pd.read_excel(path_excel)

data_ex.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex.head()
# VD23 
import pandas as pd

path_excel = 'Data_Excel.xlsx'

# Ví dụ:
# Đọc dữ liệu tại sheet đầu tiên,
# Chỉ lấy dữ liệu cột Mã SV và các cột điểm
# Thiết lập cột đầu tiên làm index
data_ex1 = pd.read_excel(path_excel,
                        sheet_name=0,
                        usecols=[1,6,7,8,9,10],
                        index_col=0)

data_ex1.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex1.head()
# VD24 
import pandas as pd

path_excel = 'Data_Excel.xlsx'

# Ví dụ 3:
# Đọc dữ liệu tại sheet 2, từ dòng 9
data_ex3 = pd.read_excel(path_excel,
                        sheet_name='4080130_02',
                        skiprows=9)

data_ex3.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex3.head()
# VD25 
import pandas as pd

path_excel = 'Data_Excel.xlsx'

# Ví dụ 4
# Đọc dữ liệu từ sheet: '4080130_03'
# Dữ liệu không chứa dòng header
data_ex4 = pd.read_excel(path_excel,
                        sheet_name='4080130_03',
                        header=None)

data_ex4.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex4.head()
# VD 26 
import pandas as pd

path_excel = 'Data_Excel.xlsx'

# Đặt tên cho các cột lần lượt là ['Mã SV', 'A', 'B1','B2','C1','C2']
# Thiết lập cột đầu tiên làm Index
data_ex41 = pd.read_excel(path_excel,
                        sheet_name='4080130_03',
                        header=None,
                        usecols=[1,6,7,8,9,10],
                        names=['Mã SV', 'A', 'B1', 'B2', 'C1', 'C2'],
                        index_col=0)

data_ex41.info()

# Hiển thị 5 dòng dữ liệu đầu tiên
data_ex41.head()
# VD31 
import pandas as pd

# Định nghĩa đường dẫn đến tệp JSON
path_json = 'json_Data_product.json'

# Đọc dữ liệu từ file JSON vào DataFrame
data_json = pd.read_json(path_json)

# Hiển thị DataFrame
print("DataFrame đọc theo cách mặc định:")
print(data_json)
# VD32 
# Sử dụng thư viện json để làm việc với dữ liệu JSON
import json
path_json = 'json_Data_product.json'
# Đọc dữ liệu từ file JSON
with open(path_json, 'r') as myfile:
    data = myfile.read()

# Chuyển đổi dữ liệu JSON thành dictionary
obj = json.loads(data)

# Kiểm tra kiểu dữ liệu
type(obj)

# Lấy giá trị của key 'Product'
a = obj['Product']
print(a)

# Lấy giá trị của key 'Price'
b = obj['Price']
print(b)
# VD38 
# Lấy dữ liệu tỷ lệ đổi tiền
import pandas as pd
import requests as rq

url_api = 'http://api.exchangeratesapi.io/v1/latest?access_key=06a81a333abfe2ac294f7bc88bac1ec9'

# Lấy dữ liệu theo url_api
result_money = rq.get(url_api)

# Kiểm tra trạng thái request
print(result_money.status_code)

# Chuyển đổi dữ liệu sang kiểu string
data_text = result_money.text

# Chuyển đổi dữ liệu sang kiểu json
data_json = result_money.json()
print('Text:', data_text)
print('--------------------------------')
print('Json:', data_json)

# Chuyển đổi dữ liệu Json sang kiểu DataFrame
df = pd.DataFrame(data_json)
print(df.head(10))

# VD39 
import pandas as pd
import requests as rq

url_api = 'http://api.exchangeratesapi.io/v1/latest?access_key=06a81a333abfe2ac294f7bc88bac1ec9'

result_money1 = rq.get(url_api, params={'symbols': 'USD, JPY, THB, VND, MYR, GBP, KRW'})
data_json1 = result_money1.json()

df1 = pd.DataFrame(data_json1)
print(df1.head(10))

# VD45 
import pymongo as mg

address = "118.70.196.130:27017"
user = "root"
pas = "Humg@123mg"
auth = "SCRAM-SHA-1"
database = "Data_Laichau"
coll_name = "LC_Meteorology"

client = mg.MongoClient(address, username=user, password=pas, authMechanism=auth)
db = client[database]
col = db[coll_name]

stationid = "TU"
data_mg = col.find({"Id": stationid}).sort([("Time", -1)])
print(type(data_mg))

# VD46 
dt_time, dt_rain, dt_t2m, dt_tm, dt_tx = [], [], [], [], []

for i in data_mg:
    dt_time.append(str(i['Time']))
    dt_rain.append(i['Rain'])
    dt_t2m.append(i['T2m'])
    dt_tm.append(i['Tm'])
    dt_tx.append(i['Tx'])

ziplist_water = list(zip(dt_time, dt_rain, dt_t2m, dt_tm, dt_tx))

import pandas as pd

df = pd.DataFrame(ziplist_water, columns=['Time', 'Rain', 'T2m', 'Tm', 'Tx'], index=None)

df.info()
df.head()

# VD51 
import sklearn.datasets

data_boston = sklearn.datasets.load_boston()
data_iris = sklearn.datasets.load_iris()
data_diabetes = sklearn.datasets.load_diabetes()
data_digits = sklearn.datasets.load_digits()
data_linnerud = sklearn.datasets.load_linnerud()
data_wine = sklearn.datasets.load_wine()
data_breast_cancer = sklearn.datasets.load_breast_cancer()

# VD52 
import sklearn.datasets as datask

X, y = datask.load_boston(return_X_y=True)

print(type(X))
print('Kích thước dữ liệu đầu vào (features):', X.shape)
print('Kích thước dữ liệu đầu ra (target):', y.shape)

# VD54 
import sklearn.datasets as datask

X_iris, y_iris = datask.load_iris(return_X_y=True)

print(type(X_iris))
print('Kích thước dữ liệu đầu vào (features):', X_iris.shape)
print('Kích thước dữ liệu đầu ra (target)   :', y_iris.shape)

print('Bộ dữ liệu 1  ', X_iris[1,:], '--', y_iris[1])
print('Bộ dữ liệu 55 ', X_iris[55,:], '--', y_iris[55])
print('Bộ dữ liệu 111', X_iris[111,:], '--', y_iris[111])
#  VD60 
import sklearn.datasets as datask

X_features, y_target = datask.make_classification(
    n_samples=200, 
    n_features=5, 
    n_classes=2
)

print(X_features[:10,:])
print(y_target[:10])

# VD61 
import sklearn.datasets as datask

X_features, y_target, coeff = datask.make_regression(
    n_samples=200,
    n_features=5,
    n_informative=3,
    n_targets=1,
    noise=0.0,
    coef=True,
    random_state=1
)

print(X_features[:10,:])
print(y_target[:10])

# VD62 
import sklearn.datasets as datask

X_features, y_target = datask.make_blobs(
    n_samples=1000,
    centers=4,
    n_features=2,
    random_state=0
)

print(X_features[:10,:])
print(y_target[:10])



