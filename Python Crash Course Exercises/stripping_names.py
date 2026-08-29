"""
2-7. Stripping Names: Use a variable to represent a person’s name, and
include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().


"""


person_name = " John Smith "



print("Unmodified:")
print(person_name)

print("\nUsing lstrip():")
print(person_name.lstrip())

print("\nUsing rstrip():")
print(person_name.rstrip())

print("\nUsing strip():")
print(person_name.strip())

print({person_name.rstrip()})
print(f"\n{person_name.lstrip()}")
print(f"\t{person_name.strip()}")
