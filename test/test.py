import unittest
from unittest.mock import patch
import sys
import os

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.hello import gerar_numero_secreto, verificar_palpite, jogo_adivinhar_numero
  

class TestJogoAdivinhaNumero(unittest.TestCase):

    def test_gerar_numero_secreto(self):
        # Testa se o número gerado está no intervalo esperado
        for _ in range(100):  # Testa várias vezes para garantir a aleatoriedade
            numero = gerar_numero_secreto()
            self.assertGreaterEqual(numero, 1)
            self.assertLessEqual(numero, 100)

    def test_verificar_palpite_maior(self):
        # Testa a resposta quando o palpite é menor que o número secreto
        self.assertEqual(verificar_palpite(50, 30), "maior")

    def test_verificar_palpite_menor(self):
        # Testa a resposta quando o palpite é maior que o número secreto
        self.assertEqual(verificar_palpite(50, 70), "menor")

    def test_verificar_palpite_certo(self):
        # Testa a resposta quando o palpite é igual ao número secreto
        self.assertEqual(verificar_palpite(50, 50), "certo")

    @patch('builtins.input', side_effect=[30, 50])
    @patch('src.hello.gerar_numero_secreto', return_value=50)
    def test_jogo_adivinhar_numero_acerto(self, mock_numero_secreto, mock_input):
        # Testa se o jogador adivinha o número corretamente
        with patch('builtins.print') as mock_print:
            from src.hello import jogo_adivinhar_numero
            resultado = jogo_adivinhar_numero(tentativas_max=4)
            self.assertTrue(resultado)
            mock_print.assert_any_call("Parabéns! Você adivinhou o número 50 em 2 tentativas!")
  
if __name__ == '__main__':
    unittest.main()
