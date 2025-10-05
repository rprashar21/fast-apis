class Profile:
    """ Basic profile of a user"""

    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address



    def get_user_profile(self):
        print(f"User name is : {self.name} ane email address is {self.email_address}")