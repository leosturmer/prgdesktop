from textual.app import App, ComposeResult
from textual.widgets import Static

class CSSApp(App):
    CSS_PATH = "estilos.css"

    def compose(self) -> ComposeResult:
        yield Static("Mensagem padrão", id="msg1")
        yield Static("Mensagem destacada", classes="minha-classe")
        yield Static("Outra mensagem")

if __name__ == "__main__":
    CSSApp().run()
