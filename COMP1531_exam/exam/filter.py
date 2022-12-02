def filter_string(inp):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in inp:
        if ele.isdigit():
            raise ValueError
        if ele in punc:
            inp = inp.replace(ele, "")
    return inp.lower().capitalize()
    