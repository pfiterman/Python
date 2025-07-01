# 1 Correct
class Contact:
    """ A contact with a first name, a last name, and an email address. """

    def __init__(self, first_name, last_name, email_address):
       """ (Contact, str, str, str) -> NoneType

       Initialize this Contact with first name first_name, last name
       last_name, and email address email_address.
        """

       self.first_name = first_name
       self.last_name = last_name
       self.email_address = email_address
    
    def add_phone_number(self, telephone_num):
        """ (Contact, str) -> NoneType

        Add phone number telephone_num for this contact.
        """

        self.phone_number = telephone_num

    def __str__(self):
        """ (Contact) -> str

        Return a string representation of this contact.
        """

        return '{0} {1} <{2}>'.format(self.first_name,
                self.last_name, self.email_address)

paul1 = Contact('Paul', 'Gries', 'paul@example.com')
print(paul1)

# 2 Correct
# Variable jen refers to a contact object. Select the correct way to print jen's email address.
# print(jen.email_address)

# 3 Correct
# Another method has been added to class Contact
# khaled.add_phone_number("555-1111")

# 4 Incorrect
# str.replace("abc 123", "123", "246")
# "abc 123".replace("123", "246")

# 5 Correct
c = Contact("Rorik", "Henrikson", "rorik@example.com")
print(str(c))
# A string containing information about the object that rorik refers to. This string contains both its type and its memory address

# 6 Correct
# After adding __str__(self)
str(c)
# "Rorik Henrikson <rorik@example.com>"

# 7 Correct
class Email:
    """ An email with a list of recipients, a subject and a body. """

    def __init__(self, recipients, subject, body):
       """ (Email, list of Contact, str, str) -> NoneType

       Initialize this Email with recipients, subject and body.       """

       self.recipients = recipients
       self.subject = subject
       self.body = body
    
    def __str__(self):
        """ (Email) -> str

        Return a string representation of this email.
        """

        result = 'To: '
        for contact in self.recipients:
            result = result + '{0}, '.format(contact)

        result = result + '\nSubject: {0}'.format(self.subject)
        result = result + '\n{0}'.format(self.body)
        return result

# new_email = Email([Contact('Kathryn', 'Z.', 'kathryn@fakedomain.com')], 'Hello', 'Hi there!\n Bye for now.')

# student1 = Contact('Hugh', 'Z.', 'hugh@fakedomain.com')
# student2 = Contact('Kathryn', 'Z.', 'kathryn@fakedomain.com')
# student3 = Contact('Karin', 'Z.', 'karin@fakedomain.com')
# students = [student1, student2, student3]
# subject = 'LTP2: E4 is posted!'
# body = 'Hello,\nE4 is posted. Good luck!\n Paul and Jen'
# new_email = Email(students, subject, body)

# 8 Correct
message = Email([Contact("Paul", "Gries", "paul@example.com"), Contact("Jen", "Campbell", "jen@example.com")], "2nd MOOC", "Hi!\nI hope your 2nd MOOC is going well!\nBye :-)")
print(message)

# To: Paul Gries <paul@example.com>, Jen Campbell <jen@example.com>,
# Subject: 2nd MOOC
# Hi!
# I hope your 2nd MOOC is going well!
# Bye :-)

# 9 Correct
# check using dir(object) on python shell
# __lower__

# 10 Correct
class Author:
   def __init__(self, name):
       """ (______, str) -> NoneType """
       self.name = name

# Author