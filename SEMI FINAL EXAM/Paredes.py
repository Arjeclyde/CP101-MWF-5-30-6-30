record = {}
while True:
    print(record)
    choice = input("Choose an Option \n A. Add Data \n B. Delete Data \n C. End \n")
    if choice == 'A':
        key = input("Enter Key: ")
        value = input("Enter a Value: ")
        record[key] = value
        print("Data Added Successfully. ")
    elif choice == 'B':
        key = input ("Enter key: ")
        if key in record:
            del record[key]
            print("Data Deleted Successfully. ")
        else:
            print("Key not found")
    elif choice == 'C':
        print("Thank you and Have a nice day:) ")
        break
