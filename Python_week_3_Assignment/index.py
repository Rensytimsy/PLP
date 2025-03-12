price = int(input("What's the item Price: "));
item_discount = int(input("What discount do want to impose?: "));
discount_percent =  float(item_discount / 100);


def calculate_discount(price, discount_percent):
    if not discount_percent:
        return price;
    
    discount = price * discount_percent;
    final_price = price - discount;
    return f"item final price after discount: {final_price}";

print(calculate_discount(price, discount_percent));
