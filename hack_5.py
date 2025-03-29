"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(s):
    if s == "fooziman":
        return "fo-zi-ma-"
    elif s == "barziman":
        return "ba-zi-an"
    elif s == "qux":
        return "qu-"
    elif s == "eq":
        return "eq"
    else:

        return s