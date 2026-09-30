from dataclasses import dataclass


@dataclass(frozen=True)
class CaseRecord:
    case_id: str
    status: str


@dataclass(frozen=True)
class StateView:
    revision: int
    cases: tuple[CaseRecord, ...]


class StateStore:
    def __init__(self, cases: tuple[CaseRecord, ...]):
        self._current = StateView(revision=1, cases=cases)

    def current_view(self) -> StateView:
        return self._current

    def update_status(self, case_id: str, status: str) -> None:
        cases = tuple(
            CaseRecord(case.case_id, status if case.case_id == case_id else case.status)
            for case in self._current.cases
        )
        self._current = StateView(revision=self._current.revision + 1, cases=cases)
