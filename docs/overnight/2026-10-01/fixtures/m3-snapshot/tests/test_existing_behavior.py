import unittest

from src.service import cases, start
from src.state_store import CaseRecord, StateStore


class ExistingSnapshotFixtureTests(unittest.TestCase):
    def setUp(self):
        self.store = StateStore((CaseRecord("C-1", "OPEN"), CaseRecord("C-2", "OPEN")))

    def test_summary_counts_current_open_cases(self):
        turn = start(self.store)
        self.assertEqual(turn.page_summary["open_count"], 2)

    def test_case_reader_returns_current_cases(self):
        self.assertEqual(len(cases(self.store)), 2)

    def test_update_changes_next_current_read(self):
        self.store.update_status("C-1", "CLOSED")
        self.assertEqual(self.store.current_view().revision, 2)
        self.assertEqual(cases(self.store)[0].status, "CLOSED")


if __name__ == "__main__":
    unittest.main()
