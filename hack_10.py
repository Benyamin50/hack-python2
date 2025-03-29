"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

def fn_hack_10(s):
    result = []
    secuencia = 1 
    
    for elementos in s:
        if isinstance(elementos, dict):
        
            diccionario = {}
            for key, value in elementos.items():
                diccionario[str(secuencia)] = str(secuencia + 1)
                secuencia += 2  
            result.append(diccionario)
        elif isinstance(elementos, set):
        
            reemplazo = set()
            for _ in elementos:
                reemplazo.add(str(secuencia))
                secuencia += 1  
            result.append(reemplazo)
    return result