import configparser
import os

config_directory = "../configurations/"
relative_configfile_name = config_directory + "config.ini"

path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, relative_configfile_name)
config = configparser.ConfigParser()
config.read(path_config_file)

class ReadConfig:


    @staticmethod
    def getURL():
        url = config.get('common', 'baseURL')
        return url

    @staticmethod
    def getLoginUsername():
        login_username = config.get('common', 'login_username')
        return login_username

    @staticmethod
    def getLoginPassword():
        login_password = config.get('common', 'login_password')
        return login_password

    @staticmethod
    def getFirstName():
        first_name = config.get('common', 'first_name')
        return first_name

    @staticmethod
    def getLastName():
        last_name = config.get('common', 'last_name')
        return last_name