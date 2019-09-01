class User:
    '''
    class that generates new instaces of users
    '''
    user_details = []

    def __init__(self,first_name,second_name,password):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password


    # saving the user 
    def save_user(self):
        '''
        save method that adds stores our user
        '''
        User.user_details.append(self)


    # deleting the user account
    def delete_account(self):
        '''
        delete account method to remove user account
        '''
        User.user_details.remove(self)

    # finding user by firstname
    @classmethod
    def find_by_fname(cls,first_name):
        '''
        finding user by their first name
        Args:
            user: user to search for 
        returns:
            user searched for
        '''
        for user in cls.user_details:
            if user.first_name == first_name:
                return user

    # confirm user exist
    @classmethod
    def user_exist(cls,first_name):
        '''
        method that checksif user exist by name
        Args:
        first_name to check if name exists
        returns a boolean depending on name existance
        '''
        for user in cls.user_details:
            if user.first_name == first_name:
                return True
        return False
    # display user
    @classmethod
    def display_user(cls):
        '''
        Function that displays users 
        '''
        return cls.user_details()