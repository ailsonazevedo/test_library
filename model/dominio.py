class Biblioteca:
    def __init__(self):
        self.livros = []
        self.funcionario = []
        self.emprestimos = []

    def cadastrarLivro(self, livro):
        self.livros.append(livro)

    def cadastrarFuncionario(self, funcionario):
        self.funcionario.append(funcionario)

    def validarFuncionario(self, funcionario):
        for func in self.funcionario:
            if func.cpf == funcionario.cpf:
                return True
        return False

    def realizarEmprestimo(self, funcionario, livro, usuario):
        if self.validarFuncionario(funcionario):
            emprestimo = Emprestimo(usuario, livro)
            self.emprestimos.append(emprestimo)
            return "Emprestimo realizado com sucesso"
        return "Funcionario invalido"

    def realizarDevolucao(self, funcionario, livro):
        if self.validarFuncionario(funcionario):
            for emprestimo in self.emprestimos:
                if livro.id == emprestimo.livro.id:
                    self.emprestimos.remove(emprestimo)
                    return "Devolucao realizada com sucesso"
            return "Devolucao nao realizada pois o livro nao encontra-se emprestado"
        return "Funcionario invalido"

    def verificarLivroEmprestado(self, livro):
        for emprestimo in self.emprestimos:
            if livro.id == emprestimo.livro.id:
                return True
        return False

    #limitar usuario de pegar até 3 livros
    def verificarLimiteUsuario(self, usuario, livros):
        contador = 0
        for emprestimo in self.emprestimos:
            if usuario.cpf == emprestimo.usuario.cpf:
                contador += 1
        if contador + len(livros) <= 3:
            return True
        return False

    #buscarLivro
    def buscarLivro(self, id):
        for livro in self.livros:
            if livro.id == id:
                return livro
        return "Livro nao cadastrado"

class Livro:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Funcionario:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.usuario = usuario
        self.livro = livro