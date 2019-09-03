import random
import string

class Credentials:
    '''
    class that generates instances of new credentials
    '''
    app_details = []
    
    def __init__(self,app,app_password):
        self.app = app
        self.app_password = app_password
    
    def save_app(self):
        '''
        function that stores our accounts
        '''
        Credentials.app_details.append(self)
    def delete_app(self):
        '''
        Function that remove app and password
        '''
        Credentials.app_details.remove(self)
    
    @classmethod
    def find_app(cls,app):
        '''
        Finding app by the name
        Args:
            app: app name to search for
        returns:
            app searched for
        '''
        for credentials in cls.app_details:
            if credentials.app == app:
                return app
    
    @classmethod
    def app_exist(cls,app):
        '''
        this it the method that checks if it exist
        Args:
            app name is checked if the app exist
        Returns:
            a boolean depends on the app that is checked for
        '''
        for credentials in cls.app_details:
            if credentials.app == app:
                return True
        return False

    @classmethod
    def gen_password(size = 8):
        '''
        Function to it generates random password with eight digits
        '''
        char = string.ascii_uppercase + string.ascii_lowercase
        gen_password = ''.join(random.choice(char) for i in range(size))
        return gen_password

    @classmethod
    def display_app(cls,app):
        '''
        Function that are displayed by the app
        '''    
        return cls: app_details()