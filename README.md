# FormalizerInsideLLM

**Axiomatic Reasoning with LLMs**  
*A framework where GPT thinks, stops, and proves—within axioms.*

---

📄 [Download the Whitepaper (PDF)](./paper/FormalizerinsideLLM__whitepaper.pdf)

---

## 🧠 What is FormalizerInsideLLM?

**FormalizerInsideLLM** is not a symbolic theorem prover.  
It is a **reasoning agent** that lives inside a world of axioms.

Originally developed as **ProofGPT**, the project was renamed to reflect its deeper identity:
> a **formal logic engine embedded within a large language model**,  
> capable of disciplined, axiom-bound reasoning—not just probabilistic generation.

> **No tricks. No prior knowledge. Just axioms.**

---

## 🔧 How It Works

FormalizerInsideLLM takes in:

- A set of axioms (from [Axiom Atlas](https://github.com/Harim923/Axiom-Atlas))
- A target problem (e.g., a geometry conjecture)
- A recursive reasoning prompt with clear logical constraints

And returns:

- ✅ A structured proof with explicit axiom references  
- ❌ Or: `"The proof is undecidable with the current axioms."`

---

## ✨ Why It Matters

Most LLMs hallucinate.  
**FormalizerInsideLLM doesn’t—because it is bound.**

It cannot invent facts. It can only reason from what it's given.  
This is not about solving problems quickly.  
This is about showing that LLMs **can think**—if we let them operate under discipline.

---

## 📚 Dependencies

- Axiom files from [`Axiom-Atlas`](https://github.com/Harim923/Axiom-Atlas)  
- GPT-4 or another LLM interface (OpenAI API or local model)

---

## 📁 Repository Structure

```plaintext
formalizer-inside-llm/
├── prompts/         # Framework prompt templates
├── experiments/     # Problem-specific logs or runs
├── paper/           # Draft whitepaper files
├── runner.py        # CLI or API interface to run the framework
└── README.md
```

🔄 Example Workflow

```plaintext
# Step 1: Load axioms
axioms = load_axioms("hilbert.json")  # from Axiom Atlas

# Step 2: Define your problem
problem = "Prove that in triangle ABC, at least one of AML, BKM, CLK has area ≤ 1/4 area(ABC)"

# Step 3: Run Formalizer
response = formalizer(reasoning_framework, axioms, problem)

# Step 4: Output result
print(response)
```

👤 Creator

FormalizerInsideLLM was created by Harim Yoo in April 2025.
Harim is a graduate student in mathematics at Texas A&M University (Distance M.S. Program).

This project was originally introduced as ProofGPT,
but rebranded to better express its identity as a formal reasoning engine
embedded inside a large language model.

If you build upon this work, please acknowledge the original author.

> 📝 This framework was originally introduced as **ProofGPT**.  
> The name has since been updated to **FormalizerInsideLLM** to better reflect its function:  
> an axiomatic reasoning engine embedded within large language models.  
> Some original files and notes are preserved for reference.


📜 License

This project is licensed under the MIT License.
Use it, remix it, publish with it—but give credit. 
