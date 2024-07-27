def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Create a generator object
gen = countdown(5)

# Iterate over the values yielded by the generator
for value in gen:
    print(value)
