import pandas as pd
#
# # Specifica il percorso del tuo file CSV
# file_path = '/Users/gabrieleadorni/Downloads/openfoodfacts_db_cleaned.csv'
#
# # Leggi il CSV
# df = pd.read_csv(file_path)
# c=0
# # Stampa le colonne e i loro tipi di dato
# for column in df.columns:
#     c+=1
#     print(f"Colonna: {column}, Tipo di dato: {df[column].dtype}")
#
# print(c)




# Percorsi del file
input_file = '/Users/gabrieleadorni/Downloads/openfoodfacts_db_def.csv'  # Modifica questo con il tuo percorso
output_file = '/Users/gabrieleadorni/Downloads/openfoodfacts_db_fin.csv'  # Dove vuoi salvare il nuovo file

# Leggi il file CSV con ';' come separatore
df = pd.read_csv(input_file, sep=';')

# Salva il file come CSV con ',' come separatore
df.to_csv(output_file, index=False)

print(f"File convertito e salvato in: {output_file}")
