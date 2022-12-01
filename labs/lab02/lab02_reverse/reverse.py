def reverse_words(string_list):
    '''
    Given a list of strings, return a new list where the order of the words is
    reversed
    '''
    new_list = []
    for string in string_list:
        words = string.split(" ")
        reverse_string = " ".join(reversed(words))
        new_list.append(reverse_string)
    
    return new_list

if __name__ == "__main__":
    print(reverse_words(["Hello World", "I am here"]))
    # it should print ['World Hello', 'here am I']
