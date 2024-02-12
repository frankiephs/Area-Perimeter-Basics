
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

for items in range(0,2):
    width = num_check("Width: ")
    print(width)

print()

for items in range(0,2):
    height = num_check("height: ")
    print(height)