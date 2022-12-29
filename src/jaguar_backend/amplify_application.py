from operating_system_interface import OperatingSystemInterface
from typing import List, Any, Union, Dict, Optional, Tuple
from _types import *
from _base import WorkflowRepresentation


class AmplifyApplication:
    """AmplifyApplication is a class"""

    def __init__(self) -> None:
        self.categories = ["notifications", 'api', 'auth', 'custom', 'storage',
                           'analytics', 'function', 'geo', 'hosting', 'interactions', 'predictions', 'xr']

        self.initial_args = len(["workflow.py", "aws", "function_signature"])
        self.workflow_ui = WorkflowRepresentation()
        self.osi = OperatingSystemInterface()

    def update_amplify_application(self, *categoryIDs: Tuple[str]) -> None:
        '''modify_amplify_application will;
        1. remove each category selected through the category ids
        2. add each category selected through the category ids
        3. check the amplify status between each addition
        4. push the changes to the amplify application
        5. pull the changes to the local backend

        ---
        Params:
        - categoryIDs : list or strings, this will be turned into a list of integers and used to access the desired
        category from the categories list

        ---
        Returns: 
        - None
        '''
        categoryIDs = categoryIDs[0]
        os.system(
            "start https://docs.google.com/spreadsheets/d/1bVORUU7gE_fYZW1FjpHu0Y-peRuyXPBO-o7_NsMurnI/edit#gid=1067183673")
        os.system(
            r'start excel "{}\onedrive\documents\amplify-55X8f_accessKeys"'.format(self.osi.gcu()))
        for categoryID in categoryIDs:
            category = self.categories[int(categoryID)]
            self.workflow_ui.pp(
                f"removing the selected categories form amplify 🗑️:{category}")
            os.system(f"amplify remove {category}")
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            os.system(f"amplify add {category}")
            self.workflow_ui.pp("checking the amplify status 🔍")
            os.system("amplify status")
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            self.workflow_ui.pp(f"pushing to amplify ✏️")
            os.system("amplify push")
            self.workflow_ui.pp(f"pull locally ⤵️")
            os.system("amplify pull")

    def modify_amplify_application(self, *categoryIDs: Tuple[str]) -> None:
        '''modify_amplify_application will;
        1. add each category selected through the category ids
        2. check the amplify status between each addition
        3. push the changes to the amplify application
        4. pull the changes to the local backend

        ---
        Params:
        - categoryIDs : list or strings, this will be turned into a list of integers and used to access the desired
        category from the categories list

        ---
        Returns: 
        - None
        '''
        categoryIDs = categoryIDs[0]
        os.system(
            "start https://docs.google.com/spreadsheets/d/1bVORUU7gE_fYZW1FjpHu0Y-peRuyXPBO-o7_NsMurnI/edit#gid=1067183673")
        os.system(
            r'start excel "{}\onedrive\documents\amplify-55X8f_accessKeys"'.format(self.osi.gcu()))
        for categoryID in categoryIDs:
            category = self.categories[int(categoryID)]
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            os.system(f"amplify add {category}")
            self.workflow_ui.pp("checking the amplify status 🔍")
            os.system("amplify status")
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            self.workflow_ui.pp(f"pushing to amplify ✏️")
            os.system("amplify push")
            self.workflow_ui.pp(f"pull locally ⤵️")
            os.system("amplify pull")

    def initialize_amplify_application(self, *categoryIDs: Tuple[str]) -> None:
        categoryIDs = categoryIDs[0]
        os.system(
            "start https://docs.google.com/spreadsheets/d/1bVORUU7gE_fYZW1FjpHu0Y-peRuyXPBO-o7_NsMurnI/edit#gid=1067183673")
        os.system(
            r'start excel "{}\onedrive\documents\amplify-55X8f_accessKeys"'.format(self.osi.gcu()))
        self.workflow_ui.pp("initialize a new amplify application 👶")
        os.system("amplify init")
        for categoryID in categoryIDs:
            category = self.categories[int(categoryID)]
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            os.system(f"amplify add {category}")
            self.workflow_ui.pp("checking the amplify status 🔍")
            os.system("amplify status")
            self.workflow_ui.pp(
                f"adding a new category to amplify ⭐ category:{category}")
            self.workflow_ui.pp(f"pushing to amplify ✏️")
            os.system("amplify push")
            self.workflow_ui.pp(f"pull locally ⤵️")
            os.system("amplify pull")

    def push_to_amplify(self, *args) -> None:
        '''
        In order to publish to amplify make sure that you have initialised the correct application
        and that the self.repository is bering configure

        According to the documentation after adding the hosting category you can commit by running amplify push
        ---
        ```cmd
        amplify push
        ```
        '''
        target_directory = os.getcwd()
        self.workflow_ui.pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        self.workflow_ui.pp("running tests using npm 🧪")
        os.system("npm test")
        self.workflow_ui.pp("formatting code using prettier ✨")
        os.system("prettier -w .")
        result = input(
            "are you satisfied with the result of the tests? (y/n):")
        if result == "y":
            self.workflow_ui.pp(
                "the tests have passed so we can push to github ✅")
            os.system("git pull")
            os.system("git add . ")
            os.system('git commit -m "make it better"')
            os.system("git push ")
            self.workflow_ui.pp("publishing the application to amplify ✅")
            os.system("amplify publish")

        self.workflow_ui.pp("workflow completed successfully ✅")
