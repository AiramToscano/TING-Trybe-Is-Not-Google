# from ting_file_management.queue import Queue
from .file_management import txt_importer
import sys


def process(path_file, instance):
    fila = instance._data
    if (path_file not in fila):
        instance.enqueue(path_file)
    fileProcess = txt_importer(path_file)
    obj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(fileProcess),
        "linhas_do_arquivo": fileProcess

    }
    sys.stdout.write(str(obj))


def remove(instance):
    fila = instance._data
    if(len(fila) != 0):
        ElementRemove = instance.dequeue()
        sys.stdout.write(f"Arquivo {ElementRemove} removido com sucesso\n")
    if(len(fila) == 0):
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# print(process('ting_file_management/teste.txt', Queue()))
