import os

def check_for_empty_or_none(*args):
    for arg in args:
        if arg is None:
            raise Exception("One of the argument is None")
        if arg == "":
            raise Exception("One of the argument is empty")


def copy(source_file, target_file):
    """
    copy source file to target file
    :param source_file:  absolute/relative path to source file
    :type source_file: String
    :param target_file: absolute/relative path to target file
    :type target_file: String
    :return:  None
    :rtype: None
    :raises Exception when inputs or bad or cannot copy a file
    """
    check_for_empty_or_none(source_file, target_file)

    if not os.path.exists(source_file):
        raise Exception(f"{source_file} not found")

    with open(source_file, "r") as sfp:
        source_file_contents = sfp.read()

    with open(target_file, 'w') as tfp:
        tfp.write(source_file_contents)


def move(source_file, target_file):
    """
    moving from source file path to target file path
    :param source_file: name of the source file
    :type source_file: String
    :param target_file: name of the target file
    :type target_file: String
    :return: None
    :rtype: None
    :raises Exception
    """
    check_for_empty_or_none(source_file,target_file)
    if not os.path.exists(source_file):
        raise Exception(f"{source_file} not found")
    with open(source_file, "r") as sfp:
        source_file_contents = sfp.read()

    with open(target_file, 'w') as tfp:
        tfp.write(source_file_contents)
        os.remove(source_file)


if __name__ == '__main__':
    source_file_path = "/Users/sainanduri/PycharmProjects/Intro/5Files/students.txt"
    target_file_path = "/Users/sainanduri/PycharmProjects/Intro/5Files/students1.txt"
    copy(source_file=source_file_path, target_file=target_file_path)
    move(source_file=source_file_path, target_file=target_file_path)
    print("Copy Successfully done")
