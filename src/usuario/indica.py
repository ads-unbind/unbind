from categoria.models import Categoria
from artigo.models import Artigo
from questionario.models import Registro

def suggest_articles(user):
        """
        Calcula a pontuação do usuário em todos os questionários realizados e identifica a categoria ideal do usuário.
        A partir desta categoria, são indicados artigos relacionados.
        :return: lista de artigos relacionados.
        """
        categorias = Categoria.objects.all()
        pontuacao_categorias = {}

        # Cria um dicionário com todas as categorias como chave e iniciadas com valor 0
        for categoria in categorias:
            pontuacao_categorias[categoria.nome] = 0

        # Itera sobre todos os questionários, sobre todas as perguntas, somando a pontuação de cada uma na categoria correta
        for questionario in user.usuario.questionario.all():
            print('ENTROU MANO')
            for pergunta in questionario.perguntas.all():
                print('ENTROU no questionario MANO')
                resposta = Registro.objects.filter(usuario=user, pergunta=pergunta)[0]
                pontuacao_categorias[pergunta.categoria.nome] += resposta.pontos  # Somando na categoria correta
        print(pontuacao_categorias)
        pontuacao_max_categoria = max(pontuacao_categorias, key=pontuacao_categorias.get)
        print(pontuacao_max_categoria)  # categoria com a maior pontuação deste usuário

        categoria_ideal = Categoria.objects.get(nome=pontuacao_max_categoria)  # Busca a categoria ideal a partir do nome
        artigos = Artigo.objects.filter(categoria=categoria_ideal).all()  # Busca todos os artigos relacionados a categoria ideal

        return artigos
