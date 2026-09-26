# e_invoice.py

# 1. Nhập thông tin sản phẩm từ người dùng
ten_san_pham = input("Nhập tên sản phẩm: ")
so_luong = int(input("Nhập số lượng: "))
don_gia = float(input("Nhập đơn giá (VNĐ): "))

# 2. Tính toán các giá trị
tong_tien_hang = so_luong * don_gia
thue_vat = tong_tien_hang * 0.08
tong_thanh_toan = tong_tien_hang + thue_vat

# 3. In hóa đơn bán hàng với định dạng phân cách hàng nghìn (:, .0f)
print("\n" + "=" * 40)
print(f"{'HÓA ĐƠN BÁN HÀNG':^40}")
print("=" * 40)
print(f"Tên sản phẩm    : {ten_san_pham}")
print(f"Số lượng        : {so_luong}")
print(f"Đơn giá         : {don_gia:,.0f} VNĐ")
print("-" * 40)
print(f"Tổng tiền hàng  : {tong_tien_hang:,.0f} VNĐ")
print(f"Thuế VAT (8%)   : {thue_vat:,.0f} VNĐ")
print("-" * 40)
print(f"Tổng thanh toán : {tong_thanh_toan:,.0f} VNĐ")
print("=" * 40)
