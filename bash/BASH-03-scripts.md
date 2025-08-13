# Scripts com BASH

Muitas tarefas cotidianas que realizamos com o BASH são bastante repetitivas. Tarefas como a de criar um ambiente de trabalho em linha de comando, que fizemos na aula passada, podem ser automatizadas com scripts.

> Um script é programa curto, que realiza uma tarefa bem específica, e que é composto por uma sequência de operações (comandos) que o computador deve realizar.

Um script BASH é uma sequência de linhas de comando salvas em um arquivo de texto que tem o seguinte formato:

```bash
#!/bin/bash

e aqui
escrevemos
uma linha de comando
por vez...
```

> A primeira linha é um código que informa ao BASH que este é um arquivo de script e que a linguagem usada para escrever ele pode ser interpretada pelo programa que está no caminho indicado na linha.

Por exemplo, este script cria um diretório chamado `trab` no diretório atual e dentro dele coloca um arquivo vazio chamado tarefas.txt.

```bash
#!/bin/bash
mkdir trab
cd trab
touch tarefas.txt
cd ..
```

Quando rodamos esse script, o BASH executa linha por linha dele, como se estivéssemos digitando elas no console.

Para rodar um script, o arquivo de texto que contém ele precisa ter `permissão de execução` para nosso usuário.

Para dar permissão de execução a um arquivo, usamos o comando `chmod` com a opção `u+x`.

- `u` significa `usuário`
- `+` significa `dar permissão`
- `x` significa `execução`.

Exemplo:

1. Salve o script do exemplo em um arquivo chamado `cproj` (de, criar projeto)
2. Dê permissão de execução ao script

```bash
$chmod u+x cproj
```

Rode o script usando a linha de comando abaixo:
```bash
$./cproj
```

Para confirmar que tudo correu bem, liste o diretório e veja se o resultado foi o esperado.
