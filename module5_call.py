from module5_mod import NumberSet

def main():
    total_num = int(input("Please input a positive, non-zero number:\n"))

    number_set = NumberSet()
    number_set.initialize_data(total_num)

    guess = int(input("Input a number to check if it is already contained within our set of numbers:\n"))
    result = number_set.search_number(guess)

    if result != -1:
        print(f"{guess} is in our set of numbers at index {result}")
    else:
        print(f"{guess} is not in our set of numbers")

if __name__ == "__main__":
    main()
