class Category:
	def __init__(self, category):
		self.category = category
		self.ledger = list()
		self.balance = 0
	
	def check_funds(self, amount):
		if amount > self.balance:
			return False
		return True
	
	def deposit(self, amount, description=""):
		self.transaction = {"amount": amount,"description": description}
		self.ledger.append(self.transaction)
		self.balance = self.balance + amount
		
	def withdraw(self, amount, description=""):
		if self.check_funds(amount) == False:
			return False
		self.transaction = {"amount": amount*-1,"description": description}
		self.ledger.append(self.transaction)
		self.balance = self.balance - amount
		return True
	
	def get_balance(self):
		return self.balance
	
	def transfer(self, amount, athCategory):
		if self.check_funds(amount) == True:
			self.withdraw(amount, f"Transfer to {athCategory.category}")
			athCategory.deposit(amount, f"Transfer from {self.category}")
			return True
		return False
			
	def calculateSpents(self):
		self.expenses = 0
		for t in self.ledger:
			if t["amount"] < 0:
				self.expenses += abs(t["amount"])
		return round(self.expenses, 2)
		
	def __repr__(self):
		self.items = list()
		self.values = list()
		for i in range(len(self.ledger)):
			self.item = f'{self.ledger[i]["description"]:<23.23}{float(self.ledger[i]["amount"]):>7.2f}'				
			self.items.append(self.item)
		self.list = "\n".join(self.items)
		return f"{self.category:*^30}\n{self.list:30}\nTotal: {self.balance:.2f}"
		
def create_spend_chart(categories):
	data = dict()
	totalSpent = 0
	for catg in range(len(categories)):
		categories[catg].calculateSpents()
		totalSpent += round(categories[catg].expenses, 2)
	for catego in range(len(categories)):
		data[categories[catego].category] = round((categories[catego].expenses/totalSpent)*100)
	
	scale = "Percentage spent by category\n"
	xAxis = "-"*(len(categories)*3 + 1)
	for row in reversed(range(0, 110, 10)):
		scale += f'{str(row)+"|":>4}'
		for v in data:
			if row <= data[v]:
				scale += " o "
			else:
				scale += "   "
		scale += " \n"
	scale += f'    {xAxis}'
	
	maxLen = max([len(word) for word in data.keys()])
	line =""
	for ix in range(maxLen):
		line += "    "
		for k in data.keys():
			try:
				line += " " + k[ix] + " "
			except IndexError:
				line += "   "
		line += " \n"
	line = line.rstrip()
	line += "  "
		
	graphic = scale + "\n" + line
	return graphic