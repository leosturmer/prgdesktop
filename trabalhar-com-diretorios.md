### Funções de Manipulação de Diretórios no Pacote `os` do Python

O pacote `os` do Python fornece diversas funções para manipulação de diretórios e interação com o sistema operacional. Algumas das funções mais comuns:

- **`os.getcwd()`**: Retorna o diretório de trabalho atual (Current Working Directory). É útil para verificar em qual diretório o script está sendo executado.

- **`os.listdir(path='.')`**: Lista todos os arquivos e diretórios no caminho especificado. Se nenhum caminho for fornecido, lista o conteúdo do diretório atual.

- **`os.mkdir(path)`**: Cria um novo diretório no caminho especificado. Se o diretório já existir, uma exceção será lançada.

- **`os.makedirs(path, exist_ok=False)`**: Cria diretórios recursivamente. Se `exist_ok` for `True`, não irá lançar uma exceção caso os diretórios já existam.

- **`os.rmdir(path)`**: Remove o diretório especificado. O diretório deve estar vazio, caso contrário, uma exceção será lançada.

- **`os.removedirs(path)`**: Remove diretórios recursivamente. Remove todos os diretórios intermediários vazios no caminho especificado.

- **`os.chdir(path)`**: Altera o diretório de trabalho atual para o caminho especificado.

- **`os.getlogin()`**: Retorna o nome do usuário atualmente logado no terminal.

- **`os.getenv(key, default=None)`**: Retorna o valor de uma variável de ambiente especificada por `key`. Se a variável não existir, retorna o valor padrão especificado.

- **`os.environ`**: Um mapeamento que contém todas as variáveis de ambiente do sistema. Pode ser usado para acessar ou modificar variáveis de ambiente.

## Exemplos

### Listar arquivos de um diretório passado como argumento

```python
import sys
import os

if len(sys.argv) < 2:
	print("Uso: python listar_arquivos.py <caminho_do_diretorio>")
	sys.exit(1)

diretorio = sys.argv[1]

if os.path.isdir(diretorio):
	print(f"Arquivos em '{diretorio}':")
	for arquivo in os.listdir(diretorio):
		print(arquivo)
else:
	print("Diretório não encontrado.")
```

### Criar um diretório a partir de argumento

```python
import sys
import os

if len(sys.argv) < 2:
	print("Uso: python criar_diretorio.py <nome_do_diretorio>")
	sys.exit(1)

novo_dir = sys.argv[1]

try:
	os.makedirs(novo_dir)
	print(f"Diretório '{novo_dir}' criado com sucesso!")
except FileExistsError:
	print(f"O diretório '{novo_dir}' já existe.")
```

