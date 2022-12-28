
from typing import List, Any, Union, Dict, Optional, Tuple
from dataclasses import dataclass
from jaguar_backend._types import Path
        
@dataclass
class File:
    """File is a class"""
    
    filename : Path
    
    def __init__(self, filename : Path) -> None:
        """__init__ has the following params
        
        Parameters
        ---
            
        filename Path
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def read(self) -> str:
        """read has the following params
        """
        ...        
                  
    
    def append(self, content : str) -> None:
        """append has the following params
        
        Parameters
        ---
            
        content str
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def write(self, content : str) -> None:
        """write has the following params
        
        Parameters
        ---
            
        content str
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def readlines(self) -> 'list[str]':
        """readlines has the following params
        """
        ...        
                  
    
    def get_json(self) -> Any:
        """get_json has the following params
        """
        ...        
                  
    
    def write_json(self, content: Union[Dict[str, Any], List[Any]]) -> None:
        """write_json has the following params
        
        Parameters
        ---
            
        content Union[Dict[str,Any]
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def writeline(self, content : str) -> None:
        """writeline has the following params
        
        Parameters
        ---
            
        content str
            to be passed as parameter 2
        
        Returns
        ---
        result: None
        """
        ...
                          
    
    def read_line_by_condition(self) -> 'list[str]':
        """read_line_by_condition has the following params
        """
        ...        
                  
    
    def delete(self) -> None:
        """delete has the following params
        """
        ...        
                  