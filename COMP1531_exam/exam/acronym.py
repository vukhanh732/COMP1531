def acronym_make(inputs):
    vowel = "AEIOUaeiou"
    oupt = ""
    for i in inputs:
        lst = i.split()      
        for word in lst:
            if word not in vowel:       
                oupt += word[0]
          
    # uppercase oupt
    oupt = oupt.upper()
    return oupt
        
print(acronym_make(['I am very tired today','This is a test']))