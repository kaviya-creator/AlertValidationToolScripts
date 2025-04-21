import pandas as pd

# Load the CSV file
df = pd.read_csv('Sample_Train.csv')

# Strip whitespace and convert to lowercase for clean comparison
df['entityType_cleaned'] = df['EntityType'].astype(str).str.strip().str.lower()

# Create the 'validates_alert' column
df['validates_alert'] = df['entityType_cleaned'].apply(
    lambda x: 'True Positive' if x in ['url', 'ip'] else ''
)

# Optional: Save the updated CSV
df.to_csv('Sample_Train_Updated.csv', index=False)

# Show sample rows to verify
print(df[['EntityType', 'entityType_cleaned', 'validates_alert']].head())
    
