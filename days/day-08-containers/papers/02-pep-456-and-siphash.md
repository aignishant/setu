---
day: 8
part: "P2"
title: "The hash that had to become unpredictable — PEP 456 and SipHash"
ids: ["PY-08"]
level: production
kind: paper
paper: ["PEP 456", "doi:10.1007/978-3-642-34931-7_28"]
prerequisites: ["2.1", "P1"]
prev: "01-the-timsort-note.md"
next: "../CHECKLIST.md"
---

# The hash that had to become unpredictable

## One-line answer

A hash table's `O(1)` lookup is an **average** over keys the table's designer assumed nobody chose on
purpose — and once attackers started choosing them, Python replaced its hash function with a keyed
cryptographic one seeded per process, which is why `hash("setu")` prints a different number every time
you start the interpreter and why that fact is a security control rather than a curiosity.

---

## The citation

Two documents: the cryptographic construction, and the proposal that adopted it into Python.

| Field | The construction | The proposal |
|---|---|---|
| **Title** | *"SipHash: A Fast Short-Input PRF"* | *"PEP 456 — Secure and interchangeable hash algorithm"* |
| **Year** | 2012 (INDOCRYPT 2012) | 2013, Final, landed in **Python 3.4** |
| **Identifier** | `doi:10.1007/978-3-642-34931-7_28` · IACR ePrint `2012/351` | `PEP 456` |
| **URL** | <https://link.springer.com/chapter/10.1007/978-3-642-34931-7_28> — fetched 2026-08-25 | <https://peps.python.org/pep-0456/> — fetched 2026-08-25 |

The PEP's abstract, verbatim:

> "This PEP proposes SipHash as default string and bytes hash algorithm to properly fix hash
> randomization once and for all. It also proposes modifications to Python's C code in order to unify
> the hash code and to make it easily interchangeable."

**What to actually read.** The PEP's **Abstract** and **Rationale** — the rationale is the part that
explains why the *previous* attempt at randomisation was not enough, which is the whole reason the
document exists. Of the construction paper, read the **abstract and the security claims**; the round
function itself is only worth following if you are implementing it, and you should not be.

---

## The story

A web framework receives a POST with a few thousand form fields. It does what every framework does:
puts them in a dictionary. The request takes a very long time. A handful of such requests, sent from a
single laptop, and the server stops answering anyone.

Nothing is broken. The dictionary is behaving exactly as
[2.1](../parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md) describes: keys are hashed to buckets,
and a lookup checks the keys that landed in the same bucket. The `O(1)` claim assumes those keys are
spread out. It is an *average over typical inputs*, and the field names in a POST body are chosen
entirely by whoever sent the request.

If the hash function is public and unkeyed — as every language's string hash was — an attacker can
compute it offline and generate thousands of distinct strings that all land in the same bucket. Every
insert then scans the whole chain. `n` insertions cost `n²` comparisons instead of `n`. A few hundred
kilobytes of request body buys minutes of CPU.

This was demonstrated against essentially every major language runtime at once. The first response was
to add a random seed to the existing hash function — which helped, until it was shown the secret could
be recovered by observing behaviour, at which point the randomisation was decoration. The real fix had
to be a function that is *designed* to keep its key secret even when an attacker can see its outputs.
That is a cryptographic requirement, and it needed a cryptographic primitive: a short-input
pseudorandom function fast enough to run on every string hash in the language.

---

## The idea in plain language

**A hash table's performance guarantee is a statistical claim, and statistics assume nobody is
choosing the inputs adversarially.** Once the inputs are attacker-controlled, the average case is not
the case you get. This is the entire subject; everything else is mechanism.

**A PRF is not a checksum.** A *pseudorandom function* takes a secret key and a message and produces
output that is indistinguishable from random to anyone who does not have the key — even after seeing
outputs for many messages they chose. That last clause is what defeats the attack: an attacker can
observe collisions all day and still cannot compute new ones, because they cannot recover the key.

