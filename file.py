class File():
	"""Armazena o maior score registrado."""

	def __init__(self,stats):
		self.filename = 'high_score_stored.txt'
		self.stats = stats

	def stored_high_score(self):
		"""Guarda o maior score no arquivo."""
		
		with open(self.filename,'w') as f_obj:
				f_obj.write(str(self.stats.high_score))
	

	def read_high_score(self):
		"""Ler o maior score e coloca na varíavel."""
		
		with open(self.filename) as f_obj:
			high_score = f_obj.read()
			
		self.stats.high_score = int(high_score)

