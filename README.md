# API para cadastro de currículos com Django e Docker Compose

Esta é uma aplicação multi-container com Docker que implementa um servidor API para cadastro de currículos.

# Requisitos básicos.

* Docker e Docker Compose instalados.

# Utilização

* Entra na pasta do projeto e rode o comando `docker-compose up` que o docker se encarregará de baixar as imagens e gerar os containers com a aplicação.

# Containers

Cada container será explicado com as suas caracteristicas.

## db

Banco de dados que utiliza, neste caso, o PostgreSQL para armazenar os dados dos currículos.

## django

Este é o container onde se roda as APIs. O docker baixa a imagem do python e se encarrega de configurar o django, djangorestframework(que cuidará das APIs) e o psycopg2-binary(que faz a conexão com o PostgreSQL). A aplicação já se encontra pronta nos fontes baixados e será configurado automaticamente quando a aplicação é executada na sua primeira vez.

## web

Servidor apache configurado para que redirecione qualquer requisição de http://avaliacao.com para https://avaliacao.com. É ele que faz o proxy reverso para garantir que o django seja acessível por https ao invés da porta 80 ou da porta configurada, que é a 8888.

# Configuração

Nesta parte vamos ver os detalhes da configuração dos servidores envolvidos. Todas as definições de geração dos containers podem ser vistos no arquivo docker-compose.yml e nos arquivos Dockerfile.

## 1) web

A parte de configuração do servidor apache se encontra na pasta apache dos arquivos do docker-compose. E consiste no seguinte:

* httpd.conf: É onde tem a configuração do apache e do virtualhost que redireciona tudo que chega na porta 80 para 443.
* httpd-ssl.conf É onde fica a configuração do virtuahost em https.

* server.crt, server.csr e server.key: Certificados utilizados para configuração do https. Esses são auto-assinados mas podem ser substituídos por outros válidos.

## 2) django

É um serviço de aplicações web em python. Nele foi configurado o app currículo para cadastro, visualização, edição e remoção do currículo.

Dentro da pasta currículo temos scripts: startup.sh e migration.sh. Ambos são responsáveis por ativar o django quando o container é levantado. Sendo que o migration.sh só funciona na primeira vez, na hora de configurar a base de dados e adicionar o usuário admin. A senha deste usuário é admin_password.

Temos outras duas pastas. A currículo e api_curriculo. Na primeira temos os settins.py, onde fica a configuração do banco de dados, idioma e adição de plugins na configuração.

A segunda pasta, a api_currículo, possui a configuração da base utilizada(models.py e serializers.py), das permissões de acesso(permissions.py) e visualização dos dados(views.py)

## 3) db

Não tem uma configuração específica. É apenas um servidor PostgreSQL que guarda os dados utilizados pelo django.


# Utlização

Para utilizar o servidor pode fazer o seguinte:

## 1) Acessar a interface adminstrativa.

Acesse https://avaliacao.com/admin e entre com os dados de login e senha do usuário admin informado anteriormente na configuração do django.

Nele pode adicionar e remover os usuários que terão acesso aos dados do currículo.

## 2) Acessar a interface da API.

A interface da API pode ser acesasda por https://avaliacao.com/curriculo. Nele o usuário pode cadastrar o currículo e listar todos os currículos cadastrados no formato json. Para consultar o currículo, o usuário pode ir no numero do índice usado para o cadastro do currículo.

Por exmeplo o usuário que quiser consultar o currículo nº 1, ele pode acessar em

https://avaliacao.com/curriculos/1/

Nele você pode editar e remover o currículo. 

Esse acesso só é valido para o usuário que cadastrou o currículo. Caso outro usuário tenta acessar, ele receberá a informação de que o acesso não é permitido.

Outro jeito de cadastrar, editar e remover o currículo é atráves dos comandos de API. Na mesma pasta do fonte foi disponibilizado o arquivo curriculo-exemplo.json para fazer o cadastro, edição e remoção do curriculo.

Vamos dar um exemplo. Para listar os currículos utilizados pelo usuário admin podemos dar o comando abaixo.

`curl -k --user admin:admin_password -XGET https://avaliacao.com/curriculos/`

Ele só vai retornar ou [] ou alguns dados já cadastrados anteriormente. Vamos cadastrar com que está no curriculo-exemplo.json.


`curl -k  --user admin:admin_password -XPOST -H "Content-Type: application/json"  https://avaliacao.com/curriculos/ --data-binary @curriculo-exemplo.json`

Ao rodar o comando ele retorna uma mensagem assim:

`{"id":1,"usuario":"admin","nome":"Fulano de Tal","data_nascimento":"1982-10-01","endereço":"Rua da imaginação 234. Faz de conta","telefone_fixo":"(21) 2345678","celular":"(21) 9999-9999","email":"teste@teste.net.br","objetivo":"Apenas testes","perfil_profissional":"Feito apenas para testes.","escolaridade":"SUPERIOR","graduação":"Faculdades da vida.\r\n2010-2014 - Sistemas de informação","idiomas":"Inglês, Espanhol","historico_profissional":"2015-atualmente\r\nFazendo testes","ultimo_salario":"R$ 2341,24","pretensão_salarial":"R$ 3500,00","date_created":"2018-02-27T16:18:45.418012-03:00","date_modified":"2018-02-27T16:18:45.418037-03:00"}`

Isso quer dizer que o cadastro foi feito com sucesso. Você pode consultar com o primeiro XGET na primeira linha ou pode acessar adicionando 1/ no final que é o número do id utilizado no cadastro.

Se quiser editar o currículo, pode-se fazer a edição no arquivo json e mandar a alteração pela diretiva XPUT no endereço do currículo nº 1 para alterar o primeiro currículo.

`curl -k  --user admin:admin_password -XPUT -H "Content-Type: application/json"  https://avaliacao.com/curriculos/1/ --data-binary @curriculo-exemplo.json`

Para remover o currículo pode utilizar o XDELETE no mesmo endereço.

`curl -k  --user admin:admin_password -XDELETE https://avaliacao.com/curriculos/1/`

Se não retornar nada é porque a remoção foi feita com sucesso.

# To do (O que precisa fazer depois).

Implementar uma interface frontend, seja via web ou aplicativo que saiba enviar os dados no formato json em https.


# Licença.

Ele está sob a licença Apache 2.0. Você pode verificar uma cópia dessa licença neste repositório git ou veja a nota abaixo.

Copyright 2018 Adilson dos Santos Dantas

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


## Versão pt_BR

Licenciada sobre a Apache License, Version 2.0 (the "License"); você não pode usar este arquivo exceto em conformidade com a Licença. Você pode obter uma cópia da Licença(em inglês) em

   http://www.apache.org/licenses/LICENSE-2.0

A menos que seja exigido pela lei aplicável ou estar de acordo, por escrito, o software distribuído sob a Licença é feito "TAL COMO ESTÁ", SEM GARANTIAS OU CONDIÇÕES DE QUALQUER TIPO, expressas ou implícitas. Consulte a Licença para o idioma específico que rege as permissões e limitações sob a Licença.