**SipHash is a PRF built for very short inputs.** Ordinary cryptographic hashes are optimised for
throughput on large messages; a language runtime needs to hash a four-character dictionary key
millions of times. SipHash was designed for exactly that regime. It takes a 128-bit key and produces a
64-bit output, and its default parameterisation is written as a pair of round counts — SipHash-2-4
means two compression rounds per message block and four finalisation rounds.

**The key is per process, and that is the point.** Python generates the secret at interpreter startup.
Two runs of the same script hash the same string to different numbers, so an attacker cannot precompute
collisions for a target they cannot see inside. The visible consequence is the one that surprises
people: **set and dict iteration order for strings can differ between runs**, and any test that
depended on it was always depending on an accident.

**`PYTHONHASHSEED` turns it off, on purpose.** Setting it to a fixed integer makes hashing
deterministic, which is what you want when reproducing a bug or making a test suite repeatable — and
exactly what you must not do on a server that takes untrusted input.

---

## Why Setu needs it

- **[2.1](../parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md) taught the hash table** and the
  `O(1)` membership test that makes [3.1](../parts/03-dedup/3.1-ten-thousand-ids-timed.md)'s dedup
  fast. This document is the fine print on that `O(1)`: it holds because the hash is unpredictable,
  not because hashing is magic.
- **[Day 4, 2.5](../../day-04-objects/parts/02-containers/2.5-hashability.md) established what makes
  an object hashable** and why `__eq__` and `__hash__` travel together. This is what the built-in
  `__hash__` for `str` and `bytes` actually is.
- **Reproducibility (Principle 4) collides with it directly.** Anything in this plan that iterates a
  set of strings and expects a stable order is relying on something that is deliberately not stable.
  The fix is `sorted()`, not `PYTHONHASHSEED`.
- **Downstream:** every retriever, cache and dedup layer in the later phases is a hash table taking
  strings from documents you did not write. The threat model in this document is the one your agent
  tooling inherits the moment it processes third-party text.

---

## The mechanism

The attack, and the defence, are both visible in a table small enough to read. First, what makes a
hash *weak* in this specific sense:

```python
BUCKETS = 64


def weak_hash(key: str) -> int:
    return sum(key.encode()) % BUCKETS


print(weak_hash("mmmm"), weak_hash("lnmm"), weak_hash("aqzd"))
```

**Line by line:**

- `sum(key.encode())` — the sum of the byte values. It is a perfectly reasonable-looking hash: cheap,
  spreads ordinary words across buckets, and satisfies the one hard requirement that equal strings
  hash equally.
- `% BUCKETS` — the fold into a bucket index, exactly as
  [2.1](../parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md) described it.
- The three arguments are the attack in miniature: `"mmmm"`, `"lnmm"` and `"aqzd"` are different
  strings whose bytes sum to the same total, so they print the same bucket. Nothing was reverse
  engineered — **addition is commutative**, so anagram-like keys collide by construction, and an
  attacker who knows the function can generate them by the thousand.

Now the defence, which is one substitution:

```python
import hashlib

BUCKETS = 64


def keyed_hash(key: str, secret: bytes) -> int:
    digest = hashlib.blake2b(key.encode(), key=secret, digest_size=8).digest()
    return int.from_bytes(digest, "big") % BUCKETS
```

**Line by line:**

- `hashlib.blake2b(..., key=secret, ...)` — a **keyed** hash. This plan uses BLAKE2b here because it is
  in the standard library and takes a key directly; CPython uses SipHash internally, which is the same
  idea tuned for very short inputs. The structural point is the `key=` argument: without it, this is
  just a public function again and the attack returns.
- `digest_size=8` — 64 bits, matching the width of a Python hash value. A hash table has no use for
  more, and shorter output is faster to fold.
