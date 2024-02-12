
def num_check(question):


    error = "please enter a number that is more than zero\n"
    while True:
        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

keep_going = ""
while keep_going == "":
    width = num_check("Width: ")
    height = num_check("height: ")

    area = width * height
    perimeter = 2 * (width * height)

    # format to str
    perimeter = str(perimeter)
    area = str(area)


    print()
    print("Perimeter: " + perimeter)
    print()
    print("Area: " + perimeter + "sqr units")

    keep_going = input("Press enter to continue and key to quit")
    print()
print("Thank u for using")