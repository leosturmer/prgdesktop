from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static

class DemoAppHeaderFooter(App):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True, icon='😉', time_format="%X")
        yield Static("Pressione o botão abaixo para interagir:")
        yield Button("Clique aqui", id="btn1")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(Static).update("Você clicou no botão!")

if __name__ == "__main__":
    DemoAppHeaderFooter().run()