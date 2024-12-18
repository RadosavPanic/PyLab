try:
    fp = open("non_existant_file.txt", "r")
except IOError as e:
    print(f"[Input/Output Error] {e}")
except Exception as e:
    print(f"Error occured. {e}")
else:
    print("File is opened successfully.")
    fp.close()
finally:
    print("File stream ended.")

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    print(f"Division is: {number1 / number2}")
except ZeroDivisionError as e:
    print(f"[ZeroDivisionError] occured: {e}")
except Exception as e:
    print(f"Error occured. {e}")

try:
    name = input("Enter your name: ")
    print(fullname)
except NameError as e:
    print(f"[NameError] {e}")
except Exception as e:
    print(f"Error occured. {e}")

completed = False
while not completed:
    try:
        a = int(input("Enter a positive integer: "))
        if a <= 0:
            raise ValueError("Value you entered is not positive. Try again.")
        print(f"Number you have entered is: {a}")
        completed = True
    except ValueError as e:
        print(f"[ValueError] {e}")
    except Exception as e:
        print(f"Error occured. {e}")