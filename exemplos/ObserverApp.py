from textual.app import App
from textual.widgets import Button, Static

class ObserverApp(App):
    def compose(self):
        yield Button("Clique para notificar", id="notificador")
        yield Static("Nenhuma notificação ainda.", id="observador")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        observador = self.query_one("#observador", Static)
        observador.update("O botão notificou o observador!")

if __name__ == "__main__":
    ObserverApp().run()