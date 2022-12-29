
import unittest
from amplifyapplication import AmplifyApplication

print("Testing:" + AmplifyApplication.__doc__)
        

class Test_AmplifyApplication(unittest.TestCase):        
    """
    
    testing the side effects of the AmplifyApplication class
    
    Example of how those tests are run
    ---
    given a method ``append_row`` which takes the following arguments
    ```txt
    row: List[List], table_name: str
    ```
    you can cause the side effect (call the method being tested) and then check the endpoints
    ```python
    # array of arguments which are expected by the method which causes the side effect under test
    side_effect_input = [[121],base_table_name]
    # array containing the expected correct result of the side effect
    side_effect_output = [pd.DataFrame([*base_df_values, 121],columns=base_df_cols)]

    # cause a side effect to test
    test_result = self.test_client.append_row(*side_effect_input)

    # test that the side effect is expected
    test_result = self.test_client.get_table(base_table_name)
    self.assertTrue(test_result.equals(side_effect_output[0]))    
    ```
    """
    
        
    def setUp(self):
        self.test_client = AmplifyApplication()
    def test_side_effects___init__(self):
        """
        test the __init__ method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.__init__(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.__init__()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_update_amplify_application(self):
        """
        test the update_amplify_application method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - 
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.update_amplify_application(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.update_amplify_application()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_modify_amplify_application(self):
        """
        test the modify_amplify_application method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - 
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.modify_amplify_application(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.modify_amplify_application()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_initialize_amplify_application(self):
        """
        test the initialize_amplify_application method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - 
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.initialize_amplify_application(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.initialize_amplify_application()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_push_to_amplify(self):
        """
        test the push_to_amplify method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - 
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.push_to_amplify(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.push_to_amplify()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        