#! /usr/bin/python
# coding=utf-8

'''
Wrapping an existing dict, or create a new one, and access it with doc notation
'''

class Storage(object):

	'''
	help info
	'''

	def __init__(self, data = None, create = True):
		'''
		Initialize storage type
		'''
		if data is None: # Input is empty and init data as a dict
			data = {}
		else:            # Transfer input into dict type
			data = dict(data)

        # Set Storage attribution
		self.__dict__['__storage_data'] = data
		self.__dict__['__storage_create'] = create

	def __getattr__(self, key):
		'''
		Get the value with key
		'''

		try:
			value = self.__dict__['__storage_data'][key]
		except KeyError:
			# Create the key with the empty value
			if not self.__dict__['__storage_create']:
				raise
			value = {}
			self.__dict__['__storage_data'][key] = value

		if isinstance(value, dict):
			value = Storage(value, self.__dict__['__storage_create'])
			self.__dict__['__storage_data'][key] = value

		return value

	def __setattr__(self, key, value):
		'''Set the key's value with the input value'''
		self.__dict__['__storage_data'][key] = value

	def __delattr__(self, key):
		'''Del the key'''
		del self.__dict__['__storage_data'][key]

	def __contains__(self, key):
		'''Check whether the key exists'''
		return key in self.__dict__['__storage_data']

	def __bool__(self):
		'''Check whether the storage is empty'''
		return 
