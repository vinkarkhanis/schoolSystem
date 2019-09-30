import configparser
# #from .models import Fees
# from django.apps import apps
# Fees=apps.get_model('studentinfo', 'Fees')

class Reader:
    @classmethod
    def read(cls, property, nature='non-numeric'):
        return ConfigReader.config_property_reader(property,nature)

class ConfigReader:
    config = configparser.RawConfigParser()
    config.read('properties/school_config_file.properties')

    @classmethod
    def config_property_reader(cls, property, nature):
        if nature=='non-numeric':
            return cls.property_reader(property)
        elif nature== 'numeric':
            return cls.numeric_property_reader(property)


    @classmethod
    def property_reader(cls, property):
        prop_tuple=()
        opt_available=cls.config.get('CategoriesSection',property)
        options=[x.strip() for x in opt_available.split(',')]
        for opt in options:
            temp_opt=(opt,opt)
            prop_tuple=(*prop_tuple, temp_opt)
        return prop_tuple

    @classmethod
    def numeric_property_reader(cls, property):
        prop_tuple = ()
        opt_available = cls.config.get('CategoriesSection',property)
        options = [x.strip() for x in opt_available.split(',')]
        for opt in options:
            temp_opt = (int(opt), int(opt))
            prop_tuple = (*prop_tuple, temp_opt)
        return prop_tuple

