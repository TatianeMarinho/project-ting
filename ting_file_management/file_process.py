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

    sys.stdout.write(str(file_data))


def remove(instance):
    if instance.is_empty():
        return sys.stdout.write("Não há elementos\n")

    removed_file = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {removed_file} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
