import pandas as pd

def read_csv_file(file_path):
    # Read CSV file using pandas
    df = pd.read_csv(file_path)
    
    # Display basic information about the dataset
    print("\nDataset Info:")
    print("-" * 50)
    print(df.info())
    
    # Display first few rows of the data
    print("\nFirst 5 rows of data:")
    print("-" * 50)
    print(df.head())
    
    # Display basic statistical summary
    print("\nStatistical Summary:")
    print("-" * 50)
    print(df.describe())

# Example usage
if __name__ == "__main__":
    csv_file_path = "./example.csv"
    read_csv_file(csv_file_path)
