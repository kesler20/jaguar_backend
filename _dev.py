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
    from operating_system_interface import OperatingSystemInterface
    from amplify_application import AmplifyApplication
    from react_application import ReactApplication
    from github_repository import GithubRepository
    from _base import WorkflowRepresentation

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
                else:
                    git.push_new_branch_to_github(sys.argv)
            else:
                print("try to run one of the following")
                print("python _dev.py git t py  -> to run the tests ")
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
            for dir in os.listdir(os.path.join(osi.gcu(),"protocol")):
                if dir == "jaguar_backend":
                    pass
                else:
                    osi = OperatingSystemInterface(os.path.join(osi.gcu(),"protocol", dir))
                    osi.copy_file_from_folder("_dev.py")

        elif sys.argv[1] == "-h":
            with open(os.path.join(osi.gcu(),"protocol","jaguar","commands.txt"), "r") as f:
                for line in f.readlines():
                    print(line)

        else:
            # if no domain is passed this will be pushed to github
            git.push_to_github(sys.argv)

    else:
        with open(os.path.join(osi.gcu(),"Protocol","jaguar","commands.txt"), "r") as f:
            for line in f.readlines():
                print(line)
