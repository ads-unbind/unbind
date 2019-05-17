<h1>Modelagem do Sistema</h1>

| Data       | Responsável      | Versão | Mudança realizada                      |
| ---------- | ---------------- | ------ | -------------------------------------- |
| 11/05/2019 | Geovanne Saraiva, Igor Aragão e Willian | 0.1 | Adição do ME-R |
| 12/05/2019 | Geovanne Saraiva e Vinícius | 0.2 | Correção do ME-R e adição do DE-R |

## Modelo Entidade-Relacionamento (ME-R)
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
* ADMINISTRADOR (idAdmin, email, senha)
* USUARIO (idUsuario, nome, email, senha, foto)
* CONQUISTA (idConquista, nome, descricao, foiConquistado, pontos, idAdmin)
* CATEGORIA (idCategoria, nome, idAdmin)
* QUESTIONARIO (idQuestionario, nome, dataResposta, estado, idAdmin)
* PERGUNTA (idPergunta, enunciado, pontos, idQuestionario, idCategoria, idAdmin)
* ARTIGO (idArtigo, titulo, texto, imagem, autor, curtidas, dataPublicacao, idCategoria, idAdmin)
* ATIVIDADE (idAtividade, titulo, descricao, dicas, estado, pontos, idCategoria, idAdmin)

### Relacionamento
* USUARIO - executa - ATIVIDADE  
Um USUARIO pode executar uma ou até 3 ATIVIDADE ao mesmo tempo, e uma ATIVIDADE pode ser executada por um ou mais USUARIO.  
Cardinalidade: n:m

* USUARIO - desbloqueia - CONQUISTA  
Um USUARIO pode desbloquear uma ou mais CONQUISTA, e uma CONQUISTA pode ser desbloqueada por um ou mais USUARIO.  
Cardinalidade: n:m

* USUARIO - responde - QUESTIONARIO  
Um USUARIO pode responder um ou mais QUESTIONARIO, e um QUESTIONARIO pode ser respondido por um USUARIO.  
Cardinalidade: n:m

* USUARIO - lê - ARTIGO  
Um USUARIO pode ler um ou mais ARTIGO, e um ARTIGO pode ser lido por um ou mais USUARIO.  
Cardinalidade: n:m

* QUESTIONARIO - tem - PERGUNTA  
Um QUESTIONARIO pode ter uma ou mais PERGUNTA, mas uma PERGUNTA só pode pertencer a um QUESTIONARIO.  
Cardinalidade: 1:n

* QUESTIONARIO - pontua - CATEGORIA  
Um QUESTIONARIO pode pontuar uma CATEGORIA, e uma CATEGORIA pode ser pontuada por um QUESTIONARIO por vez.  
Cardinalidade: 1:1

* ADMINISTRADOR - cria - CONQUISTA  
Um ADMINISTRADOR cria várias CONQUISTA, mas uma CONQUISTA só é criada por um ADMINISTRADOR.  
Cardinalidade: 1:n

* ADMINISTRADOR - cadastra - CATEGORIA  
Um ADMINISTRADOR cadastra várias CATEGORIA, mas uma CATEGORIA só é cadastrada por um ADMINISTRADOR.  
Cardinalidade: 1:n

* ADMINISTRADOR - cria - QUESTIONARIO  
Um ADMINISTRADOR cria vários QUESTIONARIO, mas um QUESTIONARIO só é criada por um ADMINISTRADOR.  
Cardinalidade: 1:n

* ADMINISTRADOR - adiciona - PERGUNTA  
Um ADMINISTRADOR adiciona várias PERGUNTA, mas uma PERGUNTA só é acionada por um ADMINISTRADOR.  
Cardinalidade: 1:n

* ADMINISTRADOR - adiciona - ARTIGO  
Um ADMINISTRADOR adiciona vários ARTIGO, mas uma ARTIGO só é adicionado por um ADMINISTRADOR.  
Cardinalidade: 1:n

* ADMINISTRADOR - cria - ATIVIDADE  
Um ADMINISTRADOR cria várias ATIVIDADES, mas uma ATIVIDADE só é criada por um ADMINISTRADOR.  
Cardinalidade: 1:n

* CATEGORIA - tem - ATIVIDADE  
Uma CATEGORIA tem várias ATIVIDADE, mas uma ATIVIDADE só pode ser de uma ATIVIDADES.  
Cardinalidade: 1:n

* CATEGORIA - tem - ARTIGO  
Uma CATEGORIA tem várias ARTIGO, mas uma ARTIGO só pode ser de uma ATIVIDADES.  
Cardinalidade: 1:n

* PERGUNTA - tem - CATEGORIA  
Uma CATEGORIA pode ser possuído por várias perguntas  
Cardinalidade: 1:n

## Diagrama Entidade-Relacionamento (DE-R)
![](modelagem_do_sistema/der_v01.jpg)
