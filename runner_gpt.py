# runner_gpt.py (FormalizerInsideLLM)
# ----------------------------------------------------------
# This module provides a symbolic reasoner using OpenAI's GPT API.
# Axioms and rules are loaded recursively from structured JSON files.
# Make sure to manage your API key securely.
# ----------------------------------------------------------

import os
import json
from formalizer.loader.axiom_loader import load_axiom_file

class Reasoner:
    def __init__(self, root_axiom_path):
        self.root_data = load_axiom_file(root_axiom_path)
        self.axioms = []
        self.rules = []
        self.flatten_axioms_and_rules(self.root_data)

    def flatten_axioms_and_rules(self, data):
        if data is None:
            return
        layer = data.get("layer")
        content = data.get("axioms_or_rules", [])

        if layer == "inference":
            self.rules.extend(content)
        else:
            self.axioms.extend(content)

        for dep in data.get("dependencies", []):
            self.flatten_axioms_and_rules(dep)

    def show_stats(self):
        print("\n=== Formalizer Reasoner Summary ===")
        print(f"📚 Total Axioms Loaded: {len(self.axioms)}")
        print(f"⚙️ Total Inference Rules Loaded: {len(self.rules)}")
        print("===================================\n")

    def list_axioms(self):
        for ax in self.axioms:
            print(f"- {ax.get('id', '?')}: {ax.get('name', '')}")

    def list_rules(self):
        for rule in self.rules:
            print(f"- {rule.get('id', '?')}: {rule.get('name', '')}")

    import re

    def extract_axiom_trace(self, response_text):
        trace_ids = set()
        matches = re.findall(r'\b([A-Z]{2,3}\d{1,3})\b', response_text)
        trace_ids.update(matches)

        lower_text = response_text.lower()
        for ax in self.axioms + self.rules:
            ax_id = ax.get("id")
            ax_name = ax.get("name", "").lower().replace("-", " ").strip()
            if ax_name and ax_name in lower_text:
                trace_ids.add(ax_id)

        return sorted(trace_ids)

    def ask_gpt_to_prove(self, statement):
        try:
            from openai import OpenAI

            client = OpenAI(api_key="<your_openai_api_key>")
            system_prompt = (
                "You are a formal proof assistant named Formalizer.\n"
                "Follow these 4 core principles:\n"
                "1. All proofs must originate from the provided axioms only.\n"
                "2. No theorem may update the axiom set.\n"
                "3. Any theorem used must be recursively reducible to axioms.\n"
                "4. Reasoning must be strictly formal and proof-driven.\n"
                "\n"
                "Do not use any external knowledge not explicitly listed in the axioms or rules.\n"
                "If a statement cannot be derived from the axioms, respond with:\n"
                "\"Undecidable.\"\n"
            )

            all_axioms = "\n".join([f"{a.get('id', '?')}: {a.get('statement', '')}" for a in self.axioms])
            all_rules = "\n".join([f"{r.get('id', '?')}: {r.get('statement', '')}" for r in self.rules])
            user_prompt = (
                f"Axioms:\n{all_axioms}\n\n"
                f"Inference Rules:\n{all_rules}\n\n"
                f"Prove the following statement using only the above:\n"
                f"\"\"\"{statement}\"\"\"\n"
                f"If not provable, respond with \"Undecidable.\""
            )

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0
            )

            answer = response.choices[0].message.content
            print("\n🧠 GPT-4o Response:\n", answer)

            axiom_trace = self.extract_axiom_trace(answer)
            print("📚 Axioms Used:", axiom_trace)

            return {
                "response": answer,
                "axiom_trace": axiom_trace
            }

        except Exception as e:
            print(f"❌ Error in GPT call: {e}")
            return None
