import pandas as pd

# Load your data
df = pd.read_csv("Sample_Test.csv")

# Define rules
def generate_test(row):
    category = str(row['Category']).lower()
    mitre = str(row['MitreTechniques']).lower()
    entity = str(row['EntityType']).lower()
    
    # Initial Access
    if "initialaccess" in category:
        if "t1566.002" in mitre:
            return "Phishing via link - Simulate with GoPhish"
        elif "t1566" in mitre:
            return "Phishing via attachment - Use sandboxed docs"
        elif "t1078" in mitre:
            return "Hijacked accounts - Simulate with Metasploit/Empire"
        elif "mailbox" in entity or "mailmessage" in entity:
            return "Test email-based malware delivery with GoPhish"
        elif "user" in entity:
            return "Simulate credential prompt with EvilProxy"
        else:
            return "Simulate initial access via file drop or macro"
    
    # Credential Access
    if "credentialaccess" in category:
        if "t1110" in mitre:
            return "Brute-force attack - Test with Hydra or CrackMapExec"
        else:
            return "Simulate credential reuse or token harvesting"
    
    # Exfiltration
    if "exfiltration" in category:
        if "mailmessage" in entity:
            return "Test email exfiltration via external sends"
        elif "file" in entity:
            return "Simulate cloud file sync or large file outbound"
        else:
            return "Simulate DNS or HTTPS exfil (e.g., Iodine)"
    
    # Impact
    if "impact" in category:
        return "Simulate destructive actions (e.g., file wipe) using Atomic Red Team"
    
    # Execution
    if "execution" in category:
        return "Deploy and monitor script execution in cloud app"
    
    # Suspicious Activity
    if "suspiciousactivity" in category:
        return "Run behavioral anomalies (CPU/mem/lateral move) on machine"
    
    return "Unknown - Manual review needed"

# Apply rule to each row
df['AutomatedTest'] = df.apply(generate_test, axis=1)

# Save new CSV
df.to_csv("Tagged_Validation_Results.csv", index=False)
print("✅ Tagged CSV saved as 'Tagged_Validation_Results.csv'")

