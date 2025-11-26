import pandas as pd

# Load the three Excel files
erp_df = pd.read_excel('ERP_Equipes Airplus.xlsx')
mes_df = pd.read_excel('MES_Extraction.xlsx')
plm_df = pd.read_excel('PLM_DataSet.xlsx')

# Drop unnecessary columns from ERP dataset
erp_df = erp_df.drop(columns=["Âge", "Description du poste", "Niveau d'expérience", "Commentaire de Carrière"])

# Drop unnecessary columns from MES dataset
mes_df = mes_df.drop(columns=["Aléas Industriels", "Nombre pièces", "Cause Potentielle"])

# Drop unnecessary columns from PLM dataset
plm_df = plm_df.drop(columns=["Criticité", "Masse (kg)", "Fournisseur"])

# Display basic information about each dataset
print("=" * 50)
print("ERP_Equipes Airplus Dataset")
print("=" * 50)
print(f"Shape: {erp_df.shape}")
print(f"Columns: {list(erp_df.columns)}")
print("\nFirst few rows:")
print(erp_df.head())

print("\n" + "=" * 50)
print("MES_Extraction Dataset")
print("=" * 50)
print(f"Shape: {mes_df.shape}")
print(f"Columns: {list(mes_df.columns)}")
print("\nFirst few rows:")
print(mes_df.head())

print("\n" + "=" * 50)
print("PLM_DataSet")
print("=" * 50)
print(f"Shape: {plm_df.shape}")
print(f"Columns: {list(plm_df.columns)}")
print("\nFirst few rows:")
print(plm_df.head())

# Export cleaned dataframes to CSV files
erp_df.to_csv('ERP_cleaned.csv', index=False, encoding='utf-8-sig')
mes_df.to_csv('MES_cleaned.csv', index=False, encoding='utf-8-sig')
plm_df.to_csv('PLM_cleaned.csv', index=False, encoding='utf-8-sig')

print("\n" + "=" * 50)
print("CSV files created successfully!")
print("=" * 50)
print("- ERP_cleaned.csv")
print("- MES_cleaned.csv")
print("- PLM_cleaned.csv")
