# Global Variable
data = []

# ---------------- Functions ----------------

def input_data():
    global data

    n = int(input("How many numbers: "))

    data = []

    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        data.append(num)

    print("Data Stored Successfully!")


def display_summary():
    """Display Summary"""

    if len(data) == 0:
        print("No Data Found")
        return

    print("\n----- DATA SUMMARY -----")
    print("Total Elements :", len(data))
    print("Minimum :", min(data))
    print("Maximum :", max(data))
    print("Sum :", sum(data))
    print("Average :", sum(data)/len(data))


def factorial(n):
    """Factorial using Recursion"""

    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)


def filter_data():
    """Lambda Function"""

    value = int(input("Enter Threshold: "))

    result = list(filter(lambda x: x > value, data))

    print("Filtered Data :", result)


def sort_data():
    """Sorting"""

    choice = input("1. Ascending\n2. Descending\nEnter Choice: ")

    if choice == "1":
        print(sorted(data))

    elif choice == "2":
        print(sorted(data, reverse=True))

    else:
        print("Invalid Choice")


def statistics():
    """Return Multiple Values"""

    return min(data), max(data), sum(data)/len(data)


def dataset_info(**kwargs):
    """kwargs Example"""

    for key, value in kwargs.items():
        print(key, ":", value)


def average(*args):
    """args Example"""

    return sum(args)/len(args)

# ---------------- Main Menu ----------------

while True:

    print("\n===== DATA ANALYZER =====")
    print("1. Input Data")
    print("2. Display Summary")
    print("3. Factorial")
    print("4. Filter Data")
    print("5. Sort Data")
    print("6. Statistics")
    print("7. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        input_data()

    elif choice == "2":
        print(display_summary.__doc__)
        display_summary()

    elif choice == "3":
        num = int(input("Enter Number: "))
        print("Factorial =", factorial(num))

    elif choice == "4":
        filter_data()

    elif choice == "5":
        sort_data()

    elif choice == "6":

        if len(data) == 0:
            print("No Data")
            continue

        mn, mx, avg = statistics()

        print("Minimum :", mn)
        print("Maximum :", mx)
        print("Average :", avg)

        print("\nkwargs Example")
        dataset_info(Total=len(data), Sum=sum(data), Average=avg)

        print("\nargs Example")
        print("Average =", average(*data))

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")