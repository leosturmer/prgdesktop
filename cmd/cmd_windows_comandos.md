### Árvore de Diretórios

Todos os arquivos de um computador estão armazenados em um banco de dados estruturado em árvore.

Uma **árvore de diretórios** é uma estrutura hierárquica usada para organizar e armazenar arquivos e pastas em um sistema de arquivos. Essa estrutura é chamada de "árvore" porque se assemelha a uma árvore invertida, onde:

- O **"tronco"** ou raiz é o diretório principal, chamado de **diretório raiz** (geralmente representado como `/` em sistemas Unix/Linux ou como uma unidade, como `C:\`, no Windows).
- Os **"galhos"** são os subdiretórios (pastas) que podem conter outros subdiretórios ou arquivos.
- As **"folhas"** são cada um dos arquivos que não possuem subdiretórios abaixo deles.


### Exemplo de uma árvore de diretórios:
```
/
├── home
│   ├── joao
│   │   ├── documentos
│   │   │   └── arquivo.txt
│   │   └── imagens
│   └── maria
├── var
└── etc
```

### Características principais:

1. **Hierarquia**: Cada diretório pode conter outros diretórios (subdiretórios) ou arquivos, formando uma relação de "pai e filho".
2. **Caminho Absoluto**: Cada arquivo ou pasta pode ser identificado por um caminho completo que começa na raiz e segue pelos subdiretórios até o destino.
   - Exemplo no Windows: `C:\Users\Joao\Documentos\arquivo.txt`
   - Exemplo no Linux: `/home/joao/documentos/arquivo.txt`
3. **Organização**: Essa estrutura facilita a organização lógica dos dados, permitindo que arquivos relacionados sejam agrupados em pastas específicas.

Essa estrutura é amplamente usada porque é intuitiva e escalável, permitindo que sistemas operacionais e usuários gerenciem grandes volumes de dados de forma eficiente.


### Comandos Mais Usados no CMD

- **`cls`**  
    Limpa a tela do terminal.  
    **Exemplo:**  
    ```cmd
    cls
    ```

- **`exit`**  
    Fecha o Prompt de Comando.  
    **Exemplo:**  
    ```cmd
    exit
    ```

- **`dir`**  
    Lista os arquivos e diretórios no diretório atual.  
    **Exemplo:**  
    ```cmd
    dir
    ```

- **`cd`**  
    Navega entre diretórios. Use `cd ..` para voltar ao diretório anterior.  
    **Exemplo:**  
    ```cmd
    cd C:\Users
    ```

- **`mkdir`**  
    Cria um novo diretório.  
    **Exemplo:**  
    ```cmd
    mkdir NovoDiretorio
    ```

- **`rmdir`**  
    Remove um diretório vazio.  
    **Exemplo:**  
    ```cmd
    rmdir NovoDiretorio
    ```

- **`del`**  
    Exclui arquivos.  
    **Exemplo:**  
    ```cmd
    del arquivo.txt
    ```

- **`attrib`**  
    Exibe ou altera atributos de arquivos.  
    **Exemplo:**  
    ```cmd
    attrib +r arquivo1.txt
    attrib +h arquivo2.txt
    attrib -r arquivo1.txt
    ```
    Os dois primeiros exemplos acima definem os atributo de:
    - "somente leitura" para o arquivo `arquivo1.txt`. Agora esse arquivo não pode ser modificado (inclusive, não pode ser apagado).
    - "escondido" para o arquivo `arquivo2.txt`. Agora esse arquivo não aparecerá na listagem de diretório.
    
    O terceiro exemplo *remove* o atributo `r` do arquivo `arquivo1.txt`. Agora o arquivo volta a poder ser modificado (inclusive, apagado).


- **`copy`**  
    Copia arquivos de um local para outro.  
    **Exemplo:**  
    ```cmd
    copy arquivo.txt C:\Backup
    ```

- **`move`**  
    Move arquivos de um local para outro.  
    **Exemplo:**  
    ```cmd
    move arquivo.txt C:\Documentos
    ```

