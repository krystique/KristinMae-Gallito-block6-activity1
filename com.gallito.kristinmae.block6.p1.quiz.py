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

    if order == 'a' or 'A':

        numbers.sort()
        result = ' '.join(str(item) for item in numbers)
        print(f"\nAscending: {result}")
        
        
    elif order == 'd' or 'D':

        numbers.sort(reverse = True)
        result = ' '.join(str(item) for item in numbers)
        print(f"\nDescending: {result}")
        
    else:
        print("\nTry again. Please just choose between A or D: ")
        continue
