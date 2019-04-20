## Histórico de Revisão
-------------------------
Data|Versão|Descrição|Autor(es)
---- |----------------------- |--------------------|-----------
20/04/2019|1|Abertura do documento| Igor Guimarães Veludo, João Pedro Mota Jardim, Byron Kamal|
20/04/2019|1.1|Arrumando indentação dos exemplos de código|Igor Guimarães Veludo, João Pedro Mota Jardim, Byron Kamal|


## Introdução

A folha de estilos é inteiramente baseada no PEP 8, que é um documento de convenções Python.

## 1 Layout de Código

## 1.1 Indentação

### 1.1.1 Use 4 espaços por nivel de identação.

Exemplo correto:

    if (constant > iterator)
	    do_something()

Exemplo errado:

	if (constant > iterator)
	  do_something()

### 1.1.2 As linhas são limitadas a um máximo de 79 caracteres de código.

Exemplo correto:

    total = ((number_of_items * base_price) + (taxes * dollar_quotation)
	         - (sub_total - commercial_discount))

 Exemplo errado:

     total = ((number_of_items * base_price) + (taxes * dollar_quotation) - (sub_total - commercial_discount))

### 1.1.3  Alinhe os operandos com a abertura do delimitador.

Exemplo correto:

    # Aligned with opening delimiter.
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)

Exemplo errado:

    # Arguments on first line forbidden when not using vertical alignment.
    foo = long_function_name(var_one, var_two,
        var_three, var_four)

### 1.1.4 O fechamento de chaves/ colchetes / parênteses pode ser alinhado sob o primeiro caractere não-espaço-branco da última linha da lista.

Exemplo correto:

    vector = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    ]

Exemplo errado:

    vector = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9]

### 1.1.5. Uma linha deve ser quebrada depois de um operador binário.

Exemplo correto:

    income = (gross_wages +
              taxable_interest +
              (dividends - qualified_dividends) -
              ira_deduction -
              student_loan_interest)

Exemplo errado:

    income = (gross_wages
              + taxable_interest
              + (dividends - qualified_dividends)
              - ira_deduction
              - student_loan_interest)

## 1.2 Linhas em branco

### 1.2.1 Adicionar duas linhas em branco acima e abaixo das definições de classe e funções top-level

### 1.2.2 As definições de métodos dentro de uma classe são cercadas por uma única linha em branco.

### 1.2.3 Linhas em branco podem ser usadas para separar grupos de funções relacionadas. Linhas em branco podem ser omitidas entre um grupo de one-liners relacionados.

Exemplo correto:

    var_1 = 0
    var_2 = 2 ** 5
    result = var_1 + var_2

    string_1 = “Hello ”
    string_2 = “World!”
    phrase = string + string2

Exemplo errado:

    var_1 = 0
    var_2 = 2 ** 5
    result = var_1 + var_2
    string_1 = “Hello ”
    string_2 = “World!”
    phrase = string + string2

## 1.3 Importes

### 1.3.1 Importes devem estar em linhas separadas

Exemplo correto:

    import os
	import sys

Exemplo errado:

    import sys, os

### 1.3.2 Os importes são sempre colocados na parte de cima do arquivo, logo após qualquer comentário e docstrings do módulo, e antes dos módulos globais e constantes.

# 2 Estrutura de comentários

## 2.1 Os comentários devem ser frases completas.

## 2.2 Todos os comentários devem ter uma linha em branco acima antes de começar

## 2.3 Os comentários devem ter um máximo de 75 caracteres por linha

## 2.4 Comentários de linha única devem ser escritos com # (espaço) (comentário)

## 2.5 Todos os comentários devem ser identificados com o código

## 2.6 Todos os comentários devem começar com a primeira letra maiúscula

## 2.7 Todos os comentários devem ser redigidos em inglês

Exemplo correto:

    # Loop to iterate in the range of table

    for x in range(0,3):

    # Printing the iterator

      print(x)

Exemplo errado:

    # Loop to iterate in the range of table
      for x in range(0, 3):
    # Printing the iterator
        print(x)

## 2.8 Vários comentários de linha devem ser enviados com "" "(espaço) (comentário) (espaço)" "" no final

## 2.9 As linhas abaixo do primeiro devem ser alinhadas com a linha acima

Exemplo correto:

    """ Loop to iterate in the range of table
          of students """

    for x in range(0, 3):

          # Printing the iterator iterator iterator iterator

          print(x)

