from .state_store import StateStore, StateView


def summarize_view(view: StateView) -> dict[str, int]:
    return {
        "revision": view.revision,
        "open_count": sum(case.status == "OPEN" for case in view.cases),
    }


def build_page_summary(store: StateStore) -> dict[str, int]:
    return summarize_view(store.current_view())
