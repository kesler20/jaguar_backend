
import unittest
from reactapplication import ReactApplication

print("Testing:" + ReactApplication.__doc__)
        
if __name__ == "__main__":
    reactapplication = ReactApplication()
    
    reactapplication.initialise_env_file(*args)
                
    reactapplication.initialise_npm_process(*args)
                
        