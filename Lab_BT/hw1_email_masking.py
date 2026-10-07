# hw1_email_masking.py

email = input("Nhập địa chỉ email: ")

# Tách tên đăng nhập và tên miền
parts = email.split("@")
username = parts[0]
domain = parts[1]

# Lấy 3 ký tự đầu tiên của tên đăng nhập
first_three = username[0:3]

# Ghép chuỗi đã che
masked_email = first_three + "***@" + domain

print("Email sau khi che:", masked_email)
