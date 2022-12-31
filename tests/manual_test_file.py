import shutil
from jaguar_backend.file import File
import os
from pathlib import Path

test_file = "test_file.txt"
json_test_file = "test_file.json"
try:
    shutil.rmtree(test_file)
    shutil.rmtree(json_test_file)
except FileNotFoundError:
    pass

if __name__ == "__main__":
    file = File(Path(test_file))

    file.append("hello world 1")
    file.append("hello world 2")

    print(file.read())
    print(file.readlines())

    file.write("hello world")
    print(file.read())

    file.writeline("hello world")
    file.append("this is a cool idea")

    print(file.read_line_by_condition(lambda item: item.startswith("t")))

    file.delete()
    print(Path(test_file).exists())

    file = File(Path(json_test_file))
    file.write_json([{ "key" : "hello world" }])
    print(file.get_json())
    file.delete()
