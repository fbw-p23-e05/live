# Instance method

class SoftwareBlueprint:

    version = 'v1.0'

    def __init__(self, user):
        
        self.user = user
        self.features = []
        self._secret_property = 'Confidential'
        
    
    def add_feature(self, feature):
        self.features.append(feature)


    def display_feature(self):
        return self.features
    
    @classmethod
    def current_version(cls):       
        return cls.version
    
    @staticmethod
    def future_glimpse(num, year):
        return 'Embrace the innovations of tomorrow.'
    

    @property
    def real_secret_property(self):
        return self._secret_property
    
    @real_secret_property.setter
    def real_secret_property(self, value):
        self._secret_property = value
    


# trial_software = SoftwareBlueprint('Isabella')

# trial_software.add_feature('UI Enhancement')
# trial_software.add_feature('Smooth Scrollbar')

# print(trial_software.display_feature())
# result = SoftwareBlueprint('Bob')
# result.add_feature('More feature')
# print(result.display_feature())



# Class method


class SoftwareSymphony:

    version = 'v1.0'

    @classmethod
    def current_version(cls):  
        cls.version = 'v2.1.0'    
        return cls.version
    

symphony_1 = SoftwareSymphony()

# print(SoftwareSymphony.current_version())
# print(symphony_1.current_version())


# Static method


class TechVisions:

    @staticmethod
    def future_glimpse(num, year):
        return 'Embrace the innovations of tomorrow.'
    

tech_1 = TechVisions()

# print(tech_1.future_glimpse(50, 2023))
# print(TechVisions.future_glimpse(100, 2024))



# Getter and Setter


class SoftwareProperties:

    def __init__(self):
        self._secret_property = 'Confidential'


    # def get_secret_property(self):
    #     return self._secret_property
    
    # def set_secret_property(self, value):
    #     self._secret_property = value

    @property
    def real_secret_property(self):
        return self._secret_property
    
    @real_secret_property.setter
    def real_secret_property(self, value):
        self._secret_property = value


software_1 = SoftwareProperties()

# print(software_1.real_secret_property)

# software_1.real_secret_property = 'PasSw0rd'

# print(software_1.real_secret_property)

# software_1.real_secret_property = 'NewPasSw0rd'

# print(software_1.real_secret_property)


# print(software_1.get_secret_property())
# print(software_1.get_secret_property())
# # print(SoftwareProperties().get_secret_property())

# software_1.set_secret_property('PasSw0rd')

# print(software_1.get_secret_property())



# Super method

class MobileTech:

    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display_type(self):
        print('This phone has IPS display.')



class Smartphone(MobileTech):

    def __init__(self, brand, ram, storage, model, camera):
        super().__init__(brand, ram, storage)
        self.model = model
        self.camera = camera
        super().display_type()

    
    def display_type(self):
        # super().display_type()
        print('This phone has Amoled display.')

    
phone_1 = Smartphone('Apple', 6, 128, 'iPhone X', '12MP')

print(phone_1.brand)
print(phone_1.model)
print(phone_1.display_type())



        

