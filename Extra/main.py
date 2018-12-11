from typing import Dict, List, TextIO, Tuple


def pet_dictionary(pets: List[List[str]]) -> Dict[str, List[Tuple[str]]]:
	"""
	Return a dictionary where the keys are the species in pets and the values are list of tuples that contain the
	names and ages (as strings) of each pet of that species.
	# >>> pets = [['Shoji', 'cat', '18'], ['Hanako', 'dog', '15'], ['Sachiko', 'alligator', '7'], ['Toby', 'dog',
	'12']]
	# >>> pet_dictionary(pets) {'cat': [('Shoji', '18')], 'dog': [('Hanako', '15'), ('Toby', '12')], 'alligator': [(
	'Sachiko', '7')]}
	"""


# Add your code here
def file_line_lengths(f: TextIO) -> Dict[int, int]:
	"""
	Return a dictionary where the keys are the lengths of the lines in the open file f, and the values are the
	numbers of lines in the file that have each length. Newline characters '\n' should not be included when counting
	the length of the string. (Download the file words.txt from the course website as an example. You should also
	create your own files to test this function.)
	# >>> word_file = open('words.txt')
	# >>> file_line_lengths(word_file) {2: 1, 5: 3, 3: 1}
	# >>> word_file.close()
	"""


# Add your code here
def next_character(s: str, n: int) -> Dict[str, str]:
	"""
	 Return a dictionary where the keys are all substrings of s with length n that have a character after them,
	and the values are lists of all single characters after any occurrence of that substring.
	# >>> next_character('abbc', 1) {'a': ['b'], 'b': ['b', 'c']}
	# >>> next_character('abbc', 2) {'ab': ['b'], 'bb': ['c']}
	# >>> next_character('abbc', 3) {'abb': ['c']}
	"""
# Add your code here
