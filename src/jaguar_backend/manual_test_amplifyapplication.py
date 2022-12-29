
import unittest
from amplifyapplication import AmplifyApplication

print("Testing:" + AmplifyApplication.__doc__)
        
if __name__ == "__main__":
    amplifyapplication = AmplifyApplication()
    
    amplifyapplication.update_amplify_application()
                
    amplifyapplication.modify_amplify_application()
                
    amplifyapplication.initialize_amplify_application()
                
    amplifyapplication.push_to_amplify()
                
        