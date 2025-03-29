"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    reemplazar = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
    }
    
    if not s:
        return s
    
    lista = list(s.lower())
    
    for i in range(len(lista)):
        if lista[i] in reemplazar:
            lista[i] = reemplazar[lista[i]]
    
 
    if len(lista) > 0:
        lista[0] = lista[0].upper()
    
  
    if len(lista) > 1:
        last_char = lista[-1]
        if len(lista) > 2 or last_char not in reemplazar.values():
            lista[-1] = lista[-1].upper()
    
    return ''.join(lista)

