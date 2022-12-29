
from typing import List, Any, Union, Dict, Optional, Tuple
from jaguar_backend._types import *
from jaguar_backend._base import WorkflowRepresentation
from jaguar_backend.operating_system_interface import OperatingSystemInterface


class ReactApplication:
    """ReactApplication is a class"""

    def __init__(self) -> None:
        self.workflow_ui = WorkflowRepresentation()
        self.osi = OperatingSystemInterface()

    def initialise_env_file(self, *args: Tuple[Any]) -> None:
        """initialise_env_file has the following params

        Parameters
        ---

        *args Tuple[Any]
            to be passed as parameter 2

        Returns
        ---
        result: 
        """
        with open(".env", "w") as env, open(os.path.join(self.osi.gcu(), "Protocol", "jaguar", "config.py"), "r") as configs:
            content = configs.read()
            env.write(content)

    def initialise_npm_process(self, *args: Tuple[Any]) -> None:
        """initialise_npm_process has the following params

        Parameters
        ---

        *args Tuple[Any]
            to be passed as parameter 2

        Returns
        ---
        result: None
        """
        target_directory = os.getcwd()
        self.workflow_ui.pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)

        self.workflow_ui.pp(f"clone react project -> {args[0]} ⤵️")
        os.system(f"git clone https://github.com/kesler20/{args[0]}")

        self.workflow_ui.pp("pull resent changes from github ↪️")
        os.system("git pull")
        self.workflow_ui.pp(
            " making sure that the npm packages are installed ⚙️")
        os.system("npm i")
        self.workflow_ui.pp("starting the application")
        os.system("npm start")
