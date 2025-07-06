import pandas as pd

# Eksempeldata (kan erstattes med input fra fil)
data = [
    {"Risiko": "Manglende underlag", "Sannsynlighet": 4, "Konsekvens": 3},
    {"Risiko": "Leveringsforsinkelser", "Sannsynlighet": 3, "Konsekvens": 4},
    {"Risiko": "Ukjent teknologi", "Sannsynlighet": 2, "Konsekvens": 5},
    {"Risiko": "Høy UE-andel", "Sannsynlighet": 3, "Konsekvens": 3}
]

# Lag DataFrame
df = pd.DataFrame(data)

# Beregn risikopoeng
df["Risikopoeng"] = df["Sannsynlighet"] * df["Konsekvens"]

# Sorter etter risikopoeng
df = df.sort_values(by="Risikopoeng", ascending=False)

# Vis resultat
print("Risikovurdering:")
print(df.to_string(index=False))

# Lagre til fil (valgfritt)
df.to_csv("risikovurdering_resultat.csv", index=False)
print("Risikovurdering lagret til risikovurdering_resultat.csv")
