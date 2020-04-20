class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty contact list

    def __init__(self,login_username,password,):

      # docstring removed for simplicity

        self.login_username = login_username
        self.password= password

    def save_user(self):

         '''
         save_user method saves user objects into user_list
         '''

        User.user_list.append(self)  

    @classmethod
    def validate_user(cls,login_username,password):
        '''
        Method that takes in login_username and password

        Args:
            login_username : name
            password :password
        '''

        for user in cls.user_list:
            if user.login_username == login_username and user.password ==password:
                return password   

          
