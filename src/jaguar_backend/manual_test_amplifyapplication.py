
from amplify_application import AmplifyApplication

print("Testing:" + AmplifyApplication.__doc__)

if __name__ == "__main__":
    amplify_application = AmplifyApplication()

    amplify_application.update_amplify_application()

    amplify_application.modify_amplify_application()

    amplify_application.initialize_amplify_application()

    amplify_application.push_to_amplify()
