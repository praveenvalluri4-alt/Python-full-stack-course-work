"""
def count_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
arr = [1,2,3,4,5] 
print("sum:", count_sum(arr))
"""
"""
#counting the digits in array
def count_digits(arr):
    count = 0
    for num in arr:
        count += 1
    return count
arr=[1,2,3,4,5]
print("digits count:", count_digits(arr))

"""
"""
def find_max(arr):
    max_value = arr[0]   # assume first element is max
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

numbers = [10, 25, 5, 40, 15]
print("Maximum value is:", find_max(numbers))
"""
expenses = []
def export_expenses(expenses):
    with open("expenses.txt" , "w") as file:
        for expense in expenses:
           file.write(expense["name"] + " " + str(expense["amount"]) + "\n")

def main():
    while True:
        print("\n1.ADD EXPENSES")
        print("2.VIEW EXPENSES")
        print("3.EXPORT TO FILE")
        print("4.EXIT")

        choice = input("enter choice:")

        if choice =="1":
            name = input("enter expense name:")
            amount = int(input("enter amount:"))

            expenses.append({"name":name,"amount":amount})
        
        elif choice == "2":
            for expense in expenses:
                print(expense["name"]," ",expense["amount"])


        elif choice == "3":
            export_expenses(expenses)


        elif choice == "4":
            print("exit the programm")
            break

        else:
            print("invalid choice, try again")

main()