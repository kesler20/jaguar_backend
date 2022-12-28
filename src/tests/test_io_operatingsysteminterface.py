
import unittest
from operatingsysteminterface import OperatingSystemInterface

print("Testing:" + OperatingSystemInterface.__doc__)
        

class Test_OperatingSystemInterface(unittest.TestCase):        
    """"""
        
    def setUp(self):
        self.test_client = OperatingSystemInterface()
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
    
    def test_io___enter__(self):
        """
        test the __enter__ method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - os
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

        test_result = self.test_client.__enter__(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.__enter__(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.__enter__(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io___exit__(self):
        """
        test the __exit__ method which accepts the following arguments:
        
        ---
        Parameters:
        

        ---
        Returns:
        - os
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

        test_result = self.test_client.__exit__(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.__exit__(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.__exit__(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_gcu(self):
        """
        test the gcu method which accepts the following arguments:
        
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

        test_result = self.test_client.gcu(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.gcu(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.gcu(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_copy_file_from_folder(self):
        """
        test the copy_file_from_folder method which accepts the following arguments:
        
        ---
        Parameters:
        file : str, source_folder : str="jaguar"

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

        test_result = self.test_client.copy_file_from_folder(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.copy_file_from_folder(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.copy_file_from_folder(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_move_folder_resources(self):
        """
        test the move_folder_resources method which accepts the following arguments:
        
        ---
        Parameters:
        destination_path : str

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

        test_result = self.test_client.move_folder_resources(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.move_folder_resources(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.move_folder_resources(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def test_io_read_word_in_directory(self):
        """
        test the read_word_in_directory method which accepts the following arguments:
        
        ---
        Parameters:
        word : str

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

        test_result = self.test_client.read_word_in_directory(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,correct_output[0])

        test_result = self.test_client.read_word_in_directory(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_types_output[0]) 

        test_result = self.test_client.read_word_in_directory(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result,invalid_values_output[0]) 
    
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
        