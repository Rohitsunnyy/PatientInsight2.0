import os
from datasets import load_dataset

def download_dataset(output_dir='data/raw'):
    """
    Download the PMC-Patients dataset and save it locally.
    """
    os.makedirs(output_dir, exist_ok=True)
    dataset = load_dataset("zhengyun21/PMC-Patients")
    
    for split in dataset.keys():
        dataset[split].to_csv(os.path.join(output_dir, f"{split}.csv"), index=False)
    
    print(f"Dataset downloaded and saved to {output_dir}")

if __name__ == "__main__":
    download_dataset()

