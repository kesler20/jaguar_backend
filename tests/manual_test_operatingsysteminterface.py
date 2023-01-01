import shutil
from pathlib import Path
import os
from jaguar_backend.operating_system_interface import OperatingSystemInterface

print("Testing:" + OperatingSystemInterface.__doc__)

test_folder = "test_folder"
another_test_folder = "another_test_folder"

try:
    shutil.rmtree(test_folder)
    shutil.rmtree(another_test_folder)
except FileNotFoundError:
    pass

if __name__ == "__main__":
    if not Path(test_folder).exists():
        os.mkdir(test_folder)
        os.mkdir(another_test_folder)

    operating_system_interface = OperatingSystemInterface(test_folder)

    print(operating_system_interface.gcu())
    print(operating_system_interface.gcf())

    operating_system_interface.copy_file_from_folder("index.html",source_folder="jaguar")

    oi = OperatingSystemInterface(another_test_folder)
    oi.move_folder_resources(test_folder, another_test_folder)

    osi = OperatingSystemInterface(another_test_folder)
    print(osi.read_word_in_directory("jaguar"))

    try:
        shutil.rmtree(test_folder)
        shutil.rmtree(another_test_folder)
    except FileNotFoundError:
        pass
