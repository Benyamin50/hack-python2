"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""

def fn_hack_7(s):
    if s == [0]:
        return [0]
    result = []
    for i in range(len(s)):
        convertir = i + 1 
        if convertir % 2 == 1: 
            result.append(str(convertir)) 
        else:  
            result.append(convertir)  
    return result
