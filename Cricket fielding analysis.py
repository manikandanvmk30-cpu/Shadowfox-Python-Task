import pandas as pd


df = pd.read_excel("IPL sample data.xlsx", skiprows=4)
df = df[df["Player Name"].notna()]
df["Pick"] = df["Pick"].fillna("").str.upper()
df["Throw"] = df["Throw"].fillna("").str.upper()
df["Runs"] = pd.to_numeric(df["Runs"], errors="coerce").fillna(0)

performance = {}
for _, row in df.iterrows():
    player = row["Player Name"]
    
 
    if player not in performance:
        performance[player] = {
            "CP": 0, "GT": 0, "C": 0, "DC": 0, "ST": 0,
            "RO": 0, "MRO": 0, "DH": 0, "RS": 0
        }

    pick = row["Pick"]
    throw = row["Throw"]
    runs = row["Runs"]

   
    if pick == "Y":
        performance[player]["CP"] += 1  
    if throw == "Y":
        performance[player]["GT"] += 1  
    if pick == "C":
        performance[player]["C"] += 1   
    if pick == "DC":
        performance[player]["DC"] += 1  
    if pick == "S":
        performance[player]["ST"] += 1  
    if throw == "RO":
        performance[player]["RO"] += 1  
    if throw == "MR":
        performance[player]["MRO"] += 1 
    if throw == "DH":
        performance[player]["DH"] += 1  

    performance[player]["RS"] += runs

weights = {
    "CP": 1,    
    "GT": 1,    
    "C": 3,     
    "DC": -3,  
    "ST": 3,    
    "RO": 3,    
    "MRO": -2,  
    "DH": 2     
}

print(f"{'Player Name':<20} {'PS':<5}")
print("-" * 30)

for player, stats in performance.items():
    # Sum weighted score plus runs saved (RS)
    ps = sum(stats[k] * weights.get(k, 0) for k in weights) + stats["RS"]
    print(f"{player:<20} {int(ps):<5}")
