class Contact:

  contacts_list = []
  next_id = 1

  def __init__(self, first_name, last_name, email, note):
    self.id = Contact.next_id
    Contact.next_id += 1
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.note = note


  def __str__(self):
    return f'''
    ID: {self.first_name} {self.last_name}, 
    E-Mail: {self.email}, 
    Notes: {self.note}
    '''
  def __repr__(self): 
    return f'{self.first_name} {self.last_name}: {self.email} - {self.note}'
    # """This method should initialize the contact's attributes"""


  @classmethod
  def create(cls, first_name, last_name, email, note):
    new_contact = Contact(first_name, last_name, email, note)
    cls.contacts_list.append(new_contact)
    return new_contact

    # """This method should call the initializer,
    # store the newly created contact, and then return it
    # """

  @classmethod
  def all(cls):
    return Contact.contacts_list
    """This method should return all of the existing contacts"""

  @classmethod
  def find(cls, user_id):
    for contact in Contact.contacts_list:
      if user_id == contact.id:
        return f'{contact.first_name} {contact.last_name} {contact.email} {contact.note}'
      else:
        return "Account doesn't exist"
    

  def update(self, contact_attribute, new_value):

    if contact_attribute == "first_name":
      self.first_name = new_value
    elif contact_attribute == "last_name":
      self.last_name = new_value
    elif contact_attribute == "email":
      self.email = new_value
    elif contact_attribute == "note":
      self.note = new_value
    else:
      print('Error')
    return Contact.contacts_list
    # """ This method should allow you to specify
    # 1. which of the contact's attributes you want to update
    # 2. the new value for that attribute
    # and then make the appropriate change to the contact
    # """




  @classmethod
  def find_by(cls, attribute_search):
    for contact in Contact.contacts_list:
      if attribute_search == contact.first_name:
        return f'{contact.first_name}'
      elif attribute_search == contact.last_name:
        return f'{contact.last_name}'
      elif attribute_search == contact.email:
        return f'{contact.email}'
      elif attribute_search == contact.note:
        return f'{contact.note}'
      else:
        return 'Information not available'

    
    # """This method should work similarly to the find method above
    # but it should allow you to search for a contact using attributes other than id
    # by specifying both the name of the attribute and the value
    # eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    # """


  @classmethod
  def delete_all(cls):
    Contact.contacts_list.clear()
    # """This method should delete all of the contacts"""


  def full_name(self):
    print(f'Name: {self.first_name} {self.last_name}')
    # """Returns the full (first and last) name of the contact"""


  def delete(self):
    Contact.contacts_list.remove(self)
    print('Item gone!')

  # Feel free to add other methods here, if you need them.contact = Contact('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')





# Creating an instance for class: Contact and testing it
# contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# print(contact1)
# contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')
# contact3 = Contact.create('wefgfsdfit', 'sdgdsot', 'bitbot@bitmakerlabs.com', 'beep boop')
# print(contact2)
# contact3 = Contact.create('Eden', 'Yosi', 'Eden@yos.com', 'ship it')
# print(contact3)
# print(len(Contact.contacts_list))

# print(Contact.all()) 
# print(contact1.id)
# print(contact2.id)
# print(contact3.id)

# CHECKING IF FIND METHOD WORKS!
# print(Contact.find())
 
# print(Contact.all()) 

# CHECKING IF UPDATE METHOD WORKS
# print(contact1.update('first_name','John'))
# contact2.update('last_name', 'Benaim') 


# CHECKING IF DELETE ALL METHODS


# contact1.full_name()

# print(Contact.all()) 

# contact1.delete()

# print(Contact.all()) 























