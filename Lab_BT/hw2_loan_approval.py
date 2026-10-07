# hw2_loan_approval.py

has_bad_debt = input("Khách hàng có nợ xấu không? (True/False): ") == "True"
income = float(input("Nhập thu nhập hàng tháng (VNĐ): "))
monthly_payment = float(input("Nhập số tiền trả góp hàng tháng (VNĐ): "))

# Bước 1: Kiểm tra CIC
if has_bad_debt:
    print("TỪ CHỐI VAY - Khách hàng có nợ xấu.")

else:
    # Bước 2: Kiểm tra thu nhập
    if income < 15_000_000:
        print("TỪ CHỐI VAY - Không đủ hạn mức thu nhập tối thiểu.")

    else:
        # Bước 3: Kiểm tra tỷ lệ DTI
        if monthly_payment <= 0.5 * income:
            print("DUYỆT KHOẢN VAY.")

        else:
            print("TỪ CHỐI VAY - Tỷ lệ rủi ro tài chính vượt mức cho phép.")
