"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""




def fn_hack_9(s):
    result = {}
    if "foo" in s:

        llave = "Foo"
        valor = s["foo"]
      
        valorTwo = valor.replace("k", "").capitalize()
        result[llave] = valorTwo
    return result