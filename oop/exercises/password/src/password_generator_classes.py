from abc import ABC, abstractmethod
import random
import string


class PasswordGenerator(ABC):
    @abstractmethod
    def __init__(self, pool_str):
        """

        :param pool_str: a string containing characters to be used for the generation of the password
        """
        self.pool = list(pool_str)

    def generate_password(self, length):
        pwd = ""
        for i in range(length):
            pwd += random.choice(self.pool)
        return pwd


class AlphaGenerator(PasswordGenerator):
    def __init__(self):
        super().__init__(string.ascii_letters) # abcdefgh....


class AlphaNumericGenerator(PasswordGenerator):
    def __init__(self):
        super().__init__(string.ascii_letters + "0123456789") # abcdefgh....01234....



