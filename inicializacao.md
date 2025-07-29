## Inicializando o Ambiente e Criando uma Aplicação Mínima com Textual

A seguir temos um passo a passo para preparar o ambiente de desenvolvimento, instalar o Textual e criar uma aplicação mínima.

### 1. Preparando o Ambiente com `venv`

O uso de ambientes virtuais é recomendado para isolar dependências e evitar conflitos entre projetos. Para criar e ativar um ambiente virtual:

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux:
```bash
python -m venv .venv
. .venv/bin/activate
```

Caso tenha problemas, dependendo do shell ou distribuição usada os comandos podem ser:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalando o Textual

Com o ambiente virtual ativado, instale o framework Textual usando o `pip`:

```bash
pip install textual
```

### 3. Escrevendo uma Aplicação Mínima

Crie um arquivo chamado `app_minima.py` com o seguinte conteúdo:

```python
from textual.app import App

class AppMinima(App):
    pass

if __name__ == "__main__":
    AppMinima().run()
```


A estrutura básica de uma aplicação Textual envolve:

- Definição de uma classe que herda de `App`
- Implementação de métodos para montar a interface e tratar eventos
- Execução da aplicação com o método `run()`

Nosso exemplo de uma aplicação mínima não incluiu a implementação de métodos para montar componentes porque ela não tem componente algum.

### 4. Executando a Aplicação

Para rodar a aplicação, execute:

```bash
python app_minima.py
```

Você verá a interface básica do Textual no terminal.

> Para sair tecle `ctrl+q`

A partir desse ponto, é possível expandir a aplicação adicionando widgets, layouts e funcionalidades conforme a necessidade.