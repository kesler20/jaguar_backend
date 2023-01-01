from random import randint
import sys
import os
import time
import json
from typing import Any, Dict, List, Union
from pathlib import Path
import shutil
try:
    from src.jaguar_backend.operating_system_interface import OperatingSystemInterface
    from src.jaguar_backend.amplify_application import AmplifyApplication
    from src.jaguar_backend.react_application import ReactApplication
    from src.jaguar_backend.github_repository import GithubRepository
    from src.jaguar_backend._base import WorkflowRepresentation
except ModuleNotFoundError: 
    from jaguar_backend.operating_system_interface import OperatingSystemInterface
    from jaguar_backend.amplify_application import AmplifyApplication
    from jaguar_backend.react_application import ReactApplication
    from jaguar_backend.github_repository import GithubRepository
    from jaguar_backend._base import WorkflowRepresentation

if __name__ == "__main__":
    osi = OperatingSystemInterface()
    amplify = AmplifyApplication()
    react = ReactApplication()
    git = GithubRepository()
    workflow_ui = WorkflowRepresentation()

    if len(sys.argv) > 1:

        if sys.argv[1] == "git":
            if len(sys.argv) > 2:
                if sys.argv[2] == "t":
                    git.test_and_push_to_github(sys.argv)
                elif sys.argv[2] == "init":
                    git.push_new_repo_to_github(sys.argv)
                elif sys.argv[2] == "describe":
                    # ["_dev.py","git","describe","description",("repository_name")]
                    git.add_description_to_repo(sys.argv[3])
                    if len(sys.argv) > 4:
                        git.add_description_to_repo(sys.argv[3],sys.argv[4])

                else:
                    git.push_new_branch_to_github(sys.argv)
            else:
                print("try to run one of the following")
                print("python _dev.py git t py -> to run the tests ")
                print("python _dev.py git init <target_directory> -> to initialize a repo ")
                print("python _dev.py git <any> <target_directory> -> to initialize a new branch ")
        
        elif sys.argv[1] == "aws":
            if sys.argv[2] == "init":
                amplify.initialize_amplify_application(sys.argv)
            elif sys.argv[2] == "edit":
                amplify.modify_amplify_application(sys.argv)
            elif sys.argv[2] == "u":
                amplify.update_amplify_application(sys.argv)
            elif sys.argv[2] == "publish":
                amplify.push_to_amplify(sys.argv)
            else:
                workflow_ui.describe("aws")
                print("these are the categories that you can select")
                for index, category in enumerate(amplify.categories):
                    print(f"{index} : ", category)

        elif sys.argv[1] == "react":
            if sys.argv[2] == "init":
                react.initialise_npm_process(sys.argv)
            elif sys.argv[2] == "config":
                react.initialise_env_file(sys.argv)
            else:
                print(
                    'running python workflow.py "react" "config" will paste the .env file in the root dir')
                print(
                    'running python workflow.py "react" "init" will initialize the react application')

        elif sys.argv[1] == "push":
            for dir in os.listdir(os.path.join(osi.gcu(),"protocol")):
                with OperatingSystemInterface(os.path.join(osi.gcu(),"protocol", dir)) as op_sys:
                    op_sys.system("python _dev.py g")

        elif sys.argv[1] == "install":
            workflow_ui.pp("INSTALLING JAGUAR <😼⏬>")
            # now you can push all of the changes to github within the protocol folder as follows
            for index, dir in enumerate(os.listdir(os.path.join(osi.gcu(),"protocol"))):
                if dir == "jaguar_backend":
                    pass
                else:
                    osi = OperatingSystemInterface(os.path.join(osi.gcu(),"protocol", dir))
                    osi.copy_file_from_folder("_dev.py")
                    if index == len(os.listdir(os.path.join(osi.gcu(),"protocol"))):
                        workflow_ui.pp("you can now paste the src.jaguar_backend in directory 😇")
                        os.system("start code jaguar_backend")

        elif sys.argv[1] == "test":
            git.run_tests(sys.argv)
            
        elif sys.argv[1] == "-h":
            with open(os.path.join(osi.gcu(),"protocol","jaguar","commands.txt"), "r") as f:
                for line in f.readlines():
                    print(line)
        
        elif sys.argv[1] == "issue":
            if sys.argv[2] == "create":
                git.create_issue(sys.argv[3], sys.argv[4])
        
            elif sys.argv[2] == "read":
                git.read_issues()
            
            elif sys.argv[2] == "close":
                # ["_dev.py","issue","close","from_val","to_val"]
                if len(sys.argv) > 4:
                    git.close_issues(int(sys.argv[3]), int(sys.argv[4]))
                else:
                    git.close_issue(sys.argv[3])
        
        elif sys.argv[1] == "readme":
            if sys.argv[2] == "create":
                git.create_issues_from_readme()
            if sys.argv[2] == "read":
                git.read_todos_from_readme()
            if sys.argv[2] == "cross":
                git.cross_todos_from_readme(sys.argv[3])
            else:
                workflow_ui.pp("apply the following methods to interact with the readme 📰")
                print("create -> to create issues from the readme")
                print("read -> to check all the readme todos")
                print("cross -> tick all the todos that have been completed by passing their title")

        else:
            # if no domain is passed this will be pushed to github
            git.push_to_github(sys.argv)

    else:
        with open(os.path.join(osi.gcu(),"Protocol","jaguar","commands.txt"), "r") as f:
            for line in f.readlines():
                print(line)
