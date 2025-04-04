# ProofGPT

**Axiomatic Reasoning with LLMs**  
*A framework where GPT thinks, stops, and proves—within axioms.*

---

📄 [Download the ProofGPT Whitepaper (PDF)](./paper/ProofGPT__whitepaper.pdf)

---

## 🧠 What is ProofGPT?

ProofGPT is not a theorem prover.  
It is a **reasoning agent** that lives inside a world of axioms.  
Unlike symbolic engines, it doesn't rely on external proof systems—  
It reasons **from the inside**, with nothing but logical rules you give it.

> **No tricks. No prior knowledge. Just axioms.**

---

## 🔧 How It Works

ProofGPT takes in:

- A set of axioms (from [Axiom Atlas](https://github.com/Harim923/Axiom-Atlas))
- A target problem (e.g., a geometry conjecture)
- A recursive reasoning prompt with clear logical constraints

And it returns:

- A structured proof with explicit axiom IDs
- Or declares:  
  `"The proof is undecidable with the current axioms."`

---

## ✨ Why It Matters

Most LLMs hallucinate.  
**ProofGPT doesn’t—because it is bound.**  
It cannot invent facts. It can only reason from the framework.

> This is not about solving.  
> This is about showing that LLMs **can think** if we let them do so **under discipline**.

---

## 📚 Dependencies

- Axiom files from [`Axiom-Atlas`](https://github.com/Harim923/Axiom-Atlas)
- OpenAI / GPT-4 or other LLM interface (can be local)

---

## 📁 Repository Structure

```plaintext
proofgpt/
├── prompts/ # Framework prompt templates
├── experiments/ # Problem-specific JSON or markdown logs
├── paper/ # Draft paper files
├── runner.py # CLI or API interface to run proofs
└── README.md
```

## 🔄 Example Workflow

```bash
# Step 1: Load axioms
axioms = load_axioms("hilbert.json")  # from Axiom Atlas

# Step 2: Define your problem
problem = "Prove that in triangle ABC, at least one of AML, BKM, CLK has area ≤ 1/4 area(ABC)"

# Step 3: Run ProofGPT
response = proofgpt(reasoning_framework, axioms, problem)

# Step 4: Output result
print(response)
```


---

## 👤 Creator

**ProofGPT** was designed and developed by Harim Yoo, April 2025.  
This project is open-source and intended to inspire new directions in AI reasoning research.

If you build upon this project, please acknowledge the original author.

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute, but give credit where it's due. 🙌


