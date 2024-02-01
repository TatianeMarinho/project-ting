import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):  # se termina com .txt
        sys.stderr.write("Formato inválido\n")
        # escrevo na saida de erro padrao

    try:
        with open(path_file) as file:
            lines = file.read().split('\n')
        return lines

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
