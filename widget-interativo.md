## Inserindo um Widget Interativo (Botão)

Neste exemplo, vamos adicionar um botão interativo à aplicação e exibir uma mensagem quando ele for pressionado.

### 1. Crie o arquivo `app_com_botao.py`

```python
from textual.app import App, ComposeResult
from textual.widgets import Button, Static

class BotaoApp(App):
    def compose(self) -> ComposeResult:
        yield Button("Clique aqui", id="meu_botao")
        yield Static("Aguardando interação...", id="mensagem")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        mensagem = self.query_one("#mensagem", Static)
        mensagem.update("Você clicou no botão!")

if __name__ == "__main__":
    BotaoApp().run()
```

### 2. Execute a aplicação

No terminal, rode:

```bash
python app_com_botao.py
```

A interface exibirá um botão e uma mensagem. Ao clicar no botão (usando Enter ou o mouse, se suportado), o texto da mensagem será atualizado para "Você clicou no botão!". Esse exemplo demonstra como tratar eventos e atualizar widgets dinamicamente, tornando a interface interativa.
