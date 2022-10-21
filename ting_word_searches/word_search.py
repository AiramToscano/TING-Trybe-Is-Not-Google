from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue


def exists_word(word, instance):
    # print(type(word))
    firstword = word.lower()
    # instance.enqueue('ting_file_management/teste.txt')
    lista = []
    fila = instance._data
    listaocorrencia = []
    for path_file in fila:
        fileProcess = txt_importer(path_file)
        for index, frase in enumerate(fileProcess):
            if(firstword in frase.lower()):
                listaocorrencia.append({"linha": index + 1})
        obj = {
            "palavra": firstword,
            "arquivo": path_file,
            "ocorrencias": listaocorrencia
        }
        if(len(listaocorrencia) != 0):
            lista.append(obj)
    return lista


# print(exists_word('pedro', Queue()))

def search_by_word(word, instance):
    firstword = word.lower()
    lista = []
    fila = instance._data
    listaocorrencia = []
    for path_file in fila:
        fileProcess = txt_importer(path_file)
        for index, frase in enumerate(fileProcess):
            if(firstword in frase.lower()):
                listaocorrencia.append({
                    "linha": index + 1,
                    "conteudo": frase
                    })
        obj = {
            "palavra": firstword,
            "arquivo": path_file,
            "ocorrencias": listaocorrencia
        }
        if(len(listaocorrencia) != 0):
            lista.append(obj)
    return lista
