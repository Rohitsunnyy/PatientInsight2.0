import pandas as pd
import os

def preprocess_data(input_dir='data/raw', output_dir='data/processed'):
    """
    Preprocess the PMC-Patients dataset.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    for file in os.listdir(input_dir):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join(input_dir, file))
            
            # Perform preprocessing steps here
            # For example:
            # 1. Remove duplicates
            df = df.drop_duplicates()
            
            # 2. Handle missing values
            df = df.fillna('Unknown')
            
            # 3. Normalize text fields
            text_columns = ['patient_profile', 'medical_history', 'symptoms', 'diagnosis', 'treatment']
            for col in text_columns:
                if col in df.columns:
                    df[col] = df[col].str.lower().str.strip()
            
            # Save preprocessed data
            output_file = os.path.join(output_dir, f"preprocessed_{file}")
            df.to_csv(output_file, index=False)
            print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data()

