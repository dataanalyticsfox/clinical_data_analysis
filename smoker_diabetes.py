import pandas as pd
from scipy import stats
import plotly.express as px

# open csv and create df
patient_history_df = pd.read_csv('/Users/carrieminerich/Desktop/verana/patient_history.csv')

# lowercase column headers for easeier analysis
patient_history_df.columns = patient_history_df.columns.str.lower()

# contingency table of # of cigs vs diabetes = 1
matrix = pd.crosstab(patient_history_df['cigsperday'], patient_history_df['diabetes'])
print(f"Matrix:{matrix}")

# chi-square test
chi2, p, _, _ = stats.chi2_contingency(matrix)

print(f"Chi-Square test for cigs per day and diabetes: {chi2}")
print(f"P-Value for cigs per day and diabetes: {p}")

# print results
if p < 0.05:
    print("The result is statistically significant. There is an association between the number of cigarettes smoked per day and the prevalence of diabetes.")
else:
    print("The result is not statistically significant. There is no strong evidence of an association between the number of cigarettes smoked per day and the prevalence of diabetes.")


# visualize results
fig = px.histogram(patient_history_df, x='cigsperday', color='diabetes', barmode='group',
                   title='Number of Cigarettes Smoked per Day vs. Prevalence of Diabetes',
                   labels={'cigsperday': 'Number of Cigarettes Smoked per Day', 'count': 'Count'},
                   category_orders={'diabetes': [0, 1]})

fig.update_layout(xaxis_title='Number of Cigarettes Smoked per Day',
                  yaxis_title='Total individual count in patient_history.csv',
                  legend_title='Diabetes: 1; No Diabetes:2')

fig.show()