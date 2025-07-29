## Adicionando um Widget à Aplicação Textual

Agora, vamos criar um exemplo simples que mostra como adicionar um widget à interface usando o Textual. O widget mais básico é o `Static`, que exibe texto na tela.

### 1. Crie o arquivo `app_com_widget.py`

```python
from textual.app import App
from textual.widgets import Static

class WidgetApp(App):
    def compose(self):
        yield Static("Olá, este é um widget Static!")

if __name__ == "__main__":
    WidgetApp().run()
```

### 2. Execute a aplicação

No terminal, rode:

```bash
python app_com_widget.py
```

Você verá o texto "Olá, este é um widget Static!" centralizado na interface do terminal. O método `compose` é utilizado para definir os widgets que serão exibidos na aplicação. O Textual oferece diversos widgets prontos, como botões, campos de texto, listas e muito mais, permitindo criar interfaces ricas e interativas.

Esse exemplo serve como base para expandir sua aplicação, adicionando múltiplos widgets, layouts e interatividade conforme a necessidade do projeto.