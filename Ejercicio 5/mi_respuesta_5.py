import string 
import re
def alphabet_position(text):

    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    text_new = re.findall("[a-z]", text.lower())

    for i in text_new:
        for index, letra in enumerate(alphabet_list):
            if i == letra:
                text_new[text_new.index(i)] = str(index+1)
    "  ".join(text_new)
    return text_new
        
print(alphabet_position("The sunset sets at twelve o' clock."))