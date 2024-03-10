# RESUMO: Fazer testes com Pytest 

**O que é Pytest?**
O Pytest é um framework de teste em Python que facilita a escrita e execução de testes automatizados para código Python. Ele é altamente configurável e pode tratar pacotes de testes complexos.

**Convenções**
- Diretório de testes: Usa o diretório "tests" para organizar arquivos de teste e diretórios de teste aninhados.
- Nomenclatura de arquivos de teste: Prefere arquivos com o prefixo "test_" para indicar que contêm código de teste.
- Nomenclatura de funções de teste: Prefixa funções de teste com "test_" para que o Pytest possa coletá-las automaticamente.
- Classes de teste e métodos de teste: Utiliza prefixos "Test" para classes de teste e "test_" para métodos de teste.
- Execução de testes: Pytest é um executor de testes que coleta, inicia e executa testes automaticamente, fornecendo relatórios detalhados ao final da execução.
- Instrução assert: Pytest habilita a instrução assert para executar comparações avançadas, fornecendo relatórios detalhados de falhas, inclusive com objetos complexos como listas e dicionários.

Essas convenções e recursos tornam o Pytest uma escolha popular para testes automatizados em Python, facilitando o processo de escrita e execução de testes.

**Métodos e classes de teste**
O Pytest permite escrever testes usando classes, oferecendo mais flexibilidade e reutilização. As classes de teste no Pytest seguem algumas regras simples, sem a necessidade de herança. Aqui está um resumo:

- **Criar uma classe de teste**: Você pode criar uma classe de teste que contém métodos de teste. Por exemplo, uma classe `TestIsDone` pode ter métodos `test_yes` e `test_no`.
  
- **Métodos auxiliares**: Pytest oferece métodos auxiliares como `setup` e `teardown` para configuração e limpeza antes e após cada teste, respectivamente. Também existem `setup_class` e `teardown_class`, executados uma vez antes e após todos os testes na classe.
  
- **Exemplo prático**: Um exemplo prático seria uma classe de teste `TestIsDone` que verifica se um arquivo contém "sim" ou "não". Os métodos de teste criam e verificam o conteúdo do arquivo.

- **Personalização dos métodos auxiliares**: Você pode personalizar esses métodos auxiliares de acordo com as necessidades do seu teste. Por exemplo, você pode adicionar um método auxiliar `write_tmp_file` para escrever conteúdo em um arquivo temporário.

- **Quando usar uma classe**: Não há regras rígidas sobre quando usar uma classe em vez de uma função. No entanto, algumas considerações incluem a necessidade de configuração ou limpeza comum entre testes, agrupamento lógico de testes relacionados e benefícios de reutilização de métodos auxiliares.

## Verificação de conhecimentos
1)  Por que é útil usar instruções assert simples com os testes do Pytest? 

( ) Isso faz com que os testes sejam executados mais rapidamente.

(X) Isso permite que você use operadores Python para qualquer comparação.

( ) Isso permite que os testes sejam executados em paralelo.


2) Qual é um motivo para agrupar testes em uma classe de teste? 

(X) Para que os testes possam se beneficiar de uma configuração ou limpeza comum.

( ) Para que os testes possam aproveitar o uso de instruções de declaração simples.

( ) Para que os testes possam ser randomizados para obter uma melhor cobertura.


3) Pytest pode ser usado como uma biblioteca de Python para testes? 

( ) Não, Pytest não tem outros módulos e auxiliares para serem usados como uma biblioteca.

( ) Não, Pytest só permite extensibilidade por meio de plug-ins.

(X) Sim, o Pytest tem módulos e auxiliares que você pode importar em seus testes.