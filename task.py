

class Transaction:
  def __init__(self, client_give, client_take, money):
    self.client_give = client_give
    self.client_take = client_take
    self.money = money

class Client:
  def __init__(self, name, bank_name, pin, start_money):
    self.name = name
    self.bank_name = bank_name
    self.pin = pin
    self.wallet = 0.0
    self.tans_history = []

class Bank:
  def __init__(self, name):
    self.name = name
    self.client_list = []

  def add_client(self,client):
    self.client_list.push(client)

if __name__ == "__main__":
  print("Start by add first bank\n Bank name:")
  bank_name = input()
  Bank1 = Bank(bank_name)
  print("Bank was created!")
  print("add some clients")

  print("first client name:")
  cl_name = input()
  print("client start money")
  cl_money = input()
  client = Client(cl_name,Bank1.name,1234,cl_money)
  Bank.add_client(client)
  print("Client added!")
  print("cnd...")
