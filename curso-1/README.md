# RESUMO: Introdução a testes no Python

unittest é um módulo de teste integrado ao Python, permitindo a criação e execução de testes automatizados. Para usá-lo, escreva testes como métodos em classes herdando de unittest.TestCase e execute os testes usando a linha de comando `unittest.main()`

É recomendado seguir convenções de nomenclatura específicas. Classes de teste devem começar com "Test" em camelcase, enquanto os métodos devem começar com "test_" separados por sublinhado. Isso facilita a identificação e execução dos testes.

As asserções são usadas para verificar se determinadas condições são verdadeiras durante a execução dos testes. O módulo unittest fornece vários métodos de asserção, como `assertEqual`, `assertTrue`, `assertFalse`, entre outros, para comparar valores, verificar condições e validar o comportamento esperado do código durante os testes. Essas asserções são fundamentais para garantir a corretude dos testes e a robustez do código testado.

Testes são fundamentais em projetos de software para garantir a robustez do código. A falta de testes pode levar a um código complexo e frágil, difícil de entender e manter. Códigos não testados são frequentemente difíceis de compreender e podem crescer em complexidade, tornando-se cada vez mais difíceis de gerenciar.

Testes lentos ou não confiáveis podem comprometer o ciclo de desenvolvimento, dificultando a identificação rápida de problemas e a validação do comportamento do código. A automação dos testes é essencial para evitar erros e garantir a confiabilidade do software, reduzindo tarefas repetitivas e aumentando a confiança no código.

Ferramentas como cobertura de teste, execução de testes e ambientes de integração contínua/distribuição contínua (CI/CD) são cruciais para facilitar e fortalecer o processo de teste, permitindo uma análise precisa do código testado e não testado, execução automática de testes e garantia de que apenas código de qualidade seja implantado.

Os tipos de teste e sua aplicação são essenciais para uma estratégia de teste eficaz.

1. **Teste de unidade**:
   - Foco na menor parte da lógica de código.
   - Rápidos, não requerem recursos externos.
   - Ideal para funções curtas e com uma única responsabilidade.

2. **Teste de integração**:
   - Concentra-se na interação entre partes do código.
   - Pode exigir recursos externos, como bancos de dados.
   - Testa a integração de diferentes componentes.

3. **Teste funcional**:
   - Testa o aplicativo como um todo.
   - Requer um ambiente semelhante ao de produção.
   - Pode ser mais lento e complexo de configurar.

4. **Integração contínua (CI)**:
   - Automatiza a execução de testes em resposta a eventos, agendamentos ou manualmente.
   - Garante que o código seja testado regularmente, prevenindo falhas na integração.

A automação é fundamental para todos os tipos de teste, garantindo um ambiente consistente e conhecido. A CI desempenha um papel importante na automação, permitindo a execução automática e regular dos testes. Isso é essencial para garantir que o código seja confiável e robusto, mesmo em projetos complexos.

## Verificação de conhecimentos
1) Qual é um efeito colateral comum para funções quando não há testes envolvidos? 

( ) As funções serão executadas mais rapidamente porque não precisam usar testes.

(X) As funções podem aumentar em complexidade e tamanho.

( ) As funções serão executadas mais lentamente e terão mais argumentos.


2) Qual é um aspecto reconhecível em funções e métodos quando o teste está envolvido? 

(X) Eles tendem a ter uma única responsabilidade em vez de fazer muitas coisas diferentes

( ) Elas são mais flexíveis, permitindo mais argumentos

( ) Eles não tendem a criar exceções


3) Qual é a invocação correta do Python para usar a descoberta automática de teste? 

( ) python -m autodiscovery

( ) python -m discovery

(X) python -m unittest
