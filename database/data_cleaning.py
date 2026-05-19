import pandas as pd
import re


def clean_product_data():

    df = pd.read_json("cleaned_data/products.json")

    # Remove currency symbol using regex
    df["price"] = df["price"].apply(
        lambda x: re.sub(r"[^\d.]", "", x)
    )

    # Convert price to float
    df["price"] = df["price"].astype(float)

    # Remove duplicate titles
    df = df.drop_duplicates(subset=["title"])

    # Save cleaned data
    df.to_csv("cleaned_data/cleaned_products.csv", index=False)

    print("Data cleaned successfully!")


if __name__ == "__main__":
    clean_product_data()