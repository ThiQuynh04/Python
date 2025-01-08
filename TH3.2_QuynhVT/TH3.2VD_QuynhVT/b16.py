class Person:
    def __init__(self, name, year, height, weight):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight
    
    def Getting(self):
        print("Thông tin: ")
        print(f"Name: {self.name}")
        print(f"Year of Birth: {self.year}")
        print(f"Height: {self.height} m")
        print(f"Weight: {self.weight} kg")
    
    def Bmi(self):
        if self.height <= 0:
            return "Chiều cao phải lớn hơn 0 để tính BMI."
        bmi_value = self.weight / (self.height ** 2)
        return round(bmi_value, 2)

def get_input():
    while True:
        try:
            print("Nhập thông tin")
            name = input("Vui lòng nhập tên: ")
            year = int(input("Vui lòng nhập năm sinh: "))
            height = float(input("Vui lòng nhập chiều cao (m): "))
            weight = float(input("Vui lòng nhập cân nặng (kg): "))
            
            if year <= 0 or height <= 0 or weight <= 0:
                raise ValueError("Năm sinh, chiều cao và cân nặng phải > 0.")
            return name, year, height, weight
        except ValueError as e:
            print(f"Lỗi nhập liệu: {e}. Vui lòng nhập lại.")

def main():
    name, year, height, weight = get_input()
    person = Person(name, year, height, weight)
    
    while True:
        print("\nChọn hành động:")
        print("1. Hiển thị thông tin")
        print("2. Tính chỉ số BMI")
        print("3. Thoát")
        
        try:
            choice = int(input("Nhập lựa chọn của bạn (1/2/3): "))
            
            if choice == 1:
                person.Getting()
            elif choice == 2:
                bmi = person.Bmi()
                print(f"BMI: {bmi}")
            elif choice == 3:
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ.")

# Chạy chương trình
main()