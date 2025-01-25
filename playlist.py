# SUPERCLASSE
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()  # Atributo protegido: Nome do programa formatado com a primeira letra maiúscula
        self.ano = ano  # Ano de lançamento do programa
        self._likes = 0  # Atributo protegido: Inicia com 0 likes

    @property
    def likes(self):
        """Retorna o número de likes do programa."""
        return self._likes

    def dar_like(self):
        """Incrementa o número de likes em 1."""
        self._likes += 1

    @property
    def nome(self):
        """Retorna o nome do programa."""
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        """Atualiza o nome do programa com a primeira letra maiúscula."""
        self._nome = novo_nome.title()

    def __str__(self):
        """Retorna uma representação em string do programa."""
        return f"{self._nome} - {self.ano} - {self._likes} Likes"


# SUBCLASSE
class Filme(Programa):  # Herda os atributos e métodos da superclasse Programa
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # Inicializa os atributos da superclasse
        self.duracao = duracao  # Duração do filme em minutos

    def __str__(self):
        """Retorna uma representação em string do filme, incluindo sua duração."""
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"


# SUBCLASSE
class Serie(Programa):  # Herda os atributos e métodos da superclasse Programa
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)  # Inicializa os atributos da superclasse
        self.temporadas = temporadas  # Quantidade de temporadas da série

    def __str__(self):
        """Retorna uma representação em string da série, incluindo suas temporadas."""
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"


# CLASSE COMPOSIÇÃO
class Playlist:
    def __init__(self, nome_playlist, programas):
        """Inicializa a playlist com um nome e uma lista de programas (filmes ou séries)."""
        self.nome_playlist = nome_playlist
        self._programas = programas  # Lista que armazena os programas (objetos das subclasses Filme e Serie)

    def __getitem__(self, item):
        """Permite acessar os programas da playlist como uma lista normal."""
        return self._programas[item]

    @property
    def listagem(self):
        """Retorna todos os programas da playlist."""
        return self._programas

    @property
    def tamanho(self):
        """Retorna a quantidade de programas na playlist."""
        return len(self._programas)


# Instâncias(objetos) de filmes e séries
vingadores = Filme("Vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

# Adicionando likes às instâncias
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

# Lista que recebe os objetos criados a partir das classes Filme e Serie
filmes_e_series = [vingadores, atlanta, demolidor, tmep]

# Criando uma playlist com os filmes e séries
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

# Itera pela playlist e imprime os detalhes de cada programa
for programa in playlist_fim_de_semana.listagem:
    print(programa)
