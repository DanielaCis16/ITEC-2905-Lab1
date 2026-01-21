from datetime import datetime

name = input("What's your name? ")
letter_count = len(name)

# Validate birthday input
while True:
    birthday = input("What's your birthday? (MM/DD/YY) ")
    try:
        # Store the parsed datetime object
        bday_obj = datetime.strptime(birthday, "%m/%d/%y")
        break
    except ValueError:
        print("Please enter in format MM/DD/YY")

# Extract month as integer
month = bday_obj.month
current_month = datetime.now().month

# Birthday month check
if month == current_month:
    birth_month = "Happy Birthday Month!"
else:
    birth_month = "It's not your birthday month yet."

# Display messages
print("Hello " + name + "!")
print("Your name has " + str(letter_count) + " letters.")
print(birth_month)
