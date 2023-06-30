from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    task_1 = {
        "nome_do_arquivo": "",
        "qtd_linhas": 9,
        "linhas_do_arquivo": [],
    }

    high_task_1 = {
        "nome_do_arquivo": "",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [],
    }

    task_2 = {
        "nome_do_arquivo": "",
        "qtd_linhas": 11,
        "linhas_do_arquivo": []
    }

    h_task_2 = {
        "nome_do_arquivo": "",
        "qtd_linhas": 2,
        "linhas_do_arquivo": []
    }

    priority_queue = PriorityQueue()

    priority_queue.enqueue(task_1)
    priority_queue.enqueue(high_task_1)
    priority_queue.enqueue(task_2)
    priority_queue.enqueue(h_task_2)

    assert len(priority_queue.high_priority) == 2
    assert len(priority_queue.regular_priority) == 2
    assert len(priority_queue) == 4
    assert priority_queue.high_priority.search(0) == high_task_1
    assert priority_queue.high_priority.search(1) == h_task_2
    assert priority_queue.regular_priority.search(0) == task_1
    assert priority_queue.regular_priority.search(1) == task_2

    assert priority_queue.search(1) == h_task_2
    assert priority_queue.search(2) == task_1
    assert priority_queue.search(3) == task_2

    assert priority_queue.dequeue() == high_task_1
    assert priority_queue.dequeue() == h_task_2
    assert priority_queue.dequeue() == task_1
    assert priority_queue.dequeue() == task_2
    assert len(priority_queue) == 0
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(1)
