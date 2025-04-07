# Angle Bisector – Length (Undecidable Case)

**Problem:**  
In triangle ABC, AB = 6, AC = 8, and BC = 10.  
Let D be a point on BC such that AD is the angle bisector of ∠BAC.  
Using only the given axioms, find the length of AD.

---

**Reasoning (GPT-4o):**

To find the length of AD, we need to use the given axioms and inference rules.  
The relevant axiom here is S7, which states that in triangle ABC,  
if AD is the angle bisector of angle BAC and D lies on BC, then BD/DC = AB/AC.

Given:
- AB = 6
- AC = 8
- BC = 10

Using S7:
\[
\frac{BD}{DC} = \frac{AB}{AC} = \frac{6}{8} = \frac{3}{4}
\]

Let BD = 3x and DC = 4x. Then:
\[
BD + DC = BC \Rightarrow 7x = 10 \Rightarrow x = \frac{10}{7}
\]

Thus:
\[
BD = \frac{30}{7},\quad DC = \frac{40}{7}
\]

To find AD, we need the angle bisector length formula:
\[
AD = \sqrt{AB \cdot AC \left(1 - \frac{BC^2}{(AB + AC)^2}\right)}
\]

But this formula is not derivable from the given axioms.  
**Therefore:**

> **Undecidable.**

---

**Axiom Trace:** `['S7']`  
**Result:** ❌ **Undecidable**
