# Store the number to guess
our_fav_number = 15

#take_user_input
user_guess = input ('Enter your name :')
type_of_user_guess = type(user_guess) #string

print(type(user_guess))

user_guess = int(user_guess)

print(type(user_guess))

if user_guess == our_fav_number:

    print ("Success, you guessed the number! Our favourite is: " + str(our_fav_number))

if user_guess < our_fav_number:

    print (" Your guess is too low! try a little higher" )

if user_guess > our_fav_number:

    print (" Your guess is too high! Try a little higher" )