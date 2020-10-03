import json

def save_to_file(data, file_name):
    with open(file_name, "w") as write_file:
        json.dump(data, write_file, indent=4)
        print("Successfully written to {}".format(file_name))


def read_from_file(file_name):
    with open(file_name, "r") as read_File:
        data = json.load(read_File)
        print("Successfully read from {}".format(file_name))
    return data