Exemplo errado:

    # Loop to iterate in the range of table Something  
    # Something Something Something Something
    for x in range(0, 3):

    # Printing the iterator
    print(x)

# 3 Organização de estruturas de controle

## 3.1 Use '(' em estruturas de decisão

Exemplo correto:

    if (age >= 18):
       print (maior de idade)

Exemplo errado:

    if age >= 18:
    print (maior de idade)

## 3.1 Em condicionais muito grandes, coloque um espaço entre eles

Exemplo correto:

    if((name == 'Lira' and age == 10) or (name == 'Jessica' and age == 8)):

 Exemplo errado:

    if((name=='Lira'and age==10)or(name=='Jessica'and age == 8)):

## 3.1 Coloque linhas brancas entre as linhas de código

Exemplo correto:

    name = input ('enter your name')<br />
    age = input ('enter your name') <br />

    people = People(name,age) <br />

    print(people.getName()) <br />
    print(people.getAge()) <br />

Exemplo errado:

    name = input ('enter your name')<br />
    age = input ('enter your name')<br />
    people = People(name , age) <br />
    print(people.getName()) <br />
    print(people.getAge()) <br />

# 4 Indentação de estruturas de controle

## 4.1 Quando uma estrutura é subordinada a outra, deve ser recuada sob essa estrutura

Exemplo correto:

    if (variable_1 > 100):
        do_this( )
    else:
        do_that( )

Exemplo errado:

    if (variable_1 > 100):
        do_this( )
        else:
        do_that( )

## 4.2 Expressões complicadas

Exemplo correto:

    if (((var_1 > var_2) && (var_1 > var_3)) ||
        ((var_1 > 1) && (var_2 < 10)) ||
        (var_3 = 0)):
            do_this( )
    else:
       do_that( )

Exemplo errado:

    if (((var_1 > var_2) && (var_1 > var_3)) ||
    ((var_1 > 1) && (var_2 < 10)) ||
    (var_3 = 0)):
        do_this( )
    else:
        do_that( )

# 5 Rotinas

## 5.1 Use linhas em branco para separar as partes da rotina.

Exemplo correto:

    def showAccount(accountNumber):

        print(accountNumber)

    def retrieveAccount(accountNumber):

        findNumber()

Exemplo errado:

    def showAccount(accountNumber):
        print(accountNumber)
    def retrieveAccount(accountNumber):
        findNumber()

## 5.1 Use a indentação padrão nos parâmetros da rotina.

Exemplo correto:

    def setBalance (
        id ,
        balance,
        date,
        user
    ):

Exemplo errado:

    def setBalance (id, balance, date, user):

# 6. Convenções de nomeação

## 6.1 Evite caracteres 'l' (letra minúscula 'L'), 'O' (letra maiúscula 'o') ou 'I' (letra maiúscula 'i') como nomes de variáveis ​​de um único caractere.

## 6.2 Nomes de classe devem usar a convenção das iniciais de cada palavra em letra maiúscula

Exemplo correto:

    class PersonNames:

Exemplo errado:

    class person_Names:

## 6.3 Variable shoud use lower_case_with_underscores convention. Nomes de variáveis devem ser escritas em letra minúscula e separadas por underline '_'

Exemplo correto:

    person_name = "John"
    person_last_name = "Smith"

Exemplo errado:

    PersonName = "John"
    PersonLastName = "Smith"

## 6.4  Variáveis devem possuir nomes curtos seguidos das suas iniciais em letra maiúscula.

Exemplo correto:

    AnyStr = Var('AnyStr', bytes, str)

Exemplo errado:

    any_str = Var('any_str', bytes, str)

## 6.5 Os nomes de exceção devem seguir a convenção de nomenclatura da classe com o sufixo "Erro".

Exemplo correto:

	except IOError:

Exemplo errado:

	except i_o_error:

## 6.6 Os nomes de função e método devem ser minúsculos, com palavras separadas por underline.

Exemplo correto:

    def calc_total(number_1, number_2):

Exemplo errado:

    def calcTotal(number_1, number_2):

## 6.7 Constantes devem ser escritas com todas as letras em maiúsculo e separadas por underline.

Exemplo correto:

    MAX_LENGTH = 25

Exemplo errado:

    max_length = 25


# Bibliografia

https://github.com/fgaTactics/tecprog2017.1/wiki/Stylesheet - Visualizado em 25/09/2017 às 14:25

http://aprenda-python.blogspot.com.br/2011/10/programe-conforme-o-pep8.html - Visualizado em 25/09/2017 às 14:25
