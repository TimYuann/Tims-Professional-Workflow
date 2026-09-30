from .case_reader import read_cases
from .state_store import StateStore
from .turn import Turn, begin_turn


def start(store: StateStore) -> Turn:
    return begin_turn(store)


def cases(store: StateStore):
    return read_cases(store)
