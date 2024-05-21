from __future__ import annotations
from typing import Optional
import pickle

from avltree import KeyNotFoundException, EmptyTreeException, AVLNode, AVLTree


class CommandsException(Exception):
    pass

    
dont_know = "Don't know such a command"


def execute_save_load(tree: AVLTree, commands: list[str]):
	if commands[1] == 'Save':
		try:
			result = tree.save(commands[2])
			if result:
				print('OK')
		except pickle.PickleError as pe:
			print(f'PickleError: {pe}')
		except pickle.PicklingError as pge:
			print(f'PicklingError: {pge}')
		except Exception as e:
			print(f'ERROR: {e}')
	
	elif commands[1] == 'Load':
		try:
			result = tree.load(commands[2])
			if result:
				print('OK')
		except pickle.UnpicklingError as ue:
			print(f'ERROR: {ue}')
		except Exception as e:
			print(f'ERROR: {e}')
	
	else:
		raise CommandsException(dont_know)


def execute_command_one(tree: AVLTree, commands: list[str]):
	""" выполняем команды длиной 1 """
	command = ''.join(commands)
	try:
		result = tree.search(command)
		if result is None:
			print('NoSuchWord')
		else:
			print(f'OK: {result.value}')
	except TypeError as e:
		print('search', e)


def execute_command_two(tree: AVLTree, commands: list[str]):
	""" выполняем команды длиной 2 """
	if commands[0] == '-':
		try:
			result = tree.remove(commands[1])
			if result is None:
				print('OK')
		except KeyNotFoundException:
			print('NoSuchWord')
		except TypeError as e:
			print('removal', e)
	else:
		raise CommandsException(dont_know)


def execute_command_three(tree: AVLTree, commands: list[str]):
	""" выполняем команды длиной 3 """
	if commands[0] == '+':
		key, value = commands[1], commands[2]
		if value is not None:
			value = int(value)
		try:
			result = tree.insert(insert_key=key, insert_value=value)
			if result is None:
				print('OK')
			else:
				print('Exist')
		except TypeError as e:
			print('insert', e)
	elif commands[0] == '!':
		execute_save_load(tree, commands)
	else:
		raise CommandsException(dont_know)


def parse_command(tree: AVLTree, line: str):
	commands = line.split()
	try:
		if len(commands) == 3:
			execute_command_three(tree, commands)
		elif len(commands) == 2:
			execute_command_two(tree, commands)
		elif len(commands) == 1:
			execute_command_one(tree, commands)
		else:
			raise CommandsException(dont_know)
	except CommandsException as ce:
		print(ce)
        

if __name__ == "__main__":

	FILEPATH = './example.txt'
	
	with open(FILEPATH, 'r', encoding='utf-8') as file:
		commands = file.read().rstrip().split('\n')
		
	dictionary_tree = AVLTree()
			
	for command in commands:
		parse_command(dictionary_tree, command)

