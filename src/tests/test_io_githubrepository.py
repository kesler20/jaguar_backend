
import unittest
from github_repository import GithubRepository

print("Testing:" + GithubRepository.__doc__)


class Test_GithubRepository(unittest.TestCase):
    """"""

    def setUp(self):
        self.test_client = GithubRepository()

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
        self.assertEqual(test_result, correct_output[0])

        test_result = self.test_client.__init__(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_types_output[0])

        test_result = self.test_client.__init__(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_values_output[0])

    def test_io_test_and_push_to_github(self):
        """
        test the test_and_push_to_github method which accepts the following arguments:

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

        test_result = self.test_client.test_and_push_to_github(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, correct_output[0])

        test_result = self.test_client.test_and_push_to_github(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_types_output[0])

        test_result = self.test_client.test_and_push_to_github(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_values_output[0])

    def test_io_push_to_github(self):
        """
        test the push_to_github method which accepts the following arguments:

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

        test_result = self.test_client.push_to_github(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, correct_output[0])

        test_result = self.test_client.push_to_github(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_types_output[0])

        test_result = self.test_client.push_to_github(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_values_output[0])

    def test_io_push_new_repo_to_github(self):
        """
        test the push_new_repo_to_github method which accepts the following arguments:

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

        test_result = self.test_client.push_new_repo_to_github(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, correct_output[0])

        test_result = self.test_client.push_new_repo_to_github(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_types_output[0])

        test_result = self.test_client.push_new_repo_to_github(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_values_output[0])

    def test_io_push_new_branch_to_github(self):
        """
        test the push_new_branch_to_github method which accepts the following arguments:

        ---
        Parameters:


        ---
        Returns:
        - 
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

        test_result = self.test_client.push_new_branch_to_github(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, correct_output[0])

        test_result = self.test_client.push_new_branch_to_github(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_types_output[0])

        test_result = self.test_client.push_new_branch_to_github(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_values_output[0])

    def test_io_style_commit_message(self):
        """
        test the style_commit_message method which accepts the following arguments:

        ---
        Parameters:
        commit_message : str

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

        test_result = self.test_client.style_commit_message(*correct_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, correct_output[0])

        test_result = self.test_client.style_commit_message(*invalid_types_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_types_output[0])

        test_result = self.test_client.style_commit_message(*invalid_values_input)
        # assert that the value of the test is correct
        self.assertEqual(test_result, invalid_values_output[0])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
