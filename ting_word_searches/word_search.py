def exists_word(word, instance):
    results = []

    for file_data in instance.queue:
        file_name = file_data["nome_do_arquivo"]
        occurrences = []

        for line_number, line_content in enumerate(
            file_data["linhas_do_arquivo"], start=1):
            if word.lower() in line_content.lower():
                occurrences.append({"linha": line_number})

        if occurrences:
            file_result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            }
            results.append(file_result)

    return results


def search_by_word(word, instance):
    results = []

    for file_data in instance.queue:
        file_name = file_data["nome_do_arquivo"]
        occurrences = []

        for line_number, line_content in enumerate(
            file_data["linhas_do_arquivo"], start=1):
            if word.lower() in line_content.lower():
                occurrence = {"linha": line_number, "conteudo": line_content}
                occurrences.append(occurrence)

        if occurrences:
            result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            }
            results.append(result)

    return results
