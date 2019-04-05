# Léxicos

## Histórico de Revisão
| Data       | Responsável                                            | Versão | Mudança realizada |
| ---------- | ------------------------------------------------------ | ------ | ----------------- |
| 31/03/2019 | Byron Kamal, Igor Veludo, João Pedro e William Almeida |  0.1   | Adicionando tópicos 1, 2 e 3 |

## Sumário

1. [Introdução](#1introdução)
2. [Objetivo](#2objetivo)
3. [Metodologia](#3metodologia)
4. [Léxicos](#léxicos)
5. [Resultado](#5resultado)

## 1.Introdução

O propósito da produção deste artefato é aplicar mais uma vez a modelagem de requisitos. Este modelo auxilia no entendimento e simplificação da compreensão do contexto do Discord pois pega termos específicos, os define e mostra onde são utilizados e quando podem ocorrer, trazendo uma familiarização com o escopo do Discord.

## 2.Objetivo

O objetivo deste artefato é trazer uma visão mais clara sobre termos específicos que permeiam o domínio do Discord. Eles se dividem em 3 tipos: verbo, objeto e estado. Cada um deles com um significado e aplicação descritos a seguir.

## 3.Metodologia

O grupo se reuniu e utilizou termos já levantados em artefatos passados, levantou novos termos que julgamos importantes para compreensão do domínio do Discord e então separamos os termos entre os integrantes e os cadastramos na ferramenta C&L. Cada léxico se mostrou bastante importante uma vez que linkados em suas aparições, revelaram mais uma vez sua ocorrência dentro do domínio.

## 4.Léxicos
| ------- | ------ |
|**Nome**| **Usuário** |
|**Classificação**| Sujeito |
|**Sinônimo**| Usuários  |
|**Noção**| Ator principal do UnBind.  Possui conta e acessa o UnBind para utilizar serviços como atividades e conversa com profissionais. |
|**Impacto**| O usuário utiliza registra atividades<br>O usuário solicita ajuda profissional;<br> O usuário cumpre os desafios propostos. |

|         |        |
| ------- | ------ |
|**Nome**| **ChatBot** |
|**Classificação**| Objeto |
|**Sinônimo**| Bot |
|**Noção**|  Software externo com comportamento específico no UnBind; Indicando artigos de interesse e enviando notificações ao usuário; |
|**Impacto**| O Bot envia artigos ao usuário;<br>O Bot notifica o usuário quando há atividades semanais e mudanças no status; |

|         |        |
| ------- | ------ |
|**Nome**| **Mensagem** |
|**Classificação**| Objeto |
|**Sinônimo**| direct messenger, conversa, chat |
|**Noção**| Forma pela qual o usuário interage com outras pessoas / bot. |
|**Impacto**| o usuário tem conversa privada chatbot;<br>O usuário tem conversa privada com profissional. |

|         |        |
| ------- | ------ |
|**Nome**| **Notificação** |
|**Classificação**| Objeto |
|**Sinônimo**| Aviso |
|**Noção**| Alerta sobre atualizações nas atividades ou no chatbot. |
|**Impacto**| O UnBind avisa quando chega mensagem;<br>O UnBind avisa quando há progresso no nível; |

|         |        |
| ------- | ------ |
|**Nome**| **Avatar** |
|**Classificação**| Objeto  |
|**Sinônimo**| Imagem de perfil |
|**Noção**| Imagem que representa o usuário  |
|**Impacto**| O usuário muda de avatar|

|         |        |
| ------- | ------ |
|**Nome**| **Logar** |
|**Classificação**| Verbo |
|**Sinônimo**| entrar, fazer login, sign in |
|**Noção**| O usuário passa a ter o estado “logado”; |
|**Impacto**| O usuário passa a ter o estado “logado”;
O usuário logado utiliza as funcionalidades do UnBind sem perder as informações após encerrar a sessão. |

|         |        |
| ------- | ------ |
|**Nome**| **Cadastrar** |
|**Classificação**| Verbo |
|**Sinônimo**| registrar, criar conta |
|**Noção**| Criar conta para acesso ao UnBind. |
|**Impacto**| O usuário que se cadastra, acessa sua conta;
O usuário passa a ter o estado “cadastrado”;
As informações do usuário ficam salvas. |

|         |        |
| ------- | ------ |
|**Nome**| **Editar Perfil** |
|**Classificação**| Verbo |
|**Sinônimo**| Redefinir perfil |
|**Noção**| Pode mudar informações do perfil do usuário. |
|**Impacto**| Usuário pode editar avatar
	    Usuário pode editar nome
	    Usuário pode editar email
                Usuário pode editar senha |

|         |        |
| ------- | ------ |
|**Nome**| **Histórico** |
|**Classificação**| Objeto |
|**Sinônimo**| Registro, documento |
|**Noção**| Lista com atividades realizadas pelo usuário. |
|**Impacto**| Atividade é inserida no histórico.
	    Usuário consulta o histórico. |

|         |        |
| ------- | ------ |
|**Nome**| **Nível** |
|**Classificação**| Objeto |
|**Sinônimo**| status bar, barra de status, progresso. |
|**Noção**| Indica o desempenho do usuário e desbloqueia recompensas. |
|**Impacto**| Usuário sobe de nível;
	    Usuário progride na aplicação |

|         |        |
| ------- | ------ |
|**Nome**| **Atividade** |
|**Classificação**| Objeto |
|**Sinônimo**| tarefa |
|**Noção**| Atividade gerada pela aplicação para o usuário. |
|**Impacto**| Usuário realiza atividade;
	    Usuário pede nova atividade;
	    Usuário troca de atividade. |

|         |        |
| ------- | ------ |
|**Nome**| **Pontuação** |
|**Classificação**| objeto |
|**Sinônimo**| pontos, contagem, score. |
|**Noção**| Medida de progresso dada aos usuários após completar atividades. |
|**Impacto**| Usuário recebe pontuação ao completar atividades.
	    Usuário transforma pontuação em prêmios. |

|         |        |
| ------- | ------ |
|**Nome**| **Ajuda** |
|**Classificação**| objeto |
|**Sinônimo**| Auxílio, suporte, assistência. |
|**Noção**| Meio onde ocorre interação do usuário com o suporte da aplicação. |
|**Impacto**| Usuário possui dificuldades em mexer na aplicação;
	   Usuário pode acessar o guia da aplicação. |

|         |        |
| ------- | ------ |
|**Nome**| **Desafio Semanal** |
|**Classificação**| objeto |
|**Sinônimo**|  |
|**Noção**| Atividade em grupo que é oferecida semanalmente que oferece maior pontuação. |
|**Impacto**| Usuário recebe desafio semanal.
	    Usuário completa desafio semanal. |

|         |        |
| ------- | ------ |
|**Nome**| **Menu** |
|**Classificação**| objeto |
|**Sinônimo**| Sidebar, menu lateral. |
|**Noção**| Aba na aplicação que pode ser acessada com um clique do mouse. |
|**Impacto**| Usuário deseja ver o seu progresso na aplicação.
	    Usuário visualiza histórico pelo menu;
	    Usuário visualiza ajuda; |

|         |        |
| ------- | ------ |
|**Nome**| **Artigos de interesse** |
|**Classificação**| objeto |
|**Sinônimo**| texto de interesse |
|**Noção**| Textos enviados pelo chatbot para o usuário com base nos interesses do mesmo. |
|**Impacto**| ChatBot envia artigo de interesse.
	    Usuário recebe artigo de interesse. |


## 5.Referências
<ul>
<li>Discord - Requisitos de Software.
Disponível em: <https://github.com/Discord-Requisitos-2018-2/Discord/wiki/L%C3%A9xico> </li>
</ul>
