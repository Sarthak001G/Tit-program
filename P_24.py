def calculate_bill(input_str):
    try:
        price, quantity = map(float, input_str.split())

        if quantity == 0:
            print("0 0 0")
            return

        total_amount = price * quantity

        if total_amount < 1000:
            tax_amount = total_amount * 0.10
        elif 1000 <= total_amount <= 9999:
            tax_amount = total_amount * 0.15
        else:
            tax_amount = total_amount * 0.20 + total_amount * 0.02

        bill_amount = total_amount + tax_amount

        print(f"{total_amount:.2f} {tax_amount:.2f} {bill_amount:.2f}")

    except ValueError:
        print("Invalid input. Please enter price and quantity as numbers separated by space.")