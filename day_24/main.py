import os
from LetterWriter import LetterWriter

letter_writer = LetterWriter()

names_path = os.path.join(os.path.dirname(__file__), 'input', 'Names', 'invited_names.txt')
start_letter_path = os.path.join(os.path.dirname(__file__), 'input', 'Letters', 'starting_letter.txt')

names_list = letter_writer.get_names(path_to_names=names_path)
letter_template = letter_writer.get_letter(path_to_letter=start_letter_path)
letter_writer.write_files(letter_template=letter_template, names_list=names_list)
