
#INCOMPLETO!!

import re

def solution(s):
    x = re.search("[A-Z]+", s)
    text = re.sub("[A-Z]+", " "+ x.group(), s)
    return text

print(solution("holaComoEstas"))