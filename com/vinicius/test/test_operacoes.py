from unittest import TestCase
from com.vinicius.operacoes import TesteAC04

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = TesteAC04()

    
    def test_multiplicacao(self):
        self.assertEqual(self.operacoes.multiplicacao([5,8]), 40)