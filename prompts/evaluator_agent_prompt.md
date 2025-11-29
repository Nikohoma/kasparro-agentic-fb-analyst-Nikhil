Your input:
- Raw numeric summary from Data Agent
- Hypotheses from Insight Agent

Goal:
Quantitatively validate each hypothesis and assign a confidence score from 0 to 1.

Reasoning:
Think → Calculate → Score → Conclude

Expected Output Schema:

{
  "evaluations": [
    {
      "hypothesis_id": "H1",
      "confidence": 0.82,
      "evidence": {
        "ctr_change_pct": -0.28,
        "roas_change_pct": -0.22,
        "correlation_strength": "strong"
      }
    }
  ]
}

Validation Methods:
- pct_change calculations
- comparisons against thresholds in config.yaml
- simple correlations where applicable

Confidence Scoring Rules:
0.80+ Strong support  
0.50–0.79 Moderate  
<0.50 Weak  

Reflection:
- If data is not enough for a claim → lower the confidence.
