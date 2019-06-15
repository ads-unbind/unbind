Data       | Versão | Descrição            | Responsáveis
---------- | ------ | -------------------- | -------------------------------------------------------------------------------------------------------
15/06/2019 | 0.1    | Criação do documento | Byron Kamal, Geovanne Saraiva, Igor Aragão, Igor Veludo, João Pedro Mota, William Almeida, José Aquiles

## Introdução

### Finalidade

Este documento tem como finalidade apresentar a arquitetura do projeto UnBind através de visões diversas para registrar as decisões arquiteturais relacionadas ao projeto. O documento é dividido da seguinte maneira: inicialmente é apresentada a representação da arquitetura da solução, em seguida as metas e restrições desta arquitetura e por fim são apresentadas visões sobre elementos da arquitetura.

### Escopo

Este documento apresenta as características arquiteturais do projeto UnBind, descrevendo em detalhes a soluções arquiteturais determinadas para o projeto, de forma a servir como base para o desenvolvimento do projeto pelos desenvolvedores de software alocados para o projeto.

### Visão Geral

Este documento está organizado da seguinte forma:

- Representação da Arquitetura
- Metas e Restrições de Arquitetura
- Visão de Casos de Uso

## Representação da Arquitetura

O sistema faz uso do Framework Django, que faz uso do padrão MVC. No entanto, tal plataforma possui uma interpretação singular em relação à organização de camadas. O indicado é considerar que a própria plataforma faz o papel da camada de controle, enquanto a camada de Modelo e de Visão devem ser adaptadas e reinterpretadas conforme o necessário. Por este motivo, ainda que o Django implemente o MVC, considera-se que o padrão de camadas externalizado pela plataforma é o MTV (_Model-Template-View_). A utilização de uma arquitetura em camadas é interessante por proporcionar uma clara separação de responsabilidades no código, proporcionando reusabilidade, e reduzindo o esforço de manutenção. Os conceitos de MVC e MTV sero apresentados nas sessões seguintes.

### Model View Controller(MVC)

- **Model**: camada de acesso a base de dados, é responsável pela leitura e escrita de dados, bem como de suas validações;

- **View**: camada de apresentação das informações, é responsável pela interação com o usuário;<br>

- **Controller**: camada responsável pelas as regras de negócios do sistema, é responsável por receber e processar as requisições do usuário, controlando o fluxo de informações entre as demais camadas. A imagem a seguir apresenta as interações entre as camadas: ![](https://pbs.twimg.com/media/Dst5pXcWsAAGdoo.jpg)

### Model Template View(MTV)

- **Model**: segue a mesma definição da model no MVC;
- **Template**: segue a mesma definição da view no MVC;
- **View**: segue a mesma definição da controller no MVC.
- **Forms**: a camada de Forms não faz parte do MTV, mas é uma forma de agrupar todas as classes usadas para descrever os formulários utilizados na aplicação. Se comunica diretamente com a modelo, de forma a mapear os atributos das entidades, e com a View, para refletir o mesmo mapeamento na camada de Template.

A imagem a seguir apresenta as interações entre as camadas: ![](https://lh3.googleusercontent.com/zOYc6WV5t4NwvWMxQiXzPt40fUa28BmWKgiAQ0ZOdQe7ZxGo_36NE-mOFVViDpMVlcUq7B1ffjl2KezDiaKfEg8D1NILqySCYZFJG3ALP5_Gycf_6rTO4920DkFsTJj0vOyf9qr2) _Figura 1\. Padrão arquitetural MTV._

## Metas e Restrições de Arquitetura

As metas e restrições do projeto que possuem influência significativa na arquitetura são:

- Todas as restrições e faixas de qualidade estipuladas no [Documento de Visão](./Documento-de-Visão.md) devem ser levadas em consideração. ## Visão de Casos de Uso + Os casos de uso do sistema são listados abaixo: + Cadastrar usuário + Cadastrar produto + Cadastrar comércio + Cadastrar preço + Ver detalhes do produto + Pesquisar produtos + Gerenciar lista de compras + Denunciar item + Gerenciar denúncias + Deletar itens + Realizar login + Realizar logout O diagrama abaixo descreve os casos de uso no sistema: ![](https://lh5.googleusercontent.com/Un0ilv1HnT1ovPZlZj882cZOBuhAdijGvS9ZSPjZZddAXhyzFxy1gcKG2FVLusd9YBPBbabdxsXyhhU-if6mfay7ItDaL_d5clWBda3pfyzEVxqSfvoKaraqNQ2z2rvEcd849VjM) _Figura 2\. Diagrama de Casos de Uso._

## Visão Lógica ARAGONES E WILLIAM

Esta seção detalha a visualização lógica da arquitetura, descrevendo as classes e pacotes mais significativos.

### Visão Geral

A visualização lógica do sistema EconomizAqui é composta de 3 pacotes principais, sendo eles:

- **Usuários**: contém as classes de models, forms e services, bem como os templates e regras de negócios relacionados às funcionalidades de usuários.

- **Produtos**: contém as classes de models, forms e services, bem como os templates e regras de negócios relacionados às funcionalidades de produtos.

- **Mercados**: contém as classes de models, forms e services, bem como os templates e regras de negócios relacionados às funcionalidades de mercados.

### Visão de Modelos

[![](https://lh4.googleusercontent.com/44vcEzxm1hpR6C8zJxLWDUmUdM_5U1IO9aGqGSQUsyB16S_KB5b32I-QfgM1ZokPX4cB682skiQnG7V1P9bzILjm5cP53WfSMHvonC6HsWZMuzTMcsddEn92FuGBxXcPp5Cmxxwz)](https://lh4.googleusercontent.com/44vcEzxm1hpR6C8zJxLWDUmUdM_5U1IO9aGqGSQUsyB16S_KB5b32I-QfgM1ZokPX4cB682skiQnG7V1P9bzILjm5cP53WfSMHvonC6HsWZMuzTMcsddEn92FuGBxXcPp5Cmxxwz) _Figura 3\. Diagrama UML das Models utilizadas no projeto._

### Visão de dados

### Visão de Implementação (Byron e Igor Veludo)

### Visão de Processo

### (Navegabilidade, Identificação de Pontos Flexíveis)

### Identificação de Pontos Fixos

### Referências
