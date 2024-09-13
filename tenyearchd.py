import pandas as pd
from scipy import stats

# open csv and set as dataframe
patient_clinical_df = pd.read_csv('/Users/carrieminerich/Desktop/verana/patient_clinical.csv')
patient_demographics_df = pd.read_csv('/Users/carrieminerich/Desktop/verana/patient_demographics.csv')

# make sure column headers are lower case for easier analysis
patient_clinical_df.columns = patient_clinical_df.columns.str.lower()
patient_demographics_df.columns = patient_demographics_df.columns.str.lower()

# merge dfs on patient_id
merged_df = patient_clinical_df.merge(patient_demographics_df, on='patient_id')

# separate merged_df into men and women df
men_df = merged_df[merged_df['male'] ==1]
women_df = merged_df[merged_df['male'] == 0]

# calculate distribution 
distribution_men = men_df['tenyearchd'].value_counts(normalize=True)
distribution_women = women_df['tenyearchd'].value_counts(normalize=True)

print(f"Distribution of TenYearCHD among men:{distribution_men}")
print(f"Distribution of TenYearCHD among women:{distribution_women}")

# matrix is count of occurance for each value male and tenyearchd
matrix = pd.crosstab(merged_df['male'], merged_df['tenyearchd'])
print(matrix)

# chi square measures difference between observed and expected
chi2, p, _, _ = stats.chi2_contingency(matrix)

print(f"\nChi-Square Test Statistic: {chi2}")
print(f"P-Value: {p}")

# print results
if p < 0.05:
    print("\nThe result is statistically significant. There is an association between gender and TenYearCHD.")
else:
    print("\nThe result is not statistically significant. There is no strong evidence of an association between gender and TenYearCHD.")
