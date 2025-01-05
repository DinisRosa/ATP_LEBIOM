# Relatório da Interface Gráfica
## Algoritmos e Técnicas de programação
## Licenciatura em Engenharia Biomédica
### Autores: Pedro Gomes A107186, Dinis Rosa A107159
### Docentes: José Carlos Ramalho, Luís Filipe Cunha


#### Índice
1. [Introdução](#introdução)
2. [Análise e requisitos](#análise-e-requisitos)
    2.1. [Requisitos Funcionais](#requisitos-funcionais)
    2.2. [Requisitos Técnicos](#requisitos-técnicos)
3. [Conceção do Algoritmo](#conceção-do-algoritmo)  
    3.1. [Estrutura de dados](#estrutura-de-dados)
    3.2. [Algoritmos](#algoritmos) 
        3.2.1. [Linha de Comandos](#linha-de-comandos)
        3.2.2. [Janela Principal](#janela-principal)
        3.2.2. [Carregar Ficheiro](#carregar-ficheiro)
        3.2.3. [Eliminar Publicação](#eliminar-publicação)
        3.2.4. [Atualizar Publicação](#atualizar-publicação)
        3.2.5. [Procurar Publicação](#procurar-publicação)
        3.2.6. [Listar Autores](#listar-autores)
        3.2.7. [Listar Keywords](#listar-keywords)
        3.2.8. [Estatísticas de Publicação](#estatísticas-de-publicação)
        3.2.9. [Importar Dados](#importar-dados)
        3.2.10. [Exportar dados](#exportar-dados)
        3.2.11. [Help](#help)
4. [Problemas de Concretização](#problemas-de-concretização)
5. [Conclusão](#conclusão)

#### Nota
Todas as figuras encontram-se na pasta Figuras

#### Introdução
O presente projeto consiste no desenvolvimento de um sistema computacional robusto, concebido em linguagem Python, dedicado à consulta, armazenamento, criação e análise de publicações científicas. O principal objetivo deste sistema é proporcionar aos utilizadores uma ferramenta eficiente e intuitiva para a gestão de informações académicas, permitindo a pesquisa de artigos científicos através de filtros sofisticados, como data de publicação, palavras-chave, autores e outros critérios relevantes.

Para além disso, o sistema é capaz de gerar relatórios analíticos detalhados, complementados com gráficos ilustrativos que apresentam estatísticas pertinentes. Estas funcionalidades são de grande utilidade na análise de métricas relacionadas com os artigos e os respetivos autores, conferindo ao utilizador uma visão abrangente e estruturada dos dados em análise.

Este relatório integra o trabalho desenvolvido no âmbito da Unidade Curricular de Algoritmos e Técnicas de Programação e encontra-se organizado da seguinte forma:
   - Apresentação detalhada dos requisitos funcionais e técnicos do sistema, seguida de uma análise minuciosa dos mesmos;
   - Descrição da conceção da solução, incluindo a estratégia e o raciocínio subjacente ao desenvolvimento dos algoritmos implementados;
   - Discussão dos principais problemas enfrentados durante o processo de realização do projeto, acompanhada das soluções encontradas para os ultrapassar;
   - Reflexão conclusiva sobre o trabalho realizado, destacando os pontos fortes e as aprendizagens obtidas ao longo do processo.


#### Análise e requisitos
O sistema foi concebido para atender aos seguintes requisitos principais:

#### Requisitos Funcionais

- **Carregamento do Dataset:** O sistema deve proporcionar a capacidade de carregar, de forma eficiente, uma base de dados de publicações armazenada em formato JSON. Esta funcionalidade é essencial para permitir que os registos sejam manipulados em memória de maneira otimizada, assegurando maior agilidade nas operações subsequentes.

- **Criação de Publicações:** Deve ser possível adicionar novas publicações à base de dados existente. Para tal, o utilizador deve fornecer informações estruturadas, incluindo título, resumo, lista de palavras-chave, lista de autores (com dados detalhados como afiliação e identificador ORCID, se aplicável), data de publicação e links relevantes (ex.: DOI ou URL do artigo completo).

- **Atualização de Publicações:** O sistema deve permitir a edição de publicações existentes, possibilitando a modificação de campos como o resumo, palavras-chave ou informações dos autores. Esta funcionalidade garante a atualização dos registos para refletir dados corrigidos ou complementares.

- **Consulta de Publicações:** Os utilizadores devem poder pesquisar publicações com base em critérios específicos, tais como título, autores, palavras-chave ou intervalos de datas. Adicionalmente, deve ser oferecida a opção de ordenar os resultados por diversos parâmetros (ex.: ordem cronológica ou alfabética).

- **Relatórios e Gráficos:** O sistema deve ser capaz de gerar relatórios analíticos que apresentem estatísticas, como a distribuição de publicações por ano, a frequência de utilização de palavras-chave ou o número de publicações por autor. Estes relatórios devem incluir gráficos informativos que ilustrem os dados de forma clara e visualmente atraente.

- **Persistência de Dados:** Todas as alterações efetuadas nas publicações devem ser persistidas de forma segura no ficheiro JSON original ou em um novo ficheiro especificado pelo utilizador, assegurando a integridade dos dados ao longo do tempo.

- **Exportação e Importação de Dados:** Deve ser possível importar dados adicionais provenientes de outras bases e exportar subconjuntos de dados filtrados. Esta funcionalidade é essencial para aumentar a interoperabilidade do sistema e facilitar a partilha de informação.


##### Requisitos Técnicos
- **Implementação em Python:** Todas as funcionalidades foram desenvolvidas utilizando a linguagem Python, fazendo uso de sua biblioteca padrão e pacotes externos.
- **Interface Gráfica e CLI:** Duas interfaces foram criadas para interação com o usuário: Interface de Linha de Comando (CLI) para maior flexibilidade e Interface Gráfica (GUI), implementada com PySimpleGUI, para facilitar a utilização.

#### Conceção do Algoritmo
##### Estrutura de dados
O sistema organiza um acervo de publicações científicas em um ficheiro JSON. Cada publicação é descrita como um dicionário com várias propriedades, incluindo title, abstract, keywords, authors, doi, pdf, publish_date e url. O campo title é indispensável, enquanto os demais são opcionais.
O campo authors guarda uma lista de dicionários, onde cada dicionário descreve um autor, com seu nome (name), afiliação (affiliation).
As publicações podem ou não ter as chaves nomeadas em cima, no entanto, a chave 'title' é constante em todas.

###### Algoritmos
O sistema é alimentado por uma combinação de módulos Python que desempenham funções específicas na manipulação de dados e interação com o utilizador. Abaixo, detalhamos os principais módulos utilizados:
- json: Facilita a leitura e escrita de ficheiros no formato JSON, sendo essencial para carregar e guardar os dados das publicações.
- os: Permite operações relacionadas ao sistema de arquivos, como verificar caminhos e manipular ficheiros.
- PySimpleGUI: Responsável pela criação da interface gráfica, tornando possível interagir com o sistema por meio de janelas e botões intuitivos.
- matplotlib.pyplot: Utilizado para gerar gráficos interativos que ilustram estatísticas das publicações, como distribuições por ano ou por autores

###### Linha de Comandos
O sistema oferece duas opções de interação para o utilizador: a interface gráfica e a linha de comando.
- A função *GUI_main()* é projetada para usuários que preferem uma experiência visual e intuitiva, com botões e janelas.
- Para aqueles que optam pela simplicidade da linha de comando, a função *Terminal_Interface()* oferece uma abordagem textual mais direta.

###### Interface Gráfica Principal 
(FIGURA 1)
O utilizador interage com o sistema por meio de uma interface gráfica definida na função *GUI_main()*. Esta interface organiza suas funcionalidades em separadores intuitivos:
- Gestão de Publicações: Permite adicionar, atualizar ou apagar publicações.
- Estatísticas: Oferece visualizações gráficas sobre os dados, como distribuições anuais ou mensais.
- Pesquisa: Realiza buscas refinadas com base em critérios como título, autor ou palavras-chave.
- Visualizar publicações: lista as publicações pela ordem da base de dados
- Help: Exibe instruções de uso detalhadas para guiar o utilizador. (FIGURA 2)



##### GESTÃO DE PUBLICAÇÕES
###### Carregar Dados
(FIGURA 3)
A função *Carregar DataSet()* gerencia o processo de carregar os dados das publicações. O procedimento segue os passos abaixo:
1. Seleção do Ficheiro: O utilizador pode escolher manualmente um ficheiro JSON por meio de uma janela de seleção, ou o sistema pode usar um caminho predefinido.
2. Leitura dos Dados: O ficheiro selecionado é aberto em modo leitura utilizando a biblioteca json. Os dados são carregados e convertidos para uma estrutura de lista de dicionários.
3. Mensagem recebida: O utilizador irá receber a mensagem  ("DataSet carregado com sucesso!)numa nova janela. (FIGURA 3_1)
4. Validação: Caso o ficheiro não exista ou não possa ser acessado, o sistema emite uma mensagem de erro e inicializa a base de dados como vazia.
5. Retorno: A função retorna os dados carregados para serem manipulados pelas demais funcionalidades do sistema.

###### Guardar Dados
(FIGURA 4)
A função *Guardar DataSet()* é responsável por armazenar as alterações feitas nas publicações de volta em um ficheiro JSON. O processo segue as etapas abaixo:
1. Escolha do Local de Salvamento: O utilizador pode selecionar manualmente o caminho e o nome do ficheiro onde os dados serão salvos. Caso nenhum caminho seja especificado, utiliza-se um padrão predefinido.
2. Gravação dos Dados: O conteúdo do dataset em memória é convertido em formato JSON e gravado no ficheiro especificado utilizando a biblioteca json.
3. Tratamento de Erros: Se ocorrer algum erro durante o processo de gravação (por exemplo, falta de permissões), o sistema informa o utilizador através de uma mensagem de erro.
4. Salvamento Automático: Ao encerrar o sistema, os dados são salvos automaticamente em um ficheiro padrão (medical_papers_updated.json), garantindo que nenhuma alteração seja perdida.
5. Mensagem recebida: O utilizador irá receber a mensagem ("DataSet guardado com sucesso!) numa nova janela. (FIGURA 4-1)

###### Adicionar Publicação 
(FIGURA 5)
*criar_publicacao()*: Esta funcionalidade é acionada pelo botão "Adicionar Publicação" e permite ao utilizador criar e inserir uma nova entrada no conjunto de dados. O processo ocorre da seguinte forma:
1. Abertura da Janela: Uma nova janela é exibida, apresentando campos para preencher as propriedades da publicação, incluindo título, resumo, palavras-chave, autores, DOI, caminho para o PDF, URL e data de publicação.

2. Campos Obrigatórios: O título (title), resumo (abstract) e data de publicação (publish_date) são campos obrigatórios. 
Caso algum deles esteja vazio, uma mensagem de erro será exibida solicitando o preenchimento. (FIGURA 5-1)

3. Validação da Data: A data de publicação é validada para garantir que está no formato YYYY-MM-DD. Além disso, datas futuras não são aceitas, e o sistema notificará o utilizador em caso de erro. (FIGURA 5-2)

4. Adição de Autores: O campo de autores aceita múltiplos valores, separados por vírgulas. Cada autor pode conter o nome. Caso a estrutura esteja incorreta, uma mensagem de aviso será exibida.

5. Armazenamento Temporário: Os dados inseridos são armazenados temporariamente em um dicionário. Este dicionário é adicionado ao conjunto de dados em memória apenas após o utilizador confirmar.

6. Atualização do Dataset: Com todos os campos validados, a nova publicação é adicionada à lista de publicações em memória, exibindo a mesangem "Publicação adicionada com sucesso" (FIGURA 5_3) e salva no ficheiro JSON.

###### Apagar Publicação
(FIGURA 17)
*gerenciar_publicacoes()*: Esta funcionalidade é acionada pelo botão "Apagar Publicação" e permite ao utilizador remover uma publicação do conjunto de dados. O processo ocorre da seguinte forma:
1. Exibição da Lista de Publicações: O sistema apresenta uma lista com todas as publicações disponíveis, mostrando seus títulos para facilitar a identificação.
2. Seleção da Publicação: O utilizador seleciona a publicação que deseja apagar clicando no título correspondente.
3. Confirmação da Exclusão: Antes de remover a publicação, o sistema exibe uma janela de confirmação para garantir que a ação é intencional. (FIGURA 17_1)
4. Remoção do Dataset: Após a confirmação (FIGURA 17_2), a publicação selecionada é removida do conjunto de dados em memória utilizando o método .remove().
5. Atualização do Dataset: O sistema salva as alterações automaticamente no ficheiro JSON para garantir que a remoção seja permanente.



###### Atualizar Publicação
(FIGURA 18)
*atualizar_publicacao()*: Esta funcionalidade é acionada pelo botão "Atualizar Publicação" e permite ao utilizador modificar informações de uma publicação já existente. O processo detalhado é o seguinte:

1. Seleção da Publicação: O utilizador é apresentado com uma lista de títulos de todas as publicações disponíveis. Ele deve selecionar o título da publicação que deseja atualizar.
2. Exibição dos Dados Atuais: Após a seleção, uma nova janela é exibida com os campos preenchidos com os dados atuais da publicação. Isso inclui informações como título, resumo, palavras-chave, autores, DOI, caminho para o PDF, URL e data de publicação. (FIGURA 18_1)

3. Modificação dos Campos: O utilizador pode editar qualquer campo desejado. Campos como autores e palavras-chave permitem múltiplos valores, que devem ser separados por vírgulas. Os campos obrigatórios, como título e data de publicação, são validados novamente para garantir consistência.

4. Validação da Data: O sistema verifica se a nova data de publicação está no formato YYYY-MM-DD e se não é uma data futura. Caso a validação falhe, uma mensagem de erro será exibida e o utilizador deverá corrigir o valor.

5. Atualização dos Dados: Após a validação, as alterações feitas pelo utilizador são aplicadas à publicação selecionada no dataset em memória.

6. Confirmação e Salvamento: O sistema solicita uma confirmação antes de salvar as alterações. Após a confirmação, os dados atualizados são gravados no ficheiro JSON para garantir a persistência das mudanças, aparecendo posteriormente a mensagem "Publicação atualizada com sucesso!"



##### PESQUISA
###### Pesquisar Publicação
(FIGURA 14)
O botão **Pesquisar Publicação** é responsável por oferecer ao utilizador a possibilidade de localizar publicações específicas com base em critérios de busca. Quando acionado, ele exibe uma janela que permite selecionar um dos seguintes filtros:
- **Título**: Filtrar publicações que contenham uma palavra ou frase específica no título.
- **Autor**: Filtrar publicações associadas a um autor específico.
- **Data de Publicação**: Filtrar publicações por ano ou data completa (YYYY-MM-DD).
- **Palavras-chave**: Filtrar publicações que contenham palavras-chave específicas.
(FIGURA 15)

O objetivo do botão é tornar o processo de busca eficiente e flexível, utilizando diferentes critérios de pesquisa.

---

## Estrutura do Botão na Interface Gráfica
O botão está incluído na aba **Pesquisar** da interface principal, juntamente com outros recursos relacionados. Ao ser clicado, a função *pesquisar_publicacao()* é acionada.


## Funcionamento
### Ciclo de Eventos
A função *pesquisar_publicacao()* utiliza um ciclo para capturar eventos acionados pelos botões disponíveis. Dependendo do botão clicado, a função correspondente ao filtro é chamada.

1. **Voltar ou Fechar a Janela**:
   - Quando o botão "Voltar" é pressionado ou a janela é fechada, o fluxo é encerrado e retorna ao menu principal.

2. **Filtrar por Critérios**:
   - Ao pressionar qualquer botão de filtro, a função associada é acionada:
     - *filtro_titulo()* para busca por título.
     - *filtro_autor()* para busca por autor.
     - *filtro_data_publicacao()* para busca por data de publicação.
     - *filtro_palavras_chave()* para busca por palavras-chave.

---

## Descrição dos Filtros

### 1. Filtro por Título
(FIGURA 15_1)
- **Objetivo**: Localizar publicações cujo título contenha uma palavra ou frase específica.
- **Fluxo**:
  1. O utilizador insere um texto no campo de entrada.
  2. O texto é convertido para letras minúsculas para garantir buscas case-insensitive.
  3. A lista de publicações é percorrida, verificando se o texto inserido está contido nos títulos.
  4. As publicações correspondentes são exibidas. (FIGURA 15_2)

### 2. Filtro por Autor
- **Objetivo**: Buscar publicações associadas a um autor específico.
- **Fluxo**:
  1. O utilizador insere o nome do autor no campo de entrada.
  2. A lista de publicações é percorrida, verificando se o autor está presente na lista de autores da publicação.
  3. As publicações que contêm o autor especificado são exibidas.

### 3. Filtro por Data de Publicação
- **Objetivo**: Filtrar publicações por ano ou data completa.
- **Fluxo**:
  1. O utilizador insere uma data no formato `YYYY-MM-DD` ou apenas o ano.
  2. A lista de publicações é percorrida:
     - Caso o utilizador insira apenas o ano, são consideradas publicações que começam com o ano fornecido.
     - Caso uma data completa seja fornecida, ela deve coincidir exatamente com a data da publicação.
  3. As publicações correspondentes são ordenadas por data (mais recentes primeiro) e exibidas.

### 4. Filtro por Palavras-chave
- **Objetivo**: Localizar publicações que contenham palavras-chave específicas.
- **Fluxo**:
  1. O utilizador insere uma palavra-chave no campo de entrada.
  2. A lista de publicações é percorrida, verificando se a palavra-chave inserida está presente na lista de palavras-chave associadas às publicações.
  3. As publicações correspondentes são exibidas.

---

## Exibição dos Resultados
Os resultados da pesquisa são exibidos em uma nova janela. Esta janela apresenta:
- **Informações da Publicação**:
  - Título
  - Resumo
  - Palavras-chave
  - Autores
  - DOI
  - URL
  - Data de publicação
- **Opções Disponíveis**:
  - **Exportar Pesquisa**: Permite exportar os resultados em formato JSON.
  - **Fechar**: Fecha a janela de resultados e retorna ao menu principal.



###### Exportar Pesquisa  
Quando o evento 'Exportar Pesquisa' é detetado, a função *exportar_dados_parcial(dados_parciais)* é chamada.
(FIGURA 15_3)
1. **Descrição**  
- A função permite ao utilizador exportar os resultados de uma pesquisa em formato JSON.  

2. **Processamento**  
- Um diálogo é exibido para o utilizador selecionar o local e nome do arquivo usando *sg.popup_get_file()*.  
- Os dados da pesquisa são salvos no arquivo especificado com a função *json.dump()*.  

3. **Gestão de Erros**  
- Caso ocorra um erro durante a exportação, uma mensagem de erro é exibida usando *sg.popup_error()*.

###### Análise do Post
Quando o evento 'Análise do Post' é detetado, a função *analise_post()* é chamada.
(FiGURA 16)
1. Criação do Layout:
- A função *analise_post* cria um layout para a janela com três botões: "Análise por Autor", "Análise por Palavras-chave" e "Voltar".
- O layout é definido como uma lista de listas, onde cada sublista representa uma linha na janela.

2. Criação da Janela:

- A janela é criada usando *sg.Window* com o título "Análise do Post" e o layout definido anteriormente.

3. Loop de Eventos:

- A função entra em um loop *while run* para ler eventos e valores da janela.
- *evento, values = window.read()* lê o próximo evento e os valores dos elementos da janela.

4. Eventos da Janela:

Fechar a Janela ou Voltar:
- Se o evento for sg.WINDOW_CLOSED ou 'Voltar', a janela é fechada e a função retorna.
Análise por Autor:
- Se o evento for 'Análise por Autor', a função analisar_por_autor(base) é chamada e a função retorna, visualizando assim os resultados de pesquisa do autor. (FIGURA 16_1)

Análise por Palavras-chave:
- Se o evento for 'Análise por Palavras-chave', a função analisar_por_palavra_chave(base) é chamada e a função retorna.

###### ESTATÍSTICAS
(FIGURA 7)
Ao pressionar o botão 'Estatísticas' é criada uma janela com as opções de distrições que é possível executar, na forma de botões, uma área abaixo desse botão para exibir o resultado da distribuição e uma nova janela para visualização do gráfico da respetiva distribuição se assim for desejado pelo utilizador.

###### Distribuião por ano
Quando o evento 'Distribuição por Ano' é detetado, a função *gerar_grafico_publicacoes_por_ano(base)* é chamada.  

1. **Criação do Layout**  
- A função *gerar_grafico_publicacoes_por_ano* não cria uma interface gráfica adicional. Em vez disso, utiliza diretamente a biblioteca *matplotlib.pyplot* para exibir os dados em um gráfico.  
- O layout visual gerado consiste em um gráfico de barras com os seguintes elementos:
  - **Eixo X**: Representa os anos de publicação.
  - **Eixo Y**: Mostra o número de publicações em cada ano.
  - **Título**: "Distribuição de Publicações por Ano".  

2. **Processamento dos Dados**  
- A função percorre a lista de publicações (`base`) fornecida como parâmetro.  
- Para cada publicação:
  - Verifica se a chave `publish_date` está presente.
  - Extrai o ano da data de publicação (primeiros quatro caracteres).  
  - Usa um dicionário para contar a quantidade de publicações por ano.  
- Ordena o dicionário de anos para garantir que os dados sejam exibidos cronologicamente.  

3. **Gerar o  Gráfico**  
- Um gráfico de barras é criado com os dados processados:
  - *plt.bar()* cria as barras, usando os anos como rótulos do eixo X e o número de publicações como altura.  
  - *plt.xlabel()*, *plt.ylabel()* e *plt.title()* configuram os rótulos e o título do gráfico.  
- O gráfico é exibido com *plt.show()*.  
(FIGURA 8)

4. **Eventos da Janela**  
- O botão 'Distribuição por Ano' está definido no método *GUI_main()* na aba **Estatísticas** da interface gráfica.  
- Quando pressionado, a função *gerar_grafico_publicacoes_por_ano(base)* é chamada com a base de dados carregada.  

5. **Ciclo Completo**  
- O evento inicia a análise dos dados.
- O gráfico é exibido e, ao fechá-lo, o fluxo retorna à interface principal.  

###### Distribuião por mês

Quando o evento 'Distribuição por Mês' é detetado, a função *gerar_grafico_publicacoes_por_mes(base)* é chamada.  

1. **Criação do Layout**  
- A função *gerar_grafico_publicacoes_por_mes* cria uma interface gráfica adicional para selecionar o ano desejado. 
(FIGURA 9) 
- O layout consiste em:
  - **Texto**: "Selecione o ano".
  - **ComboBox**: Mostra a lista de anos disponíveis nas publicações.
  - **Botões**: "Gerar Gráfico" e "Cancelar".  

2. **Criação da Janela**  
- A janela é criada utilizando *sg.Window* com o título "Distribuição de Publicações por Mês" e o layout descrito anteriormente.  

3. **Loop de Eventos**  
- A função entra em um loop *while True* para ler os eventos e os valores da janela.
- *evento, values = window.read()* captura o evento atual e os valores dos elementos da janela.  

4. **Eventos da Janela**  
- **Fechar a Janela ou Cancelar**:
  - Se o evento for *sg.WINDOW_CLOSED* ou 'Cancelar', a janela é fechada e a função retorna.  
- **Gerar Gráfico**:
  - Se o evento for 'Gerar Gráfico', o valor selecionado no ComboBox é lido.
  - Se um ano válido for selecionado:
    - Os dados de publicações são filtrados por mês para o ano especificado.
    - Um gráfico de barras é criado com os meses no eixo X e o número de publicações no eixo Y.
    - O gráfico é exibido utilizando *plt.show()*. (FIGURA 9_1)
  - A janela é então fechada.  

5. **Processamento dos Dados**  
- A função inicializa um dicionário para os meses (de "01" a "12") com contagem zero.  
- Para cada publicação no ano selecionado:
  - Incrementa a contagem no mês correspondente.  
- Os meses são mantidos na ordem correta para o gráfico.  

6. **Gerar o Gráfico**  
- Um gráfico de barras é criado com os dados processados:
  - *plt.bar()* cria as barras, usando os meses como rótulos do eixo X e o número de publicações como altura.  
  - *plt.xlabel()*, *plt.ylabel()* e *plt.title()* configuram os rótulos e o título do gráfico.  
- O gráfico é exibido com *plt.show()*.  

###### Top Autores
Quando o evento 'Top Autores' é detetado, a função *gerar_grafico_top_autores(base)* é chamada.  

1. **Criação do Layout**  
- A função *gerar_grafico_top_autores* não cria uma interface gráfica adicional. Em vez disso, processa os dados diretamente e gera um gráfico horizontal.  
- O layout visual gerado consiste em:
  - **Eixo Y**: Lista dos autores com mais publicações (até os 20 principais autores).  
  - **Eixo X**: Número de publicações por autor.  
  - **Título**: "Top 20 Autores com Mais Publicações".  

2. **Processamento dos Dados**  
- A função inicializa um dicionário para armazenar a contagem de publicações por autor.  
- Para cada publicação na lista `base`:
  - Verifica se a chave `authors` está presente.
  - Extrai a lista de autores associados à publicação.  
  - Incrementa a contagem no dicionário para cada autor encontrado.  
- Ordena o dicionário de autores em ordem decrescente com base no número de publicações e seleciona os 20 primeiros autores.  

3. **Gerar o Gráfico**  
- Um gráfico de barras horizontal é criado com os dados processados:
  - *plt.barh()* cria as barras horizontais, usando os nomes dos autores como rótulos do eixo Y e o número de publicações como comprimento das barras.  
  - *plt.xlabel()*, *plt.ylabel()* e *plt.title()* configuram os rótulos e o título do gráfico.  
  - *plt.gca().invert_yaxis()* inverte o eixo Y para que o autor com mais publicações fique no topo.  
- O gráfico é exibido com *plt.show()*.  
(FIGURA 10)

4. **Eventos da Janela**  
- O botão 'Top Autores' está definido no método *GUI_main()* na aba **Estatísticas** da interface gráfica.  
- Quando pressionado, a função *gerar_grafico_top_autores(base)* é chamada com a base de dados carregada.  

5. **Ciclo Completo**  
- O evento inicia a análise dos dados.
- O gráfico é exibido e, ao fechá-lo, o fluxo retorna à interface principal.  

###### Publicações por Ano (autor)
Quando o evento 'Publicações por Ano (Autor)' é detetado, a função *gerar_grafico_publicacoes_por_ano_autor(base)* é chamada.  

1. **Criação do Layout**  
- A função *gerar_grafico_publicacoes_por_ano_autor* cria uma interface gráfica para selecionar o autor desejado.  
- O layout consiste em:
  - **Texto**: "Selecione o autor".  (FIGURA 11)
  - **ComboBox**: Lista de autores únicos encontrados nas publicações.  
  - **Botões**: "Gerar Gráfico" e "Cancelar".  

2. **Criação da Janela**  
- A janela é criada utilizando *sg.Window* com o título "Distribuição de Publicações por Ano (Autor)" e o layout definido.  

3. **Loop de Eventos**  
- A função entra em um loop *while* para capturar os eventos e os valores da janela.
- *evento, values = window.read()* lê os eventos da janela e os valores dos elementos do layout.  

4. **Eventos da Janela**  
- **Fechar a Janela ou Cancelar**:
  - Se o evento for *sg.WINDOW_CLOSED* ou 'Cancelar', a janela é fechada e a função retorna.  
- **Gerar Gráfico**:
  - Se o evento for 'Gerar Gráfico', o autor selecionado no ComboBox é lido.
  - Os dados são filtrados para obter as publicações do autor selecionado e organizados por ano.
  - Um gráfico de barras é gerado e exibido utilizando *plt.show()*. (FIGURA 11_1)
  - A janela é então fechada.  

5. **Processamento dos Dados**  
- A função inicializa um dicionário para armazenar as publicações por ano para o autor selecionado.  
- Para cada publicação:
  - Verifica se o autor está listado na publicação.
  - Incrementa a contagem no ano correspondente.  
- Ordena os anos para exibição cronológica.  

6. **Geração do Gráfico**  
- Um gráfico de barras é criado:
  - *plt.bar()* cria as barras, com os anos como rótulos do eixo X e o número de publicações como altura.  
  - *plt.xlabel()*, *plt.ylabel()* e *plt.title()* configuram os rótulos e o título do gráfico.  
- O gráfico é exibido com *plt.show()*.  

7. **Eventos do Fluxo**  
- O botão 'Publicações por Ano (Autor)' está definido no método *GUI_main()* na aba **Estatísticas**.  
- Quando pressionado, a função *gerar_grafico_publicacoes_por_ano_autor(base)* é chamada com a base de dados carregada.  

###### Top Palavras-chave
Quando o evento 'Top Palavras-chave' é detetado, a função *gerar_grafico_top_palavras_chave(base)* é chamada.  

1. **Criação do Layout**  
- A função *gerar_grafico_top_palavras_chave* não cria uma interface gráfica adicional. Em vez disso, processa os dados diretamente e gera um gráfico horizontal.  
- O layout visual gerado consiste em:
  - **Eixo Y**: Lista das palavras-chave mais frequentes (até as 20 principais).  
  - **Eixo X**: Frequência de uso de cada palavra-chave.  
  - **Título**: "Top 20 Palavras-chave Mais Frequentes".  

2. **Processamento dos Dados**  
- A função inicializa um dicionário para armazenar a frequência de cada palavra-chave.  
- Para cada publicação na lista `base`:
  - Verifica se a chave `keywords` está presente.
  - Extrai as palavras-chave, dividindo-as por vírgulas.
  - Incrementa a contagem no dicionário para cada palavra-chave encontrada.  
- Remove caracteres especiais das palavras-chave e garante que elas sejam tratadas de forma uniforme.  
- Ordena o dicionário em ordem decrescente com base na frequência e seleciona as 20 palavras-chave mais frequentes.  

3. **Geração do Gráfico**  
- Um gráfico de barras horizontal é criado:
  - *plt.barh()* cria as barras horizontais, usando as palavras-chave como rótulos do eixo Y e a frequência como comprimento das barras.  
  - *plt.xlabel()*, *plt.ylabel()* e *plt.title()* configuram os rótulos e o título do gráfico.  
  - *plt.gca().invert_yaxis()* inverte o eixo Y para que a palavra-chave mais frequente fique no topo.  
- O gráfico é exibido com *plt.show()*.  (FIGURA 12)

4. **Eventos da Janela**  
- O botão 'Top Palavras-chave' está definido no método *GUI_main()* na aba **Estatísticas** da interface gráfica.  
- Quando pressionado, a função *gerar_grafico_top_palavras_chave(base)* é chamada com a base de dados carregada.  

5. **Ciclo Completo**  
- O evento inicia a análise dos dados.
- O gráfico é exibido e, ao fechá-lo, o fluxo retorna à interface principal.  

###### Palavras-chave por Ano
Quando o evento 'Palavras-chave por Ano' é detetado, a função *gerar_grafico_palavras_chave_por_ano(base)* é chamada.  

1. **Criação do Layout**  
- A função *gerar_grafico_palavras_chave_por_ano* cria uma interface gráfica para selecionar o ano desejado.  
- O layout consiste em:
  - **Texto**: "Selecione o ano".  (FIGURA 13)
  - **ComboBox**: Lista de anos únicos encontrados nas publicações.  
  - **Botões**: "Gerar Gráfico" e "Cancelar".  

2. **Criação da Janela**  
- A janela é criada utilizando *sg.Window* com o título "Palavras-chave por Ano" e o layout definido.  

3. **Loop de Eventos**  
- A função entra em um loop *while* para capturar os eventos e os valores da janela.
- *evento, values = window.read()* lê os eventos da janela e os valores dos elementos do layout.  

4. **Eventos da Janela**  
- **Fechar a Janela ou Cancelar**:
  - Se o evento for *sg.WINDOW_CLOSED* ou 'Cancelar', a janela é fechada e a função retorna.  
- **Gerar Gráfico**:
  - Se o evento for 'Gerar Gráfico', o ano selecionado no ComboBox é lido.
  - Os dados são filtrados para obter publicações do ano especificado.
  - As palavras-chave das publicações são processadas e organizadas por frequência.
  - Um gráfico de barras é gerado e exibido utilizando *plt.show()*. (FIGURA 13_1)
  - A janela é então fechada.  

5. **Processamento dos Dados**  
- A função inicializa um dicionário para armazenar a frequência das palavras-chave nas publicações do ano selecionado.  
- Para cada publicação no ano especificado:
  - Verifica se a chave `keywords` está presente.
  - Extrai e limpa as palavras-chave, incrementando a contagem no dicionário.  
- As palavras-chave são ordenadas por frequência para exibição no gráfico.  

6. **Geração do Gráfico**  
- Um gráfico de barras é criado:
  - *plt.bar()* cria as barras, com as palavras-chave como rótulos do eixo X e a frequência como altura.  
  - *plt.xlabel()*, *plt.ylabel()* e *plt.title()* configuram os rótulos e o título do gráfico.  
  - *plt.xticks(rotation=45)* rotaciona os rótulos do eixo X para melhor visualização.  
- O gráfico é exibido com *plt.show()*.  

7. **Eventos do Fluxo**  
- O botão 'Palavras-chave por Ano' está definido no método *GUI_main()* na aba **Estatísticas**.  
- Quando pressionado, a função *gerar_grafico_palavras_chave_por_ano(base)* é chamada com a base de dados carregada.  

###### Visualizar Publicações
(FIGURA 6)
O botão **Listar Publicações** é uma funcionalidade destinada a exibir todas as publicações disponíveis, organizadas de forma clara e acessível. 
Apresentar uma lista completa de publicações, nomeando o título, em ordem cronológica ou personalizada.

#### Conclusão
Com este projeto, foi possível aplicar os conhecimentos adquiridos ao longo do semestre . O processo exigiu dedicação, com inúmeras horas de trabalho e resolução de problemas, consolidando a nossa aprendizagem por meio de um ciclo de tentativa e erro.
O suporte da Unidade Curricular foi essencial para o desenvolvimento dos algoritmos e da interface, proporcionando a base necessária para a manipulação de dados e bibliotecas.