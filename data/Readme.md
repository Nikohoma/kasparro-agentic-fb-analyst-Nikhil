# Kasparro-agentic-fb-analyst-Nikhil
a multi-agent system that autonomously diagnoses Facebook Ads performance, identifies reasons behind ROAS fluctuation, and recommends new creative directions using both quantitative signals and creative messaging data.


# Marketing Intelligence Agent Suite

A lightweight multi-agent system that analyzes ad-campaign data, generates insights, evaluates performance, and produces creative recommendations automatically.

Outputs include:

insights.json – structured hypotheses, confidence, and evidence

creatives.json – creative recommendations for low-CTR campaigns

report.md – final summarized report for marketers

## Quick Start
1. Create Environment and install dependencies
```
pip install -r requirements.txt

```

2. Run the complete agentic workflow

Input file must be a CSV with columns:

```
python src/orchestrator/run.py "Analyze ROAS drop"

```
3. Output will be saved in 
```
reports/report.md
reports/insights.json

```

## Project Structure
```
kasparro-agentic-ads/
│
├── requirements.txt
│
├── config/
│   └── config.yaml
│
├── src/
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── data_agent.py
│   │   ├── insight_agent.py
│   │   ├── evaluator_agent.py
│   │   └── creative_agent.py
│   │
│   ├── orchestrator/
│   │   └── run.py
│   │
│   └── utils/
│       ├── io_utils.py
│       ├── math_utils.py
│       └── logger.py
│
├── prompts/
│   ├── planner_prompt.md
│   ├── insight_prompt.md
│   ├── evaluator_prompt.md
│   ├── creative_prompt.md
│   └── system_prompt.md
│
├── data/
│   ├── sample_facebook_ads.csv   ← Synthetic example dataset
│   └── README.md
│
├── logs/
│   └── run_*.json
│
├── reports/
│   ├── report.md
│   ├── insights.json
│   └── creatives.json
│
├── tests/
│   ├── test_evaluator.py
│   └── test_data_agent.py
│
├── Makefile
│
└── run.sh
```

## System Overview

The system uses following lightweight agents:

System Architecture: 

1. Planner Agent

Breaks down user request into structured subtasks.
Output format: JSON with tasks + dependencies.

2. Data Agent

Loads dataset, cleans fields, computes summaries:

Spend, CTR, ROAS, Impressions, Revenue

Campaign-level aggregates

Detection of missing or anomalous data

Produces a clean numeric summary used by other agents.

3. Insight Agent

Generates qualitative hypotheses such as:

“Drop in ROAS correlated with fall in CTR”

“Audience fatigue detected due to rising frequency”

“Creative type X underperforming after date Y”

Uses structured reasoning: Think → Analyze → Conclude.

4. Evaluator Agent

Validates hypotheses using quantitative checks:

% changes

Threshold comparisons (from config.yaml)

Trend analysis

Produces confidence scores + statistical evidence.

5. Creative Generator Agent

Finds low-CTR campaigns and generates:

Better headlines

New angles

CTA variations

Messaging inspired by existing creative text

## Data Flow

```
User Request
     ↓
Planner Agent
     ↓ (tasks)
Data Agent → Summary
     ↓
Insight Agent → Hypotheses
     ↓
Evaluator Agent → Validated insights (scores + evidence)
     ↓
Creative Agent → Improved creative directions
     ↓
Final Report

```

## Example Outputs
insights.json

