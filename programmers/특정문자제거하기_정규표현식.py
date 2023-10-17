import re

print("BCBdbe".replace('B', ''))

print(re.sub('B', '', 'BCBdbe'))
print(re.sub('[1-9]', '', 'B1111C22Bd45232be'))
print(re.sub('[a-zA-Z]', '', 'B1111C22Bd45232be'))

import re
def solution(my_string, letter):
    # return "".join(list(filter(lambda x : x != letter, my_string)))
    return re.sub(letter, '', my_string)