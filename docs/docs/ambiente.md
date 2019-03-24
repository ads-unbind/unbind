# Ambiente de Desenvolvimento

## Instalação do Docker
* Baixe e instale Docker CE em seu sistema operacional:
    * [Linux - Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
    * [macOS](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
    * [Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

* Baixe e instale Docker Compose no [site oficial](https://docs.docker.com/compose/install/).

## Rodar a Aplicação
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
