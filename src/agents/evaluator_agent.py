class EvaluatorAgent:

    def __init__(self, summary: dict, insights: dict):
        self.summary = summary
        self.insights = insights["insights"]

    def evaluate(self) -> dict:
        evaluations = []
        avg_roas = self.summary["overall"]["average_roas"]
        avg_ctr  = self.summary["overall"]["average_ctr"]
        low_ctr_campaigns = self.summary.get("low_ctr_campaigns", [])

        for insight in self.insights:
            issue = insight["issue"]

            if issue == "Low ROAS":
                evaluation = {
                    "issue": "Low ROAS",
                    "is_valid": avg_roas < 5,
                    "evidence": {
                        "average_roas": avg_roas,
                        "threshold": 5
                    }
                }
                evaluations.append(evaluation)

            elif issue == "Low CTR":
                evaluation = {
                    "issue": "Low CTR",
                    "is_valid": avg_ctr < 0.01,
                    "evidence": {
                        "average_ctr": avg_ctr,
                        "threshold": 0.01
                    }
                }
                evaluations.append(evaluation)

            elif issue == "Low CTR Campaigns":
                evaluation = {
                    "issue": "Low CTR Campaigns",
                    "is_valid": len(low_ctr_campaigns) > 0,
                    "evidence": {
                        "low_ctr_campaigns": low_ctr_campaigns,
                        "count": len(low_ctr_campaigns),
                        "threshold_ctr": 0.01
                    }
                }
                evaluations.append(evaluation)

        return {
            "evaluations": evaluations,
            "issues_validated": sum([1 for e in evaluations if e["is_valid"]])
        }

ea = EvaluatorAgent(da.get_summary(), ia.analyze())
ea.evaluate()