```
{
    'insights': [{'issue': 'Low CTR Campaigns',
   'hypothesis': 'Some campaigns show very low CTR, likely creative or audience mismatch.',
   'evidence': {'low_ctr_campaigns': [' OMEN COTTON CLASSICS',
     '-omen-Studio Sports',
     'M-n Bold Colors Drop',
     'MEN  Signture  Soft',
     'MEN B LD COLORS DROP',
     'MEN BOL COLORS DROP',
     'MEN BOLD  OLORS DROP',
     'MEN BOLD COL RS DROP',
     'MEN BOLD COLORS DROP',
     'MEN COMFORTMA LAUNCH',
     'MEN PREMIUM MOD-L',
     'MEN Sinature Soft',
     'Me   Premium  Modal',
     'Men  Bold  Colors  Drop',
     'Men  Bold  Coors  Drop',
     'Men -old Colors Drop',
     'Men B-ld Colors Drop',
     'Men Bol Colors Drop',
     'Men Bold -olors Drop',
     'Men Bold Col-rs Drop',
     'Men Bold Colors Dr p',
     'Men Bold Colors Drop',
     'Men BoldColors Drop',
     'Men Prem um Modal',
     'Men Premium -odal',
     'Men Premium M-dal',
     'Men remium Modal',
     'Men- Premium  Modal',
     'Men-Premium Modal',
     'Men_Bold_Colors_Drop',
     'W MEN Cotton Classics',
     'W men Summer Invisible',
     'WMEN Seamless Everyday',
     'WOEN  Cotton  Classics',
     'WOEN FIT & LIFT',
     'WOMEN  -eamless  Everyday',
     'WOMEN  Seamles   Everyday',
     'WOMEN  Seamless  Everyday',
     'WOMEN COTTON CLASSIS',
     'WOMEN Cot-on Classics',
     'WOMEN SEAM ESS EVERYDAY',
     'WOMEN SEAMLESS EV RYDAY',
     'WOMEN SEAMLESS EVE YDAY',
     'WOMEN SEAMLESS EVERYDAY',
     'WOMEN Seamless Eeryday',
     'WOMEN Seamless Everyday',
     'WOMEN Seamless Everydy',
     'WOMEN Semless Everyday',
     'WOMEN eamless Everyday',
     'WOMEN | SUDIO SPORTS',
     'WOMENSeamless Everyday',
     'WOMEN_Cot-on_Classics',
     'WOMEN_Seamless_Ever-day',
     'WOMEN_Seamless_Everyday',
     'WOMN_Cotton_Classics',
     'Wmen | Studio Sports',
     'Women C-tton Classics',
     'Women Co-ton Classics',
     'Women Cottn Classics',
     'Women Cotton lassics',
     'Women Fit  Lift',
     'Women Seamless Everyday',
     'Women Summer In-isible',
     'Women | Stu io Sports',
     'Women | Studio Sp rts',
     'Women | Studio Spo-ts',
     'Women-Studio -ports',
     'Women-Studio S orts',
     'Women-Studio-Sports',
     'WomenCotton Classics',
     'Women_|-Studio_Sports',
     'me bold colors drop',
     'men bld colors drop',
     'men bold colors drop',
     'w men cotton classics',
     'w-men cotton classics',
     'wo-en seamless everyday',
     'women  Summ r  Invisible',
     'women  Summer  Invi ible',
     'women Su mer Invisible',
     'women Summer In-isible',
     'women Summer Invisble',
     'women Summer Invisi-le',
     'women c-tton classics',
     'women cott n classics',
     'women fit & li t',
     'women s amless everyday',
     'women s-mmer invisible',
     'women seam-ess everyday',
     'women seamess everyday',
     'women seamless everday',
     'women seamless everyday',
     'women seamless-everyday',
     'women su-mer invisible',
     'women summe- invisible',
     'women summer in isible',
     'women | studio spo ts',
     'women_Summe _Invisible',
     'women_Summer_Inisible',
     'women_Summer_Invisi-le',
     'womn cotton classics']},
   'confidence': 0.8,
   'recommendation': 'Improve creatives for these campaigns or re-evaluate targeting.'}],
 'total_issues_found': 1
}

```
creatives.json

```
[
  {
    "headline": "Holiday Deals That Warm Up Your Winter",
    "body": "Stock up on cozy essentials and save big before the season ends. Comfort meets style at the perfect price.",
    "cta": "Shop Winter Deals",
    "angle": "value",
    "confidence": 0.87
  },
  {
    "headline": "Last Chance to Grab Cozy Holiday Favorites",
    "body": "Our best-selling winter pieces are almost gone. Don’t miss out on limited-time holiday savings.",
    "cta": "Claim Your Offer",
    "angle": "urgency",
    "confidence": 0.84
  },
  {
    "headline": "See Why Thousands Love Our Winter Essentials",
    "body": "Shoppers rave about the comfort and quality of our holiday collection. Discover the pieces everyone is talking about.",
    "cta": "Shop Best Sellers",
    "angle": "social proof",
    "confidence": 0.89
  },
  {
    "headline": "Premium Winter Styles Made for Everyday Comfort",
    "body": "Experience warm, durable essentials crafted for all-day wear. Elevate your winter wardrobe effortlessly.",
    "cta": "Explore the Collection",
    "angle": "quality",
    "confidence": 0.86
  },
  {
    "headline": "Holiday Exclusives You’ll Regret Missing",
    "body": "Cozy, stylish, limited. Get early access to winter favorites before they disappear for good.",
    "cta": "Get Early Access",
    "angle": "FOMO",
    "confidence": 0.88
  }
]


```

  





