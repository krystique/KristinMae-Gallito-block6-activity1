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

while True

    

        def insert(list, n):
# Insert the element into the list
list.append(n)
# Sort the list
sorted_list = sorted(list)
return sorted_list
 
list = [1, 2, 4]
n = 3
print(insert(list, n))

    option = input('''\nWhat do you like to do next?

Insert [I]
Exit   [X]

I or X: ''')

        if option == 'i' or 'I':
            num = int(input("\nInsert a number: ")\
            
            
