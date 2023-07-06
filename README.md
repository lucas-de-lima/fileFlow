# :construction: README em construção ! :construction:

Olá! Apresento a você o pacote FileFlow, um projeto que visa facilitar o gerenciamento de arquivos por meio de uma fila otimizada. Com o FileFlow, você poderá importar notícias de arquivos TXT, processá-las e armazená-las de forma eficiente na fila.

A fila implementada segue o princípio FIFO, garantindo que o primeiro arquivo a entrar seja o primeiro a sair. Você poderá realizar operações de inserção, remoção e busca de elementos na fila, tudo isso utilizando estruturas de dados otimizadas.

Além disso, o pacote oferece funções para importar os arquivos TXT, tratando erros caso o arquivo não exista ou possua um formato inválido. Após importar as notícias, você poderá processá-las e armazenar as informações em um dicionário, que será inserido na fila. A cada nova inserção válida, os dados processados serão exibidos na saída padrão.

Caso deseje remover o primeiro arquivo processado, basta utilizar a função apropriada, que irá emitir uma mensagem informando o sucesso da remoção. Também é possível obter informações superficiais de um arquivo processado, fornecendo o índice correspondente.

E para garantir a qualidade do código, implementamos testes para a classe PriorityQueue, responsável por armazenar arquivos pequenos de forma prioritária na fila. Com esses testes, verificamos se a lógica de prioridades está sendo respeitada nos métodos de inserção, remoção e busca.

Com o pacote FileFlow, você terá uma solução eficiente e confiável para o gerenciamento de arquivos. Aproveite todas as funcionalidades e desfrute de uma experiência aprimorada no processamento e organização de seus dados.
