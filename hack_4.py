"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""



def fn_hack_4(s):
  reemplazar = {
        'f': '',
        'b': '',
        'n': ''
    }
 
  acceder = list(s)

  for i in range(len(acceder)):
     if acceder[i] in reemplazar:
         acceder[i] = reemplazar[acceder[i]]

  return ''.join(acceder)
 