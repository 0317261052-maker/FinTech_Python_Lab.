# hw1_tax_calculator.py

income = float(input("Nhập tổng thu nhập chịu thuế (VNĐ): "))

if income <= 5_000_000:
    tax = income * 0.05

elif income <= 10_000_000:
    tax = 5_000_000 * 0.05 + (income - 5_000_000) * 0.10

elif income <= 18_000_000:
    tax = (5_000_000 * 0.05
           + 5_000_000 * 0.10
           + (income - 10_000_000) * 0.15)

else:
    tax = (5_000_000 * 0.05
           + 5_000_000 * 0.10
           + 8_000_000 * 0.15
           + (income - 18_000_000) * 0.20)

print(f"Thuế TNCN phải nộp: {tax:,.0f} VNĐ")
