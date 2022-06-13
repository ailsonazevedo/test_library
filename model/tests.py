from unittest import TestCase
from dominio import Biblioteca, Livro, Funcionario, Usuario, Emprestimo

class TestBiblioteca(TestCase):
    #verificar livro ja emprestado
    def test_verificar_livro_ja_emprestado(self):
        livro1 = Livro(1, 'livro1')
        empresto1 = Emprestimo(Usuario('usuario1', '06532785350'), livro1)

        livro2 = Livro(2, 'livro2')
        empresto2 = Emprestimo(Usuario('usuario2', '12332785370'), livro2)

        biblioteca = Biblioteca()
        biblioteca.livros = [livro1, livro2]
        biblioteca.emprestimos = [empresto1, empresto2]

        self.assertEqual(biblioteca.verificarLivroEmprestado(livro1), True)

    #buscar livro nao cadastrado na biblioteca
    def test_busca_livro_nao_cadastrado(self):
        livro1 = Livro(1, 'livro1')
        livro2 = Livro(2, 'livro2')
        livro3 = Livro(3, 'livro3')

        biblioteca = Biblioteca()
        biblioteca.livros = [livro1, livro2]

        self.assertEqual(biblioteca.buscarLivro(3), "Livro nao cadastrado")

    #devolver um livro nao emprestado
    def test_devolver_livro_nao_emprestado(self):
        livro1 = Livro(1, 'livro1')
        livro2 = Livro(2, 'livro2')
        livro3 = Livro(3, 'livro3')

        biblioteca = Biblioteca()
        biblioteca.livros = [livro1, livro2, livro3]
        usuario1 = Usuario('usuario1', '14000000002')
        livros_usuario1 = [livro1, livro2]

        funcionario1 = Funcionario('funcionario1', '56700000040')
        biblioteca.funcionarios = [funcionario1]
        biblioteca.realizarEmprestimo(funcionario1, livros_usuario1, usuario1)

        self.assertEqual(biblioteca.verificarLivroEmprestado(livro3), False)

    #limitar usuario de pegar no maximo 3 livros
    def test_limitar_usuario_de_pegar_no_maximo_3_livros(self):
        livro1 = Livro(1, 'livro1')
        livro2 = Livro(2, 'livro2')
        livro3 = Livro(3, 'livro3')
        livro4 = Livro(4, 'livro4')
        livro5 = Livro(5, 'livro5')
        livro6 = Livro(6, 'livro6')

        usuario1 = Usuario('usuario1', '14000000002')
        usuario2 = Usuario('usuario2', '08691600004')

        biblioteca = Biblioteca()
        biblioteca.livros = [livro1, livro2, livro3, livro4, livro5, livro6]
        biblioteca.usuarios = [usuario1, usuario2]

        livros_usuario1 = [livro1, livro2]
        livros_usuario2 = [livro3, livro4, livro5, livro6]

        self.assertEqual(biblioteca.verificarLimiteUsuario(usuario1,livros_usuario1,), True)
        self.assertEqual(biblioteca.verificarLimiteUsuario(usuario2, livros_usuario2), False)

    #solicitar emprestimo com funcionario invalido
    def test_solicitar_emprestimo_com_funcionario_invalido(self):
        livro1 = Livro(1, 'livro1')
        usuario1 = Usuario('usuario1', '14000000002')
        funcionario1 = Funcionario('funcionario1', '12300000003')

        biblioteca = Biblioteca()
        biblioteca.livros = [livro1]

        self.assertEqual(biblioteca.realizarEmprestimo(funcionario1, livro1, usuario1),'Funcionario invalido')
