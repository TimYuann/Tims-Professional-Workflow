# Absorb knowledge demos · observations (DBG-05 / DBG-16)

State: **bounded observation record** by `tpw-night-check` (Pi session `01a0f66d-0b7b-7701-8c51-8d262cb2f8d4`, `commandcode/deepseek/deepseek-v4.1-flash` / max), 2026-10-01. Authority: Owner request relayed by the Driver inside `ABSORB-FULL-CORRECTION-BRIEF.md` ("two cheap local demonstrations for the new knowledge, if useful"). Report only: no core/product/UCBIP change, no new gate, no commit.

Objects exercised (night tree, current bytes):

| Object | Identity |
| --- | --- |
| DBG-05 draft rev.2 | `docs/overnight/2026-10-01/ABSORB-DRAFT-DBG-05-EVIDENCE.md` SHA-256 `40d0213f97d01a4f23362407731a850dc8ab2bb12dbf5346166019d9c757a8a1` |
| DBG-16 draft rev.2 | `docs/overnight/2026-10-01/ABSORB-DRAFT-DBG-16-MOCK-ADAPTER.md` SHA-256 `73fdb667b8fcf54b3bee039a41a4f9d6ae36a14ffb6bb5d4ab2ac793b33413d9` |
| Demo directory | `/Users/yuantian/Developer/tim-professional-workflow/.worktrees/verification/absorb-demos/` — disposable, untracked, synthetic-only |
| Runtime | node `v22.22.2`; no network, no service, no real credentials or user data; all fixtures are JSON created for the demo |

Write set was exactly the demo directory plus this file. Nothing else was modified; nothing was committed.

## 1 · DBG-05 · redact-first evidence vs “write full raw, then grep”

Command (from the demo directory):

```
node dbg05/redact-first-demo.mjs
```

**Exit code: 0.** Fixture `dbg05/fixture-http-401-synthetic.json` is declared synthetic in-file and contains **5** `FAKE_SECRET_SENTINEL_*` occurrences (Authorization header, request body, `set-cookie`, JSON `message`, `provider_token_hint`). It is not a production capture.

Key output (verbatim excerpt):

```
fixture sentinels: 5
redacted evidence -> .../dbg05/out/redacted-evidence.txt
HTTP/1.1 401 Unauthorized
content-type: application/json
www-authenticate: Bearer realm="payments", error="token_expired"
x-request-id: req_synthetic_7f3c9d01
error=token_expired
raw capture (synthetic) -> .../dbg05/out/raw-capture.json | sentinels on disk: 5
grep-after-raw -> .../dbg05/out/grep-after-raw.txt | sentinels in displayed lines: 0
PASS  redacted evidence contains no FAKE_SECRET_SENTINEL_*
PASS  redacted evidence keeps the diagnostic signal
PASS  the error code supplies the 401 reason (www-authenticate alone would not)
PASS  raw-capture.json persisted FAKE_SECRET_SENTINEL_* values (display != storage)
PASS  grep-after-raw.txt itself is clean but the raw file it came from is not
observations matched expectations: yes (5/5)
```

Observation: the default route persisted only a five-line evidence record containing **no** sentinel and keeping the diagnostic signal (`HTTP/1.1 401`, `www-authenticate`, `x-request-id`, `error=token_expired`). The `error=token_expired` value is what names the 401 cause; `www-authenticate: Bearer` alone does not — matching the draft’s §3 example. The wrong route wrote the **complete** synthetic response to `raw-capture.json` (sentinels still on disk) and only then extracted clean display lines. **The clean grep output does not mean the raw was not saved**: the raw file remains on disk with the sentinels; displaying a few lines after persistence is not redaction. This aligns with DBG-05.1 (redact first) and DBG-05.3 (minimal in-line artifact boundary); the independent raw branch (DBG-05.4) was **not** opened, and `step`/`capture` (DBG-05.5) was not exercised.

Limits: synthetic fixture only; proves the example’s discriminating power, not runtime enforcement by any host/hook/tool; no real redaction tool, terminal echo or cleanup/retention boundary was tested; “sufficient signal” holds for this fixture only; the wrong-route raw file (synthetic) stays inside the disposable demo directory.

## 2 · DBG-16 · port-level green while the production adapter boundary is broken

Command:

```
node dbg16/run-demo.mjs
```

**Exit code: 0.** Inputs are local JSON “fake HTTP responses” (`dbg16/fixtures/price-nested-null.json`, `dbg16/fixtures/price-nested-missing-price.json`); no server and no network are involved.

