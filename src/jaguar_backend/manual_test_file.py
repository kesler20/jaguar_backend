
from jaguar_backend.file import File
import os
from pathlib import Path

print("Testing:" + File.__doc__)
        
if __name__ == "__main__":
    file = File(Path(os.getcwd()))
    
    file.read()
                
    file.append("hello world")
                
    file.write("hello world")
                
    file.readlines()
                
    file.get_json()
                
    file.write_json([{ "key" : "hello world" }])
                
    file.writeline("hello world")
                
    file.read_line_by_condition(lambda item: item.startswith("w"))
                
    file.delete()
                
        