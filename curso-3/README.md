# RESUMO: Teste Avançado com Pytest

**Parametrização**

O recurso de parametrização do Pytest permite fornecer facilmente diferentes entradas para um teste que executa a mesma declaração. É útil em cenários onde você precisa testar várias condições ou casos de uso semelhantes. 

- **Quando usar a parametrização**: Dois cenários comuns que justificam o uso da parametrização são o uso de for-loops em testes e testes que declaram o mesmo comportamento repetidamente.

- **Problemas com for-loops**: Usar for-loops em testes pode ser problemático, pois torna difícil identificar exatamente quais itens falharam. Além disso, todas as combinações são consideradas como um único teste, o que dificulta a correção de falhas específicas.

- **Problemas com testes repetitivos**: Testes que declaram o mesmo comportamento repetidamente podem ser difíceis de manter e propensos a erros de digitação. Isso pode levar os engenheiros a evitar certos casos de uso.

- **Uso da parametrização**: Para usar a parametrização, importe o pytest como uma biblioteca e use o decorador `@pytest.mark.parametrize`. Este decorador permite que você especifique os parâmetros e os valores a serem testados.

- **Relatórios de teste avançados**: Pytest considera cada item na lista de parâmetros como um teste separado, o que permite relatar falhas de forma mais precisa. Ele mostra exatamente qual entrada falhou e onde.

- **Uso de vários argumentos**: Além de usar uma lista de itens como parâmetros, você também pode usar vários argumentos para parametrização. No entanto, tenha cuidado para não tornar os testes muito complexos.

A parametrização do Pytest é uma ferramenta poderosa para escrever testes mais eficientes e fáceis de manter. Ao evitar repetições e permitir testar várias condições de uma só vez, ela melhora a robustez e a legibilidade dos testes.

**Acessórios de Pytest**

O Pytest oferece a capacidade de usar acessórios, que são auxiliares para testes, permitindo configurar, fornecer dados ou realizar ações necessárias para testes de forma mais organizada e reutilizável. 

- **O que são acessórios**: Acessórios são auxiliares para testes em Pytest, semelhantes a funções ou métodos auxiliares, mas com a capacidade de ter sua própria configuração e código de limpeza.

- **Casos de uso dos acessórios**: Acessórios podem ser usados para fornecer dados prontos para uso, iniciar ou interagir com serviços externos (como bancos de dados), criar objetos com comportamento específico para testes e muito mais.

- **Criação de acessórios**: A criação de um acessório envolve a definição de uma função decorada com `@pytest.fixture`, que pode ter seu próprio escopo e código de limpeza. Os acessórios podem ser definidos em arquivos de teste ou em arquivos especiais chamados `conftest.py`, que são automaticamente disponibilizados para todos os testes no diretório.

- **Escopos de acessórios**: Os acessórios têm escopos como "função", "classe", "módulo" e "sessão", controlando quantas vezes são executados e quando são limpos. Isso permite uma execução eficiente e gerenciamento de recursos.

- **Limpeza de acessórios**: Os acessórios podem ser configurados para limpar recursos após o uso, garantindo que os testes sejam executados em um estado consistente e evitando vazamentos de recursos.

- **Acessórios internos do Pytest**: Pytest também fornece acessórios internos úteis, como `cache`, `capsys`, `tmpdir` e `monkeypatch`, que facilitam a realização de tarefas comuns de teste, como gerenciamento de cache, captura de saída padrão e substituição de comportamento de código.

- **Aplicação de patch e substituição**: O acessório `monkeypatch` permite substituir funções, métodos ou variáveis durante a execução dos testes, facilitando a simulação de cenários complexos, como a interação com recursos externos.

O uso adequado de acessórios pode tornar os testes mais eficientes, organizados e fáceis de manter, permitindo a criação de testes mais robustos e confiáveis para o código de produção.

## Verificação de conhecimentos
1)  Qual é um recurso útil da adição de acessórios ao arquivo conftest.py? 

( ) Isso permite importar esses acessórios para um conjunto de testes.

(X) Isso permite compartilhar os acessórios sem importá-los para um conjunto de testes.

( ) Porque permite que os acessórios exijam acessórios de Pytest.


2. O que faz um teste ser um bom candidato para parametrize()? 

(X) Quando um teste precisa fazer loop sobre entradas para a mesma declaração

( ) Quando um teste precisa capturar várias exceções.

( ) Quando um teste precisa ser executado em paralelo


3. Por que usar vários argumentos com a parametrização pode não ser uma boa ideia? 

( ) Porque Pytest não permite isso. Em vez disso, uma exceção é gerada.

( ) Porque as funções de teste não permitem vários argumentos.

(X) Porque isso pode tornar os testes mais difíceis de ler.