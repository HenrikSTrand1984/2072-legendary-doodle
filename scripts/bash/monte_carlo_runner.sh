#!/bin/bash
# -------------------------------------------
# Formål: Kjør Monte Carlo-simulering i Python
# Bruk: ./monte_carlo_runner.sh
# Forutsetning: Python 3 og nødvendige moduler installert
# -------------------------------------------

echo "Starter Monte Carlo-simulering..."

# Sett riktig sti hvis nødvendig
PYTHON_SCRIPT="kode/monte_carlo/monte_carlo_simulering.py"

# Sjekk om scriptet finnes
if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "FEIL: Fant ikke $PYTHON_SCRIPT"
  exit 1
fi

# Kjør Python-skriptet
python3 "$PYTHON_SCRIPT"

# Ferdig
echo "Simulering fullført."
