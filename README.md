# Projeto-AnaliseDeDados

Projeto feito de acordo de formato academico para fins de alcançar a meta do semestre.

Primeiro foi feita a modelagem dos dados das tabelas dentro do star UML, conforme consta no "modelo.mdj",
e vendo quais seriam os atributos, colunas e entre outros antes de passar para o MySQL.

Depois foi feita a modelagem física onde criei o banco de dados, seguindo as formas normais
orientada, e depois atribuindo suas respectivas regras para as tabelas. Podendo ser conferido
"modelagem.sql" foi feita passo a passo podendo ser um exemplo para quem quiser utilizar posteriormente por
quem encontra alguma dificuldade em SQL.
Ela foi criada no MySql Command Line- Unicode e os dados inseridos pelo mesmo.


Criei uma massa pequena de dados para ter o que trabalhar, utilizei do chat-gpt para criar os nomes e datas de nascimento pois a criatividade já não estava colaborando muito haha.
Os dados inseridos também encontram na "modelagem.sql" podendo ser acessados.

E por fim, conectei tudo em python transformando num gráfico com os jogos alugados com a maior 
média encontrada.
Foi feito primeiramente uma conexão ao MySql com o mysql-connector, depois executado o comando sql
para pesquisar os dados requeridos.
Depois importado o pandas e o MatplotLib, onde o resultado da pesquisa foi passsado para um 
DataFrame do pandas e feito um agrupamento por nome e depois utilizando a median(), onde busca a media de todos os valores.
E por último transformamos em um gráfico, onde mostrou que o Call of Duty foi o jogo com a maior média.


