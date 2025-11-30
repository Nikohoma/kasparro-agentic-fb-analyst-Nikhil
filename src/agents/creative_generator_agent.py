
import json
import google.generativeai as genai


class CreativeGenerator:
    def __init__(self, api: str, model: str = "gemini-2.5-flash"):
        genai.configure(api_key=api)
        self.model_name = model
        self.model = genai.GenerativeModel(model)

    def _build_prompt(self, campaign):

        CREATIVE_PROMPT = f"""
You are a senior Creative Strategist for Facebook Ads.

Generate **5 new creative variations** to improve CTR.
Use the tone, style, and themes inspired by the existing creative messages.

## Campaign Info
- Campaign: {campaign}


## Output Format (JSON):
[
  {{
    "headline": "...",
    "body": "...",
    "cta": "...",
    "angle": "...",
    "confidence": 0.0
  }}
]

Guidelines:
- Headline: 6–12 words, catchy, scroll-stopping.
- Body: 1–2 sentences max.
- CTA: strong and clear.
- Angle: each variation must use a DIFFERENT angle (value, urgency, social proof, quality, FOMO).
- Make the versions meaningfully different.
"""

        return CREATIVE_PROMPT

    def plan(self, campaign):
        prompt = self._build_prompt(campaign)
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.9,
                "response_mime_type": "application/json",
            }
        )

        return json.loads(response.text)



cg = CreativeGenerator("your-gemini-api-key")

creatives = cg.plan("Holiday Sale")
print(creatives)



