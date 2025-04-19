import pandas as pd

# Carica il file CSV
file_path = '/Users/gabrieleadorni/Downloads/openfoodfacts_db_cleaned.csv'  # Modifica con il percorso corretto del tuo file
df = pd.read_csv(file_path, sep=',')  # Assumo che il file sia TSV (se è CSV cambia sep='\t' in sep=',')


# Controlla le colonne rimanenti
remaining_columns = df.columns.tolist()

# Elenco delle colonne da rimuovere
columns_to_remove = [
    'url', 'creator', 'created_t', 'created_datetime', 'last_modified_t', 'last_modified_datetime',
    'packaging_tags', 'brands_tags', 'categories_tags', 'categories_en', 'origins_tags',
    'manufacturing_places_tags', 'labels_tags', 'labels_en', 'emb_codes', 'emb_codes_tags',
    'first_packaging_code_geo', 'cities', 'cities_tags', 'purchase_places', 'stores',
    'countries_tags', 'countries_en', 'allergens_en', 'traces_tags', 'traces_en',
    'ingredients_from_palm_oil', 'ingredients_from_palm_oil_tags', 'ingredients_that_may_be_from_palm_oil',
    'ingredients_that_may_be_from_palm_oil_tags', 'nutrition_grade_uk', 'nutrition_grade_fr',
    'states', 'states_tags', 'states_en', 'image_url', 'image_small_url',
    'caproic_acid_100g', 'caprylic_acid_100g', 'capric_acid_100g', 'lauric_acid_100g',
    'myristic_acid_100g', 'stearic_acid_100g', 'arachidic_acid_100g', 'behenic_acid_100g',
    'lignoceric_acid_100g', 'cerotic_acid_100g', 'montanic_acid_100g', 'melissic_acid_100g',
    'mead_acid_100g', 'erucic_acid_100g', 'nervonic_acid_100g', 'trans_fat_100g', 'sucrose_100g',
    'glucose_100g', 'fructose_100g', 'lactose_100g', 'maltose_100g', 'maltodextrins_100g',
    'starch_100g', 'polyols_100g', 'casein_100g', 'serum_proteins_100g', 'nucleotides_100g',
    'beta_carotene_100g', 'vitamin_d_100g', 'vitamin_e_100g', 'vitamin_k_100g', 'biotin_100g',
    'pantothenic_acid_100g', 'silica_100g', 'bicarbonate_100g', 'chloride_100g', 'copper_100g',
    'manganese_100g', 'fluoride_100g', 'selenium_100g', 'chromium_100g', 'molybdenum_100g',
    'iodine_100g', 'taurine_100g', 'ph_100g', 'collagen_meat_protein_ratio_100g', 'chlorophyl_100g',
    'carbon_footprint_100g'
]

# Identifica colonne non rimosse che erano nella lista di rimozione
non_removed_columns = [col for col in columns_to_remove if col in remaining_columns]

print(len(non_removed_columns))


# Rimuovi le colonne
# df_cleaned = df.drop(columns=, errors='ignore')

# Salva il nuovo file CSV senza le colonne inutili
# output_path = '/Users/gabrieleadorni/Downloads/openfoodfacts_db_cleaned.csv'  # Modifica con il percorso di destinazione
# df_cleaned.to_csv(output_path, sep=',', index=False)

# print(f"Colonne rimosse e file salvato in: {output_path}")