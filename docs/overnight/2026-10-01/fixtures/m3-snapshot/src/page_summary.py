from .state_store import StateStore


def build_page_summary(store: StateStore) -> dict[str, int]:
    view = store.current_view()
    return {
        "revision": view.revision,
        "open_count": sum(case.status == "OPEN" for case in view.cases),
    }
