
total_num = int(input("Please input a positive, non-zero number:\n"))

num_set = []
for i in range(total_num):
	curr_input = int(input("Input a number:\n"))
	num_set.append(curr_input)

guess = int(input("Input a number to check if it is already contained within our set of numbers:\n"))
if guess in num_set:
	index = num_set.index(guess)
	print(f"{guess} is in our set of numbers at index {index}\n")
else:
	print(f"{guess} is not in our set of numbers\n")

