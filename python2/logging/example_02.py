import logging
from threading import Thread
from time import sleep
import logging.config
from logging.config import dictConfig
from logging import StreamHandler
from logging import FileHandler
from random import randint

#logging.basicConfig(level=logging.DEBUG)

logging.config.dictConfig({
	"version": 1,
	"loggers": {
		"root": {
			"handlers": ["console"],
			"level": "DEBUG",
			"propagete": 0
		},
		"system": {
			"handlers": ["console"],
			"level": "DEBUG",
			"propagete": 0
		},		
		"system.networking": {
			"handlers": ["console"],
			"level": "DEBUG",
			"propagete": 0
		},
		"system.db": {
			"handlers": ["console", "file"],
			"level": "DEBUG",
			"propagete": 1
		},
		"system.networking": {
			"handlers": ["console"],
			"level": "DEBUG",
			"propagete": 0
		},
		"system.networking.http": {
			"handlers": ["console"],
			"level": "DEBUG",
			"propagete": 0
		},
		"system.networking.smtp": {
			"handlers": ["console"],
			"level": "DEBUG",
			"propagete": 0
		},
		"system.media": {
			"handlers": ["console", "file"],
			"level": "DEBUG",
			"propagete": 1
		}
	},
	"formatters": {
		"f1": {
			"format": "%(asctime)s %(message)s"
		},
		"f2": {
			"format": "%(asctime)s %(levelname)s %(module)s %(name)s %(message)s"
		}
	},
	"handlers": {
		"console": {
				"level": "DEBUG",
				"class": "logging.StreamHandler",
				"formatter": "f2",
				"stream" : "ext://sys.stdout"
		},
		"file": {
				"level": "DEBUG",
				"class": "logging.FileHandler",
				"filename": "system.log",
				"mode": "a",
				"formatter": "f2",
		}
	}
	})


class Networking(object):
	def __init__(self):
		self.logger = logging.getLogger("system.networking")
		self.logger.debug("Konstruktor")
	
class Http(Networking):
	"""
		Klasa Http.
	"""
	config = {
		'request':{
			'timeout': 1000
		},
		'response':{
			'timeout': 2000
		}
	}
	
	def __init__(self):
		self.logger = logging.getLogger("system.networking.http")
		self.logger.debug("Konstruktor")
	
	def get(self, url, args=None):
		self.logger.debug("Processing get request")
		result = randint(0, 10)
		if result == 0:
			self.logger.debug("Processing get request")
		elif result > 0 and result <=4:
			self.logger.warning("Processing get request")
		elif result > 4 and result < 8: 
			self.logger.error("Processing get request")
		elif result == 9:
			self.logger.critical("Critical")
		else:
			self.logger.debug("Result is 10")
		
	def post(self, url, querystring):
		self.logger.debug("Processing post request url: %s, args: %s", url, querystring)
	
	
class Smtp(Networking):
	"""
		Klasa SMTP
	"""
	def __init__(self):
		self.logger = logging.getLogger("system.networking.smtp")
		self.logger.debug("Konstruktor")

	def sent_email(self, message, subject, to):
		self.logger.debug("Sending email to %s", to)
		
	
class Media(object):
	"""
		Klasa media
	"""
	def __init__(self):
		self.logger = logging.getLogger("system.media")
		self.logger.debug("Konstruktor")
	
	def play_audio(self):
		try:
			self.logger.info("Plying audio...")
		except Exception as ex:
			self.logger.exception(ex)
			
			
			
class System(Thread):
	def __init__(self):
		self.logger = logging.getLogger("system")
		Thread.__init__(self)
		self.networking = Networking()
		self.smtp = Smtp()
		self.http = Http()
		self.media = Media()
		self.start()
		
		
	def run(self):
		self.logger.warning("System thread")
		while 1:
			sleep(5)
			self.http.get("http://google.com")
			self.smtp.sent_email("user@gmail.com", "Hello World", "Hello")
			


System()