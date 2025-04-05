# 🧪 ProofGPT Experiment Log
**Date:** 2025-04-05

This markdown documents formal reasoning experiments using ProofGPT with various axiom sets and GPT models.

| Title | Statement | Axiom Set | Model | Result | Notes |
|-------|-----------|-----------|-------|--------|-------|
| Two Points Determine a Line | Any two distinct points determine a unique line. | hilbert.json | gpt-4o | ✅ Valid proof | Matched exactly with Axiom 1. GPT-4o stopped immediately after recognizing it as a direct axiom statement. |
| Two Lines Always Intersect | Any two lines intersect at a point. | hilbert.json | gpt-4o | ❌ Undecidable | Correctly identified lack of a parallel axiom. GPT-4o refused to fabricate proof. This is a key test of axiomatic boundaries. |
| Modular Division: 3n ≡ 3 (mod 5) | If 3n ≡ 3 (mod 5), then the smallest natural value of n is 1. | logic + number theory (w/ Modular Cancellation) | gpt-4o | ✅ Valid proof with Axiom 74, 75, 76 | Proper use of modular cancellation with coprime. Fails without Axiom 74. GPT-4o halts when cancellation isn’t valid. |
| Modular Division: 4n ≡ 8 (mod 10) | If 4n ≡ 8 (mod 10), find smallest natural n. | logic + number theory (w/ Axiom 80) | gpt-4o | ✅ Valid proof | Used Axiom 80 to reduce the congruence. GPT-4o handled gcd(4,10)=2 correctly and derived n ≡ 2 (mod 5). |
| Fails with GPT-3.5 | Same Hilbert axiom proof tests | hilbert.json | gpt-3.5-turbo | ❌ Often incorrect or ignores axioms | Does not halt on invalid reasoning. Sometimes makes up new definitions. Cannot reliably quote axioms unless statement exactly matches. |
