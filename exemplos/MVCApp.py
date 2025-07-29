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

if __name__ == "__main__":
    MVCApp().run()