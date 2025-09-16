class Supermercado:
  def __init__(self):
    self.produtos = {}
    self.lista_de_compra = []

  def cadastrar_produto(self):
    nome = str(input("Qual o nome do Produto ?\n"))
    if nome in self.produtos:
      print("Produto ja cadastrado!")
      
    else:
      while True:
        try:
          valor = float(input("Qual o valor do Produto ?\n"))
          quantidade = int(input("Qual a quantidade de produto ?\n"))
          self.produtos[nome] = {'valor' : valor, 'quantidade' : quantidade}
          print("Produto cadastrado!")
          break
        except ValueError:
          print("Digiti apenas numeros")
          continue 

  def Lista_de_produto(self):
    if not self.produtos:
      print("Não a produto cadastrado!\n")
    else:
      for nome, i in self.produtos.items():
        print(f"Produto : {nome}, Valor : {i['valor']:.2f} R$, Quantidade : {i['quantidade']}")

  def Adicionar_quantidade(self):
    nome = str(input("Qual produto deseja altera a qauntidade?\n")).lower()
    mercado.Consultar_produto(nome)
    while True:
        try:
          quantidade = int(input("Qual a nova quantidade ?\n"))
          antiga_quantidade = self.produtos[nome]['quantidade']
          self.produtos[nome]['quantidade'] = (quantidade + antiga_quantidade)
          break
        except ValueError:
          print("Digiti apenas numeros")
          continue 

  def Remover_produto(self):
    nome = str(input("Qual produto deseja remover ?\n"))
    mercado.Consultar_produto(nome)
    del self.produtos[nome]
    print("Produto ",nome, " removido!")


  def comprovante_de_compras(self):
    if not self.lista_de_compra:
      print("Não a registros de compras!\n\n")
    else:
      for compra in self.lista_de_compra:
        print(f"Cliente: {compra['Cliente']}")
        for nome, dados in compra['Produtos comprados'].items():
          print(f"  Produto: {nome}, Valor: {dados['valor']:.2f} R$, Quantidade: {dados['quantidade']}")
          print("-" * 30)

  def Consultar_produto(self,nome):
    if nome in self.produtos:
      return
    else:
      print("Não a produto com esse nome!\n")
      

  def carrinho(self):
      lista_temporario = {}
      lista_temporario = self.produtos
      valor_a_pagar = 0
      lista_temporaria_cliente = {}
      cpf_cliente = int(input("CPF do cliente ?\n"))
      nome_cliente = cliente.consultar_cliente(cpf_cliente)
      opcao = int(input("\n\n1 - comprar\n0 - sair\n"))
      if opcao == 1 :
        while True:
          for indice,(nome, i) in enumerate (lista_temporario.items()):
              print(f"{indice + 1} - Produto : {nome}, Valor : {i['valor']:.2f} R$, Quantidade : {i['quantidade']}")
          opcao = input("\n\nDigiti o nome do produto\n")
          if opcao in lista_temporario:
            quant = int(input("Qual a quantidade ?\n"))
            if quant <= lista_temporario[nome]['quantidade']:

              valor_a_pagar += lista_temporario[opcao]['valor'] * quant
              lista_temporario[opcao]['quantidade'] -= quant
              opcao = int(input("1 - continuar comprando\n 2 - Pagar compra\n"))
              if opcao == 1:
                continue
              elif opcao == 2:
                opcao_b = int(input(f"Valor total é: {valor_a_pagar:.2f} R$\nQual a forma de pagamento?\n1 - Cartão\n2 - Pix\n3 - Dinheiro\n"))
                if opcao_b == 1:
                  print("Por favor insira o cartao!\nPagamento aprovado!")
                  
                  self.lista_de_compra.append({'Cliente' : nome_cliente, 'Produtos comprados' : lista_temporario.copy()})
                  self.produtos = lista_temporario
                  break

                elif opcao_b == 2:
                  print("Esse e nosso pix!\nPagamento aprovado")
                  self.lista_de_compra.append({'Cliente' : nome_cliente, 'Produtos comprados' : lista_temporario.copy()})
                  self.produtos = lista_temporario
                  break
                elif opcao_b == 3:
                  print("Obrigado e volte sempre!")
                  self.lista_de_compra.append({'Cliente' : nome_cliente, 'Produtos comprados' : lista_temporario.copy()})
                  self.produtos = lista_temporario
                  break
                else:
                  print("Opcao invalida")
                  continue
            else:
              print("Quantidade superior maior do que disponivel!\n")
              break
          else:
            print("Não a produto com esse nome!\n")
            break

      elif opcao == 0 :
        return

class Cliente:
  def __init__(self):
    self.cliente = {}

  def Cadastrar_cliente(self):
    while True:
      try:
        cpf = int(input("CPF do cliente\n"))         
        if cpf in self.cliente:
          print("CPF ja esta cadastrado")
          break  
          
        else:
          nome = str(input("Nome do cliente\n"))
          while True:
            try:
              telefone = int(input("Telefone do cliente\n")) 
              self.cliente[cpf] = {'nome': nome, 'telefone' : telefone}
              print(f"Cliente cadastrado !\n" )
              break
                
            except ValueError:
              print("Digiti apenas numeros")
              continue
          
      except ValueError:
        print("Digiti apenas numeros")
        continue     

  def Lista_de_cliente(self):
    if not self.cliente:
      print("Não a produto cadastrado!\n")
    else:
      for cpf, i in self.cliente.items():
        print(f"Cliente : {i['nome']}, Telefone : {i['telefone']}, CPF : {cpf}")

  def consultar_cliente(self, cpf_cliente):
    if cpf_cliente in self.cliente:
      dados_temporarios = self.cliente[cpf_cliente]['nome']
      return dados_temporarios
    else:
      print("Não a cliente com esse CPF!")

def menu(mercado,cliente):  
  while True:
    try:
      opcao = int(input("1- Produto\n2- Cliente\n3- Compras\n9- Sair\n"))    
      match opcao:        
        case 1:
          while True:
            try:              
              opcao = int(input("1- Cadastrar Produto\n2- Lista de produto\n3- Adicionar quantidade\n4- Remover produto\n9- Menu anterior\n"))         
              match opcao:
                  case 1:
                    mercado.cadastrar_produto()
                  case 2:
                    mercado.Lista_de_produto()
                  case 3:
                    mercado.Adicionar_quantidade()
                  case 4:
                    mercado.Remover_produto()          
                  case 9:
                    break             
            except ValueError:
              print("Digiti apenas numeros")
              continue    
            break         
        case 2:
          while True:
            try:  
              opcao = int(input("1- Cadastrar cliente\n2- Lista de cliente\n9- Menu anterior\n"))
              match opcao:
                case 1:
                  cliente.Cadastrar_cliente()
                case 2:
                  cliente.Lista_de_cliente()      
                case 9:
                  break
            except ValueError:
              print("Digiti apenas numeros")
              continue           
        case 3:
          while True:
            try:
              opcao = int(input("1- Compras\n2- Lista de compras\n9- Menu anterior\n"))
              match opcao:
                case 1:
                  mercado.carrinho()
                case 2 :
                  mercado.comprovante_de_compras()
        
                case 9:
                  break
            except ValueError:
                print("Digiti apenas numeros")
                continue          
        case 9:
            break         
    except ValueError:
        print("Digiti apenas numeros")
        continue
        


mercado = Supermercado()
cliente = Cliente()


menu(mercado, cliente)

