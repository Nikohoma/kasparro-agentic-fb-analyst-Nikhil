import json
from typing import Dict
import google.generativeai as genai


class PlannerAgent:
    """
    Planner Agent:
    - Reads the user query
    - Breaks into subtasks
    - Assigns tasks to correct agents
    - Returns structured JSON plan
    """

    def __init__(self, api_key: str, model: str = "gemini-2.5-flash"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)

    # ------------------------------------------------------------------
    # MAIN METHOD
    # ------------------------------------------------------------------
    def plan(self, user_query: str) -> Dict:
        """
        Generate a structured task plan for other agents.
        """

        prompt = self._build_prompt(user_query)

        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.2,
                "response_mime_type": "application/json"
            }
        )

        # Gemini returns text JSON → convert to dict
        return json.loads(response.text)

    # ------------------------------------------------------------------
    # PROMPT GENERATION
    # ------------------------------------------------------------------
    def _build_prompt(self, query: str) -> str:
        return f"""{self.SYSTEM_PROMPT}

User query: "{query}"

Generate the complete JSON task plan now.
"""

    # ------------------------------------------------------------------
    # SYSTEM PROMPT
    # ------------------------------------------------------------------
    SYSTEM_PROMPT = """
You are the Planner Agent in a multi-agent marketing analytics system.

Your responsibilities:
1. Understand the user's question.
2. Decompose it into minimal, atomic subtasks.
3. Assign each subtask to the correct agent.
4. Produce ONLY valid JSON following the schema.
5. Ensure tasks are in correct execution order.
6. Do NOT answer the query; only create the plan.
7. Enforce dependency ordering between tasks.

Agents:
- DataAgent → summarize, load, aggregate dataset
- InsightAgent → generate hypotheses (ROAS, CTR, CPC, fatigue)
- EvaluatorAgent → validate hypotheses with metrics
- CreativeAgent → generate new creatives (headlines, captions, CTAs)

JSON Schema:
{
  "tasks": [
    {
      "id": <int>,
      "agent": "<DataAgent | InsightAgent | EvaluatorAgent | CreativeAgent>",
      "action": "<atomic operation>",
      "input": "<depends on previous task>",
      "expected_output": "<what next task receives>"
    }
  ]
}

Rules:
- Never solve the user’s query.
- Only provide the task plan.
- Output MUST be valid JSON.
"""

planner = PlannerAgent(api_key="your-gemini-api-key")
plan_result = planner.plan("What caused the spike in CPA yesterday?")
print(plan_result)
