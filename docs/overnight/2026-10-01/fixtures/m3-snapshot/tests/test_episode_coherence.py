import unittest

from src.service import cases, start
from src.state_store import CaseRecord, StateStore


def store_with(*pairs: tuple[str, str]) -> StateStore:
    return StateStore(tuple(CaseRecord(case_id, status) for case_id, status in pairs))


def presented_pairs(turn) -> list[tuple[str, str]]:
    return [(case.case_id, case.status) for case in turn.cases]


def open_count_of(pairs: list[tuple[str, str]]) -> int:
    return sum(status == "OPEN" for _, status in pairs)


class EpisodeCoherenceTests(unittest.TestCase):
    """Coverage for B-1..B-6 and DS-I1..I7 through the pinned episode carrier."""

    def test_mid_episode_update_cannot_straddle_the_presented_pair(self):
        # X-2 / B-1 / B-6(b): one resolution per presented view.
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        turn = start(store)
        store.update_status("C-1", "CLOSED")
        self.assertEqual(turn.page_summary["revision"], 1)
        self.assertEqual(turn.page_summary["open_count"], 2)
        self.assertEqual(presented_pairs(turn), [("C-1", "OPEN"), ("C-2", "OPEN")])
        # B-6(a) / DS-I2: the count is faithful to the details of the same view.
        self.assertEqual(turn.page_summary["open_count"], open_count_of(presented_pairs(turn)))

    def test_episode_observations_are_pinned_values(self):
        # C-3 / C-5: observations are values, and the pin cannot change under later updates.
        store = store_with(("C-1", "OPEN"))
        turn = start(store)
        returned = turn.page_summary
        returned["open_count"] = 99
        del returned["revision"]
        store.update_status("C-1", "CLOSED")
        self.assertEqual(turn.page_summary, {"revision": 1, "open_count": 1})
        self.assertEqual(presented_pairs(turn), [("C-1", "OPEN")])
        self.assertIsInstance(turn.cases, tuple)

    def test_update_completed_before_episode_is_visible(self):
        # X-3 / B-2 / B-5 / DS-I5.
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        store.update_status("C-1", "CLOSED")
        turn = start(store)
        self.assertEqual(turn.page_summary["revision"], 2)
        self.assertEqual(turn.page_summary["open_count"], 1)
        self.assertEqual(presented_pairs(turn), [("C-1", "CLOSED"), ("C-2", "OPEN")])

    def test_later_episode_revision_never_decreases(self):
        # B-3 / B-6(c) / DS-I3; also fixes the fixture's start-1 / step-1 behaviour (C-8).
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        revisions = []
        for index in range(3):
            revisions.append(start(store).page_summary["revision"])
            store.update_status("C-1", "CLOSED" if index % 2 == 0 else "OPEN")
        self.assertEqual(revisions, sorted(revisions))
        self.assertEqual(revisions, [1, 2, 3])

    def test_equal_revision_presents_equal_case_data(self):
        # X-1 / B-4 / DS-I4: no update between episodes.
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        first = start(store)
        second = start(store)
        self.assertEqual(first.page_summary["revision"], second.page_summary["revision"])
        self.assertEqual(presented_pairs(first), presented_pairs(second))

    def test_each_update_between_episodes_is_visible(self):
        # X-4 / B-2 / B-5: two completed updates are reflected by the next episode.
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        first = start(store)
        store.update_status("C-1", "CLOSED")
        store.update_status("C-2", "CLOSED")
        second = start(store)
        self.assertGreater(second.page_summary["revision"], first.page_summary["revision"])
        self.assertEqual(second.page_summary["open_count"], 0)
        self.assertEqual(presented_pairs(second), [("C-1", "CLOSED"), ("C-2", "CLOSED")])

    def test_empty_case_set_presents_zero_open_and_no_details(self):
        # X-6 / B-1.
        turn = start(store_with())
        self.assertEqual(turn.page_summary, {"revision": 1, "open_count": 0})
        self.assertEqual(presented_pairs(turn), [])

    def test_update_with_unknown_case_id_leaves_all_statuses_unchanged(self):
        # DS-I7 with DS-U2: the statuses are unchanged; the fixture keeps advancing the revision (D-4).
        store = store_with(("C-1", "OPEN"), ("C-2", "OPEN"))
        before = start(store)
        store.update_status("C-9", "CLOSED")
        after = start(store)
        self.assertEqual(presented_pairs(after), presented_pairs(before))
        self.assertEqual(after.page_summary["revision"], before.page_summary["revision"] + 1)

    def test_existing_entry_points_stay_callable_with_a_bare_store(self):
        # C-8: the pre-existing call forms keep their shape and results.
        store = store_with(("C-1", "OPEN"))
        turn = start(store)
        self.assertEqual(set(turn.page_summary), {"revision", "open_count"})
        self.assertIsInstance(cases(store), tuple)
        self.assertTrue(all(isinstance(case, CaseRecord) for case in cases(store)))


if __name__ == "__main__":
    unittest.main()
