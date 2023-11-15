from password_generator_classes import AlphaGenerator, AlphaNumericGenerator


class PasswordGeneratorFactory:
    @staticmethod
    def create_object(generator_type):
        """
        Generates a class depending on the parameter
        :param generator_type: "Alpha" or "AlphaNumeric"
        :return: object AlphaGenerator or AlphaNumericGenerator
        """
        # complete this method

        if generator_type == "Alpha":
            return AlphaGenerator()
        elif generator_type == "AlphaNumeric":
            return AlphaNumericGenerator()
            

