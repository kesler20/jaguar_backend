
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
import os


class Path(Protocol):
    ...
            

class OperatingSystemInterface(Protocol):   
        
    def __init__(self) -> None:
        ...
          
    def __enter__(self) -> os:
        ...
          
    def __exit__(self) -> os:
        ...
          
    def gcu(self) -> str:
        ...
          
    def copy_file_from_folder(self, file) -> None:
        ...
          
    def move_folder_resources(self, destination_path : str) -> None:
        ...
          
    def read_word_in_directory(self, word : str) -> 'list[str]':
        ...
        
           
class File(Protocol):   
        
    def __init__(self, filename : Path) -> None:
        ...
          
    def read(self) -> str:
        ...
          
    def append(self, content : str) -> None:
        ...
          
    def write(self, content : str) -> None:
        ...
          
    def readlines(self) -> 'list[str]':
        ...
          
    def get_json(self) -> Any:
        ...
          
    def write_json(self, content: Union[Dict[str, Any], List[Any]]) -> None:
        ...
          
    def writeline(self, content : str) -> None:
        ...
          
    def read_line_by_condition(self) -> 'list[str]':
        ...
          
    def delete(self) -> None:
        ...
        
