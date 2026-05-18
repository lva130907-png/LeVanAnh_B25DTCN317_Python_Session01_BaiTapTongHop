""" 
Các bước làm:
B1: Khai báo các biến chứa thông tin bệnh nhân
B2: Cho người dùng nhập và ép kiểu dữ liệu tương ứng
B3: Hiển thị theo yêu cầu

"""
import random

patient_name = input("Mời nhập tên bệnh nhân: ")
gender = input("Mời nhập giới tính: ")
birth_year = int(input("Mời nhập năm sinh: "))
phone_number = input("Mời nhập số điện thoại: ")
email = input("Mời nhập email: ")
initial_symptoms = input("Mời nhập triệu chứng: ")
examination_cost = float(input("Nhập chi phí khám: "))

print("--- THẺ BỆNH NHÂN ---")

# 3. Hiển thị theo yêu cầu:
#  Mã bệnh nhân: theo quy tắc: "BN" + năm sinh + 3 số ngẫu nhiên
random_number = random.randint(100, 999)
print("Mã bệnh nhân là: ", "BN" + str(birth_year) + str(random_number))
print("Tên: ", patient_name)
print("Năm sinh: ",birth_year)
print("Điện thoại: ",phone_number)
print("Email: ",email)
print("Triệu chứng: ",initial_symptoms)
print("Chi phí: ",examination_cost)