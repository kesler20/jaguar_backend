
from typing import List, Any, Union, Dict, Optional, Tuple
import os
import shutil
import sys


class OperatingSystemInterface:
    """OperatingSystemInterface is a class
    you can access the interface like a resource manager such as

    ```python
    with OperatingSystemInterface(directory) as osi:
        osi.do_something()
    # alternatively if there are multiple calls that you want to make you can use
    osi = OperatingSystemInterface()
    with osi as oi:
        oi.system("echo hello world")
    ```
    """

    def __init__(self, directory=os.getcwd()) -> None:
        self.directory: str = directory

    def __enter__(self) -> os:
        '''signature description'''
        os.chdir(self.directory)
        return os

    def __exit__(self, *args) -> os:
        '''signature description'''
        os.chdir(os.getcwd())

    def gcf(self) -> str:
        """returns the current folder where the file is being run"""
        if sys.platform == "linux":
            return __file__.split("protocol")[1].split(r"/")[1]
        else:
            return __file__.split("protocol")[1].split(r"\ ".replace(" ", ""))[1]

    def gcu(self) -> str:
        """gcu has the following params"""
        '''Get the current user i.e. C:/Users/CBE-User 05'''
        return os.path.abspath(__file__).split(r"\protocol")[0]

    def copy_file_from_folder(self, file: str, source_folder: Optional[str] = "jaguar_backend") -> None:
        """The folder that you are currently working on will be used as destination file
        The source folder will be searched in the protocol folder and is jaguar_backend by default
        the file which will be replace in the local directory has path 
        ``os.path.join(self.directory,file)``

        Parameters
        ---

        file str
            the file that we want to move to the root directory from the source_folder
        source_folder : str
            the folder where the file will be searched, this is jaguar_backend by default

        Returns
        ---
        result: None
        """

        source = os.path.join(os.path.abspath(__file__).split(
            r"\{}".format(source_folder))[0], source_folder, file)
        destination = os.path.join(self.directory, file)

        print(r'''
        copying {} 
        ---> into 
        {}
        '''.format(source, destination))
        print(os.getcwd())
        shutil.copy(source, destination)

    def copy_folder_from_folder(self, folder: str, source_folder: Optional[str] = os.path.join("protocol", "jaguar_backend")) -> None:
        """The folder that you are currently working on will be used as destination folder
        The source folder will be searched in the protocol folder and is protocol by default
        the folder which will be replace in the local directory has path 
        ``os.path.join(self.directory,folder)``

        Parameters
        ---

        folder str
            the folder that we want to move to the root directory from the source_folder
        source_folder : str
            the folder where the folder will be searched, this is protocol by default

        Returns
        ---
        result: None
        """

        source = os.path.join(os.path.abspath(__file__).split(
            r"\{}".format(source_folder))[0], source_folder, folder)
        destination = os.path.join(self.directory, folder)

        print(r'''
        copying {} 
        ---> into 
        {}
        '''.format(source, destination))
        print(os.getcwd())
        try:
            shutil.copytree(source, destination)
        except FileExistsError as err:
            print(err)
            print("reinstalling the folder...⚙️")
            shutil.rmtree(destination)
            shutil.copytree(source, destination)


    def move_folder_resources(self, source_path: str, destination_path: str) -> None:
        """move_folder_resources 
        the directory passed as a property will be used as a source path

        Parameters
        ---

        destination_path str
            this is the folder where the files will be moved to
        source_path str
            this is the folder where the files will be moved from

        Returns
        ---
        result: None
        """
        for resource in os.listdir(source_path):
            destination_dir = os.path.join(destination_path, resource)
            source_dir = os.path.join(source_path, resource)
            os.rename(source_dir, destination_dir)

    def read_word_in_directory(self, word: str) -> 'list[str]':
        """read_word_in_directory has the following params

        Parameters
        ---

        word str
            The word that will be searched on the current directory

        Example
        ---

        for example this function can be used by moving the Os interface to the desired 
        directory to search
        ```python
        with OperatingSystemInterface(desired_directory) as osi:
            list_of_files = osi.read_word_in_directory("<class_name>")
        print(list_of_files)
        ```
        Returns
        ---
        result: 'list[str]'
        """
        result = []
        for root, directories, files in os.walk(self.directory):
            for file in files:
                with open(os.path.join(self.directory, file)) as f:
                    content = f.read()
                    if content.find(word) != -1:
                        result.append(file)

        return result
