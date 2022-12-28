
import unittest
from file import File

print("Testing:" + File.__doc__)
        

class Test_File(unittest.TestCase):        
    """"""
        
    def setUp(self):
        self.test_client = File(
            filename
        )
        
    def test_io___init__(self):
        """
        test the __init__ method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.__init__(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.__init__(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.__init__(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_read(self):
        """
        test the read method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - str
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.read(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.read(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.read(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_append(self):
        """
        test the append method which accepts the following arguments:
        
        ---
        Parameters:
        content : str

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.append(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.append(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.append(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_write(self):
        """
        test the write method which accepts the following arguments:
        
        ---
        Parameters:
        content : str

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.write(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.write(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.write(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_readlines(self):
        """
        test the readlines method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - 'list[str]'
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.readlines(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.readlines(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.readlines(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_get_json(self):
        """
        test the get_json method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - Any
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.get_json(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.get_json(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.get_json(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_write_json(self):
        """
        test the write_json method which accepts the following arguments:
        
        ---
        Parameters:
        content : Union[Dict[str,Any]

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.write_json(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.write_json(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.write_json(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_writeline(self):
        """
        test the writeline method which accepts the following arguments:
        
        ---
        Parameters:
        content : str

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.writeline(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.writeline(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.writeline(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_read_line_by_condition(self):
        """
        test the read_line_by_condition method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - 'list[str]'
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.read_line_by_condition(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.read_line_by_condition(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.read_line_by_condition(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_delete(self):
        """
        test the delete method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - None
        """
        # array of arguments which are expected by the method being tested
        correct_input = []
        # array containing the expected correct result of the function call
        correct_output = []

        # array of arguments containing an invalid type 
        invalid_types_input = []
        # array containing the result of the function call
        invalid_types_output = []

        # array of arguments containing an invalid value 
        invalid_values_input = []
        # array containing the result of the function call
        invalid_values_output = []

        test_result = self.test_client.delete(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.delete(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.delete(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        