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
