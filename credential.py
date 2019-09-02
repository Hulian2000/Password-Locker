class Credentials:
    '''
    class that generates instances of new credentials
    '''
    new_app = []
    def __init__(self,username,add_app,add_password):
        self.username = username
        self.add_app = add_app
        self.add_password = add_password

    def save_app(self):
        '''
        save method that adds stores our credentials
        '''
        Credentials.new_app.append(self)


    def delete_account(self):
        '''
        delete account method to remove user account
        '''
        Credentials.new_app.remove(self)
        
    @classmethod
    def find_by_appname(cls,app_name):
        '''
        finding app by their app name
        Args:
            App: app to search for 
        returns:
            app searched for
        '''
        for credential in cls.new_app:
            if credential.add_app == add_app:
                return credential

    @classmethod
    def app_exist(cls,app_name):
        '''
        method that checksif app exist by name
        Args:
        app_name to check if app exists
        returns a boolean depending on name existance
        '''
        for credentials in cls.new_app:
            if credentials.add_app == add_app:
                return True
        return False

    @classmethod
    def display_app(cls):
        '''
        Function that displays app 
        '''
        return cls.new_app()