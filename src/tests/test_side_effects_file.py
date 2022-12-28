
import unittest
from file import File

print("Testing:" + File.__doc__)
        

class Test_File(unittest.TestCase):        
    """
    
    testing the side effects of the File class
    
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
        self.test_client = File(
            filename
        )
        
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
    
    def test_side_effects_read(self):
        """
        test the read method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - str
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.read(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.read()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_append(self):
        """
        test the append method which accepts the following arguments:
        
        ---
        Parameters:
        content : str

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.append(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.append()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_write(self):
        """
        test the write method which accepts the following arguments:
        
        ---
        Parameters:
        content : str

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.write(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.write()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_readlines(self):
        """
        test the readlines method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - 'list[str]'
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.readlines(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.readlines()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_get_json(self):
        """
        test the get_json method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - Any
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.get_json(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.get_json()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_write_json(self):
        """
        test the write_json method which accepts the following arguments:
        
        ---
        Parameters:
        content : Union[Dict[str,Any]

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.write_json(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.write_json()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_writeline(self):
        """
        test the writeline method which accepts the following arguments:
        
        ---
        Parameters:
        content : str

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.writeline(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.writeline()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_read_line_by_condition(self):
        """
        test the read_line_by_condition method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - 'list[str]'
        """
        # array of arguments which are expected by the method which causes the side effect under test
        side_effect_input = []
        # array containing the expected correct result of the method after the side effect
        side_effect_output = []

        # cause a side effect to test
        test_result = self.test_client.read_line_by_condition(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.read_line_by_condition()
        self.assertEqual(test_result,side_effect_output[0])
    
    def test_side_effects_delete(self):
        """
        test the delete method which accepts the following arguments:
        
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
        test_result = self.test_client.delete(*side_effect_input)

        # test that the side effect is expected
        test_result = self.test_client.delete()
        self.assertEqual(test_result,side_effect_output[0])
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        