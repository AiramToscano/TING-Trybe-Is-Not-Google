import sys


def txt_importer(path_file):
    caminhoCerto = path_file.split('.')
    try:
        if (caminhoCerto[1] == 'txt'):
            with open(path_file) as f:
                # https://www.pythontutorial.net/python-basics/python-read-text-file/
                lines = [line.strip() for line in f.readlines()]
            return lines
        else:
            # https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
            sys.stderr.write("Formato inválido\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


# print(txt_importer('ting_file_management/teste.txt'))
