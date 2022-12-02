from filter import filter_string

def frequency_get(multilinestr):
    
    str = filter_string(multilinestr).split()         
    list = []

    for i in str:             
        if i not in list:
            list.append(i)
    
    for i in range(0, len(list)):
        print(list[i].upper(), ':' , str.count(list[i]))


inputstr = """ I like you
I really, really, like you!
Yes I really do
"""

print(frequency_get(inputstr))
