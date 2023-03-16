user_details = {
    "name": "kevin",
    "age": 25,
    "skills": ["Python", "Ansible",
               "Ruby", "Perl"]
}

print(user_details)

print("The user name is", user_details["name"], "and age is", user_details["age"] )

print(f"The user name is {user_details['name']} and age is {user_details['age']}")

print(f"The user name is {user_details.get('name')} and age is {user_details.get('age')}")

print("==" * 20)

for i in user_details:
    print(i)