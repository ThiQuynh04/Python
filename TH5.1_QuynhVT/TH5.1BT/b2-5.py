def calculate_bmi(height, weight):
    height_m = height / 100
    return weight / (height_m ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese"
    else:
        return "Extremely Obese"

bmi_categories = {
    "Underweight": 0,
    "Normal": 0, 
    "Overweight": 0,
    "Obese": 0,
    "Extremely Obese": 0
}

try:
    with open('C:\\Users\\TV\\Documents\\BTTH_Python\\TH5.1_TrangTTH\\TH5.1BT\\Data_BMI.txt', 'r') as file:
        for line in file:
            height, weight = map(float, line.strip().split())
            bmi = calculate_bmi(height, weight)
            category = classify_bmi(bmi)
            bmi_categories[category] += 1
            
    total = sum(bmi_categories.values())
    print(f"Tổng số: {total}")
    print("-" * 40)
    for i, (category, count) in enumerate(bmi_categories.items(), 1):
        print(f"{i}. {category:<15}: {count}")

except FileNotFoundError:
    print("Error: File Data_BMI.txt not found")
except Exception as e:
    print(f"Error occurred: {e}")