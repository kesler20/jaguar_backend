from random import randint
import sys
import os
import time
import json
from typing import Any, Dict, List, Union
from pathlib import Path
import shutil
from src.jaguar_backend.operating_system_interface import OperatingSystemInterface
from src.jaguar_backend.amplify_application import AmplifyApplication
from src.jaguar_backend.react_application import ReactApplication
from src.jaguar_backend.github_repository import GithubRepository
from src.jaguar_backend._base import WorkflowRepresentation

if __name__ == "__main__":
    osi = OperatingSystemInterface()
    user_directory = osi.gcu()

    amplify = AmplifyApplication()
    react = ReactApplication()
    git = GithubRepository()
    workflow_ui = WorkflowRepresentation()

    if sys.argv[1] == "git":
        if sys.argv[2] == "t":
            git.test_and_push_to_github(*sys.argv[2:])
        elif sys.argv[2] == "init":
            git.push_new_repo_to_github(sys.argv[2:])
        else:
            git.push_to_github(*sys.argv[2:])

    elif sys.argv[1] == "aws":
        if sys.argv[2] == "init":
            amplify.initialize_amplify_application(sys.argv[2:])
        elif sys.argv[2] == "edit":
            amplify.modify_amplify_application(sys.argv[2:])
        elif sys.argv[2] == "u":
            amplify.update_amplify_application(sys.argv[2:])
        elif sys.argv[2] == "sync":
            amplify.sync_env_variable_to_aws_exports(
                sys.argv[2:])
        elif sys.argv[2] == "publish":
            amplify.push_to_amplify(sys.argv[2:])
        else:
            workflow_ui.describe("aws")
            print("these are the categories that you can select")
            for index, category in enumerate(amplify.categories):
                print(f"{index} : ", category)

    elif sys.argv[1] == "react":
        if sys.argv[2] == "init":
            react.initialise_npm_process(*sys.argv[2:])
        elif sys.argv[2] == "config":
            react.initialise_env_file(*sys.argv[2:])
        else:
            print(
                'running python workflow.py "react" "config" will paste the .env file in the root dir')
            print(
                'running python workflow.py "react" "init" will initialize the react application')

    elif sys.argv[1] == "push":
        for dir in os.listdir(r"C:\Users\CBE-User 05\protocol"):
            with OperatingSystemInterface(os.path.join(r"C:\Users\CBE-User 05\protocol", dir)) as op_sys:
                op_sys.system("python workflow.py g")

    elif sys.argv[1] == "install":
        workflow_ui.pp("INSTALLING JAGUAR <😼⏬>")
        # now you can push all of the changes to github within the protocol folder as follows
        for dir in os.listdir(r"C:\Users\CBE-User 05\protocol"):
            if dir == "jaguar":
                pass
            else:
                with OperatingSystemInterface(os.path.join(r"C:\Users\CBE-User 05\protocol", dir)) as op_sys:
                    # simulate that you are in the sofia silent folder
                    op_sys.system("mkdir interfaces")
                osi = OperatingSystemInterface(
                    os.path.join(r"C:\Users\CBE-User 05\protocol", dir))
                osi.copy_file_from_folder(r"interfaces\os_interface.py")
                osi.copy_file_from_folder("workflow.py")

    elif sys.argv[1] == "-h":
        with open("commands.txt", "r") as f:
            for line in f.readlines():
                print(line)

    elif sys.argv[1] == "copy":
        folders = []
        files = []
        for arg in sys.argv[2:]:
            if arg.startswith("f "):
                files.append(arg)
            else:
                folders.append(arg)
        files = [file.replace("f ", "") for file in files]
        for dir in folders:
            if dir == "jaguar":
                pass
            else:
                for file in files:
                    osi = OperatingSystemInterface(
                        os.path.join(r"C:\Users\CBE-User 05\protocol", dir))
                    osi.copy_file_from_folder(r"{}".format(file))

    else:
        git.push_to_github(sys.argv[1:])
