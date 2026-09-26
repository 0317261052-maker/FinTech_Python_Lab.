# hw2_roi.py

def main():
    initial = float(input("Nhập vốn ban đầu: "))
    final = float(input("Nhập giá trị bán ra: "))

    net_profit = final - initial
    roi = (net_profit / initial) * 100

    print(f"Lợi nhuận ròng: {net_profit:,.0f} VNĐ")
    print(f"Tỷ lệ ROI: {roi:.2f}%")

if __name__ == "__main__":
    main()
