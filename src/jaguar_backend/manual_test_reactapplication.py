
from react_application import ReactApplication

print("Testing:" + ReactApplication.__doc__)

args = ("this",)
if __name__ == "__main__":
    react_application = ReactApplication()

    react_application.initialise_env_file(args)

    react_application.initialise_npm_process(args)
