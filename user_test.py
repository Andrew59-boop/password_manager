import unittest 
from user import User 

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Andrew","grey") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.login_username,"Andrew")
        self.assertEqual(self.new_user.password,"grey")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
    

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Candy","liap") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)   

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Candy","liap") 
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)  

    def test_validate_user(self):
        '''
        test to check if we can validate a user_loginusename and password
        '''

        self.new_user.save_user()
        test_user = User("Andrew","grey") 
        test_user.save_user()

        validated_user = User.validate_user("Andrew","grey")

        self.assertEqual(validated_user,test_user.password)               
    
     


if __name__ == '__main__':
    unittest.main()