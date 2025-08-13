## Exemplos de Utilitários em Linha de Comando com Python

A seguir, veja ideias de utilitários que podem ser criados em Python usando os módulos e operações apresentados nas lições anteriores. Cada exemplo inclui um breve comentário sobre o funcionamento e os módulos envolvidos.


### Buscador de Palavras em Arquivos
Procura uma palavra em um arquivo de texto e mostra as linhas onde ela aparece.

```python
# Busca por uma palavra em um arquivo
import sys
palavra = sys.argv[2]
with open(sys.argv[1], 'r') as f:
	for i, linha in enumerate(f, 1):
		if palavra in linha:
			print(f"Linha {i}: {linha.strip()}")
```

### Conversor de CSV para Lista
Lê um arquivo CSV e exibe os dados em formato de lista.
```python
# Lê um arquivo CSV e exibe os dados
import csv, sys
with open(sys.argv[1], 'r', encoding='utf-8') as f:
	leitor = csv.reader(f)
	for linha in leitor:
		print(linha)
```

### Gerenciador de Inventário RPG com Shelve
Salva, lê e atualiza dados de inventário de RPG usando o módulo `shelve`.
```python
# Adiciona um item ao inventário
import shelve, sys
with shelve.open('inventario.db') as db:
	itens = db.get('itens', [])
	itens.append(sys.argv[1])
	db['itens'] = itens
	print('Inventário:', db['itens'])
```

---

## Exercícios: Criando Utilitários em Linha de Comando com Python

Desenvolva os utilitários abaixo, reutilizando ou expandindo a lógica dos exemplos apresentados:

1. **Contador de Linhas**
	- Escreva um programa que receba o nome de um arquivo de texto e exiba o número total de linhas desse arquivo.

2. **Filtro de Linhas por Palavra**
	- Crie um utilitário que receba um arquivo de texto e uma palavra, e salve em um novo arquivo apenas as linhas que contêm essa palavra.

3. **Conversor de CSV para TXT**
	- Implemente um programa que leia um arquivo CSV e salve os dados em um arquivo de texto simples, um registro por linha.

4. **Inventário RPG: Remover Item**
	- Expanda o gerenciador de inventário para permitir a remoção de um item informado pelo usuário.

5. **Listador de Itens do Inventário**
	- Crie um utilitário que exiba todos os itens atualmente salvos no inventário RPG (usando shelve).

6. **Busca de Personagem em CSV**
	- Escreva um programa que receba o nome de um personagem e busque seus dados em um arquivo CSV de personagens. Faz parte do exercícios criar o formato desse arquivo CSV.

7. **Relatório de Palavras**
	- Faça um utilitário que conte quantas vezes cada palavra aparece em um arquivo de texto e exiba um relatório ordenado (da maior para a menor quantidade de ocorrências).

8. **Atualizador de HP de Personagem**
	- Implemente um script que atualize o valor de HP de um personagem salvo no inventário (shelve), recebendo o nome e o novo valor por argumento.
