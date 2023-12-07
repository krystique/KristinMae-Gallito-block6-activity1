print("<<< INSERTion SORT >>>\n")

numbers = []
for index in range(5):
    num = int(input("Enter a number: "))
    result = numbers.append(num)
    result = ' '.join(str(item) for item in numbers)

print(f"\n{result}")

while True:
    

    order = input('''\nHow do you like to sort your numbers?

Ascending  [A]
Descending [D]

A or D: ''')
