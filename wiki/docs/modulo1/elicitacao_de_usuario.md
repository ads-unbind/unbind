<h1>Elicitação de requisitos de usuário</h1>
<h3>Histórico de revisão</h3>

| Data       | Responsável      | Versão | Mudança realizada                      |
| ---------- | ---------------- | ------ | -------------------------------------- |
| 27/03/2019 | Geovanne Saraiva | 1.0    | Primeira versão do plano de elicitação |

<h3> Introdução </h3>
Este documento foi desenvolvido para a disciplina de Desenho e Arquitetura de Software, da Universidade de Brasília, no qual o grupo procura elicitar as funcionalidades do site jim care, que é obter o máximo de informações necessárias para o conhecimento de um objeto. No contexto da engenharia de software, a elicitação de requisitos provê o mais correto e completo entendimento do que é demandado de um determinado software. A análise foi dividida em tópicos, os mesmos são: usuário, site.

<h3> Objetivo </h3>
O documento presente visa definir as técnicas que serão aplicadas como forma de levantar requisitos de Usuário do site jim care, focando nos processos de elicitação: Introspecção e HistoryTelling.

<h3> Universo de informação </h3>
As informações necessárias para coleta de requisitos e para a construção de todo o trabalho foram mapeadas pelas seguintes fontes:<br />
<ul>
  <li>Pesquisa Científica:http://www.scielo.br/pdf/rpc/v34n5/a05v34n5</li>
  <li>Sites e Revistas</li>
</ul>

<h1>Plano de elicitação</h1>
Não há uma técnica padrão de elicitação de requisitos, por isso é necessário conhecer diversas técnicas e avaliar qual/quais serão mais adequadas ao projeto, facilitando o processo de elicitação. No desenvolvimento deste projeto serão utilizadas as técnicas a seguir:

<h3>History Telling</h3>
![Design](https://github.com/ads-unbind/unbind/blob/master/wiki/docs/documentacao/img/story_boarding_2.jpeg?raw=true)

<h3>Introspecção</h3>
Consiste em entender quais propriedades o sistema deve possuir para ser um sucesso, deve-se imaginar o que o usuário gostaria, se lhe tivesse dado uma respectiva tarefa, neste caso será analisado o usuário padrão(que procura um site que possa fazer ele começar a ter hábitos que melhore sua saúde mental) <br />
<h4>Relato de introspecção: comportamento de usuário sem estar logado e após login feito</h4>
<h5>Relator: Geovanne Santos</h5>
1. Cadastrar Usuário <br />
2. Acessar Perfil <br />
3. Escolher áreas de interesse <br />
4. Responder Questionário <br />
5. Gerenciar Dados de Usuário<br />
6. Excluir Conta<br />
7. Acessar Artigos Personalizados<br />
8. Selecionar Artigo<br />
9. Acessar Tarefas<br />
10. Listar tarefas concluídas e não concluídas<br />
11. Selecionar tarefas individuais<br />
12. Marcar tarefa como concluída<br />
13. Selecionar prêmio<br />
14. Trocar prêmios por pontos<br />
15. Login de admin do site<br />
16. Cadastrar admin<br />
17. Gerenciar Atividades<br />
18. Acessar categorias gerais<br />
19. Acessar Artigo<br />
20. Sair do site<br />


<h2> Moscow (priorização de requisitos)</h2>
Os requisitos listados abaixo foram obtidos a partir das técnicas de elicitação apresentadas anteriormente.

<h5>Explicação de como foi avaliado os requisitos em: must, should, could, would.</h5>
<p>
- Must: O que acontece se esse requisito não for atendido? ”Se a resposta for cancelar o projeto então deve se usar o must, não é possível entregar na data prevista sem isso, Inseguro sem isso.
</p>
<p>
- Should: Importante, mas não vital, pode ser doloroso deixar de fora, mas a solução ainda é viável.
</p>
<p>
- Could: Os requisitos rotulados como Could são desejáveis, mas não necessários, e podem melhorar a experiência do usuário ou a satisfação do cliente por um pequeno custo de desenvolvimento. Estes serão tipicamente incluídos se o tempo e os recursos permitirem..
</p>
<p>
- Would: Requisitos rotulados como Would terão que ser acordados pelas partes interessadas como os itens menos críticos e de menor retorno, ou não são apropriados naquele momento. Como resultado, os requisitos não serão planejados no cronograma do próximo timebox de entrega. Os requisitos não serão eliminados ou reconsiderados para inclusão em um timebox posterior..
</p>

| Requisitos                                                                              | Must(deve ter) | Should(deveria ter) | Could(poderia ter) | Would(seria legal ter) |
| --------------------------------------------------------------------------------------- | -------------- | ------------------- | ------------------ | ---------------------- |
| Cadastrar Usuário                                            | x              |                     |                    |                        |
| Acessar Perfil                                                        | x              |                     |                    |                        |
| Escolher áreas de interesse                                                       | x               |                    |                    |                        |
| responder questionário                                       | x               |                     |                   |                        |
| Gerenciar dados de usuário                                    |   x             |                     |                   |                        |
| Excluir conta                                                               |  x              |                    |                    |                        |
| Acessar artigos personalizados    |   x             |                    |                    |                        |
| Selecionar artigo |  x              |                     |                    |                       |
| Acessar tarefas                                                                            | x              |                     |                    |                        |
| Listar tarefas concluídas e não concluídas                                                              |                |    x                 |                   |                        |
| Selecionar tarefas individuais                                                              |                |   x                  |                   |                        |
| Marcar tarefa como concluída                                                              |                |     x                |                   |                        |
| Selecionar prêmio                                                             |                |            x         |                   |                        |
| Trocar prêmios por pontos                                                             |                |    x                 |                   |                        |
| Login de admin do site                                                              |  x              |                     |                   |                        |
| Cadastrar admin                                                              |   x             |                     |                   |                        |
| Gerenciar Atividades                                                              |                |     x                |                   |                        |
| Acessar categorias gerais                                                              |                |   x                  |                  |                        |
| Acessar Artigo                                                              |  x              |                     |                   |                        |
| Sair do site                                                             |   x             |                     |                   |                        |


8 requisitos de usuário foram elicitados neste módulo.

<h2> Bibliografia </h2>
- Anguera, Metodologia de la observación en las Ciencias Humanas, 1985. <br />
- McIntyre, John (October 20, 2016). "Moscow or Kano - how do you prioritize?
