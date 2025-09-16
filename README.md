# Sistema de Gerenciamento de Supermercado em Python

## Descrição
Este é um mini projeto em Python que simula um sistema de gerenciamento de supermercado via (console). O sistema permite o cadastro e gerenciamento de produtos, clientes e compras, com funcionalidades básicas como adicionar itens ao carrinho, processar pagamentos simulados e gerar comprovantes de compras.

O projeto é ideal para iniciantes em programação, demonstrando conceitos como classes, dicionários, loops, exceções e interações com o usuário via input/output, poo.

## Funcionalidades Principais
- **Gerenciamento de Produtos**:
  - Cadastro de novos produtos (nome, valor e quantidade).
  - Listagem de produtos disponíveis.
  - Adição de quantidade a produtos existentes.
  - Remoção de produtos.

- **Gerenciamento de Clientes**:
  - Cadastro de clientes (CPF, nome e telefone).
  - Listagem de clientes cadastrados.
  - Consulta de clientes por CPF.

- **Compras e Carrinho**:
  - Simulação de carrinho de compras: seleção de produtos, quantidade e cálculo de total.
  - Opções de pagamento simuladas (cartão, PIX ou dinheiro).
  - Geração de comprovantes de compras com detalhes do cliente e produtos adquiridos.

- **Menu Interativo**:
  - Navegação por menus para acessar as funcionalidades.
  - Tratamento de erros para entradas inválidas (ex.: valores não numéricos).

## Tecnologias Utilizadas
- Python 3 (sem bibliotecas externas, apenas recursos nativos).
- Estruturas de dados: Dicionários para armazenar produtos e clientes.
- Controle de fluxo: Loops (`while`), condicionais (`if/else`), `match/case` e exceções (`try/except`).

## Como Executar
1. Certifique-se de ter Python 3 instalado.
2. Baixe o arquivo principal (`supermercado.py` ou similar).
3. Execute o script no terminal:
   ```
   python supermercado.py
   ```
4. Siga as instruções no menu para interagir com o sistema.

## Limitações
- Não persiste dados (tudo é armazenado em memória; reiniciar o programa reseta os cadastros).
- Pagamentos são simulados (sem integração real com bancos ou APIs).
- Interface puramente textual (sem GUI).

## Ideias para Melhorias
- Adicionar persistência de dados com arquivos JSON ou banco de dados (ex.: SQLite).
- Implementar uma interface gráfica com bibliotecas como Tkinter.
- Adicionar relatórios de vendas ou estoque baixo.
- Suporte a descontos, promoções ou múltiplos supermercados.

Este projeto foi desenvolvido como exercício de programação orientada a objetos e pode ser expandido para fins educacionais ou portfólio.

## Autor
- Leonardo Santos / SbioSS

## Linkedin
- linkedin.com/in/leonardo-santos-724979275/
