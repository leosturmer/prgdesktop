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

O código inicia importando App e o widget Static do framework Textual. 
Em seguida, é criada a classe Exemplo1, herdada de App, que faz a aplicação funcionar dentro do Textual.
Então é criado um método de composição da tela, onde é criado um widget do tipo Static que mostra a mensagem "Bem-vindo ao Textual!".
Por fim, é chamada a classe Exemplo1() com o método run() para rodar o programa.

-----------------------------------------------------------------------------------------------------------

2. O que acontece se você alterar o texto do widget Static no exemplo acima para "Olá, mundo!"?

Quando alterado, o texto que aparece no programa se tornará "Olá, mundo!".

-----------------------------------------------------------------------------------------------------------

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

O código inicia importanto App e ComposeResult do framework Textual, bem como os widgets Button e Static.
Em seguida, é criada a classe Exemplo2, que herda funções da classe App.
É criada a composição da tela, onde se espera um resultado do tipo ComposeResult. 
Nessa composição, há um botão escrito "Clique" e com o id "btn" e um Static escrito "Aguardando..." com o id "msg".

Outra função é definida para acontecimento de clique no botão. Nesta função, é utilizado o método "query_one" 
que busca, na árvore de widgets, o widget com id "msg" do tipo Static e atualiza a mensagem dele para "Botão Pressionado".

-----------------------------------------------------------------------------------------------------------

4. No exemplo acima, o que mudaria se o id do Static fosse alterado para "mensagem"?

Se o id do Static fosse modificado para "mensagem", o programa não conseguirá encontrar o widget com este id, logo dará um erro.
Se mudar o id para "mensagem", será necessário, dentro do query_one, modificar para "#mensagem".

-----------------------------------------------------------------------------------------------------------

5. Analise o código e explique o papel do método `compose`:

```python
class MinhaApp(App):
    def compose(self):
        yield Static("Texto 1")
        yield Static("Texto 2")
```

No Textual, o método "compose" serve para criar a composição da tela. 
Neste exemplo, a tela é composta com dois widgets Static, um com o texto "Texto 1" e outro com o texto "Texto 2".

-----------------------------------------------------------------------------------------------------------

6. O que acontece se você adicionar mais widgets Static dentro do método `compose`?

Quanto mais widgets forem adicionados, mais widgets aparecerão na tela "MinhaApp()".
Eles aparecerão por ordem que estão posicionados. 

-----------------------------------------------------------------------------------------------------------

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

O programa utiliza Textual. 
Dentro da tela ContadorApp, ele tem um contador que é inicializado em 0.
Dentro da composição da tela, há um botão "Incrementar" e um static "Valor" que mostra o número do contador.
O botão, quando pressionado, adiciona um número ao contador e atualiza o valor do contador no estático.

Se pressionado duas vezes, o botão irá mostrar o número 2.

-----------------------------------------------------------------------------------------------------------

8. No exemplo acima, explique como o valor exibido é atualizado.

O valor é atualizado por dois motivos: o contador e pelo botão.
O botão, quando pressioando, tem duas funções:
- somar 1 ao valor do contador
- atualizar o valor do contador dentro do static

-----------------------------------------------------------------------------------------------------------

9. Analise o código e explique o que o método `query` faz:

```python
for widget in self.query(Static):
    widget.update("Atualizado!")
```

O código é um loop que pega todos os widgets static e atualiza o texto para "Atualizado!".
Neste caso, o método query está pegando todos os widgets do tipo static, e não apenas um.

-----------------------------------------------------------------------------------------------------------

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

A partir do CSS, serão afetados os seguintes widgets da seguinte maneira:
- Static: todos widgets do tipo Static receberão a cor dos textos #fff
- #msg1: o widget com id msg1 terá a cor de fundo alterada para #333
- .avisos: os widgets com a classe avisos receberão uma borda solid 2px da cor #ff0


---

Responda cada exercício explicando o funcionamento do código e os conceitos envolvidos.

