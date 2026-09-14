import unittest

from deep_tests.contract_model import Command, IdempotencyConflict, ReferenceStore, generate_valid_trace, replay


class QuaestorDomainHardeningTests(unittest.TestCase):
    def test_duplicate_ledger_post_is_exactly_once(self) -> None:
        store = ReferenceStore()
        post = Command("create", "entry-20260914-0001", "debit:100|credit:100", "ledger-post-0001")
        first = store.apply(post)
        revision = store.revision
        for _ in range(40):
            self.assertEqual(store.apply(post), first)
        self.assertEqual(store.revision, revision)

    def test_ledger_idempotency_key_cannot_rebind_amount(self) -> None:
        store = ReferenceStore()
        store.apply(Command("create", "entry-20260914-0001", "amount-100", "stable-ledger-key"))
        store.apply(Command("create", "entry-20260914-0002", "amount-25", "second-entry"))
        with self.assertRaises(IdempotencyConflict):
            store.apply(Command("update", "entry-20260914-0001", "amount-125", "stable-ledger-key"))

    def test_ledger_trace_converges_under_duplicate_delivery(self) -> None:
        commands = generate_valid_trace(2026091403, steps=900)
        snapshots = {replay(commands, duplicate_every=n).snapshot() for n in (2, 3, 8, 21)}
        self.assertEqual(len(snapshots), 1)


if __name__ == "__main__":
    unittest.main()