Key output (verbatim excerpt):

```
PASS  business: SKU-A total 1200  [{"sku":"SKU-A","totalCents":1200}]
PASS  business: SKU-B total 400 after discount  [{"sku":"SKU-B","totalCents":400}]
-- adapter contract surface vs lenient/buggy production adapter --
FAIL  lenient production adapter (defect): nested null discount parses to 1200/0  [returned {"unitPriceCents":0,"discount":0}]
FAIL  lenient production adapter (defect): missing unit_price_cents is not swallowed to 0  [returned {"unitPriceCents":0,"discount":0}]
-- adapter contract surface vs strict production adapter --
PASS  strict production adapter (correct): nested null discount parses to 1200/0  [returned {"unitPriceCents":1200,"discount":0}]
PASS  strict production adapter (correct): missing unit_price_cents is not swallowed to 0  [threw PriceAdapterError: unit_price_cents missing or not a number]
...
key observation: business suite passed 2/2 while the lenient production adapter failed 2/2 adapter contract checks; the strict adapter passed 2/2.
observations matched expectations: yes
```

Observation: the business port suite stayed fully green with the in-memory adapter while the defect-bearing production-style adapter silently coerced nested/missing fields to `{unitPriceCents: 0, …}` instead of erroring. The adapter contract surface caught the defect (both checks red), and the strict adapter — raising on null/missing rather than swallowing into 0 — passed both checks, including the thrown `PriceAdapterError` for the missing `unit_price_cents`. This matches the draft’s §3 mechanism (flat-shape assumption vs nested `data`) and its §1.3 coverage boundary: port/in-memory tests do not execute the production transport/serialization adapter. The implied corrective surface is adapter-level contract observation (or moving normalization below the port), not the business layer.

Limits: synthetic local JSON only; no real service, transport or serialization stack; proves the discriminator for these fixtures, not any real project’s adapter; does not prove test-framework integration and creates no global integration gate; the strict adapter is demo-authored, not a production artifact.

## 3 · What this establishes and what it does not

- Establishes (bounded): both drafted knowledge items are usable at the example level; their examples distinguish the default from the wrong route (DBG-05) and port-level coverage from adapter-level correctness (DBG-16).
- Does **not** establish: runtime enforcement or host behavior; UCBIP adoption or qualification; universal efficiency, cost or business effects; results in any product repository’s test runtime; any change to old M3 evidence status; nor that all scripts/runtime paths were validated.
- No new gate, validator, composer, framework, registry or persistent role was created. The demo directory is disposable and outside tracked core/product paths.

## 4 · Disposable artifact hashes

```
a973b7f089c0bc3a2a5a567a005027f43169969a440fe02779b9b146bb8d95ba  README.md
ac48faeb8aff20871f3b161e7a5ba836b13d6739049ab7d196e03bd61c14e49d  dbg05/fixture-http-401-synthetic.json
e58ebf5b93fa0e7436033047db6bbaa6f63c12e9d03c4e35fae06a657fe09ee4  dbg05/out/grep-after-raw.txt
ac48faeb8aff20871f3b161e7a5ba836b13d6739049ab7d196e03bd61c14e49d  dbg05/out/raw-capture.json
cacb9f480125288e11dd520122e72addbfe346342c1758813a60f9693cbd5a25  dbg05/out/redacted-evidence.txt
049f269e52fbb2a516f42f9aed72c0b859f8b3db31bebec3974acbbc874d4d90  dbg05/redact-first-demo.mjs
5d2d7f80a7f022563d46c60845e9e9636c39c962736aa432c2989b959e8b9667  dbg16/business.mjs
dd8c124639440433cd5f2609287cafbae6e1ded798f2a1f909a976f5ae6ed8a3  dbg16/fixtures/price-nested-missing-price.json
01df575587b575e9684f5f6c155cfde46d7746c4d15c97916e74d83e2c0548f3  dbg16/fixtures/price-nested-null.json
fd862cd5bded6eed4cae41899afaec90b67b1bc907d33692f2b99d02aadf07ea  dbg16/lenient-adapter.mjs
be0c2b5f29cd79b2f3864b6bc244349d27cbae5aed9a37d886daba506822a5e9  dbg16/production-adapter.mjs
225d0fdeb4ad533ddd9c8d8db3c32952bad8078dba6f2149b9df72580b100fde  dbg16/run-demo.mjs
```

`raw-capture.json` is byte-identical to the synthetic fixture (same SHA-256), which is expected: the wrong route persisted exactly the fixture bytes before grepping. No production bytes were involved.
