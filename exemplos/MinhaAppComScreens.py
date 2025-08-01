from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.binding import Binding
from textual.screen import Screen

class TelaInicial(Screen):
    def compose(self):
        yield Static("Esta é a tela inicial.")

class TelaSecundaria(Screen):
    def compose(self):
        yield Static("Esta é a tela secundária.")


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

if __name__ == "__main__":
    app = MinhaAppComScreens()
    app.run()