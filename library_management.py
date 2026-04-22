books = {}
members = {}
issued = {}

while True:
    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. View Books")
    print("4. Add Member")
    print("5. View Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Fine Calculation")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bid = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        books[bid] = name
        print("Book Added")

    elif choice == "2":
        bid = input("Enter Book ID to remove: ")
        if bid in books:
            del books[bid]
            print("Book Removed")
        else:
            print("Book not found")

    elif choice == "3":
        print("Books:", books)

    elif choice == "4":
        mid = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        members[mid] = name
        print("Member Added")

    elif choice == "5":
        print("Members:", members)

    elif choice == "6":
        bid = input("Enter Book ID to issue: ")
        mid = input("Enter Member ID: ")
        if bid in books and mid in members:
            issued[bid] = mid
            del books[bid]
            print("Book Issued")
        else:
            print("Invalid Book ID or Member ID")

    elif choice == "7":
        bid = input("Enter Book ID to return: ")
        name = input("Enter Book Name: ")
        books[bid] = name
        if bid in issued:
            del issued[bid]
        print("Book Returned")

    elif choice == "8":
        days = int(input("Enter number of days: "))
        if days > 5:
            fine = (days - 5) * 10
            print("Fine:", fine)
        else:
            print("No Fine")

    elif choice == "9":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
