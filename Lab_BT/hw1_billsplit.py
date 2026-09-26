# hw1_billsplit.py

def main():
    # Nhập thông tin từ người dùng
    X = float(input("Nhập tổng hóa đơn (X đồng): "))
    Y = float(input("Nhập phần trăm tiền tip (Y %): "))
    N = int(input("Nhập số người chia (N): "))

    # Tính tổng tiền tip và tổng số tiền phải trả
    tip_amount = X * (Y / 100)
    total_amount = X + tip_amount

    # Tính số tiền mỗi người phải trả
    per_person = total_amount / N

    # Làm tròn đến số nguyên 
    result = round(per_person)

    # In kết quả
    print(f"Số tiền thực tế mỗi người phải trả: {result:,} đồng")

if __name__ == "__main__":
    main()

