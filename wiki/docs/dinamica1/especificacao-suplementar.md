# Especificação Suplementar
### Histórico de revisão
Data | Versão | Descrição | Autor |
--------- | ------ | ------------ | --------- |
14/04/2019 | 0.1 | Abertura do documento | Geovanne Saraiva |
30/05/2019 | 0.2 | Refatoração de documento | Geovanne Saraiva, Willian, Vinicius |

## 1. Introdução
### 1.1 Finalidade
O objetivo deste documento de especificação suplementar é detalhar todos os aspectos não abordados diretamente nos documentos de visão, caso de uso ou arquitetura. São estes aspectos, legais e reguladores, como as normas estabelecidas para bom funcionamento do sistema, atributos de qualidade, como padrões de usabilidade, confiabilidade, desempenho e suportabilidade.

### 1.2 Escopo
Esta especificação suplementar documenta aspectos do Unbind, site que dará auxílio as pessoas que procuram um meio de incentivo na busca da felicidade, como artigos e atividades especializados para o perfil de cada usuário, e mais tarde pode haver um aumento de escopo para consultas online.

### 1.3 Visão Geral
Essa especificação define os requisitos não-funcionais do sistema, como confiabilidade, usabilidade, desempenho e suportabilidade, bem como os requisitos funcionais comuns a vários casos de uso.

## 2. Funcionalidade
Abaixo apresentamos uma lista com os requisitos funcionais,  alguns desses serão abordados nos diagramas de caso de uso.

### 2.1 Requisitos funcionais
Os requisitos funcionais, e suas prioridades, podem ser encontrados no documento [MoSCoW](moscow.md).

### 2.2 Requisitos não funcionais
|Identificador | Descrição
|--- | ---
|RNF 01|Sistema de autenticação de usuário (Segurança)
|RNF 02|Serviço de busca (Base de Dados)
|RNF 03|Telas de interação responsivas (Usabilidade)
|RNF 04|Interface simples e interativa ao usuário (Usabilidade)

### 2.3 Requisitos para plataformas específicas

Identificador | Dispositivos | Modelo | Sistema operacional
--- | --- | --- | ---
RNF 01 | Safari | Qualquer dispositivo | Versão 6 ou superior.
RNF 02 | Internet Explorer | Qualquer dispositivo | Versão 10 ou superior.
RNF 03 | Google Chrome | Qualquer dispositivo | Última versão
RNF 04 | Mozilla Firefox | Qualquer dispositivo | versão mais recente ou imediatamente anterior
RNF 05 | Opera | Qualquer dispositivo| 12 ou superior.

## 3. Usabilidade
### 3.1 Facilidade de uso
Os recursos e funcionalidades do serviço devem apresentar-se de forma intuitiva para que o usuário possa facilmente navegar por eles, não sendo necessário a realização de qualquer tipo de treinamento prévio por parte do usuário.

### 3.2 Mensagens de Erro
O serviço deve apresentar mensagens de erro de forma clara e objetiva, localizadas próximas ao conteúdo ou ação que motivou o erro.

### 3.3  Eficiência
O sistema deve fornecer rápido acesso a qualquer funcionalidade.

### 3.4 Consistência e padronização
O sistema deve manter a maior parte da interface a mesma para cada tipo de usuário, mantendo um padrão de cores e estrutura.

### 3.5 Design simples
O sistema deve ter ícones intuitivos.

## 4. Confiabilidade
### 4.1 Disponibilidade
O sistema estará disponível no modo 24/7.

### 4.2 Suportabilidade
O sistema deve suportar 100000 usuários ativos simultaneamente.

### 4.3 Direitos autorais
* O sistema deve garantir que os direitos autorais dos autores dos artigos sejam preservados.
* O sistema deve oferecer suporte para que o usuário possa realizar denúncias ao se deparar com conteúdos que violem direitos de propriedade intelectual ou conteúdos que sejam ofensivos.

### 4.4 Segurança e Privacidade
* O sistema deve assegurar a segurança e privacidade dos dados gerados, armazenando senhas e dados sensiveis de forma segura.
* O sistema deve ser transparente quanto as informações coletadas referentes a dados pessoais do usuário e preferencias de conteúdo e fornecer ao usuário a possibilidade de ajustar a visibilidade de tais informações.
* O sistema deve fornecer ao usuário controle sobre o conteúdo de comunicação que irá receber, como notificações e e-mails.

## 5. Desempenho
### 5.1 Tempo de resposta
O aplicativo tem de responder as ações do usuário de imediato.

### 5.2 Volume de assinantes
O sistema será capaz de suportar 100000 de usuários ativos simultaneamente.

### 5.3 Modo de degradação
Se o sistema estiver sofrendo com algo que degrade o site, como a internet com sinal fraco, terá páginas que não serão carregadas.

### 5.4 Utilização de recursos
+ OS X 10.9 ou superior
+ Windows 7 ou superior
+ Versão 6 ou superior.
+ Smartphone

## 6. Suportabilidade
### 6.1 Software do usuário
O usuário será capaz de utilizar o sistema através de um navegador de internet. Não será necessário que nenhum software personalizado resida no computador pessoal. Estes são os requisitos de sistema para usar o UNBIND e acessar seu conteúdo por meio do site.

## 7. Restrições de Design
### 7.1 Restrição de Design Um
O sistema deverá ser disponibilizado em diversas línguas, quando o usuário mudar o idioma nas opções de configuração o site se modificará.

### 7.2 Responsividade
O sistema deverá se ajustar de forma responsiva, ou seja, ajustando todo o conteúdo da tela à plataforma que o usuário estiver utilizando.

### 7.3 Restrição de Design Cinco
Antes do usuário poder ver as funcionalidades do site, terá que ter uma tela inicial com a opção de login e cadastro.

### 7.4 Restrição de Design Sete
O nome da página sempre estará no topo do layout.

## 8. Requisitos de Sistema de Ajuda e de Documentação de Usuário On-line
O serviço deverá possuir uma seção destinada a ajudar o usuário a utilizar o serviço, responder suas dúvidas e encontrar soluções. Esta seção deverá disponibilizar:
+ Área de busca para encontrar soluções para as questões mais frequentes
+ Tutoriais claros e objetivos de como o usuário pode utilizar os recursos do serviço
+ Fórum para que os usuários possam interagir e compartilhar soluções e ideias

## 9. Interfaces
### 9.1 Interfaces de Usuário
O usuário interage com o sistema por meio das interfaces. Abaixo apresentamos alguns exemplos de interfaces disponíveis aos usuários.
+ Tela onde o usuário pode fazer Login.
+ Tela onde o usuário pode se cadastrar.
+ Tela inicial onde o usuário pode escolher por qual funcionalidade navegar.

### 9.2 Interfaces de Hardware
O software oferece suporte aos dispositivos apresentados abaixo.
+ Smartphones.
+ Computadores Notebooks.
+ Computadores Desktop.

### 9.3	Interfaces de Comunicações
As comunicações entre os serviços são feitas por meio de conexão  remota via internet (wifi, internet móvel e etc).
