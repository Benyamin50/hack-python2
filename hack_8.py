"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""



def fn_hack_8(s):
    result = []
    logintud = len(s)
    for i in range(logintud):
        original_pos = logintud - i  
        if logintud % 2 == 1:  
            result.append(f"{s[logintud - 1 - i]}-{original_pos}")
        else:  
            result.append(str(original_pos))
    return result
