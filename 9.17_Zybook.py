contact_data = input().split()
search_name = input()

contacts = {}

for item in contact_data:
    name, phone_number = item.split(',')
    contacts[name] = phone_number

print(contacts[search_name])
