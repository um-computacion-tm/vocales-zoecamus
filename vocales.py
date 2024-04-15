import unittest

def conta_voc(mi_string):
    resultado = {}
    for letra in mi_string:
        if letra in 'aeiou' :
             if letra not in resultado:
                  resultado [letra] = 0
             resultado[letra]  += 1
        if letra in 'AEIOU' :
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] +=1
        if letra in 'áéíóú' :
            if letra not in resultado :
                resultado[letra] = 0
            resultado[letra] +=1
        if letra in 'ÁÉÍÓÚ' :
            if letra not in resultado :
                resultado[letra] = 0
            resultado[letra] +=1
    return resultado

class TestVocales(unittest.TestCase):
    
    
    def test_nada0(self):
        resultado = conta_voc ('zzz')
        self.assertEqual(resultado, {})
    
    def test_nada1(self):
        resultado = conta_voc ('cas')
        self.assertEqual(resultado, {'a':1})

    def test_nada2(self):
        resultado = conta_voc ('casa')
        self.assertEqual(resultado, {'a':2})

    
    def test_nada3(self):
        resultado = conta_voc ('bese')
        self.assertEqual(resultado, {'e':2})

    
    def test_nada4(self):
        resultado = conta_voc ('mesa')
        self.assertEqual(resultado, {'a':1, 'e' :1})

    def test_nada5(self):
        resultado = conta_voc ('cAmpo')
        self.assertEqual(resultado, {'A':1, 'o' :1})

    def test_nada6(self):
        resultado = conta_voc ('llUvIA')
        self.assertEqual(resultado, {'A':1, 'U' :1, 'I' :1})
    
    def test_nada7(self):
        resultado = conta_voc ('músicA')
        self.assertEqual(resultado, {'A':1, 'ú' :1, 'i' :1})
    
    def test_nada8(self):
        resultado = conta_voc ('ÁrbOl')
        self.assertEqual(resultado, {'Á':1, 'O' :1})
    

#unittest.main()

while(True):
    palabra = input('Ingrese una palabra: ')
    print(conta_voc(palabra))

