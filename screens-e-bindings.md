## Uso de Screen e BINDINGS no Textual

O Textual permite criar aplicações com múltiplas telas (screens), facilitando a navegação entre diferentes partes da interface, como menus, formulários ou painéis de configuração. Para isso, utiliza-se a classe `Screen` e os métodos `push_screen`, `pop_screen` e `switch_screen` da classe `App`.

### O que é uma Screen?

Uma `Screen` representa uma tela independente dentro da aplicação. Cada tela pode conter sua própria árvore de widgets e lógica de interação. Você pode criar quantas telas quiser, cada uma como uma subclasse de `Screen`.

Exemplo de definição de screens:

```python
from textual.screen import Screen
from textual.widgets import Static

class TelaInicial(Screen):
    def compose(self):
        yield Static("Esta é a tela inicial.")

class TelaSecundaria(Screen):
    def compose(self):
        yield Static("Esta é a tela secundária.")
```

### Navegação entre Screens

A navegação é feita pelos métodos:

- `push_screen("nome")`: Empilha uma nova tela sobre a atual (útil para diálogos ou  modais).
- `pop_screen()`: Remove a tela atual e retorna para a anterior.
- `switch_screen("nome")`: Troca a tela atual por outra, sem empilhar.

Para registrar as telas, utilize o método `App.install_screen` ou o dicionário `SCREENS`:

Exemplo usando dicionário `SCREENS`:

```python
class MinhaAppComScreens(App):
    SCREENS = {
        "inicial": TelaInicial,
        "secundaria": TelaSecundaria,
    }
    # ...compose e outros métodos...
```

Exemplo usando método `install_screen()`:

```python
def on_mount(self):
        self.title = "Exemplo de uso de Screen"        
        self.install_screen(TelaInicial, 'tela_inicial')
        self.install_screen(TelaSecundaria, 'tela_secundaria')
```

### O que são BINDINGS?

O atributo `BINDINGS` permite mapear atalhos de teclado a métodos da aplicação. Cada binding associa uma tecla a uma ação (método), facilitando a navegação e interação.

Exemplo de uso de BINDINGS para navegação entre screens:

```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.binding import Binding

class MinhaAppComScreens(App):
    BINDINGS = [
        Binding("n", "ir_para_secundaria", "Ir para tela secundária"),
        Binding("b", "voltar", "Voltar para tela anterior"),
        Binding("s", "switch_inicial", "Switch para tela inicial"),
    ]

    SCREENS = {
        "inicial": TelaInicial,
        "secundaria": TelaSecundaria,
    }

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_ir_para_secundaria(self):
        self.push_screen("secundaria")

    def action_voltar(self):
        self.pop_screen()

    def action_switch_inicial(self):
        self.switch_screen("inicial")
```

#### Explicação dos métodos

- `action_ir_para_secundaria`: Chamado ao pressionar "n", empilha a tela "secundaria".
- `action_voltar`: Chamado ao pressionar "b", desempilha a tela atual.
- `action_switch_inicial`: Chamado ao pressionar "s", troca para a tela "inicial".

### Resumo

- **Screen**: Define telas independentes.
- **push_screen**: Empilha uma nova tela.
- **pop_screen**: Remove a tela atual.
- **switch_screen**: Troca a tela atual.
- **BINDINGS**: Mapeia teclas para métodos de ação, facilitando a navegação entre screens.


```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class ScreenApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Conteúdo da tela inicial")
        yield Footer()

    def action_ir_para_secundaria(self):
        self.push_screen("secundaria")

    def action_voltar(self):
        self.pop_screen()

    def action_switch_inicial(self):
        self.switch_screen("inicial")

if __name__ == "__main__":
    ScreenApp().run()
```

---
> Listagem dos exemplos de código utilizados:
> 
> [github.com/lgmaciel/prgdesktop/exemplos](https://github.com/lgmaciel/prgdesktop/tree/main/exemplos)


---