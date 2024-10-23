
def calculate_total():
    total = subtotal + tax
    return total
def main():
    subtotal = 100
    tax = 15
    print(calculate_total())
    print(subtotal)


if __name__ == "__main__":
    main()
