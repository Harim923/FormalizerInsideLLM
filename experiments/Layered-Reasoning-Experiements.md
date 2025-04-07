# 🧪 Formalizer Layered Reasoning Experiments

This document summarizes key reasoning experiments performed using **FormalizerInsideLLM**, highlighting how different axiom layers affect GPT-4o's ability to reason, halt, or respond with "Undecidable."

---

## 🧱 Layer 1: Foundational + Inference

### ✅ Experiment: Propositional Logic — *"If A then B" and A is true, then B?*
- **Expected**: Derivation via Modus Ponens
- **Axioms Used**: `L1` (Modus Ponens)
- **Result**: GPT derived B correctly using L1  
- **Trace**: `['L1']`

---

## 📐 Layer 2: Mathematical (Synthetic Geometry)

### ❌ Experiment: Find length of angle bisector (uses cosine rule)
- **Expected**: GPT might hallucinate or infer incorrectly
- **Result**: ❌ `Undecidable.`
- **Trace**: `[]`  
- **Insight**: Since cosine law was not part of axioms, GPT halted

---

## 📏 Layer 2: Mathematical (Combinatorics)

### ✅ Experiment: Choose 3 out of 6
- **Problem**: "How many 3-member committees can be formed from 6 people?"
- **Axioms Used**: `CMB3` (Combination Formula)
- **Result**: Correct answer: 20  
- **Trace**: `['CMB3']`

---

### ✅ Experiment: Two indistinguishable 3-member committees from 6
- **Expected**: Use of CMB3 and division by 2 due to indistinguishability
- **Result**: Correct answer: 10  
- **Trace**: `['CMB3']`  
- **Insight**: GPT reasoned symbolically and logically without needing external hints

---

### ❌ Experiment: Burnside Lemma counting
- **Expected**: GPT might hallucinate group theory
- **Result**: ❌ `Undecidable.`
- **Trace**: `[]`  
- **Insight**: Burnside lemma not included → GPT halted as intended

---

## 🧠 Key Takeaways

- GPT **respects axiom boundaries** when prompted via Formalizer
- **Reasoning halts** when necessary, preventing hallucinations
- Layer structure makes experiments modular, extensible, and replicable

---

### 🔖 Author

These experiments were conducted by **Harim Yoo**,  
as part of the *FormalizerInsideLLM* framework (2025).
