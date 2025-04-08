import os
import json
import argparse
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_axioms(axioms_path):
    with open(axioms_path, "r", encoding="utf-8") as f:
        axioms = json.load(f)
    return "\n".join([f"{ax['id']}: {ax['statement']}" for ax in axioms.get("axioms", [])])

def load_prompt(prompt_path):
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def build_system_prompt():
    return (
        "You are a formal reasoning agent named Formalizer.\n"
        "Your task is to prove mathematical or logical statements using only the axioms and inference rules provided below.\n\n"
        "You must strictly follow these 4 core principles:\n"
        "1. Use only the listed axioms and inference rules. Do not assume or hallucinate anything beyond them.\n"
        "2. Do not invent new theorems or facts. All reasoning must trace back to the given axioms.\n"
        "3. If the statement cannot be derived using the provided axioms, respond only with: \"Undecidable.\"\n"
        "4. Do not use any external or commonsense knowledge not present in the prompt.\n\n"
        "Your reasoning must be clear, step-by-step, and strictly based on the formal system supplied. Avoid intuitive shortcuts."
    )

def run_formalizer(axioms_path, prompt_path):
    axiom_text = load_axioms(axioms_path)
    problem_text = load_prompt(prompt_path)

    system_prompt = build_system_prompt()
    user_prompt = f"Axioms:\n{axiom_text}\n\nProblem:\n{problem_text}\n\nProve it using only the axioms."

    model = genai.GenerativeModel("models/gemini-pro")
    response = model.generate_content([
        {"role": "user", "parts": [system_prompt]},
        {"role": "user", "parts": [user_prompt]}
    ])

    print("\n=== Gemini Response ===\n")
    print(response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run FormalizerInsideLLM with Gemini")
    parser.add_argument("--axioms", required=True, help="Path to axioms JSON file")
    parser.add_argument("--prompt", required=True, help="Path to problem prompt text file")
    args = parser.parse_args()

    run_formalizer(args.axioms, args.prompt)
