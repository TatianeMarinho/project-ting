from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in instance._data:
        if path_file == item['nome_do_arquivo']:
            return

    lines = txt_importer(path_file)

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(file_data)

    sys.stdout.write(f"{file_data}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
