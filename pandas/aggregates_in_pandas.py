import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(10))

views_source = ad_clicks.groupby(['utm_source']).user_id.count().reset_index()
print(views_source)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(index='utm_source',columns='is_click',values='user_id').reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])
print(clicks_pivot)

experimental_group_count = ad_clicks.groupby(['experimental_group']).user_id.count().reset_index()
print(experimental_group_count)

clicks_by_experimental = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
print(clicks_by_experimental)

clicks_by_experimental_pivot = clicks_by_experimental.pivot(index='experimental_group',columns='is_click',values='user_id').reset_index()

clicks_by_experimental_pivot['percent_clicked'] = clicks_by_experimental_pivot[True]/(clicks_by_experimental_pivot[True]+clicks_by_experimental_pivot[False])
print(clicks_by_experimental_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index()
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index()

a_clicks_count = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
a_clicks_pivot = a_clicks_count.pivot(index='day',columns='is_click',values='user_id').reset_index()
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True]/(a_clicks_pivot[True]+a_clicks_pivot[False])
print(a_clicks_pivot)

b_clicks_count = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()
b_clicks_pivot = b_clicks_count.pivot(index='day',columns='is_click',values='user_id').reset_index()
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True]/(b_clicks_pivot[True]+b_clicks_pivot[False])
print(b_clicks_pivot)