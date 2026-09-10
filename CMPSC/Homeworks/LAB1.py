# LAB1
# REMINDER: The work in this assignment must be your own original work and must be completed alone

def frequency(txt):
    '''
        >>> frequency('mama')
        {'m': 2, 'a': 2}
        >>> answer = frequency('We ARE Penn State!!!')
        >>> answer
        {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
        >>> frequency('One who IS being Trained')
        {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1}
    '''
    # - YOUR CODE STARTS HERE -
    count={}
    for letter in txt:
        if letter.isalpha():
            letter=letter.lower()
            if letter in count:
                count[letter]+=1
            else:
                count[letter]=1
    return count



def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -
    inv_d={}
    repete_value=[]
    for key,value in d.items():
        if value in repete_value:
            try:
                del inv_d[value]
            except:
                pass
        else:
            inv_d[value]=key
            repete_value.append(value)
    return inv_d


def employee_update(d, bonus, year):
    """
        >>> records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
        >>> employee_update(records,7500,2022)
        {2020: {'John': ['Managing Director', 'Full-time', 65000], 'Sally': ['HR Director', 'Full-time', 60000], 'Max': ['Sales Associate', 'Part-time', 20000]}, 2021: {'John': ['Managing Director', 'Full-time', 70000], 'Sally': ['HR Director', 'Full-time', 65000], 'Max': ['Sales Associate', 'Part-time', 25000]}, 2022: {'John': ['Managing Director', 'Full-time', 77500], 'Sally': ['HR Director', 'Full-time', 72500], 'Max': ['Sales Associate', 'Part-time', 32500]}}
    """
    # - YOUR CODE STARTS HERE -
    d[year]={}
    for employee in d[year-1]:
        d[year][employee]=[d[year-1][employee][0],d[year-1][employee][1],d[year-1][employee][2]+bonus]
    return d



def run_tests():
    import doctest

    # Run start tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace frequency with the name of the function you want to test
    #doctest.run_docstring_examples(frequency, globals(), name='LAB1',verbose=True)   

if __name__ == "__main__":
    run_tests()

    # 运行题目自带示例 / Run the provided examples.
    import doctest
    from copy import deepcopy

    result = doctest.testmod()
    assert result.failed == 0, "题目示例失败 / Provided examples failed"

    # 空输入、大小写和非字母 / Empty input, letter case, and nonletters.
    assert frequency('') == {}
    assert frequency('123 !?') == {}
    assert frequency('AaB b!') == {'a': 2, 'b': 2}

    # 重复两次、三次，以及保留唯一值 / Repeated and unique values.
    assert invert({}) == {}
    assert invert({'a': 1, 'b': 1}) == {}
    values = {'a': 1, 'b': 2, 'c': 1, 'd': 1, 'e': 3}
    original_values = values.copy()
    assert invert(values) == {2: 'b', 3: 'e'}
    assert values == original_values

    # 新年份加薪，保留历史记录 / Add bonuses while preserving history.
    records = {
        2020: {'Alex': ['Engineer', 'Full-time', 40000]},
        2021: {
            'Alex': ['Engineer', 'Full-time', 50000],
            'Sam': ['Assistant', 'Part-time', 20000],
        },
    }
    original_records = deepcopy(records)
    expected = deepcopy(records)
    expected[2022] = {
        'Alex': ['Engineer', 'Full-time', 57500],
        'Sam': ['Assistant', 'Part-time', 27500],
    }
    assert employee_update(records, 7500, 2022) == expected
    for year in original_records:
        assert records[year] == original_records[year]

    # 修改新记录不应影响旧记录 / New records must not share old lists.
    records[2022]['Alex'][2] = 60000
    assert records[2021]['Alex'][2] == 50000

    # 零奖金和无员工 / Zero bonus and no employees.
    assert employee_update(records, 0, 2023)[2023] == records[2022]
    assert employee_update({2021: {}}, 100, 2022) == {2021: {}, 2022: {}}

    print('所有测试通过 / All tests passed')
