default_app_config ='studentinfo.apps.StudentinfoConfig'
import configparser

class ConfigReader:
    config = configparser.RawConfigParser()
    config.read('properties/school_config_file.properties')
    @classmethod
    def category_reader(cls):
        return cls.property_reader('categories')
    @classmethod
    def standard_reader(cls):
        return cls.property_reader('standard')
    @classmethod
    def division_reader(cls):
        return cls.property_reader('divison')
    @classmethod
    def gender_reader(cls):
        return cls.property_reader('gender')

    @classmethod
    def property_reader(cls, property):
        prop_tuple=()
        opt_available=cls.config.get('CategoriesSection',property)
        options=[x.strip() for x in opt_available.split(',')]
        for opt in options:
            temp_opt=(opt,opt)
            prop_tuple=(*prop_tuple, temp_opt)
        return prop_tuple



