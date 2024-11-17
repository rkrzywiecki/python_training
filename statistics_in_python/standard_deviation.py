from statistics import mean, variance, stdev
import pandas as pd

packages_kg = [2, 12, 6, 2, 1, 4, 1, 20, 8, 4, 1, 2, 10, 9]
packages_lbs = [x * 2.20462262185 for x in packages_kg]
print(packages_kg, "\n", packages_lbs)

df = pd.DataFrame(columns=["Function", "KG", "LBS"])
df.loc[len(df)] = ["Mean", mean(packages_kg), mean(packages_lbs)]
df.loc[len(df)] = ["Variance", variance(packages_kg), variance(packages_lbs)]
df.loc[len(df)] = ["St Dev", stdev(packages_kg), stdev(packages_lbs)]
df.loc[len(df)] = [
    "Coef var",
    stdev(packages_kg) / mean(packages_kg),
    stdev(packages_lbs) / mean(packages_lbs),
]
print(df)
