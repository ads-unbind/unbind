<h1>Modelagem do Sistema</h1>

| Data       | Responsável      | Versão | Mudança realizada                      |
| ---------- | ---------------- | ------ | -------------------------------------- |
| 11/05/2019 | Geovanne Saraiva, Igor Aragão e Willian | 0.1 | Adição do ME-R |

#### Modelo Entidade-Relacionamento (ME-R)
### Entidades:
* ADMINISTRADOR
* USUARIO
* CONQUISTA
* CATEGORIA
* QUESTIONARIO
* PERGUNTA
* ARTIGO
* ATIVIDADE

### Atributos:
* ADMINISTRADOR (id, email, senha)
* USUARIO (id, nome, email, senha, foto, scoreTotal)
* CONQUISTA (id, nome, descricao, foiConquistado, pontos)
* CATEGORIA (id, nome, score)
* QUESTIONARIO (id, dataResposta, estado)
* PERGUNTA (id, categoria, enunciado, pontos)
* ARTIGO (id, titulo, categoria, texto, imagem, autor, curtidas, dataPublicacao)
* ATIVIDADE (id, titulo, categoria, descricao, dicas, estado, pontos)

#### Relacionamentos:
* USUARIO - executa - ATIVIDADE  
Um USUARIO pode executar uma ou até 3 atividades ao mesmo tempo, e uma ATIVIDADE pode ser executada por um ou mais usuários.  
Cardinalidade: n:m
* USUARIO - desbloqueia - CONQUISTA  
Um USUARIO pode desbloquear uma ou mais conquistas, e uma CONQUISTA pode ser desbloqueada por um ou mais usuários.  
Cardinalidade: n:m
* USUARIO - responde - QUESTIONARIO  
Um USUARIO pode responder um ou mais questionários, e um QUESTIONARIO pode ser respondido por um usuário.  
Cardinalidade: 1:n
* USUARIO - lê - ARTIGO  
Um USUARIO pode ler um ou mais artigos, e um ARTIGO pode ser lido por um ou mais usuários.  
Cardinalidade: n:m
* QUESTIONARIO - tem - PERGUNTA  
Um QUESTIONARIO pode ter uma ou mais perguntas, e uma PERGUNTA pode pertencer a um ou mais questionários.  
Cardinalidade: n:m
* QUESTIONARIO - pontua - CATEGORIA  
Um QUESTIONARIO pode pontuar uma ou mais categorias, e uma CATEGORIA pode ser pontuada por um questionário por vez.  
Cardinalidade: 1:n
