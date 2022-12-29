
from jaguar_backend.operating_system_interface import OperatingSystemInterface

print("Testing:" + OperatingSystemInterface.__doc__)

if __name__ == "__main__":
    operating_system_interface = OperatingSystemInterface()

    operating_system_interface.gcu()

    operating_system_interface.copy_file_from_folder(file, source_folder)

    operating_system_interface.move_folder_resources(destination_path)

    operating_system_interface.read_word_in_directory(word)
