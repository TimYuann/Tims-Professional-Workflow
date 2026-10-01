from dataclasses import dataclass

from .page_summary import summarize_view
from .state_store import CaseRecord, StateStore, StateView


@dataclass(frozen=True)
class Turn:
    """A read episode pinned to the StateView resolved when it opened."""

    view: StateView

    @property
    def page_summary(self) -> dict[str, int]:
        return summarize_view(self.view)

    @property
    def cases(self) -> tuple[CaseRecord, ...]:
        return self.view.cases


def begin_turn(store: StateStore) -> Turn:
    return Turn(view=store.current_view())
