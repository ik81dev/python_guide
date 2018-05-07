import logging


module_logger = logging.getLogger(__name__)
module_logger.debug("Http module")
print __name__

class Http:
	"""Klasa HTTP"""
	
	
	def __init__(self, logger=None):
		"""Konstruktor"""
		self.logger = logger or logging.getLogger(__name__)
		self.logger.debug("Konstruktor")
	
	
	def do_get(self, url):
		"""Metoda GET"""
		print "HTTP get method..."
		self.logger.debug("GET request to %s", url)
	
	@staticmethod
	def do_get_static(url):
		print "HTTP get method..."
		logging.debug("GET request to %s", url)
		
	
	def do_post(self, url):
		"""Metoda POST"""
		self.logger.debug("POST request to %s", url)
