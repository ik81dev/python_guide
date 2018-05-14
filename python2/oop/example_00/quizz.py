#-*-coding:utf-8 -*-
import os
import sys
import logging
import logging.config
import random

class QuizzItem(object):
	
	def __init__(self, title, q0, q1, q2, answer, logger=None):
		self.logger = logger or logging.getLogger(__name__)
		self.title = title
		self.q0 = q0
		self.q1 = q1
		self.q2 = q2
		self.answer = answer
	
	def __repr__(self):
		""""""
		return "{}\n\t{}\n\t{}\n\t{}".format(self.title, self.q0, self.q1, self.q2)
	
	def __str__(self):
		""""""
		return "{}\n\t{}\n\t{}\n\t{}".format(self.title, self.q0, self.q1, self.q2)
	
	
class Quizz(object):

	quizitems = []
	summary = 0
	
	def __init__(self, path, logger=None, **kwargs):
		self.kwargs = kwargs
		self.logger = logger or logging.getLogger(__name__)
		assert os.path.exists(path), "Nie ma takiego pliku w podanej lokalizacji"
		lines = open(path, "r").readlines()
		assert len(lines) % 5 == 0, "Niewlasciwa liczba linii w pliku z pytaniami"
		self.logger.debug(lines)
		self.quizitems = [QuizzItem(*map(str.strip, lines[i:i+5])) for i in range(0, len(lines), 5)]
	
	
	def check_answer(self, question, answer, **kwargs):
		"""Sprawdzenie odpowiedzi"""
		self.logger.debug("Argumenty pozycyjne funkcji to: %s"%kwargs)
		self.logger.debug("Twoja odpowiedz: %s, odpowiedz: %s ", question.answer, answer)
		if "ignore_case" in kwargs and kwargs["ignore_case"]:
			return question.answer.lower() == answer.lower()
		else:
			return question.answer == answer
	
	def shuffle(self):
		"""Pomieszanie pytan"""
		self.logger.debug("Przemieszanie pytań.")
		random.shuffle(self.quizitems)
		return self
	
	
	def start(self):
		self.logger.debug("Uruchamiam quizz.")
		self.summary = 0
		for qid, question in enumerate(self.quizitems, 1):
			print "Pytanie ", qid, "\n", question
			answer = raw_input("Odpowiedz: ")
			if self.check_answer(question, answer, **self.kwargs):
				self.summary += 1 
				
		print "Liczba punktow: ", self.summary , " na ", len(self.quizitems), " pytań." 
		
			
	def __str__(self):
		return ""
	
	def __repr__(self):
		"""Formatowanie wyswietlanego te"""
		self.logger.debug("Metoda __repr__")
		result = []
		for question in self.quizitems:
			result.append(str(question))
		
		return "".join(result)
	
	
if __name__ == "__main__":
	try:
		logging.config.fileConfig("log.ini")
		assert len(sys.argv) == 2, "Błędna liczba argumentów."
		Quizz(sys.argv[1], logger=logging.getLogger(), ignore_case=True).shuffle().start()
	except Exception as ex:
		logging.getLogger().error(str(ex))