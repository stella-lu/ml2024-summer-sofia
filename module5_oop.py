class NumberSet:
    def __init__(self):
        self.num_set = []

    def initialize_data(self, total_num):
        for i in range(total_num):
            curr_input = int(input("Input a number:\n"))
            self.num_set.append(curr_input)

    def search_number(self, guess):
        if guess in self.num_set:
            index = self.num_set.index(guess)
            return index
        else:
            return -1

total_num = int(input("Please input a positive, non-zero number:\n"))

number_set = NumberSet()
number_set.initialize_data(total_num)

guess = int(input("Input a number to check if it is already contained within our set of numbers:\n"))
result = number_set.search_number(guess)

if result != -1:
    print(f"{guess} is in our set of numbers at index {result}")
else:
    print(f"{guess} is not in our set of numbers")

