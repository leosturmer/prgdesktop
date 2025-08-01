## O que é a classe App no Textual?

A classe `App` é o ponto central de qualquer aplicação desenvolvida com o framework Textual. Ela representa a aplicação em si, sendo responsável por gerenciar o ciclo de vida, a árvore de widgets (DOM), eventos, estilos, temas e a interação do usuário.

### Papel da classe App

- **Gerenciamento do ciclo de vida**: Inicializa, executa e encerra a aplicação.
- **Composição da interface**: Define quais widgets compõem a interface, geralmente através do método `compose`.
- **Gerenciamento de eventos**: Recebe e distribui eventos de teclado, mouse e widgets, permitindo a implementação de callbacks (event handlers).
- **Estilização**: Permite aplicar temas e CSS para personalizar a aparência dos widgets.
- **Acesso ao DOM**: Fornece métodos para consultar, atualizar e manipular widgets dinamicamente.

A class App serve de container para telas (subclasses de Screen) e dá à aplicação o loop principal de eventos.


### Como funciona a classe App

Para criar uma aplicação com Textual, você deve criar uma subclasse de `App` e sobrescrever métodos conforme necessário. O método mais importante é o `compose`, onde você define a hierarquia de widgets da interface.

Exemplo básico:

```python
from textual.app import App, ComposeResult
from textual.widgets import Static

class MinhaApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Olá, mundo!")

if __name__ == "__main__":
    MinhaApp().run()
```

#### Principais métodos e propriedades

- `compose(self)`: Método que deve ser sobrescrito para definir os widgets da interface.
- `run(self)`: Inicia o loop principal da aplicação.
- `on_event(self, event)`: Permite tratar eventos genéricos.
- `on_<widget>_<evento>(self, event)`: Handlers automáticos para eventos específicos (ex: `on_button_pressed`).
- `query` e `query_one`: Métodos para buscar widgets no DOM.
- `CSS_PATH` ou `CSS`: Permite definir o caminho para arquivos CSS ou estilos inline.

#### Ciclo de vida resumido

1. A aplicação é criada instanciando a subclasse de `App`.
2. O método `run()` é chamado, inicializando o ambiente e a interface.
3. O método `compose()` é executado para montar a árvore de widgets.
4. O loop de eventos é iniciado, processando entradas do usuário e atualizações de interface.
5. Ao encerrar, o Textual finaliza o terminal e libera recursos.


Veja mais sobre o ciclo de vida da aplicação aqui:
[https://deepwiki.com/Textualize/textual#application-lifecycle](https://deepwiki.com/Textualize/textual#application-lifecycle)

### Referências

- [Overview do Textual no DeepWiki](https://deepwiki.com/Textualize/textual/1-overview)
- [Documentação oficial do Textual](https://textual.textualize.io/)
