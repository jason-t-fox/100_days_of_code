from LetterWriter import LetterWriter

names_path = 'input/Names/invited_names.txt'
start_letter_path = 'input/Letters/starting_letter.txt'

letter_writer = LetterWriter(path_to_names=names_path, path_to_letter=start_letter_path)

names_list = letter_writer.get_names()
letter_template = letter_writer.get_letter()
letter_writer.write_files()
