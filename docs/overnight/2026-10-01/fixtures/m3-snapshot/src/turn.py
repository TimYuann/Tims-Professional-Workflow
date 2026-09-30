from dataclasses import dataclass

from .page_summary import build_page_summary
from .state_store import StateStore


@dataclass(frozen=True)
class Turn:
    page_summary: dict[str, int]


def begin_turn(store: StateStore) -> Turn:
    return Turn(page_summary=build_page_summary(store))
