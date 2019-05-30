# Documento de Visão
### Histórico de revisão
Data | Versão | Descrição | Autor |
--------- | ------ | ------------ | --------- |
04/04/2019 | 0.1 | Abertura do documento | José Aquiles |
05/04/2019 | 0.1.1 | Atualização do nome do produto | Vinícius Cantuária |
05/04/2019 | 0.2 | Refatoração do documento | Igor Aragão |

## 1. Introdução
Nesta introdução serão abordados tópicos referentes a uma visão geral do produto, definindo seu propósito, escopo, definições, acrônimos, abreviações e referências.

### 1.1 Propósito
Esse documento visa especificar todo o escopo de funcionamento do UNBIND, deixando claro seu objetivo, a razão de sua necessidade e a forma como busca solucionar os problemas aos quais se propõe, deixando claro possíveis restrições. Dessa forma, sua principal utilidade objetiva também, ao esclarecer o que é o sistema para os desenvolvedores, clientes e usuários, estabelecer entre os mesmos um eficiente alinhamento de ideias.

### 1.2 Escopo
Suprir a necessidade de um sistema web para acompanhamento de saúde mental de indivíduos ou grupos de usuários cujas capacidades abrangem funcionalidades como:
* Monitorar score de saúde mental
* Sugerir artigos relacionados à saúde mental
* Sugerir atividades cotidianas, que colaboram pra saúde mental

### 1.3 Definições, acrônimos e abreviações

| **Abreviação** | **Definição** |
| :--------: | :-------: |
| FGA | Faculdade do Gama |
| UnB | Universidade de Brasília |

### 1.4 Referências

ACHOR, Shawn. **O jeito Harvard de ser feliz**. São Paulo: Saraiva, 2010.

### 1.5 Visão Geral
A organização do documento é feita de maneira a prover ao leitor a capacidade de através do mesmo entender o produto em seus vários aspectos de forma coesa. Para tal, são apresentados primeiramente os tópicos referentes a função geral do software e as motivações que levaram a sua criação, após isso, é descrito o posicionamento do produto em relação ao mercado e as partes interessadas, incluindo a forma como a criação do sistema afetará os usuários. Por fim, são descritas as principais funcionalidades do software, bem como algumas de suas restrições e requisitos.

## 2. Posicionamento

### 2.1 Oportunidade de Negócios
Nos tempos atuais, a felicidade é considerada um valor tão precioso e indiscutível que, como um exemplo emblemático, podemos citar a Declaração de Independência dos EUA, que registra que “todo homem tem o direito inalienável à vida, à liberdade e à busca da felicidade” (Lunt, 2004).
A literatura aponta que tanto para nações quanto para indivíduos, superado um limiar de subsistência com dignidade (incluindo comida, água e saneamento básico), o aumento do poder aquisitivo não se correlaciona com um incremento significativo nos níveis de felicidade (Csikszentmihalyi, 1999; Veenhoven, 1991).

### 2.2 Instrução do Problema
|  | |
| :--------: | :-------: |
| **Problema**| Indices de depressão e comportamento autodestrutivo vem crescendo nos ultimos anos |
| **Funções afetadas** | Pessoas acabam por se refugiar em redes sociais |
| **Efeito** | Pioram o problema, pois redes sociais podem ser um lugar muito tóxico para a saúde mental |
| **Solução** | Uma plataforma web que não siga o mesmo exemplo das redes sociais que contribuem para o problema |

### 2.3 Instrução de Posição do produto
|  |  |
| :--: | :--: |
| **Público Alvo** | Cidadãos que usam internet e tem interesse em psicologia positiva |
| **Carência** | Necessidade de um melhor acesso, e ferramentas de manejo, a informações relacionadas ao comércio exterior de bens e serviço no Brasil |
| **Solução** | UNBIND |
| **Descrição da Solução** | Uma plataforma web que que instiga o usuário a cumprir metas, para que ele esteja um passo mais próximo de alcançar a felicidade e talvez ajude outras pessoas a alcançarem o mesmo objetivo |
| **Diferenciais** | As metas serão disponibilizadas em cartões para que o usuário tenha o controle do que tem para fazer, e o que já foi feito. Acesso à um histórico de evolução da saúde mental do mesmo  |

## 3. Descrição dos Envolvidos e dos Usuários

### 3.2 Descrição dos Usuários   
|  |  |
| :--------: | :-------: |
| **Representantes** | Pessoas que buscam por ajuda |
| **Descrição** | Indivíduos que estão incomodados com seu nível de saúde mental |
| **Responsabilidades** | Serem receptivos para receber ajuda e se esforçarem para sair de uma zona de conforto |
| **Critérios de Sucesso** | Realizar as atividades propostas, que as fazem bem, contribuindo para o aumento do score de saúde mental |

### 3.3 Ambiente do Usuário
O acesso aos serviços do software poderá ser feito por navegadores de internet, como:
* Google Chrome;
* Mozila Firefox;

### 3.4 Principais necessidades dos usuários ou envolvidos
| **Necessidade** | **Prioridade** |
| :-------: | :-------: |
| Sugestão de atividades que ajudem na saúde mental | Alta | 
| Sugestão de artigos que ajudem na saúde mental | Alta |

## 4. Visão Geral do Produto

### 4.1 Perspectiva do produto
Para montarmos a lógica de como nosso site irá funcionar, foi feita uma pesquisa em artigos científicos que abordaram o assunto felicidade. A felicidade é uma emoção básica caracterizada por um estado emocional positivo, com sentimentos de bem-estar e de prazer, associados à percepção de sucesso e à compreensão coerente e lúcida do mundo (por isso a importância do usuário colocar as áreas de interesse para que o site explore as atividades que darão prazer, por meio de feedbacks de incentivo e desafios esporádicos).

## 5. Recursos do Produto
* Perfil de usuário contendo seu score e pontos, que permitirão o desbloqueio de novas atividades.
* Atividades com pontuações variadas.
* Artigos elaborados por profissionais da área, voltados à saúde mental.

## 6. Restrições

### 6.1 Restrições de implementação
O sistema deverá ser implementado na linguagem Python, construindo uma aplicação web com o uso do framework Django.

### 6.2 Restrições externas
Dentre as restrições externas as que mais irão influenciar são a inexperiência com a linguagem e frameworks, além de possíveis transtornos entre a equipe de desenvolvimento.

### 6.3 Restrições de design
O sistema deve ter uma interface que seja de fácil uso para pessoas. Dessa forma, será necessária uma plataforma intuitiva, com ícones e botões de fácil pesquisa e acesso. O sistema deve evitar possuir expressões negativas na aplicação, visto que é um site que trabalha com saúde mental.

## 7. Faixas de Qualidade
Para maior eficiência, a aplicação será web, pois o gerenciamento de dados e informações seria dificultado no caso de uma aplicação exclusiva para aparelhos mobile.

## 8. Requisitos do Produto
### 8.1 Requisitos do Sistema
O sistema poderá ser acessado pelo usuário através de um navegador, tendo a necessidade de conexão com a internet.

### 8.2 Requisitos de Design
O sistema deverá ser intuitivo e autoexplicativo, possibilitando uma fácil interação com o usuário. O sistema deve ser gamificado para prender a atenção do usuário.

### 8.3 Requisitos de Portabilidade
O sistema é utilizável através da maior parte dos navegadores web atuais, sendo compatível com os principais sistemas operacionais como Windows, Mac OS e Linux.

### 8.4 Requisitos de Confiabilidade
O sistema deve se comprometer respeitar a privacidade de cada usuário no que for de seu interesse em ser preservada.
