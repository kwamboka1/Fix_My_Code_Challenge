#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Iniatialization of the user class """

    def __init__(self):
        """ Taking email """
        self.__email = None

    @email.setter
    def email(self, value):
        """ Making sure the email is a string """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    @property
    def email(self):
        """ Method that returns an email """
        return self.__email
   
    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
