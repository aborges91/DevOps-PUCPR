import unittest
from unittest.mock import patch
from src.hello import gerar_numero_secreto, verificar_palpite, jogo_adivinhar_numero  

class TestJogoAdivinhaNumero(unittest.TestCase):

    def test_gerar_numero_secreto(self):
        numero = gerar_numero_secreto()
        self.assertGreaterEqual(numero, 1)
        self.assertLessEqual(numero, 100)

    def test_verificar_palpite(self):
        numero_secreto = 50
        self.assertEqual(verificar_palpite(numero_secreto, 30), "maior")
        self.assertEqual(verificar_palpite(numero_secreto, 70), "menor")
        self.assertEqual(verificar_palpite(numero_secreto, 50), "certo")

  
    def test_jogo_adivinhar_numero(self, mock_print, mock_input):
        with patch('src.hello.gerar_numero_secreto', return_value=50):  
            resultado = jogo_adivinhar_numero(tentativas_max=10)
            self.assertTrue(resultado)
            mock_print.assert_any_call("Parabéns! Você adivinhou o número 50 em 3 tentativas!")

if __name__ == '__main__':
    unittest.main()
