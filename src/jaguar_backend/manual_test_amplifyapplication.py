from pathlib import Path
import os
import shutil
import sys
try:
    from src.jaguar_backend.amplify_application import AmplifyApplication
except ModuleNotFoundError:
    from amplify_application import AmplifyApplication

print("Testing:" + AmplifyApplication.__doc__)

try:
    shutil.rmtree(os.path.join(__file__.split("\src")[0],"src","jaguar_backend","amplify"))
except FileNotFoundError:
    pass

if __name__ == "__main__":
    pass
    # amplify_application = AmplifyApplication()
    # print(amplify_application.categories)

    # amplify_application.initialize_amplify_application(sys.argv)

    # amplify_application.modify_amplify_application(sys.argv)

    # amplify_application.update_amplify_application(sys.argv)

    # amplify_application.push_to_amplify()
