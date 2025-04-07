# ❌ Experiment Log: Burnside Lemma Failure (Undecidable)

This experiment tests whether GPT-4o, under Formalizer constraints, can solve a problem that implicitly requires Burnside's Lemma—a combinatorics principle not included in the axiom set.

---

## 🧠 Problem

> "How many distinct colorings are there of the vertices of a square using two colors, up to rotation?"

This is a classic **group action** problem requiring Burnside’s Lemma to count symmetry-invariant configurations.

---

## 📦 Axiom Layer Used

- **Layer**: `mathematical/combinatorics_extended.json`
- **Included Axioms**:
  - CMB1: Definition of Factorial
  - CMB2: Permutation Formula
  - CMB3: Combination Formula ✅
  - CMB4: Binomial Theorem
  - CMB5: Pascal’s Rule
  - CMB6: Inclusion-Exclusion Principle (2 sets)
  - CMB7: Complement Principle

❗ **Burnside's Lemma is not included.**

---

## 🔍 Result

🧠 GPT-4o Response: Undecidable. 📚 Axioms Used: []

---

## ✅ Interpretation

- GPT **recognized** that the problem could not be solved with the given axioms.
- It did **not hallucinate** an answer or invent a formula.
- Instead, it **stopped safely**, responding with `Undecidable.`

---

## 🧠 Why This Matters

This experiment shows that:

- GPT-4o, under the Formalizer framework, **does not cheat**.
- It cannot apply mathematical facts that are **not formally introduced**.
- This confirms that Formalizer effectively enforces **axiomatic discipline**.

---

## 🧩 Future Direction

To solve this type of problem:

- Add **Burnside’s Lemma** as a new axiom (e.g., `CMB8`)
- Retest using a revised combinatorics layer including symmetry/group theory tools

---

## 🧾 Log Author

This experiment was conducted by **Harim Yoo** using the FormalizerInsideLLM system (2025).
