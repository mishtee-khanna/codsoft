import random
import string

def generate_password(length_password):
    # The characters that are used to generate passwords
    lowercase_characters = string.ascii_lowercase
    uppercase_characters = string.ascii_uppercase
    digit_characters = string.digits
    special_characters = string.punctuation

    # Combining all the characters
    all_characters = lowercase_characters + uppercase_characters + digit_characters + special_characters

    #Generation of random password
    password = ''.join(random.choice(all_characters) for i in range(length_password))

    return password

while True:
    try:
        length_password = int(input("Enter your desired length of the password : "))
        if length_password < 8:
            print("The length of the password should be more than 8 characters!")
        else:
            break
    except ValueError:
        print("Invalid Input!")
        print("Kindly enter a number")
generated_password = generate_password(length_password)

#Displaying the password
print("Your generated password is :" , generated_password)