- `int.from_bytes(digest, "big")` — the digest is bytes; a bucket index needs an integer. The
  endianness is stated explicitly rather than left to the platform, for the same reason
  [Day 4's IEEE 754 part](../../day-04-objects/papers/01-ieee-754.md) states it: an unstated default is
  a bug waiting for a different machine.
- `secret` is passed in rather than read from a global, so the demo can show two secrets producing two
  different layouts. CPython does the equivalent once at startup, into `_Py_HashSecret`.

What Python actually reports about its own hash:

```python
import sys

print(sys.hash_info.algorithm, sys.hash_info.hash_bits, sys.hash_info.seed_bits)
```

**Line by line:**

- `sys.hash_info.algorithm` — the name of the implementation in this interpreter. On Python 3.12 it is
  `siphash13`, **not** `siphash24`: CPython moved its default from SipHash-2-4 to SipHash-1-3 in 3.11,
  trading rounds for speed. The PEP adopted one parameterisation; the runtime later chose another.
- `hash_bits` is 64 — the output width, matching `digest_size=8` above.
- `seed_bits` is 128 — the size of the per-process secret, which is SipHash's key size. That number is
  the security parameter: it is what an attacker would have to guess.

---

## The demo

One project, one feature: **carry out the collision attack against an unkeyed hash table, then defeat
it by keying the hash**. No web framework, no network, no real SipHash implementation — the claim
being demonstrated is that keying the hash is what removes the attacker's control.

```text
hash-dos/
├── weak_table.py        # a chained hash table, an unkeyed hash, a keyed one, and the attack keys
└── test_weak_table.py   # the PEP's claim, asserted
```

`weak_table.py`, in full:

```python
"""The attack PEP 456 exists to stop, and the one change that stops it."""

import hashlib
from itertools import product

BUCKETS = 64


def weak_hash(key: str, secret: bytes = b"") -> int:
    """An unkeyed hash: the attacker can compute it too, so the attacker can choose collisions."""
    return sum(key.encode()) % BUCKETS


def keyed_hash(key: str, secret: bytes) -> int:
    """PEP 456's shape: the same input, mixed with a per-process secret the attacker cannot see."""
    digest = hashlib.blake2b(key.encode(), key=secret, digest_size=8).digest()
    return int.from_bytes(digest, "big") % BUCKETS


class Table:
    """A hash table with chained buckets. `probes` counts the work an insert actually did."""

    def __init__(self, hash_fn, secret: bytes = b"") -> None:
        self.buckets: list[list[str]] = [[] for _ in range(BUCKETS)]
        self.hash_fn = hash_fn
        self.secret = secret
        self.probes = 0

    def insert(self, key: str) -> None:
        bucket = self.buckets[self.hash_fn(key, self.secret)]
        for existing in bucket:  # the linear scan the attacker is trying to lengthen
            self.probes += 1
            if existing == key:
                return
        bucket.append(key)

    def longest_bucket(self) -> int:
        return max(len(b) for b in self.buckets)


def colliding_keys(count: int) -> list[str]:
    """Every 4-letter key whose bytes sum to the same total - computed offline, before the attack."""
    target = 4 * ord("m")
    found = []
    for combo in product(range(ord("a"), ord("z") + 1), repeat=4):
        if sum(combo) == target:
            found.append("".join(chr(c) for c in combo))
            if len(found) == count:
                break
    return found
```

**Line by line:** — `weak_hash` and `keyed_hash` are the mechanism above; only what is new here is
walked through.

- `weak_hash(key, secret=b"")` takes a `secret` it ignores, purely so the two functions have the same
  signature and `Table` can hold either. Making the insecure and secure versions interchangeable is
  the demo's whole shape — and it is also PEP 456's second goal, quoted in the citation above: making
  the hash *interchangeable* so it can be replaced again later.
- `self.buckets: list[list[str]] = [[] for _ in range(BUCKETS)]` — a list comprehension, not
  `[[]] * BUCKETS`, which would create 64 references to **one** list. That is
  [Day 4's aliasing trap](../../day-04-objects/parts/02-containers/2.3-aliasing-two-names-one-object.md)
  and it would make every key land in every bucket at once.
- `for existing in bucket: self.probes += 1` — the counter increments once per key already sitting in
  the bucket. This is the cost model: a lookup is `O(1)` only if this loop is short, and the attack
  consists entirely of making it long.
- `if existing == key: return` — the equality check that a hash table must do even after the hash
  matches, because a hash collision is not an equality. This is where the CPU goes.
- `longest_bucket()` — the diagnostic that distinguishes "slow" from "under attack". A table doing a
  lot of work with a max chain of 20 is loaded; one with a max chain of 400 is being attacked.
- `target = 4 * ord("m")` — an arbitrary achievable total for four lowercase letters. Any target works;
  `m` is the middle of the alphabet, so it has the most combinations.
- `product(range(ord("a"), ord("z") + 1), repeat=4)` — brute force over four-letter keys, filtered to
  those hitting the target sum. It runs in a fraction of a second, which is the uncomfortable part:
  **the attacker's preparation is trivial** when the hash is public.

`test_weak_table.py`, in full:

```python
"""The PEP's claim, asserted: keying the hash removes the attacker's control."""

import os
import random
import string

from weak_table import Table, colliding_keys, keyed_hash, weak_hash

SECRET = os.urandom(16)


def random_keys(count: int) -> list[str]:
    random.seed(0)
    return ["".join(random.choices(string.ascii_lowercase, k=4)) for _ in range(count)]


def test_the_attack_works_against_an_unkeyed_hash():
    keys = colliding_keys(400)
    table = Table(weak_hash)
    for key in keys:
        table.insert(key)
    assert table.longest_bucket() == len(keys)
    assert table.probes > len(keys) ** 2 / 4


def test_honest_traffic_is_cheap_on_the_same_table():
    table = Table(weak_hash)
    for key in random_keys(400):
        table.insert(key)
    assert table.probes < 400 * 20


def test_keying_the_hash_defeats_the_precomputed_collisions():
    keys = colliding_keys(400)
    table = Table(keyed_hash, SECRET)
    for key in keys:
        table.insert(key)
    assert table.longest_bucket() < len(keys) / 4
    assert table.probes < 400 * 20


def test_a_different_secret_gives_a_different_layout():
    keys = colliding_keys(50)
    first = [keyed_hash(k, b"secret-one") for k in keys]
    second = [keyed_hash(k, b"secret-two") for k in keys]
    assert first != second
```

**Line by line:**

- `SECRET = os.urandom(16)` — 16 bytes, 128 bits, SipHash's key size, drawn from the OS entropy source.
  Generated once at import, exactly as CPython generates its secret once at startup. Using
  `random.random()` here would be a real bug: that generator is predictable, and a predictable secret
  is not a secret.
- `assert table.longest_bucket() == len(keys)` — **every single key** in one bucket. Not "many"; all
  400. The attack is not statistical, it is exact, because the attacker computed the same function the
  table did.
- `assert table.probes > len(keys) ** 2 / 4` — the quadratic claim, stated as a bound rather than an
  exact figure. `n` insertions into one chain cost about `n²/2` probes; the test asserts comfortably
  under that so it cannot fail for an off-by-one, and comfortably over linear so it cannot pass by
  accident.
- `test_honest_traffic_is_cheap_on_the_same_table` uses the **same weak hash**. That is what makes the
  pair of tests an argument: the function is not slow, and the table is not badly written. The only
  variable is who chose the keys.
- `random.seed(0)` in `random_keys` — the honest traffic is reproducible, so a future failure of this
  test means the table changed, not that the dice fell differently.
- `assert table.longest_bucket() < len(keys) / 4` in the keyed test — a loose bound, deliberately.
  With 400 keys in 64 buckets the expected chain is a little over six; asserting `< 100` states "the
  attacker no longer controls the distribution" without making the test fragile to the random secret
  it draws each run.
- `test_a_different_secret_gives_a_different_layout` compares two fixed secrets rather than using
  `SECRET`, so the assertion is deterministic. This is the property that makes precomputation
  worthless: the same keys, a different secret, a different layout.

Run it:

```console
$ uv run --with pytest python -m pytest -q
....                                                                     [100%]
4 passed in 0.08s

$ uv run python -c "
import os, random, string
from weak_table import Table, colliding_keys, weak_hash, keyed_hash
random.seed(0)
honest = [''.join(random.choices(string.ascii_lowercase, k=4)) for _ in range(400)]
attack = colliding_keys(400)
secret = os.urandom(16)
for name, keys, fn, sec in [
  ('honest keys, unkeyed hash', honest, weak_hash, b''),
  ('crafted keys, unkeyed hash', attack, weak_hash, b''),
  ('crafted keys, keyed hash  ', attack, keyed_hash, secret)]:
    t = Table(fn, sec)
    for k in keys:
        t.insert(k)
    print(f'{name}  probes={t.probes:7d}  longest bucket={t.longest_bucket():4d}')"
honest keys, unkeyed hash  probes=   1512  longest bucket=  21
crafted keys, unkeyed hash  probes=  79800  longest bucket= 400
crafted keys, keyed hash    probes=   1220  longest bucket=  12
```

Three lines, one argument. Same table, same number of keys: **1 512 probes** of work becomes **79 800**
— fifty times more — purely because the attacker chose the keys. Then keying the hash brings it back
to 1 220, with the longest chain down from 400 to 12. The attacker's precomputed list is now just four
hundred ordinary strings.

**What this demo deliberately leaves out.** The actual SipHash round function (BLAKE2b stands in for
it, because you should never hand-roll a primitive); open addressing and probing, which is what CPython
really uses rather than chaining; table resizing and load factors; and the collision-resolution
improvements — total ordering fallbacks, per-instance limits — that runtimes added alongside
randomisation. It demonstrates the *one* claim the PEP rests on: an unkeyed hash hands the attacker
the distribution, and a keyed one does not.

---

## When it breaks

The first thing this breaks is a test that was always wrong:

```python
print(hash("setu"))
```

Run twice, in two processes:

```text
-2933868002120763299
-7688708470019131446
```

Same string, same interpreter, different number — by design. Anything downstream of that is
non-deterministic too, most visibly the iteration order of a `set` of strings. A test asserting
`list(my_set) == ["a", "b", "c"]` passes on your machine, passes in review, and fails in CI on the
run where the seed happens to reorder it.

Pin the seed and it stops:

```text
$ PYTHONHASHSEED=0 python -c "print(hash('setu'), hash(b'setu'), hash(1))"
6369047189767812498 6369047189767812498 1
```

Three things in that line are worth reading. The value is now stable across runs. `str` and `bytes`
hash **identically**, which PEP 456 specifies deliberately. And `hash(1)` is `1` — small integers are
not hashed at all, because the attack is against *string* keys parsed from untrusted input, and paying
a cryptographic function for integer keys would be a large cost for nothing.

**The smallest fix — and the wrong one.** The wrong fix is setting `PYTHONHASHSEED=0` to make the test
pass. That disables a security control process-wide, and if the same configuration reaches a service
that puts untrusted strings into dictionaries, the attack in the demo becomes available again. The
right fix is `sorted(my_set)` in the assertion, because the code should never have depended on hash
order in the first place. Reserve `PYTHONHASHSEED` for reproducing a specific bug.

---

## What did not survive

**The first fix did not work, and that is the reason this document exists.** Before PEP 456, Python
already had hash randomisation — an earlier scheme that mixed a random prefix and suffix into the
existing hash. It was shown that the secret could be recovered by an attacker who could observe the
behaviour of a running server, which reduced the defence to an inconvenience. The lesson generalises
beyond hashing: *adding randomness to a non-cryptographic function does not produce a cryptographic
one*.

**The chosen parameterisation did not survive.** The PEP adopted SipHash-2-4, the construction's own
recommended default. CPython's default is now **SipHash-1-3** — fewer rounds, more speed — which
`sys.hash_info.algorithm` will tell you on any current interpreter. The security margin was judged
larger than this application needs. Whether that judgement is right is a live question, and it is a
good example of a paper's recommended defaults being *tuned* rather than *followed* once a real system
adopts it.

**The threat model moved.** Randomised hashing stops precomputed collision attacks; it does not stop
an attacker who can observe timing and adapt, and it does nothing for hash tables keyed by
attacker-controlled data in a system that leaks ordering. Runtimes have layered further defences on
top — collision counting, ordering fallbacks — and web frameworks independently added limits on the
number of parameters per request, which is arguably the more robust control because it bounds the
damage regardless of the hash.

**And the visible cost landed somewhere nobody planned.** Randomisation broke a large amount of code
that had accidentally depended on stable iteration order, and a decade later `PYTHONHASHSEED=0` still
appears in CI configurations where it does not belong — usually to make a flaky test stop failing.
A security control that is routinely disabled by people trying to be tidy is a design lesson in
itself.

---

## In production

**What a professional does.** They never depend on hash order — `sorted()` in any assertion, any
serialisation, any output a human will diff. They leave `PYTHONHASHSEED` unset in every environment
that faces untrusted input, and set it only in a debugging session. And when a dictionary keyed by
external strings shows up in a hot path, they bound the *number of keys* accepted rather than trusting
the hash alone, because the hash defends against chosen collisions and not against volume.

**What changes at scale.** In a long-running service, the per-process secret means two workers hash
the same string differently — so anything that shards by `hash(key) % n_workers` is unstable across
processes and across restarts. Distributed systems consequently do not use the built-in hash for
partitioning: they use an explicit, stable function such as `hashlib.blake2b` or a non-cryptographic
hash with a fixed seed, precisely *because* they need the property Python deliberately removed. Knowing
which of the two you want is the whole skill.

**The failure that only appears with real data.** A cache keyed by user-supplied strings runs happily
for a year. One caller starts generating keys from a template that produces near-identical strings by
the million; latency climbs, CPU is pinned in one process, and profiling shows time inside dictionary
lookups. It is not an attack — but it is the same failure, because "adversarial" and "unlucky" are
indistinguishable to a hash table.

**The review comment a senior engineer leaves.** On `PYTHONHASHSEED=0` in a CI file — *"This disables
hash randomisation for the whole suite to fix an ordering assumption. Sort the assertion instead and
take the seed back out."* On `shard = hash(user_id) % 16` — *"`hash()` is seeded per process; two
workers will disagree and a restart will reshuffle everything. Use `blake2b` with a fixed key for
anything that must be stable across processes."*

**The interview question.** *"Why does `hash('a')` change between runs?"* The shallow answer is "hash
randomisation". The answer that shows you have read the source is: *because dictionary lookup is `O(1)`
only when keys are spread out, and if the hash is public an attacker can craft thousands of colliding
keys and turn one request into quadratic work — so the string hash is a keyed PRF with a per-process
secret, which makes precomputation impossible.* The follow-up is usually *"when would you turn it
off?"*, and the answer that matters is: *to reproduce a bug locally, never in a process that reads
untrusted input.*

---

## Check yourself

Run this now:

```bash
uv run python -c "import sys; print(sys.hash_info.algorithm, sys.hash_info.hash_bits, sys.hash_info.seed_bits)"
uv run python -c "print(hash('setu'))"
uv run python -c "print(hash('setu'))"
```

The first line should name a SipHash variant with 64 output bits and a 128-bit seed; the next two
should print **different** numbers for the same string. If they match, check whether something in your
environment has set `PYTHONHASHSEED` — and find out why.

**Say this out loud, without scrolling up:** *explain how an attacker turns a dictionary into a denial
of service using nothing but chosen key names, say what keying the hash changes about that, and give
one reason you would still never use `hash()` to shard data across workers.*

Back to the day: [`CHECKLIST.md`](../CHECKLIST.md)
