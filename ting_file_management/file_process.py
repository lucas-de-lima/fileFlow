import sys

from ting_file_management.file_management import txt_importer
from ting_file_management.abstract_queue import AbstractQueue

def process(path_file: str, instance: AbstractQueue):
    # Verifica se o arquivo já foi processado anteriormente
    for item in instance.queue:
        if item["nome_do_arquivo"] == path_file:
            # Arquivo já existente na fila, ignorar
            return

    # Realiza o processamento do arquivo
    lines = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    instance.enqueue(data)

    # Exibe os dados processados via stdout
    print(data)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return

    file_data = instance.dequeue()
    path_file = file_data["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        print(file_data)
    except IndexError:
        print("Posição inválida", file=sys.stderr)