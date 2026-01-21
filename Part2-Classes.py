# Ask user how many classes they're taking
number_of_classes = int(input("How many classes are you taking this semester? "))

# Create a list to store the classes
semester = []

# Loop to collect class names
for i in range(number_of_classes):
    class_name = input(f"Enter the name of class {i+1}: ")
    semester.append(class_name)

print("\nHere are your classes this semester:")
for sem in semester:
    print(sem)
