# Declare variables as the text the user inputs
# Information automatically saved as string type
# We are happy with all this information being a string so we don't need to change the data type
first_name = input('Enter first name\n=> ').capitalize()
middle_name = input('Enter middle name\n=> ').capitalize()
last_name = input('Enter last name\n=> ').capitalize()
address_first_line = input('Enter first line of address\n=> ').title()
postcode = input('Enter postcode\n=> ').upper()
NI_number = input('Enter your National Insurance number\n=> ').upper()
sparta_course = input("Enter the course you're applying to\n=> ").capitalize()
education = input('Enter most recent education qualification\n=> ').capitalize()
# save the age as an integer datatype instead of string
age = int(input('Enter age: '))

# Print out the variables using .capitalize() to capitalize the functions
# Use `f"{}"` to format the data neatly
print(f"name: {first_name} {middle_name} {last_name}")
# Use `.upper()` to make the postcode upper case
print(f"Address: {address_first_line}\n         {postcode}")
print(f"NI number: {NI_number}")
print(f"Course: {sparta_course}")
print(f"Education: {education}")
print(f"Age {age}")

# store data in dictionary
user_details = {
    "Name": first_name + ' ' + middle_name + ' ' + last_name,
    "Address": address_first_line + ' ' + postcode.upper(),
    "NI_number": NI_number,
    "Course": sparta_course,
    "Education": education,
    "Age": age,
    "Hobbies": ["surfing", "rugby", "Snowboarding"]
}

# print hobbies list in reverse
print(user_details["Hobbies"][::-1])