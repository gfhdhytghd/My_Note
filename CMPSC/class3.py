def frequency(input_str:str):
    count={}
    for letter in input_str:
        if letter.isalpha():
            letter=letter.lower()
            if letter in count:
                count[letter]+=1
            else:
                count[letter]=1
    return count

