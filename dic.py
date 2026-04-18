# 1. Create an empty dictionary
my_dict = {}

# 2. Prompt for 5 people
print("Enter the name and age for 5 people:")
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    age = int(input(f"Enter age for {name}: "))
    
    # Store in dictionary: name is the Key, age is the Value
    my_dict[name] = age

# 3. Print the dictionary
print(f"\nDictionary Contents: {my_dict}")

# 4. Analysis
# Get the number of people
num_people = len(my_dict)

# Get all ages as a list to perform math
ages = list(my_dict.values())
total_age = sum(ages)
average_age = total_age / num_people

# Find oldest and youngest
# We use the 'key' argument to tell min/max to look at the values (ages)
oldest_name = max(my_dict, key=my_dict.get)
youngest_name = min(my_dict, key=my_dict.get)

print("-" * 30)
print(f"Total people: {num_people}")
print(f"Sum of all ages: {total_age}")
print(f"Average age: {average_age:.2f}")
print(f"Oldest person: {oldest_name} ({my_dict[oldest_name]})")
print(f"Youngest person: {youngest_name} ({my_dict[youngest_name]})")