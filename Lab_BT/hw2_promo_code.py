# hw2_promo_code.py

# Nhập họ tên và năm sinh
full_name = input("Nhập họ tên đầy đủ: ")
birth_year = input("Nhập năm sinh: ")

# Tách họ tên thành các từ
name_parts = full_name.split()

# Lấy tên cuối cùng
last_name = name_parts[-1]

# Lấy 3 chữ cái đầu của tên và viết hoa
promo_name = last_name[0:3].upper()

# Tạo mã ưu đãi bằng F-string
promo_code = f"{promo_name}-{birth_year}-VIP"

# In kết quả
print("Mã ưu đãi:", promo_code)
