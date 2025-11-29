import pandas as pd
from typing import Dict, List


class InsightAgent:

    def __init__(self, summary: dict):
        """
        summary = output of DataAgent.get_summary()
        (overall stats + campaign-level stats)
        """
        self.summary = summary

    def analyze(self) -> dict:
        insights = []

        # --- 1. ROAS Drop Detection ---
        avg_roas = self.summary["overall"]["average_roas"]
        if avg_roas < 5:  # Simple threshold
            insights.append({
                "issue": "Low ROAS",
                "hypothesis": "Overall ROAS is below expected benchmark.",
                "evidence": {
                    "average_roas": avg_roas
                },
                "confidence": 0.7,
                "recommendation": "Check creative performance & audience targeting."
            })

        # --- 2. CTR Decline Detection ---
        avg_ctr = self.summary["overall"]["average_ctr"]
        if avg_ctr < 0.01:
            insights.append({
                "issue": "Low CTR",
                "hypothesis": "Ads are not engaging enough; possible creative fatigue or poor messaging.",
                "evidence": {
                    "average_ctr": avg_ctr
                },
                "confidence": 0.75,
                "recommendation": "Try refreshing creatives or testing new messaging."
            })

        # --- 3. Identify Underperforming Campaigns (Low CTR) ---
        low_ctr_campaigns = self.summary.get("low_ctr_campaigns", [])

        if low_ctr_campaigns:
            insights.append({
                "issue": "Low CTR Campaigns",
                "hypothesis": "Some campaigns show very low CTR, likely creative or audience mismatch.",
                "evidence": {
                    "low_ctr_campaigns": low_ctr_campaigns
                },
                "confidence": 0.8,
                "recommendation": "Improve creatives for these campaigns or re-evaluate targeting."
            })

        return {
            "insights": insights,
            "total_issues_found": len(insights)
        }

ia = InsightAgent(da.get_summary())
ia.analyze()