record = {}
while True:
    print(record)
    choice = input("Choose an Option \n 1. Add Data \n 2. Delete Data \n 3. End \n")
    if choice == '1':
        key = input("Enter Key: ")
        value = input("Enter a Value: ")
        record[key] = value
        print("Data Added Successfully. ")
    elif choice == '2':
        key = input ("Enter key: ")
        if key in record:
            del record[key]
            print("Data Deleted Successfully. ")
        else:
            print("Key not found")
    elif choice == '3':
        print("Thank you and Have a nice day:) ")
        break
