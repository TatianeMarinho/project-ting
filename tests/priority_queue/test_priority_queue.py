from ting_file_management.priority_queue import PriorityQueue
import pytest

mock_file_um = {
    "nome_do_arquivo": "Estratégias_Paradigma_Globalizado.txt",
    "qtd_linhas": 4,
    "linhas_do_arquivo": [
        "Por outro lado, a execução dos pontos do programa desafia",
        "do retorno esperado a longo prazoAs experiências",
        "clara de objetivos faz parte de um processo de gerenciamento das",
        "Podemos já vislumbrar o modo pelo qual o comprometimento entre as",
    ],
}

mock_file_dois = {
    "nome_do_arquivo": "Estratégias_Paradigma_Globalizado_dois.txt",
    "qtd_linhas": 12,
    "linhas_do_arquivo": [
        "Por outro lado, a execução dos pontos do programa desafia",
        "do retorno esperado a longo prazoAs experiências",
        "clara de objetivos faz parte de um processo de gerenciamento das",
        "Podemos já vislumbrar o modo pelo qual o comprometimento entre as",
        "Por outro lado, a execução dos pontos do programa desafia",
        "do retorno esperado a longo prazoAs experiências",
        "clara de objetivos faz parte de um processo de gerenciamento das",
        "Podemos já vislumbrar o modo pelo qual o comprometimento entre as",
        "Por outro lado, a execução dos pontos do programa desafia",
        "do retorno esperado a longo prazoAs experiências",
        "clara de objetivos faz parte de um processo de gerenciamento das",
        "Podemos já vislumbrar o modo pelo qual o comprometimento entre as",
    ],
}


def test_basic_priority_queueing():
    test_queue = PriorityQueue()

    test_queue.enqueue(mock_file_um)
    test_queue.enqueue(mock_file_dois)

    assert len(test_queue) == 2
    assert test_queue.dequeue() == mock_file_um
    assert len(test_queue) == 1

    with pytest.raises(IndexError):
        test_queue.search(6)

    test_queue.enqueue(mock_file_um)

    assert test_queue.search(0)
    ['nome_do_arquivo'] == mock_file_um["nome_do_arquivo"]
    assert test_queue.search(0)['qtd_linhas'] == mock_file_um["qtd_linhas"]

    assert test_queue.search(1)
    ['nome_do_arquivo'] == mock_file_dois["nome_do_arquivo"]
    assert test_queue.search(1)['qtd_linhas'] == mock_file_dois["qtd_linhas"]

    test_queue.dequeue() == mock_file_um
    test_queue.dequeue() == mock_file_dois
    assert len(test_queue) == 0
