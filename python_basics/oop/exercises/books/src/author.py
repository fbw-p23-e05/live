class Author:
    
    def __init__(self, name, email, gender):
        self._name = name
        self.__email = email
        self._gender = gender


    def get_name(self):
        return self._name
    

    def get_email(self):
        return self.__email
    

    def set_email(self, mail):
        self.__email = mail


    def get_gender(self):
        return self._gender
    

    def __str__(self):
        return f'Author[name={self._name},email={self.__email},gender={self._gender}]'
