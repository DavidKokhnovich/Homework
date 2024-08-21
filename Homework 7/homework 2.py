import random
import string
def generate_contacts(n):
    contacts = []
    for i in range(n):
        name = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 7)))
        phone = ''.join(random.choices(string.digits, k=12))
        contacts.append({'имя': name, 'номер телефона': phone})
    return contacts

def find_contact(contacts, search_key):
    found_contacts = []
    for contact in contacts:
        if search_key in contact['имя'] or search_key in contact['номер телефона']:
            found_contacts.append(contact)
    return found_contacts

contacts_list = generate_contacts(3)
print(contacts_list)

search_key = ('jkljj')
found_contacts = find_contact(contacts_list, search_key)
print(found_contacts)
