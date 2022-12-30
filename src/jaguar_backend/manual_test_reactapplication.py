import sys
from pathlib import Path
import os
try:
    from src.jaguar_backend.react_application import ReactApplication
except ModuleNotFoundError:
    # from react_application import ReactApplication
    pass

print("Testing:" + ReactApplication.__doc__)

args = ("this",)
if __name__ == "__main__":
    react_application = ReactApplication()

    react_application.initialise_env_file()

    try:
        react_application.initialise_npm_process(sys.argv)
    except:
        pass
    
    if Path(".env").exists():
        os.system("del .env")