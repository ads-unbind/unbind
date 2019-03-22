# Arquitetura e Desenho de Software

## Colaboradores
| Nome | Matrícula | GitHub |
| --- | --- | --- |
| Bayron Kamal | 15/0007281 | [byronkamal](https://github.com/byronkamal) |
| Geovanne Santos | 15/0035756 | [saraivinha97](https://github.com/saraivinha97) |
| Igor Aragão | 15/0011903 | [roginaldosemog](https://github.com/roginaldosemog) |
| Igor Guimarãs | 13/0028240 | [IgorVeludo](https://github.com/IgorVeludo) |
| João Pedro Mota | 16/0031982 | [jpmota2208](https://github.com/jpmota2208) |
| José Aquiles | 16/0010331 | [aquiles23](https://github.com/aquiles23) |
| Ramon Sales | 14/0160205 | [ramonsales](https://github.com/ramonsales) |
| Vinícius Cantuária | 14/0165169 | [cantuariavc](https://github.com/cantuariavc) |
| William Almeida | 16/0020280 | [WillAllmeida](https://github.com/WillAllmeida) |

<!-- ## Documentação

Documentação disponível na [Wiki](https://github.com/ads-2019-1/wiki-ads-2019-1).
-->
## Licença

[MIT License](https://github.com/ads-2019-1/repo-ads-2019-1/blob/master/LICENSE)

## Como Contribuir

Para contribuir com a gente, o colaborador deve ler o [código de conduta](https://github.com/ads-2019-1/repo-ads-2019-1/blob/master/.github/CODE_OF_CONDUCT.md), dá um _fork_ e enviar um [pull request](https://github.com/ads-2019-1/repo-ads-2019-1/pulls) com sua contribuição.
O código será analisado por um dos proprietários do projeto e, se aprovado, incluído no núcleo da aplicação.


## Rodar a Aplicação
* Baixe e instale Docker CE em seu sistema operacional:
    * [Linux - Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
    * [macOS](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
    * [Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

* Baixe e instale Docker Compose no [site oficial](https://docs.docker.com/compose/install/).

#### Clone o repositório e entre nele
* Escolha uma forma de clonar o repositório:
    * HTTP: ``` git clone https://github.com/ads-2019-1/repo-ads-2019-1.git ```
    * SSH: ``` git clone git@github.com:ads-2019-1/repo-ads-2019-1.git ```

#### Levante seu ambiente
```
docker-compose up
```

---

#### Comandos úteis
#### Como baixar uma imagem do docker
```
docker pull <imagem-desejada>
```

#### Listando imagens locais
```
docker images
```

#### Deletando imagens
```
docker rmi -f <id-da-imagem>
```

#### Listando contêineres em execução
```
docker ps
```

#### Removendo contêineres
```
docker rm [-f] <nome-do-contêiner-ou-id>
```

#### Execução de comandos de fora do contêiner
```
docker exec <nome-do-contêiner> <comando-desejado>
```
