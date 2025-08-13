### Usando variáveis de ambiente em Python

Variáveis de ambiente são valores definidos no sistema operacional que podem ser acessados pelos programas. Elas são úteis para guardar configurações, caminhos ou segredos (como senhas de banco de dados).

#### Como definir uma variável de ambiente no terminal

- No Linux:
	```bash
	export MEU_EXEMPLO=valor_teste
	python seu_script.py
	```
- No Windows (cmd):
	```cmd
	set MEU_EXEMPLO=valor_teste
	python seu_script.py
	```


#### Exemplo: Lendo e usando uma variável de ambiente

```python
import os

# Suponha que exista uma variável de ambiente chamada 'USER' (Linux) ou 'USERNAME' (Windows)
usuario = os.getenv('USER') or os.getenv('USERNAME')

if usuario:
		print(f"Usuário atual: {usuario}")
else:
		print("Variável de ambiente de usuário não encontrada.")

# Você também pode definir uma variável de ambiente temporariamente no script:
os.environ['MEU_EXEMPLO'] = 'valor_teste'
print("MEU_EXEMPLO:", os.environ['MEU_EXEMPLO'])
```

