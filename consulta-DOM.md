##  Consulta a Componentes com `query` e `query_one` no DOM da Aplicação

A consulta a componentes é uma funcionalidade poderosa do Textual, permitindo que você acesse e manipule widgets da interface de forma dinâmica. 

O Textual mantém em memória uma árvore de componentes (DOM - Document Object Model), semelhante ao DOM do HTML, onde cada widget pode ser identificado por um id, classe ou tipo.

A consulta a componentes com `query` e `query_one` é essencial para criar interfaces flexíveis e dinâmicas no Textual, aproximando o desenvolvimento desktop do paradigma web e facilitando a manutenção e evolução das aplicações.

### Explicação

Os métodos `query` e `query_one` são utilizados para buscar componentes na árvore de widgets:
- `query(selector)`: retorna um iterador sobre todos os componentes que correspondem ao seletor informado.
- `query_one(selector, tipo)`: retorna o primeiro componente que corresponde ao seletor e tipo informado.

O seletor pode ser um id (`#id_do_componente`), uma classe (`.classe_do_componente`) ou o nome do tipo do widget (`Static`, `Button`, etc). Com esses seletores podemos localizar componentes específicos para atualizar seus estados, modificar seus conteúdos ou aplicar estilos a eles.

### Exemplo de Código

Vamos criar uma aplicação que possui vários widgets e utiliza consultas para atualizar e interagir com eles:

```python
from textual.app import App, ComposeResult
from textual.widgets import Button, Static

class ConsultaApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Mensagem inicial", id="msg1")
        yield Static("Outra mensagem", id="msg2")
        yield Button("Atualizar todas", id="btn_all")
        yield Button("Atualizar uma", id="btn_one")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_all":
            # Atualiza todos os widgets Static
            for widget in self.query(Static):
                widget.update("Atualizado pelo botão 'Atualizar todas'!")
        elif event.button.id == "btn_one":
            # Atualiza apenas o widget com id 'msg1'
            widget = self.query_one("#msg1", Static)
            widget.update("Atualizado pelo botão 'Atualizar uma'!")
```

### Explicação do Funcionamento

- O método `self.query(Static)` retorna todos os widgets do tipo `Static` presentes na interface. O loop percorre cada um deles e atualiza seu conteúdo.
- O método `self.query_one("#msg1", Static)` retorna apenas o widget com id `msg1` e tipo `Static`, permitindo atualização individual.
- Os seletores podem ser combinados para buscas mais refinadas, como widgets de uma determinada classe ou com atributos específicos.

#### Seletores Comuns
- `#id`: busca por id único do componente.
- `.classe`: busca por classe (útil para agrupar widgets).
- `Tipo`: busca por tipo de widget (ex: `Static`, `Button`).

### Vantagens da Consulta no DOM
- Permite manipular dinamicamente qualquer parte da interface.
- Facilita a implementação de lógica reativa e interativa.
- Torna o código mais organizado e desacoplado, pois não é necessário manter referências diretas a todos os widgets.
