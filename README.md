
# Tabela do Campeonato Brasileiro em Python

Desenvolvi essa biblioteca com a finalidade de ajudar aqueles que estão começando a estudar Python e querem trabalhar com informações atualizadas do Campeonato Brasileiro - Série A. Visto que tinham poucos projetos ou ideias em cima disso, resolvi criar esse projeto que faz uma raspagem de dados e captura as informações atualizadas do campeonato.
## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/oadailton/tabela-brasileiro-py
```

Entre no diretório do projeto

```bash
  cd my-project
```

Instale as dependências

```bash
  pip install requests
  pip install pandas
  pip install certifi
```

Adicionando no Python

```bash
  import gerador 
```
Caso você deixe a biblioteca em uma pasta separada, igual fizemos aqui, antes chamar ela precisará acionar esses comandos abaixo:

```bash
  import sys
  sys.path.append('src')
  import gerador
```

## Uso

Para começarmos a usar a biblioteca, basta acionar a seguinte ação

```python
gerador.tabelabrasileiro(tipo(int), timeout(int), classificação(int), informação(str))
```

#### Tipo 
Aqui você pode escolher até três opções de saída das informações.
0: Ele imprimirá a tabela inteira como string
1: Com base na classificação retorna o objeto ou um valor específico de acordo com a informação.
2: Pega o  nome do time de acordo com a classificação escolhida.

#### Timeout 

Define o tempo limite de aguardo da resposta do servidor. Por ser um processo um pouco demorado, o recomendável é sempre deixar 60.

#### Classificação 

Quando usamos o tipo 1 e 2, precisamos informar o número respectivo da classificação para pegar a informação. Suponhamos que queíramos pegar o nome do lanterna, teríamos que usar 

```PYTHON
nomelanterna = gerador.tabelabrasileiro(2, 60, 19) 
```
Reparem que para pegar o 20º lugar, usamos 19, salientando que aqui a classificação começa do 0, logo sempre para obter uma informação precisa de uma determinada posição precisamos sempre diminuir 1 número. Por exemplo, o 6º colocado, seria 5.

#### Informação

Aplicado especialmente quando definimos tipo igual a 1, conseguimos puxar determinados dados de uma respectiva classificação. 

Antes de começar você pode ver que informações pode obter acionando, por exemplo:

```PYTHON
gerador.tabelabrasileiro(1,60,0)
```

```BASH
Posição     1º  0  Botafogo - RJ
PTS                           33
J                             13
V                             11
E                              0
D                              2
GP                            22
GC                             7
SG                            15
CA                            33
CV                             3
%                             84
Recentes                 V  V  V
Próx                         NaN
```

Pois bem, suponhamos que eu queria pegar o saldo de gols ("SG") do líder? Logo usaremos a seguinte função:

```PYTHON
gerador.tabelabrasileiro(1,60,0,"SG")
```

Que nos retornará:

```BASH
15
```

## Exemplo

#### Impressão da tabela completa:

```PYTHON
print(gerador.tabelabrasileiro(0,60))
```

Retorno:

```BASH
                              Posição  PTS   J   V  ...  CV   %  Recentes  Próx
0                1º  0  Botafogo - RJ   33  13  11  ...   3  84   V  V  V   NaN
1                  2º  0  Grêmio - RS   26  13   8  ...   1  66   V  V  V   NaN
2                3º  0  Flamengo - RJ   25  13   8  ...   0  64   D  V  V   NaN
3               4º  0  Palmeiras - SP   23  13   6  ...   2  58   D  D  E   NaN
4    5º  +2  Red Bull Bragantino - SP   23  13   6  ...   2  58   V  V  V   NaN
5             6º  -1  Fluminense - RJ   21  13   6  ...   5  53   E  V  D   NaN
6              7º  +4  São Paulo - SP   21  13   6  ...   3  53   V  D  V   NaN
7          8º  -2  Internacional - RS   21  13   6  ...   0  53   V  V  E   NaN
8    9º  0  Athletico Paranaense - PR   20  13   6  ...   1  51   D  V  E   NaN
9       10º  0  Atlético Mineiro - MG   20  13   5  ...   4  51   E  D  E   NaN
10            11º  -3  Fortaleza - CE   20  13   5  ...   1  51   V  V  D   NaN
11          12º  0  Cruzeiro Saf - MG   18  13   5  ...   2  46   D  V  E   NaN
12           13º  +3  Cuiabá Saf - MT   15  13   4  ...   3  38   D  D  V   NaN
13               14º  -1  Santos - SP   13  13   3  ...   3  33   D  D  D   NaN
14                15º  -1  Bahia - BA   12  13   3  ...   2  30   V  D  D   NaN
15          16º  -1  Corinthians - SP   12  13   3  ...   0  30   V  D  D   NaN
16                 17º  0  Goiás - GO   11  12   3  ...   2  30   E  V  D   NaN
17  18º  0  Vasco da Gama S.a.f. - RJ    9  13   2  ...   1  23   D  V  D   NaN
18        19º  0  América Fc Saf - MG    9  13   2  ...   2  23   D  D  E   NaN
19              20º  0  Coritiba - PR    4  12   0  ...   2  11   E  D  D   NaN
```

#### Impressão da diferença de pontos entre o primeiro e o último colocado 

```PYTHON
diferenca = gerador.tabelabrasileiro(1,60,0,"PTS")-gerador.tabelabrasileiro(
1,60,19,"PTS")
print(diferenca)
```

Retorno: 

```BASH
29
```

#### Impressão do nome do time que está no meio da tabela (10º)

```PYTHON
meiodatabela = gerador.tabelabrasileiro(2,60,9)
print(meiodatabela)
```

Retorno:

```BASH
Atlético Mineiro - MG
```
## Screenshots

![Example.py rodando no terminal](https://github.com/oadailton/tabela-brasileiro-py/blob/master/screenshots/cmd.gif)

