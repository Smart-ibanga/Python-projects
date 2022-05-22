
def calculate():

    operator = input('''

Please select the  maths operation to calculate with:
+ for addition
- for subtraction
* for multipliation
/ for division

'''
)
  #Enter Numbers
    first = int(input("Enter first number: "))
    second= int(input("Enter second number: "))

        #Addition
    if operator == "+":
        print('{} + {} = '.format( first , second))
        print(first + second)

    elif operator == "-":
        #Subtraction
        print('{} - {} = '.format( first , second))
        print(first - second)

    elif operator == "*":
        #Multiplication
        print('{} * {} = '.format( first , second))
        print(first * second)

    elif operator == "/":
        #Division
        print('{} / {} = '.format( first , second))
        print(first / second)

    else:
        print("your operator is not valid")

def again():
    cal_again = input('''
Would you want to calculate again?
Pls type Y for YES or N for NO

 ''')

    if cal_again.upper() == 'Y':
       calculate()
    elif cal_again.upper() == 'N':
        print('Goodbye')
    else:
        again()

calculate()