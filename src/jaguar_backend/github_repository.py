
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass
from jaguar_backend._types import *
from jaguar_backend._base import WorkflowRepresentation
from random import randint

@dataclass
class GithubRepository:
    """GithubRepository is a class"""

    workflow_ui = WorkflowRepresentation()

    def test_and_push_to_github(self, args: List[str]) -> None:
        '''test_and_push_to_github will:
        1. cd into target_directory
        2. git pull the latest changes from github
        3. run the tests, depending on whether is a python or javascript repo:
        - jest for javascript
        - pytest for python
        4. code formatting using prettier
        5. push the changes to github with the custom message

        you can call this method by running:
        ```bash
        python workflow.py "git" "t" "py" "t commit message for changing test code"
        ```
        ---
        Parameters:
        - _type - str : this can be py or js and it dictates what types of tests are run 
        - target_directory - str : this is the directory which the os will cd into

        ---
        Returns:
        - None
        '''
        # arg is of the following typ ["filename", "git", "t", "py", "commit_message","target_directory"]
        _type = "py"
        commit_message = "c make it better (untested)"
        target_directory = os.getcwd()
        if len(args) == 3:
            pass
        elif len(args) == 4:
            _type = args[3]
        elif len(args) == 5:
            _type = args[3]
            commit_message = args[4]
        else:
            _type = args[3]
            commit_message = args[4]
            target_directory = args[5]

        self.workflow_ui.pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        self.workflow_ui.pp(f"pull recent changes from github 😼⤵️")
        os.system("git pull")

        if _type == "js":
            self.workflow_ui.pp("running tests using npm ☕Script 🧪")
            os.system("npm test")

        if _type == "py":
            self.workflow_ui.pp("running tests using pytest 🐍🧪")
            os.system("python -m pytest src/tests")
            self.workflow_ui.pp("checking types 🐍📰")
            os.system("mypy src")

        self.workflow_ui.pp("formatting code using prettier ✨")
        os.system("prettier -w .")

        test_result = input("have all the tests passed? (y/n):")
        if test_result == "y":
            self.workflow_ui.pp(
                "the tests have passed so we can push to github ✅")
            os.system("git add . ")
            os.system(
                f'git commit -m "{self.__style_commit_message(commit_message)}"')
            os.system("git push ")
        else:
            self.workflow_ui.pp("workflow completed without pushing ❌")

    def push_to_github(self, args: List[str]) -> None:
        """push_to_github has the following params
        """
        # arg is of the following type ["filename", "commit_message"] 
        commit_message = "c make it better (untested)"
        if len(args) > 1:
            commit_message = args[1]
        target_directory = os.getcwd()

        self.workflow_ui.pp("pushing untested code 😞")
        self.workflow_ui.pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        os.system("git pull")
        os.system("git add . ")
        os.system(
            f'git commit -m "{self.__style_commit_message(commit_message)}"')
        os.system("git push ")

    def push_new_repo_to_github(self, args: List[str]) -> None:
        """push_new_repo_to_github has the following params
        """
        # arg is of the following type ["filename", "git", "init", "target_directory"] 
        target_directory = os.getcwd()
        if len(args) >= 4:
            target_directory = args[3]

        self.workflow_ui.pp("making a new folder 📁")
        os.system(f"mkdir {target_directory}")
        self.workflow_ui.pp("initializing a new github repository ➡️")
        os.chdir(target_directory)
        os.system("git init")
        os.system("git add . ")
        os.system(
            f'git commit -m "{self.__style_commit_message("c first commit")}"')
        self.workflow_ui.pp("now you can publish the branch from VS Code")
        os.system(f"start code {target_directory}")

    def push_new_branch_to_github(self, args: List[str]) -> None:
        """push_new_branch_to_github has the following params
        """
        # arg is of the following type ["filename", "git", "-b", "target_directory"] 
        target_directory = os.getcwd()
        if len(args) >= 4:
            target_directory = args[3]
            
        os.chdir(target_directory)
        self.workflow_ui.pp("making a new branch 🌳")
        os.system("git checkout -b new-feature")
        os.system("git add . ")
        os.system(
            f'git commit -m "{self.__style_commit_message("c add new feature")}"')
        self.workflow_ui.pp("publishing the new branch to github ⌚")
        os.system(f"git push --set-upstream origin new-feature")

    def __style_commit_message(self, commit_message: str) -> str:
        """style_commit_message has the following params

        Parameters
        ---

        commit_message str
            to be passed as parameter 2

        Returns
        ---
        result: str
        """
        # this is to make commit messages more interesting
        code_commit_message_emojis = ["😕", "⭐", "✊", "🤝", "👐"]
        if commit_message.startswith("t "):
            message_prefix = "test:"
            message_suffix = "🧪"
            commit_message = commit_message.replace("t ", " ")

        elif commit_message.startswith("d "):
            message_prefix = "documentation:"
            message_suffix = "📰"
            commit_message = commit_message.replace("d ", " ")

        elif commit_message.startswith("c "):
            message_prefix = "code:"
            message_suffix = code_commit_message_emojis[randint(
                0, len(code_commit_message_emojis) - 1)]
            commit_message = commit_message.replace("c ", " ")

        elif commit_message.startswith("TODO:"):
            message_prefix = ""
            message_suffix = "🔴🔴🔴"

        else:
            message_prefix = ""
            message_suffix = ""

        return message_prefix + commit_message + message_suffix
