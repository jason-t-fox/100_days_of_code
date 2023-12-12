import os


class LetterWriter:
    @staticmethod
    def get_names(path_to_names):
        with open(path_to_names, "r") as names_file:
            names_list = [line.strip() for line in names_file.readlines()]
        return names_list

    @staticmethod
    def get_letter(path_to_letter):
        with open(path_to_letter, "r") as input_letter_file:
            letter_template = input_letter_file.readlines()
        return letter_template

    @staticmethod
    def write_files(names_list, letter_template):
        for name in names_list:
            letter_contents = [s.replace('[name]', name) for s in letter_template]
            letter_output = "".join(letter_contents)
            end_letter_path = os.path.join(os.path.dirname(__file__), 'Output', 'ReadyToSend', name + '.txt')
            with open(end_letter_path, "w") as output_letter_file:
                output_letter_file.write(letter_output)
