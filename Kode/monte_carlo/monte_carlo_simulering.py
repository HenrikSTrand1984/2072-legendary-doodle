import numpy as np
import matplotlib.pyplot as plt

# Parametere (kan erstattes med input fra fil senere)
kostnad_base = 10_000_000  # Basiskostnad i kroner
kostnad_usikkerhet = 0.10  # +/- 10 % usikkerhet

simuleringer = 10000

# Simulering
kostnader = kostnad_base * (1 + np.random.uniform(-kostnad_usikkerhet, kostnad_usikkerhet, simuleringer))

# Resultater
print(f"Gjennomsnittlig kostnad: {kostnader.mean():,.0f} NOK")
print(f"5-persentil: {np.percentile(kostnader, 5):,.0f} NOK")
print(f"95-persentil: {np.percentile(kostnader, 95):,.0f} NOK")

# Plot
plt.hist(kostnader, bins=50, edgecolor='black')
plt.title('Monte Carlo simulering – Prosjektkostnad')
plt.xlabel('Kostnad (NOK)')
plt.ylabel('Frekvens')
plt.grid(True)
plt.show()
