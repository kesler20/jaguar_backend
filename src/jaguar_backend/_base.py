import os
from typing import List
import time

class WorkflowRepresentation:

    def pp(self, print_message: str):
        print(f"------------- {print_message}")
        time.sleep(1)
    
    def run_tests(self,args: List[str]):
        """runs the tests found within the repository
        
        Parameters
        ---
        args : List[str]
            the last parameter is whether you want to
            run manual tests or not
            ``["_dev.py","test","py","manual"]``
        
        Returns
        ---
        None
        """
        _type = args[2]
        if _type == "py":
            if len(args) > 3:
                self.pp("running manual tests in python 🐍 🧪 ⚙️")
                manual_test_folder = os.path.join(
                    __file__.split("jaguar_backend")[0],
                    "jaguar_backend",
                    "tests"
                )
                if len(args) > 4:
                    manual_test_folder = os.path.join(
                        __file__.split("protocol")[0],
                        "protocol",
                        args[4],
                        "tests"
                    )

                test_passed = []
                for test_file in os.listdir(manual_test_folder):
                    try:
                        print(os.path.join(manual_test_folder,test_file))
                        self.pp(f"running the following test {test_file}")
                        os.system(f"python {os.path.join(manual_test_folder,test_file)}")
                        self.pp(f"test passed at {test_file} ✅")
                        test_passed.append(test_file)
                        for test_file_passed in test_passed:
                            print("passed the following tests ✅",test_file_passed)
                    except:
                        self.pp("ERROR found in:",test_file)
                        self.pp(f"test passed at {test_file} ❌")
            else:
                self.pp("running automatic tests in python 🐍 🧪 🤖")
                os.system("python pytest tests")
        else:
            self.pp("running javascript tests using npm ☕ 🧪")
            os.system("npm tests")

    def describe(self, topic: str):
        if topic == "aws":
            print("=============== INIT ==============")
            print("to initialise a brand new application run 'aws init'")
            print(
                "this is preferred to do in it in the console as you will not have the amplify application")
            print("configured locally")
            print("make sure that you are in your root directory !!")
            print("make sure to document each of the amplify names and resources")
            print("=============== IMPORT ==============")
            print("to import an existing application you can use the 'amplify pull appid' suggested through the console")
            print("make sure that there are no amplify related files locally first")
            print("=================== ADD ===========================")
            print(
                "to update an amplify application use the 'aws edit' command and otherwise the 'aws update'")
            print("the former is used to add new categories to your amplify application")
            print(
                "the latter is used to remove existing categories and to replace them with new ones")