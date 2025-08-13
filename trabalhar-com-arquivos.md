## Manipulação de Arquivos de Texto em Python

O Python oferece uma interface simples e poderosa para manipulação de arquivos de texto. A seguir, veja como realizar as operações mais comuns: abertura, leitura, escrita, atualização, criação e exclusão de arquivos.

### 1. Abrindo Arquivos

Para abrir um arquivo, utilize a função `open()`. O modo mais comum é o de leitura (`'r'`), mas você pode abrir arquivos para escrita (`'w'`), adição (`'a'`), leitura e escrita (`'r+'`), entre outros.

```python
# Abrir um arquivo para leitura
arquivo = open('exemplo.txt', 'r')
# ... use o arquivo ...
arquivo.close()
```

O recomendado é usar o bloco `with`, que garante o fechamento automático do arquivo:

```python
with open('exemplo.txt', 'r') as arquivo:
	conteudo = arquivo.read()
	print(conteudo)
```

### 2. Lendo Arquivos

Você pode ler todo o conteúdo de uma vez, linha por linha, ou em partes:

```python
# Lendo todo o conteúdo
with open('exemplo.txt', 'r') as arquivo:
	texto = arquivo.read()
	print(texto)

# Lendo linha por linha
with open('exemplo.txt', 'r') as arquivo:
	for linha in arquivo:
		print(linha.strip())

# Lendo todas as linhas em uma lista
with open('exemplo.txt', 'r') as arquivo:
	linhas = arquivo.readlines()
	print(linhas)
```

### 3. Escrevendo em Arquivos

Para escrever, abra o arquivo em modo de escrita (`'w'`) ou adição (`'a'`). O modo `'w'` sobrescreve o arquivo, enquanto `'a'` adiciona ao final.

```python
# Sobrescrevendo o arquivo
with open('exemplo.txt', 'w') as arquivo:
	arquivo.write('Primeira linha\n')
	arquivo.write('Segunda linha\n')

# Adicionando ao final do arquivo
with open('exemplo.txt', 'a') as arquivo:
	arquivo.write('Mais uma linha\n')
```

### 4. Atualizando Arquivos

Para atualizar (modificar) partes de um arquivo, normalmente você lê o conteúdo, faz as alterações em memória e depois grava novamente:

```python
# Exemplo: substituir uma palavra em todas as linhas
with open('exemplo.txt', 'r') as arquivo:
	linhas = arquivo.readlines()

linhas_modificadas = [linha.replace('velha', 'nova') for linha in linhas]

with open('exemplo.txt', 'w') as arquivo:
	arquivo.writelines(linhas_modificadas)
```

### 5. Criando Arquivos

Abrir um arquivo em modo de escrita (`'w'`) ou adição (`'a'`) já cria o arquivo se ele não existir. Para garantir que não sobrescreva, use `'x'`:

```python
# Criar um novo arquivo (erro se já existir)
try:
	with open('novo_arquivo.txt', 'x') as arquivo:
		arquivo.write('Conteúdo inicial')
except FileExistsError:
	print('Arquivo já existe!')
```

### 6. Excluindo Arquivos

Para excluir arquivos, use o módulo `os`:

```python
import os

if os.path.exists('exemplo.txt'):
	os.remove('exemplo.txt')
	print('Arquivo removido!')
else:
	print('Arquivo não encontrado.')
```

Essas operações cobrem o essencial para trabalhar com arquivos de texto em Python. Sempre trate possíveis erros (como arquivos inexistentes) e prefira o uso do bloco `with` para garantir o fechamento correto dos arquivos.