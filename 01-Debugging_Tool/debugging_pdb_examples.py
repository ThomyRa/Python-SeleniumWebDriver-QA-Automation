"""
Official doc = https://docs.python.org/3/library/pdb.html
c = continue
n = next
l = show current line
s = step
h = help
pp = pretty print
"""

import pdb


# Example 1
# print("I am the 1st line")
# fname = "Thomas"
# lname = "Ramirez"
#
# pdb.set_trace()
#
#
# print("I am the 2nd line")
# print("I am the 3rd line")
# print(f"first name is '{fname}' and last name is '{lname}'")

# Example 2
def get_user_name(name):
    user_names = {
        "alice": "ak",
        "joe": "joe99",
        "mary": "marryrocks2020"
    }
    print(f'The user "{user_names[name]}" is logged in.')
    # pdb.set_trace()

    return user_names[name]


user_1 = get_user_name("alice")
print("User 1: " + user_1)
pdb.set_trace()


user_2 = get_user_name("joe")
print("User 2: " + user_2)
