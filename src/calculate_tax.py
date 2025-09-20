def calculate_tax(price,tax_rate):
    result = (price * tax_rate / 100) + price
    return result


if __name__ == '__main__':

    print(calculate_tax(50,5))