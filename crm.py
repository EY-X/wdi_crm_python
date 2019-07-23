from contact import Contact
import sys

class CRM:

  # As a user, upon starting the CRM, I am presented with a prompt to add, modify, delete, display all, search by attribute, and exit.
  def main_menu(self):
    try:
      while True:
        self.print_main_menu()
        user_selected = int(input())
        self.call_option(user_selected)
    except ValueError:
      sys.exit('Goodbye')
  
  

  def print_main_menu(self):
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')


  def __repr__(self): 
    return f'{self.print_main_menu()} '

  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      exit('Take Care!')
  
  
  # As a user, if I select add I am prompted to enter a 'first name', 'last name', 'email' and 'note'.
  def add_new_contact(self):
    first_name = input(('Enter First Name: '))
    last_name = input(('Enter Last Name: '))
    email = input(('Enter Email Address: '))
    note = input(('Enter a Note: '))
    Contact.create(first_name, last_name, email, note)


  # As a user, if I select modify I am prompted to enter an id for the contact to be modified.
  def modify_existing_contact(self):
    id_x = int(input('Enter your ID\n'))
    contact_attribute = input(('Which attribute do you want to edit?: '))
    new_value = input(('New value to be?: '))
    for contact in Contact.contacts_list: 
      if id_x == contact.next_id:
        if contact_attribute == 'first_name': 
          contact.update(contact_attribute, new_value)
    print(self.display_all_contacts())
  
  
  
  def delete_contact(self):
    id_x = int(input('Enter your ID'))
    for contact in Contact.contacts_list: 
      if id_x == contact.next_id:
        contact.remove(id_x)


  
  def display_all_contacts(self):
    print(Contact.all())

  def search_by_attribute(self):
    Contact.find_by()



# Contact('John', 'fruc', 'john@john.com', 'rock on')
# # print(Contact.contacts_list)

# a_crm_app = CRM()
# print(a_crm_app.modify_existing_contact() )
# # a_crm_app.main_menu()



crm1 = CRM()
print(crm1.main_menu())
# crm1.display_all_contacts()
Contact.create('John', 'fruc', 'john@john.com', 'rock on')
crm1.display_all_contacts()
crm1.delete_contact()
# crm1.display_all_contacts()
# crm1.modify_existing_contact() 


# crm1.display_all_contacts()

# crm1.add_new_contact()
