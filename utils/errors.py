"""Test for exceptions raised in the tesseract.exe logfile"""

class Tesser_General_Exception(Exception):
	pass

class Tesser_Invalid_Filetype(Tesser_General_Exception):
	pass