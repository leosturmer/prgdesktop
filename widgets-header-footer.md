## Usando os Widgets `Header` e `Footer` em Aplicações Textual

Os widgets `Header` e `Footer` são componentes prontos fornecidos pelo framework Textual. Eles ajudam a estruturar a interface, fornecendo áreas dedicadas para informações de contexto, navegação, atalhos e status da aplicação.

### O que são `Header` e `Footer`?

- **Header**: Exibe um cabeçalho no topo da aplicação, geralmente contendo o nome do aplicativo, informações do usuário...
- **Footer**: Exibe um rodapé na parte inferior, normalmente mostrando dicas de teclas, status, mensagens rápidas ou informações associadas ao contexto.

Esses widgets se adaptam automaticamente ao tema e ao layout da aplicação Textual.

---

### Por que usar `Header` e `Footer`?

- **Padronização**: Proporcionam uma aparência profissional e consistente.
- **Usabilidade**: Facilitam a navegação e o entendimento da interface pelo usuário.
- **Produtividade**: Permitem adicionar informações úteis (atalhos, status, título) sem esforço extra de layout.

---

### Exemplo Prático: Aplicação Mínima com `Header` e `Footer`

A seguir, um exemplo completo de como criar uma aplicação mínima utilizando esses widgets:

```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class AppComHeaderFooter(App):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)  # Exibe o cabeçalho com relógio
        yield Static("Bem-vindo à aplicação com Header e Footer!")
        yield Footer()  # Exibe o rodapé padrão

if __name__ == "__main__":
    AppComHeaderFooter().run()
```

#### Explicação do Código

- `Header(show_clock=True)`: Cria um cabeçalho que, além do nome da aplicação, exibe um relógio digital no canto direito.
- `Static(...)`: Um widget central apenas para exibir uma mensagem.
- `Footer()`: Adiciona um rodapé padrão, que mostra dicas de teclas úteis como `ctrl+c` para sair, `ctrl+q` para fechar, entre outros.

---

### Personalizando o Header

O widget `Header` pode ser personalizado com argumentos como:

- `show_clock`: Mostra ou oculta o relógio.
- `time_format`: Define o formato do relógio. Ex: `%H:%M` Horas e Minutos; `%X` Horas, minutos e segundos.
- `icon`: Um único caractere que será usado como ícone

Exemplo:

```python
yield Header(show_clock=True, icon='❤', time_format="%X")
```

---

### Personalizando o Footer

O `Footer` pode ser customizado para exibir dicas de teclas específicas, status ou mensagens personalizadas. Por padrão, ele já mostra os atalhos mais comuns, mas você pode criar um rodapé customizado se necessário.

---

### Dicas de Uso

- Sempre adicione o `Header` antes dos demais widgets para garantir que ele fique no topo.
- O `Footer` deve ser adicionado por último para aparecer na base da interface.
---

### Exemplo Completo com Interatividade

```python
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
```



Para saber mais, consulte a [documentação oficial do Textual](https://textual.textualize.io/widgets/header/), explore as opções de personalização desses widgets.