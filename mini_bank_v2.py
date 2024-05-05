class MiniBank:

	users = []

	def __init__(user):

		self.user = user
		users.apend(self.user)

	def depositar(user, value):

		if self.user in users:
			

	def sacar(user, value):

		if self.user in users:
			if value <= self.total:
				self.total -= value
				return f'{self.user}, seu saque foi feito com sucesso!, o novo valor da sua conta é {self.total}'
