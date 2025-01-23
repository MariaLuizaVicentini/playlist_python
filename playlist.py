# Criando classe generica(Superclasse)
class Programa: # Classe Mãe
    
    # Definindo quais serão os atributos (características) da classe mãe
    def __init__(self, nome, ano):
        self._nome = nome.title() 
        self.ano = ano
        self._likes = 0 # Atributo opcional: ao criar uma instância dessa classe, não é necessário atribuir valor a este atributo. 

    # Definindo o método propriedade: Obter likes
    @property
    def likes(self):
        return self._likes # Retorna o valor atual do atributo "likes"

    # Definindo método da instância: Modifica o valor do atributo "self._likes"
    def dar_like(self):
        self._likes += 1 # Incrementa (adiciona) o valor do atributo "likes" em 1 sempre que é chamado.

    # Definindo o método propriedade: Obter nome
    @property
    def nome(self):
        return self._nome # Retorna o valor atual do atributo "nome"

    # Definindo o método setter: Define um novo valor para o atributo "self._nome"
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title() # O atributo "_nome" recebe um novo nome que será formatado com a primeira letra maiúscula

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"

# Criando classe filha (subclasse)
class Filme(Programa): # A classe Programa é herdada, permitindo utilizarmos atributos e métodos dentro da classe filha
    # Definindo quais são os atributos da classe filha:
    def __init__(self, nome, ano, duracao):
        # Herdando os atributos da classe mãe através do método "super()"
        super().__init__(nome, ano) # Herdando nome e ano da classe mãe que já foram definidos
        # Definindo atributo "duração"
        self.duracao = duracao # Esse atributo não foi herdado, ele é exclusivo da classe FILME

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"

# Criando classe filha (subclasse)
class Serie(Programa): # A classe Programa é herdada, permitindo utilizarmos atributos e métodos dentro da classe filha
    # Inicializando os atributos da classe filha
    def __init__(self, nome, ano, temporadas):
        # Herdando atributos da classe mãe
        super().__init__(nome, ano) 
        # Definindo o atributo "temporadas"
        self.temporadas = temporadas # Esse atributo não foi herdado, ele é exclusivo da classe SERIE

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome 
        super().__init__(programas)

# Criando uma instância a partir da classe "Filme"
vingadores = Filme("Vingadores - guerra infinita", 2018, 160) # Argumentos que serão atribuídos aos atributos
# Criando uma instância a partir da classe "Serie"
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

# O objeto chama a função que permite dar likes
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

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana: 
    print(programa)

