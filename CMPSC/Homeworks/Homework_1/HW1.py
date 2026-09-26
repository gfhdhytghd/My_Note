# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

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


def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    if perimeter%2!=0:
        return False
    h=1
    w=perimeter//2-h
    while w*h < area and w*h >=0:
        h+=1
        w-=1
    if w*h==area:
        return int(w)
    else:
        return False



def to_decimal(oct_num):
    """
        >>> to_decimal(237)
        159
        >>> to_decimal(35)
        29
        >>> to_decimal(600)
        384
        >>> to_decimal(420)
        272
    """
    #- YOUR CODE STARTS HERE
    dec_output=0
    digit=0
    while oct_num>0:
        dec_output+=8**digit*(oct_num%10)
        oct_num=oct_num//10
        digit+=1
    return dec_output


def has_hoagie(num):
    """
        >>> has_hoagie(737)
        True
        >>> has_hoagie(35)
        False
        >>> has_hoagie(-6060)
        True
        >>> has_hoagie(-111)
        True
        >>> has_hoagie(6945)
        False
    """
    #- YOUR CODE STARTS HERE
    num = abs(num)
    while num >= 100:
        if num%10==num//100%10:
            return True
        num = num//10
    return False


def to_identical(num_in):
    """Removes consecutive repeated digits from a positive integer."""
    num_in = abs(num_in)
    num_out = 0
    last_digit = -1
    divisor = 1
    while num_in // divisor >= 10:
        divisor *= 10
    while divisor > 0:
        current_digit = num_in // divisor
        num_in %= divisor
        divisor //= 10
        if current_digit != last_digit:
            num_out = num_out * 10 + current_digit
            last_digit = current_digit
    return num_out


def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765)
        False
        >>> is_identical(2023, 20)
        False
    """
    return to_identical(num_1)==to_identical(num_2)
    #- YOUR CODE STARTS HERE


def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    output_list=[num]
    while num!=1:
        if num%2==0:
            num=num//2
        else:
            num=num*3+1
        output_list.append(num)
    return output_list


def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True
    """
    #- YOUR CODE STARTS HERE
    if key not in d:
        d[key]=value
    else:
        if not isinstance(d[key],list):
            d[key]=[d[key]]
        d[key].append(value)


def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    #- YOUR CODE STARTS HERE
    dict_by_department={}
    for empid,employee in d.items():
        if employee['department'] not in dict_by_department:
            dict_by_department[employee['department']]=[]
        dict_by_department[employee['department']].append({"emp_id":empid,"name":employee['name'],"position":employee['position']})
    return dict_by_department


def successors(file_name):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better
    # --- YOU CODE STARTS HERE
    tokens=[]
    current=''
    for char in contents:
        if char.isalnum():
            current+=char
        else:
            if current!='':
                tokens.append(current)
                current=''
            if char.strip()!='':
                tokens.append(char)
    if current!='':
        tokens.append(current)

    output_dict={'.':[]}
    previous='.'
    for token in tokens:
        if previous not in output_dict:
            output_dict[previous]=[]
        if token not in output_dict[previous]:
            output_dict[previous].append(token)
        previous=token
    return output_dict


def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}

        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    #- YOUR CODE STARTS HERE
    for letter in word:
        if letter not in trie:
            trie[letter]={}
        trie=trie[letter]
    trie['word']=True


def createDictionaryTrie(file_name):
    """
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better
    #- YOUR CODE STARTS HERE
    trie={}
    for word in contents.split():
        addToTrie(trie,word.lower())
    return trie


def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    #- YOUR CODE STARTS HERE
    for letter in word:
        if letter not in trie:
            return False
        trie=trie[letter]
    return 'word' in trie




def run_tests():
    """Runs additional normal and boundary tests for every required function."""
    assert rectangle(14,10)==5
    assert rectangle(4,1)==1
    assert rectangle(7,3)==False

    assert to_decimal(1)==1
    assert to_decimal(10)==8
    assert to_decimal(777)==511

    assert has_hoagie(10)==False
    assert has_hoagie(101)==True
    assert has_hoagie(-12321)==True

    assert is_identical(111,1)==True
    assert is_identical(100,10)==True
    assert is_identical(10,1)==False

    assert hailstone(1)==[1]
    assert hailstone(2)==[2,1]
    assert hailstone(3)==[3,10,5,16,8,4,2,1]

    d={}
    overloaded_add(d,'x',1)
    assert d=={'x':1}
    overloaded_add(d,'x',2)
    assert d=={'x':[1,2]}
    overloaded_add(d,'x',3)
    assert d=={'x':[1,2,3]}

    employees={1:{'name':'A','position':'P','department':'D'}}
    assert by_department({})=={}
    assert by_department(employees)=={'D':[{'emp_id':1,'name':'A','position':'P'}]}
    assert employees=={1:{'name':'A','position':'P','department':'D'}}

    following=successors('items.txt')
    assert following['.']==['We','Maybe']
    assert following['to']==['learn','have','make']
    assert following[',']==['eat']

    trie={}
    addToTrie(trie,'a')
    assert trie=={'a':{'word':True}}
    addToTrie(trie,'at')
    assert wordExists(trie,'at')==True
    addToTrie(trie,'dog')
    assert wordExists(trie,'dog')==True

    file_trie=createDictionaryTrie('list_of_words.txt')
    assert wordExists(file_trie,'ball')==True
    assert wordExists(file_trie,'treat')==True
    assert wordExists(file_trie,'cat')==False

    assert wordExists(trie,'a')==True
    assert wordExists(trie,'app')==False
    assert wordExists(trie,'dogs')==False

if __name__ == "__main__":
    run_tests()
