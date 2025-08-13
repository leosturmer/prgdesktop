# Trabalhando com arquivos

	
## <code>touch</code> - Usado informalmente para criar aquivos vazios.
O 'touch', na verdade, serve para 'cutucar' um arquivo, para testar a leitura e a escrita no arquivo. O comando 'touch' faz isso atualizando as informações de data e hora do arquivo. Essa é a única mudança que ele faz no arquivo.

Quando o arquivo passado ao touch como parâmetro não existe, então o touch cria esse arquivo e deixa ele vazio.

Sintaxe
	touch <nome do arquivo>

Exemplo

Cria um arquivo chamado 'mensagem.txt' caso ele já não exista.

Se o arquivo já existir, atualiza os dados de data e hora de acesso ao arquivo
	
	$touch mensagem.txt

## <code>rm</code> - Apaga arquivos
	
Sintaxe
	rm <nome do arquivo>

Exemplo

Apaga o arquivo 'mensagem.txt' que está no diretório atual

	$rm mensagem.txt

## <code>mv</code> - Move arquivos

Renomeia arquivos

Sintaxe

	mv <arquivo de origem> <caminho destino>

Exemplo

Move o arquivo 'mensagem.txt' para o diretório 'textos' que 
está no diretório atual (./)

	$mv mensagem.txt ./textos

Muda o nome do arquivo 'mensagem.txt' para 'msg.txt'

	$mv mensagem.txt msg.txt

Move o arquivo 'mensagem.txt' do diretório 'textos' para o
diretório atual (o diretório atual é referido pelo '.')

	$mv textos/mensagem.txt .

## <code>cat</code> - Imprime o conteúdo de um arquivo de texto

Sintaxe
	cat <arquivo>

Exemplo

	cat /etc/motd



## <code>less</code> - paginador 

Imprime o conteúdo de um arquivo de texto usando paginação. Ele mostra o conteúdo do arquivo uma tela cheia por vez e permite
avançar e retroceder no arquivo usando as setas do teclado.

Para sair do less e voltar ao prompt, digite 'q'.

Sintaxe

	less <nome do arquivo>

## `cp` - copiar arquivo

Copia um arquivo de um diretório para outro, opcionalmente renomeando o arquivo de destino.

Sintaxe

	cp <origem> <destino>

	origem - nome de arquivo
	destino - nome de arquivo ou diretório

> Não podem haver 2 arquivos nem 2 diretórios com o mesmo nome dentro do **mesmo** diretório.

Exemplos

1. Copiar o arquivo `oi.js`, que está no diretório atual, para dentro do diretório atual também.

	$cp oi.js oioi.js

Foi preciso trocar o nome do arquivo de destino para fazer a cópia.

2. Copiar o arquivo `cmdbash.txt` para dentro do diretório `set`. 


	$cp cmdbash.txt ~/anotacoes/2023/set

O diretório `set` está dentro de `2023`, que está dentro de `anotacoes` que está dentro do diretório `home` do usuário.

	~
	+--anotacoes
		+--2023
			+--set

Nesse caso não é preciso trocar o nome do arquivo, pos ele será copiado para outro local.

Se quisermos trocar o nome do arquivo ao copiá-lo, também é possível. Assim:

	$cp cmdbash.txt ~/anotacoes/2023/set/comandosbash.txt

Nesse caso o novo arquivo será chamado `comandosbash.txt`.
