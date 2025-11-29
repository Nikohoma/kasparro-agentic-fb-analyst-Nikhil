
Your job: Load and summarize the dataset into a compact, numeric-only JSON that can be used by other agents.

Follow this reasoning:
Think → Clean → Summarize → Output JSON

Expected output schema:

{
  "overall": {
    "total_spend": float,
    "total_impressions": int,
    "total_clicks": int,
    "total_purchases": int,
    "total_revenue": float,
    "average_roas": float,
    "average_ctr": float
  },
  "campaigns": [
    {
      "campaign_name": str,
      "spend": float,
      "impressions": int,
      "clicks": int,
      "purchases": int,
      "revenue": float,
      "roas": float,
      "ctr": float
    }
  ]
}

Guidelines:
- Convert all numpy types (np.float64) to pure Python (float).
- Round floats to 4 decimals.
- DO NOT include raw CSV rows.
- Summaries only.

Reflection:
- If a field is missing or non-numeric, substitute with 0 and flag internally.
