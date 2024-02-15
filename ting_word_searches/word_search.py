def exists_word(word, instance):
    occurrences = []  # armazena as ocorrencias das palavras

    for item in instance._data:  # itero sobre cada item da fila
        file_name = item["nome_do_arquivo"]  # extraio o nome do arquivo
        lines = item["linhas_do_arquivo"]  # linhas do arq p/buscar a pal.
        file_occurrences = []  # armaz.ocorrencias no arq. atual

        for index, line in enumerate(lines, start=1):  # itera l do arq atual
            if word.lower() in line.lower():  # conv. e verif. a palavra
                file_occurrences.append({"linha": index})
                # armaz. a linha onde a palavra foi encontrada

        if file_occurrences:  # se tem ocorrencias
            occurrences.append({  # armaz. os dados 
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": file_occurrences
            })

    return occurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
