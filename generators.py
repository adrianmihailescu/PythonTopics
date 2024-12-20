def generate_numbers(limit):
    num = 0
    while num < limit:
        yield num
        num += 1

for number in generate_numbers(5):
    print(number)
