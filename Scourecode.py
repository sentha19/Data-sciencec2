print(df.isnull().sum()) #Check the null values count0
df_cleaned = df.dropna() # Removes rows with missing values
print(df)
df["Passesssed"] = encoder.fit_transform(df["Passed"
