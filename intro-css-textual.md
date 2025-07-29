## Introdução ao Uso de CSS no Textual

O Textual traz para o desenvolvimento de interfaces em Python o poder e a flexibilidade do CSS, permitindo que você estilize widgets de forma declarativa e organizada, semelhante ao desenvolvimento web. O CSS do Textual é inspirado no padrão web, mas adaptado para o ambiente de terminal, possibilitando controle sobre cores, espaçamento, bordas, fontes, alinhamento e muito mais.

### DOM

O Document Object Model (DOM) é um conceito fundamental para o desenvolvimento de interfaces modernas, tanto na web quanto em frameworks como o Textual. 

No contexto do Textual, o DOM representa a estrutura hierárquica dos componentes (widgets) que compõem a interface da aplicação. Cada widget, como botões, textos, campos de entrada e containers, é um nó na *árvore DOM*.

Exemplo de árvore DOM de widgets em Textual:

```
App
│
├── Static (id="msg1")
│
├── Static (id="msg2")
│
├── Button (id="btn_all")
│
└── Button (id="btn_one")
```

Uma estrutura em árvore permite que o desenvolvedor visualize, manipule e interaja com cada elemento de forma organizada e eficiente.

A árvore DOM no Textual é construída a partir do método `compose`. Nesse método os widgets serão instanciados e organizados em uma hierarquia lógica (a árvore).

Uma estrutura em árvore facilita a navegação entre componentes, a aplicação de estilos CSS, a escuta de eventos e a atualização do estado da interface. Por exemplo, é possível buscar todos os widgets de um determinado tipo, encontrar um widget específico pelo id, ou aplicar estilos a um grupo de widgets que compartilham uma classe.

Assim como no desenvolvimento web, onde o DOM é utilizado para acessar e modificar elementos HTML dinamicamente, o Textual oferece métodos para consultar, atualizar e reagir a eventos dos widgets presentes na interface. Cada componente pode ser identificado por tipo, id ou classe, e manipulado individualmente ou em grupo.


### Como funciona o CSS no Textual?

Você pode definir estilos CSS em arquivos `.css` separados ou diretamente em strings dentro do código Python. Os estilos são aplicados aos widgets por meio de seletores (id, classe ou tipo), permitindo personalização granular da interface. O Textual processa o CSS e aplica os estilos aos widgets durante a renderização.

### Sintaxe do CSS no Textual

A sintaxe do CSS utilizada no Textual é muito semelhante à do CSS tradicional da web. Os estilos são definidos em blocos, onde cada bloco começa com um seletor (tipo, id ou classe) seguido por chaves `{}` contendo as propriedades e valores desejados. Cada propriedade é separada por ponto e vírgula e pode controlar aspectos visuais como cor, fundo, borda, espaçamento, alinhamento, fonte, entre outros.

Exemplo de sintaxe:

```css
Static {
    background: #222;
    color: #f5f5f5;
    border: solid #00ff00;
    padding: 1;
    text-align: center;
}

#msg1 {
    background: #004488;
    color: #fff;
    border: solid #ffcc00;
}

.minha-classe {
    background: #ffdddd;
    color: #880000;    
}

```

- **Seletores**: `Static` (tipo), `#msg1` (id), `.minha-classe` (classe)
- **Propriedades**: `color`, `background`, `border`, `padding`, `font-weight`, etc.
- **Valores**: cores em hexadecimal, valores numéricos para espaçamento, palavras-chave para estilos de fonte, etc.

O Textual interpreta esses estilos e aplica aos widgets correspondentes, permitindo personalização visual detalhada e consistente.

### Exemplo de Código: Estilizando Widgets Static com CSS

#### 1. Criando um arquivo CSS

Crie um arquivo chamado `estilos.css` com o seguinte conteúdo:

```css
Static {
    background: #222;
    color: #f5f5f5;
    border: solid #00ff00;
    padding: 1;
    text-align: center;
}

#msg1 {
    background: #004488;
    color: #fff;
    border: solid #ffcc00;
}

.minha-classe {
    background: #ffdddd;
    color: #880000;    
}

```

#### 2. Aplicando o CSS na aplicação

No seu código Python, carregue o CSS e utilize os seletores para estilizar os widgets:

```python
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
```

#### 3. Explicação dos estilos

- O seletor `Static` estiliza todos os widgets desse tipo.
- O seletor `#msg1` aplica estilos específicos ao widget com id `msg1`.
- O seletor `.minha-classe` estiliza widgets com a classe `minha-classe`.

Você pode combinar seletores para criar interfaces visualmente atraentes e organizadas, controlando cada aspecto dos widgets conforme a necessidade do projeto.

### Vantagens do CSS no Textual
- Separação clara entre lógica e apresentação.
- Reutilização e manutenção facilitada dos estilos.
- Flexibilidade para criar temas e personalizar a interface.
- Familiaridade para quem já trabalha com desenvolvimento web.
