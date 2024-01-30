while True:

    problem = input("enter your problem e.g 2 * 3: ").split()


    if len(problem)!= 3:
        print("Wrong format!")
        continue
    if problem[1]not in ["+" , "-" , "*" , "/"]:
        print("Wrong format!")
        continue

    first_number = float(problem[0])
    operator = problem[1]
    second_number = float(problem[2])


    if operator == "+":
        result = first_number + second_number
        print(result)

    elif operator == "-":
        result = first_number - second_number
        print(result)

    elif operator == "*":
        result = first_number * second_number
        print(result)

    elif operator == "/":
        result = first_number / second_number
        print(result)













