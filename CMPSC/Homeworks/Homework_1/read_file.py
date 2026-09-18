def get_path(file_name):
    """
        Returns a string with the absolute path of a given file_name located in the same directory as this script

        # Do not modify this function in any way

        >>> get_path('words.txt')   # HW1.py and words.txt located in HW1 folder
        'G:\My Drive\CMPSC132\HW1\words.txt'
    """
    import os
    target_path = os.path.join(os.path.dirname(__file__), file_name)
    return target_path


def use_iteration(filename):
  file_path = get_path(filename)
  with open(file_path, 'r') as file:
    for line in file:
        print(line)


def use_read(filename):
    file_path = get_path(filename)
    with open(file_path, 'r') as file:
        contents = file.read()
    
    print(contents)



def use_readlines(filename):
    file_path = get_path(filename)
    with open(file_path, 'r') as file:
        contents = file.readlines()
    
    print(contents)

