import os


class LetterWriter:
    def __init__(self, path_to_names, path_to_letter):
        self.path_to_names = path_to_names
        self.path_to_letter = path_to_letter

    def get_names(self):
        with open(self.path_to_names, "r") as names_file:
            names_list = [line.strip() for line in names_file.readlines()]
        return names_list

    def get_letter(self):
        with open(self.path_to_letter, "r") as input_letter_file:
            letter_template = input_letter_file.readlines()
        return letter_template

    def write_files(self):
        names_list = self.get_names()
        letter_template = self.get_letter()
        for name in names_list:
            letter_contents = [s.replace('[name]', name) for s in letter_template]
            letter_output = "".join(letter_contents)
            end_letter_path = os.path.join(os.path.dirname(__file__), 'Output', 'ReadyToSend', name + '.txt')
            with open(end_letter_path, "w") as output_letter_file:
                output_letter_file.write(letter_output)
