greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name)

print(intrupution, formatted)

#Hand on exercise
school = "Code Academy"
address = "{} 123 Main St"
full_address = address.format(school)
print(full_address)

#upper and lower case
print(school.upper())
print(school.lower())
print(full_address.replace("Code Academy", "Code Academy, Inc."))