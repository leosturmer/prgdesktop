
## Leitura e Escrita de Dados Estruturados (CSV) em Python

Arquivos CSV (Comma-Separated Values) são muito usados para armazenar dados tabulares, como planilhas ou informações de jogos. O Python possui o módulo `csv` para facilitar a leitura e escrita desses arquivos.

### 1. Escrevendo Dados de Personagens de RPG em um Arquivo CSV

Para gravar dados em formato CSV, use o módulo `csv` e o método `writer`:

```python
import csv

personagens = [
	['nome', 'classe', 'nivel', 'hp'],
	['Arthos', 'Guerreiro', 5, 42],
	['Lyra', 'Maga', 4, 28],
	['Dorn', 'Clérigo', 3, 35]
]

with open('personagens.csv', 'w', newline='', encoding='utf-8') as arquivo:
	escritor = csv.writer(arquivo)
	escritor.writerows(personagens)
```

Esse código cria um arquivo `personagens.csv` com cabeçalho e três personagens de um dungeon crawler/RPG.

### 2. Lendo Dados de Personagens de um Arquivo CSV

Para ler dados de um arquivo CSV, use o método `reader`:

```python
import csv

with open('personagens.csv', 'r', encoding='utf-8') as arquivo:
	leitor = csv.reader(arquivo)
	for linha in leitor:
		print(linha)
```

Cada linha é retornada como uma lista de strings.

### 3. Usando Dicionários com CSV para Itens de RPG

O módulo `csv` também permite trabalhar com dicionários, facilitando o acesso aos dados pelo nome da coluna.

#### Escrevendo com `DictWriter`:

```python
import csv

itens = [
	{'nome': 'Espada Longa', 'tipo': 'arma', 'dano': '1d8'},
	{'nome': 'Poção de Cura', 'tipo': 'consumível', 'dano': '-'},
	{'nome': 'Escudo de Ferro', 'tipo': 'armadura', 'dano': '-'}
]

with open('itens.csv', 'w', newline='', encoding='utf-8') as arquivo:
	campos = ['nome', 'tipo', 'dano']
	escritor = csv.DictWriter(arquivo, fieldnames=campos)
	escritor.writeheader()
	escritor.writerows(itens)
```

#### Lendo com `DictReader`:

```python
import csv

with open('itens.csv', 'r', encoding='utf-8') as arquivo:
	leitor = csv.DictReader(arquivo)
	for linha in leitor:
		print(linha['nome'], linha['tipo'], linha['dano'])
```

---

Essas técnicas permitem manipular dados estruturados de forma simples e eficiente em Python, facilitando a criação de sistemas de inventário, personagens e outros elementos de jogos dungeon crawler/RPG.
