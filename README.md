# DelloiteChallenge

# DESAFIO BACK-END

A Agência Cronos, que presta serviços de tecnologia (desenvolvimento, marketing e UX
design), contratou você para o desenvolvimento de uma API para gerenciamento do
conteúdo do site institucional.
Faça um CRUD de Serviços, Posts e Integrantes da Equipe, permitindo que o administrador
do site consiga criar, editar, deletar e visualizar os dados através de um painel
administrativo.
O gerenciamento dos dados deve ser feito com uma API REST conectada ao banco de
dados relacional.

# REQUISITOS MÍNIMOS BACK-END


- Todos os códigos deverão estar em um repositório no Github com README.md
descrevendo tecnologias utilizadas no projeto.
- API:
```
a. CRUD (Criar, ler, atualizar e deletar) de Serviços
b. CRUD (Criar, ler, atualizar e deletar) de Posts
c. CRUD (Criar, ler, atualizar e deletar) de Integrantes da Equipe
```
- Banco de dados:
```
a. Utilizar banco de dados relacional
b. Adicionar dados para teste
```
# OPCIONAIS BACK-END


- Autenticação de administrador para gerenciamento do conteúdo
- Documentação da API
- Testes automatizados
- Deploy da aplicação

#Minha solução

Foi criada uma imagem docker para criar o CRUD
Para executar basta digitar: 
`docker-compose up --build`
Dentro do diretorio com a imagem Docker
O banco de dados usado foi o sqlite3
É possivel adicionar, deletar e modificar os arquivos como administrador
![alt text](https://raw.githubusercontent.com/masuta16/RaizenChallenge/main/images/Screenshot%20from%202022-01-30%2002-48-47.png)

