def calculate_emi(principal: float, annual_rate: float, months: int) -> tuple[float, float]:
    """
    Tính số tiền trả góp hàng tháng (EMI) và tổng tiền lãi phải trả trong toàn bộ chu kỳ.

    Parameters:
    ----------
    principal : float
        Số tiền vay gốc (P).
    annual_rate : float
        Lãi suất năm (tính theo %, ví dụ: 12 tức là 12%/năm).
    months : int
        Thời gian vay tính theo tháng (n).

    Returns:
    -------
    tuple[float, float]
        Một Tuple gồm 2 giá trị:
        - EMI (float): Số tiền phải trả hàng tháng.
        - total_interest (float): Tổng tiền lãi phải trả trong toàn bộ chu kỳ.
    """
    r = annual_rate / 12 / 100
    n = months
    P = principal

    if r == 0:
        emi = P / n
        total_interest = 0.0
    else:
        emi = P * (r * (1 + r)**n) / ((1 + r)**n - 1)
        total_payment = emi * n
        total_interest = total_payment - P

    return round(emi, 2), round(total_interest, 2)


# --- NHẬP DỮ LIỆU TỪ BÀN PHÍM ---
if __name__ == "__main__":
    print("=== CHƯƠNG TRÌNH TÍNH LÃI TRẢ GÓP (EMI) ===")
    
    vay_goc = float(input("Nhập số tiền vay gốc (VNĐ): "))
    lai_suat_nam = float(input("Nhập lãi suất năm (%): "))
    thoi_gian_thang = int(input("Nhập thời gian vay (tháng): "))

    # Gọi hàm và nhận 2 giá trị trả về
    emi_thang, tong_lai = calculate_emi(vay_goc, lai_suat_nam, thoi_gian_thang)

    print("\n--- KẾT QUẢ ---")
    print(f"Số tiền trả góp hàng tháng (EMI): {emi_thang:,.2f} VNĐ")
    print(f"Tổng tiền lãi phải trả: {tong_lai:,.2f} VNĐ")
