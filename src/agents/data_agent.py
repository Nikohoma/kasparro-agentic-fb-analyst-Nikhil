import pandas as pd
import numpy as np

class DataAgent:
  def __init__(self,data):
    self.data = data



  def clean_data(self):
    self.data.drop_duplicates(inplace=True)
    self.data.fillna(0, inplace=True)
    self.data['date'] = pd.to_datetime(self.data['date'])
    numeric_cols = ['spend', 'impressions', 'clicks', 'ctr', 'purchases', 'revenue', 'roas']
    for col in numeric_cols:
      self.data[col] = pd.to_numeric(self.data[col], errors='coerce').fillna(0)

  def get_summary(self):
    summary = {}

    overall = {
        'total_spend':  np.sum(self.data['spend']),
        'total_impressions':  np.sum(self.data['impressions']),
        'total_clicks':  np.sum(self.data['clicks']),
        'total_purchases':  np.sum(self.data['purchases']),
        'total_revenue':  np.sum(self.data['revenue']),
        'average_roas':  np.mean(self.data['roas']),
        'average_ctr':  np.mean(self.data['ctr'])
    }
    # Campaign-level summaries
    campaign_group = self.data.groupby('campaign_name').agg({
            'spend': 'sum',
            'impressions': 'sum',
            'clicks': 'sum',
            'purchases': 'sum',
            'revenue': 'sum',
            'roas': 'mean',
            'ctr': 'mean'
        }).reset_index()


    campaigns = []
    for _, row in campaign_group.iterrows():
        campaigns.append({k:(v)  for k, v in row.items()})

    #CTR
    low_ctr_threshold = 0.01
    low_ctr_campaigns = [
        row['campaign_name']
        for _, row in campaign_group.iterrows()
        if row['ctr'] < low_ctr_threshold
    ]

    return {
        'overall': overall,
        'campaigns': campaigns,
        'low_ctr_campaigns': low_ctr_campaigns
    }


data = pd.read_csv('/path/to/the/csv')
da = DataAgent(data)
da.clean_data()
print(f'Summary of the data: {da.get_summary()}')
