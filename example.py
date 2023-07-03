"""Vamos importar as bibliotecas para acionar nossa bibliotea"""
import sys
sys.path.append('src') #Como o nosso codigo está na pasta SRC, vamos acionar ela antes
import gerador

tabela = gerador.tabelabrasileiro(0,60) #Aqui vamos pegar a tabela completa do campeonato
nomelider = gerador.tabelabrasileiro(2,60,0) #Pegaremos o clube que está na liderança
vicelider = gerador.tabelabrasileiro(2,60,1) #Pegaremos o clube que está na vice-liderança
pontolider = gerador.tabelabrasileiro(1, 60, 0, "PTS") #Pegaremos a pontuação do líder
pontovice = gerador.tabelabrasileiro(1, 60, 1, "PTS") #Pegaremos a pontuação do vice
nomeg6 = gerador.tabelabrasileiro(2, 60, 5) #Pegaremos o time que está na ultima posição do G6
nomeg7 = gerador.tabelabrasileiro(2, 60, 6) #Pegaremos o primeiro time depois do G6
ponto6 = gerador.tabelabrasileiro(1, 60, 5, "PTS") #Pegaremos a pontuação do sexto
ponto7 = gerador.tabelabrasileiro(1, 60, 6, "PTS") #Pegaremos a pontuação do setimo
nome16 = gerador.tabelabrasileiro(2, 60, 15) #Pegaremos o primeiro time acima do Z4
nome17 = gerador.tabelabrasileiro(2, 60, 16) #Pegaremos o primeiro time dentro do Z4
ponto16 = gerador.tabelabrasileiro(1, 60, 15, "PTS") #Pegaremos a pontuação do 16º colocado
ponto17 = gerador.tabelabrasileiro(1, 60, 16, "PTS") #Pegaremos a pontuação do 17º colocado
nomevc = gerador.tabelabrasileiro(2, 60, 18) #Pegaremos o vice-lanterna
nomelanterna = gerador.tabelabrasileiro(2, 60, 19) #Pegaremos o lanterna
vicelanterna = gerador.tabelabrasileiro(1, 60, 18, "PTS") #Pegaremos a pontuação do vice-lanterna
lanterna = gerador.tabelabrasileiro(1, 60, 19, "PTS") #Pegaremos a pontuação do lanterna

print("Campeonato Brasileiro de Futebol \r\n \r\n")
print("Confira a tabela atualizada do campeonato: \r\n \r\n")
print(tabela+"\r\n \r\n")
print("A disputa pelo campeonato continua mais acirrada do que nunca \r\n")
print("O "+nomelider+" continua na liderança com ",pontolider," pontos \r\n")
print("Atrás dele vem o "+vicelider+" com ",pontovice," pontos \r\n")
print("A distância do líder é de: ",pontolider-pontovice," pontos.\r\n")
print("O que promete muito jogão! \r\n")
print("Indo um pouco para baixo na disputa por uma vaga na Libertadores \r\n")
print("do ano que vem, temos, o "+nomeg7+" tentando entrar no G6 \r\n")
print("com a diferença de ",ponto6-ponto7," pontos do sexto colocado, o \r\n")
print(nomeg6+" o "+nomeg7+" vai fazer de tudo para se classificar pro torneio continental. \r\n")
print("Enquanto isso na famosa degola, temos o "+nome16+"\r\n")
print("perto da zona de rebaixamento, ele que está há",ponto16-ponto17, "pontos \r\n")
print("do primeiro do Z4, "+nome17+" está tendo que lutar para fugir do fantasma da série B \r\n")
print("A situação do "+nome16+" e "+nome17+" está dificil, mas não tanto quanto \r\n")
print(nomelanterna+" que coitado está na lanterna com ",lanterna," pontos \r\n")
print("ele atualmente está há ",vicelanterna-lanterna," pontos do "+nomevc+"\r\n")
print("que está em 19º lugar da tabela, que fase dificil do "+nomelanterna)
