# Exercícios de leitura de código

## Exercícios de Leitura de Código

1. Analise o código abaixo e explique o que será exibido no terminal ao executar:

```python
from textual.app import App
from textual.widgets import Static

class Exemplo1(App):
    def compose(self):
        yield Static("Bem-vindo ao Textual!")

Exemplo1().run()
```

2. O que acontece se você alterar o texto do widget Static no exemplo acima para "Olá, mundo!"?

3. Observe o código a seguir. O que acontece ao pressionar o botão?

```python
from textual.app import App, ComposeResult
from textual.widgets import Button, Static

class Exemplo2(App):
    def compose(self) -> ComposeResult:
        yield Button("Clique", id="btn")
        yield Static("Aguardando...", id="msg")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one("#msg", Static).update("Botão pressionado!")

Exemplo2().run()
```

4. No exemplo acima, o que mudaria se o id do Static fosse alterado para "mensagem"?

5. Analise o código e explique o papel do método `compose`:

```python
class MinhaApp(App):
    def compose(self):
        yield Static("Texto 1")
        yield Static("Texto 2")
```

6. O que acontece se você adicionar mais widgets Static dentro do método `compose`?

7. Veja o código abaixo. O que será exibido após pressionar o botão duas vezes?

```python
from textual.app import App, ComposeResult
from textual.widgets import Button, Static

class ContadorApp(App):
    def __init__(self):
        super().__init__()
        self.contador = 0

    def compose(self) -> ComposeResult:
        yield Button("Incrementar", id="inc")
        yield Static(f"Valor: {self.contador}", id="valor")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.contador += 1
        self.query_one("#valor", Static).update(f"Valor: {self.contador}")

ContadorApp().run()
```

8. No exemplo acima, explique como o valor exibido é atualizado.

9. Analise o código e explique o que o método `query` faz:

```python
for widget in self.query(Static):
    widget.update("Atualizado!")
```

10. Dado o CSS abaixo, quais widgets serão afetados?

```css
Static {
    color: #fff;
}
#msg1 {
    background: #333;
}
.avisos {
    border: solid 2px #ff0;
}
```

---

Responda cada exercício explicando o funcionamento do código e os conceitos envolvidos.

