# your improved User class goes here

class Users:
    def __init__(self, name, email, dln):
        self.name = name
        self.email = email
        self.dln = dln


tony = Users('Anthony','abc@gmail.com','12345')
ana = Users('Viviana', 'vjc@gmail.com', '67890')
miah = Users('Miah', 'mac@gmail.com', '98765')

print(tony.dln)