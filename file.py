class File():
	"""Armazena o maior score registrado."""

	def __init__(self):
		self.filename = 'high_score_stored.txt'
		

	def stored_high_score(self,high_score):
		"""Guarda o maior score no arquivo."""
		
		with open(self.filename,'w') as f_obj:
				f_obj.write(str(high_score))
	

	def read_high_score(self):
		"""Ler o maior score e coloca na varíavel."""
		try:
			with open(self.filename) as f_obj:
				high_score = f_obj.read()
		
		except FileNotFoundError:

			return 0
		else:	
		
			return int(high_score)

