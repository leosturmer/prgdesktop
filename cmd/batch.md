## Arquivos BATCH no Windows

Arquivos BATCH são scripts de texto simples usados no Windows para automatizar tarefas repetitivas. Eles contêm uma sequência de comandos que são executados em ordem pelo Prompt de Comando (CMD). Esses arquivos têm a extensão `.bat` ou `.cmd` e são amplamente utilizados para tarefas como manipulação de arquivos, configuração de ambiente e execução de programas.

### Exemplos de Arquivos BATCH

1. **Criar uma árvore de diretórios para um projeto simples em Python:**

```cmd
@echo off
cd C:\
mkdir MeuProjeto
cd MeuProjeto
mkdir src
mkdir tests
echo print("Hello, World!") > src\main.py
echo Projeto criado com sucesso!
```

2. **Escrever uma frase no terminal usando parâmetros recebidos em linha de comando:**

```cmd
@echo off
echo Olá, %1! Bem-vindo ao mundo dos arquivos BATCH.
```

*Como executar:*  
Salve o arquivo como `exemplo2.bat` e execute no CMD:  
```
exemplo2.bat João
```

3. **Criar uma árvore de diretórios cuja raiz é fornecida por linha de comando:**

```cmd
@echo off
if "%1"=="" (
    echo Por favor, forneça o nome do diretório raiz.
    exit /b
)
mkdir %1
cd %1
mkdir src
mkdir docs
mkdir bin
echo Estrutura de diretórios criada em %1.
```

*Como executar:*  
Salve o arquivo como `exemplo3.bat` e execute no CMD:  
```
exemplo3.bat MeuProjeto
```


### Uso de Variáveis em scripts BATCH
Em scripts BATCH, variáveis são usadas para armazenar e manipular valores, como strings ou números, durante a execução do script.

### Declaração e Uso de Variáveis

1. **Definir uma variável**:
   Use o comando `SET` para criar ou atribuir um valor a uma variável. Por exemplo:
   ```cmd
   SET minhaVariavel=Olá, Mundo!
   ```

2. **Acessar o valor de uma variável**:
   Para usar o valor de uma variável, coloque o nome dela entre `%`. Por exemplo:
   ```cmd
   ECHO %minhaVariavel%
   ```

3. **Variáveis com entrada do usuário**:
   Você pode usar o comando `SET /P` para solicitar que o usuário insira um valor:
   ```cmd
   SET /P nome=Digite seu nome: 
   ECHO Olá, %nome%!
   ```

4. **Variáveis de ambiente**:
   O BATCH também permite acessar variáveis de ambiente do sistema, como `%PATH%` ou `%USERNAME%`. Por exemplo:
   ```cmd
   ECHO O usuário atual é %USERNAME%
   ```

### Escopo de Variáveis
- As variáveis definidas com `SET` são locais ao script e não persistem após sua execução.
- Para criar variáveis persistentes, você precisará usar comandos como `SETX`.

### Exemplo Completo
Aqui está um exemplo de script BATCH que usa variáveis:
```cmd
@ECHO OFF
SET /P nome=Digite seu nome: 
SET idade=25
ECHO Olá, %nome%! Você tem %idade% anos.
PAUSE
```
