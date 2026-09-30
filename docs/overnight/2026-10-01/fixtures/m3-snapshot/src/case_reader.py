from .state_store import CaseRecord, StateStore


def read_cases(store: StateStore) -> tuple[CaseRecord, ...]:
    return store.current_view().cases
