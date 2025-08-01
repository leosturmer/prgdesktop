from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class AppComHeaderFooter(App):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True, icon='❤', time_format="%X")  # Exibe o cabeçalho com relógio
        yield Static("Bem-vindo à aplicação com Header e Footer!")
        yield Footer()  # Exibe o rodapé padrão

if __name__ == "__main__":
    AppComHeaderFooter().run()