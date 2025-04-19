import pandas as pd

# Percorso del file TSV originale
input_tsv = '/Users/gabrieleadorni/Downloads/openfoodfacts_db.tsv'

# Percorso del file CSV da creare
output_csv = '/Users/gabrieleadorni/Downloads/openfoodfacts_db.csv'

# Carica il file TSV
df = pd.read_csv(input_tsv, sep='\t')

# Salva come file CSV
df.to_csv(output_csv, sep=',', index=False)

print(f"Conversione completata: {output_csv}")
