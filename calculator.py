def command():
        
    print("Select operation: ")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    while True:
        choice = input("Enter choice -> 1,2,3,4 or 0 to stop: ")
        if choice == '0':
            break



        if choice in ['1','2','3','4']:

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            if choice == '1':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print(f"{num1}/{num2} = Error. No division by zero.")
                else:
                    result = num1/num2
                    print(f"{num1} / {num2} =  {result}" )
        else:
            print("Invalid choice. ")
            
         




print("Starting very basic caluculator...")
print("This calculator only takes in 2 input numbers!")

command()
