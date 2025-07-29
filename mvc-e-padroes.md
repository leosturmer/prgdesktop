## Para entender o funcionamento dos widgets interativos

### Padrão Observer/Observable

O padrão Observer/Observable é um dos pilares do desenvolvimento de interfaces reativas. No contexto do Textual (e de muitos frameworks de UI), widgets e componentes podem "observar" eventos ou mudanças de estado. O objeto observável (por exemplo, um botão) emite eventos quando algo acontece (como um clique), e os observers (geralmente métodos ou outros componentes) reagem a esses eventos. Isso permite que diferentes partes da aplicação se comuniquem de forma desacoplada, facilitando a manutenção e a expansão do código.

No exemplo do botão, o próprio botão é o observável, e o método `on_button_pressed` é o observer, que reage ao evento de clique.

### O que é um método callback (event handler)

Um callback é uma função ou método passado como argumento ou definido para ser chamado em resposta a um evento específico. No Textual, métodos como `on_button_pressed` são callbacks: eles são automaticamente chamados pelo framework quando o evento correspondente ocorre. Esses métodos recebem informações sobre o evento (por exemplo, qual botão foi pressionado) e podem executar ações, como atualizar a interface ou modificar o estado da aplicação.

No exemplo, `on_button_pressed` é um callback que atua como event handler para o evento de clique do botão. O Textual detecta o evento e chama esse método, permitindo que o desenvolvedor defina o comportamento desejado.

### O papel dos eventos de interface na arquitetura MVC

O Textual utiliza conceitos clássicos de design de software para criar interfaces interativas e reativas, facilitando o desenvolvimento de aplicações desktop modernas com Python.

A arquitetura MVC (Model-View-Controller) separa a lógica de negócio (Model), a interface (View) e o controle de fluxo (Controller). No Textual, os eventos de interface (como cliques, teclas pressionadas, etc.) são fundamentais para essa separação. Os widgets (View) emitem eventos, e os métodos event handlers (Controller) recebem esses eventos e decidem como reagir, muitas vezes alterando o estado do Model ou atualizando a View.

O Textual implementa esse fluxo de forma natural: os widgets disparam eventos, os métodos de callback tratam esses eventos e, conforme necessário, atualizam outros componentes ou o estado da aplicação. Isso permite criar aplicações organizadas, escaláveis e fáceis de manter, seguindo os princípios do MVC.


## Exemplos de Código Ilustrando os Conceitos

Estes exemplos de código ilustram como os conceitos de observer/observable, callbacks e eventos na arquitetura MVC são aplicados na prática com o Textual.

### Exemplo do padrão Observer/Observable

No Textual, o padrão observer/observable é implementado através dos eventos e dos métodos que os observam. Veja um exemplo simples:

```python
from textual.app import App
from textual.widgets import Button, Static

class ObserverApp(App):
    def compose(self):
        yield Button("Clique para notificar", id="notificador")
        yield Static("Nenhuma notificação ainda.", id="observador")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        observador = self.query_one("#observador", Static)
        observador.update("O botão notificou o observador!")
```

Neste exemplo, o botão é o observável e o método `on_button_pressed` é o observer, que reage ao evento emitido pelo botão.

### Exemplo de método callback (event handler)

O método abaixo é um callback que será chamado automaticamente pelo framework quando o evento de clique ocorrer:

```python
    def on_button_pressed(self, event: Button.Pressed) -> None:
        print(f"Botão pressionado: {event.button.id}")
```

Esse método é registrado pelo Textual como handler do evento `Button.Pressed` e será chamado sempre que qualquer botão for pressionado.

### Exemplo do papel dos eventos na arquitetura MVC

No Textual, a separação entre Model, View e Controller pode ser ilustrada assim:

```python
from textual.app import App
from textual.widgets import Button, Static

# Model: estado da aplicação
class Contador:
    def __init__(self):
        self.valor = 0

class MVCApp(App):
    def __init__(self):
        super().__init__()
        self.contador = Contador()

    def compose(self):
        yield Button("Incrementar", id="btn_inc")
        yield Static(f"Valor: {self.contador.valor}", id="lbl_valor")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_inc":
            self.contador.valor += 1  # Controller altera o Model
            label = self.query_one("#lbl_valor", Static)
            label.update(f"Valor: {self.contador.valor}")  # Atualiza a View
```

Neste exemplo, o botão (View) emite o evento, o método handler (Controller) trata o evento e altera o estado do contador (Model), atualizando a interface (View) conforme o padrão MVC.

