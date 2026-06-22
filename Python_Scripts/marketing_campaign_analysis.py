import os
import sqlite3
import pandas as pd


def create_marketing_database():
    # 1. Connect to SQLite (This creates 'marketing_analytics.db' automatically if it doesn't exist)
    db_name = "marketing_analytics.db"
    print(f"Creating and connecting to database: {db_name}...")
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # 2. Create the CampaignData table
    print("Creating CampaignData table...")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS CampaignData (
            CampaignID INTEGER PRIMARY KEY,
            CampaignName TEXT NOT NULL,
            Budget REAL,
            ActualSpend REAL,
            Impressions INTEGER,
            Clicks INTEGER,
            Conversions INTEGER,
            Revenue REAL
        );
    """
    )

    # 3. Clear out existing old data if you run the script multiple times
    cursor.execute("DELETE FROM CampaignData;")

    # 4. Define rich mock data for your analysis questions
    mock_campaigns = [
        (1, "Summer_Sale_FB", 5000.00, 4800.00, 150000, 4500, 220, 9500.00),
        (
            2,
            "Black_Friday_Google",
            12000.00,
            12500.00,
            350000,
            12000,
            840,
            31000.00,
        ),
        (3, "Holiday_Retargeting", 3000.00, 2900.00, 80000, 3100, 310, 8800.00),
        (4, "Spring_Launch_Insta", 4000.00, 4100.00, 110000, 3800, 150, 3900.00),
        (5, "Chrsitmas_Brand_TikTok", 7000.00, 7200.00, 250000, 9500, 410, 14500.00),
    ]

    # 5. Insert mock data into the table
    print("Inserting mock marketing data rows...")
    cursor.executemany(
        """
        INSERT INTO CampaignData (CampaignID, CampaignName, Budget, ActualSpend, Impressions, Clicks, Conversions, Revenue)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """,
        mock_campaigns,
    )

    # Commit transactions and close connection safely
    conn.commit()
    conn.close()
    print("Database created and seeded successfully!")


def verify_database_data():
    # Quick function to read data via pandas to make sure it looks correct
    conn = sqlite3.connect("marketing_analytics.db")
    df = pd.read_sql_query("SELECT * FROM CampaignData;", conn)
    conn.close()

    print("\n--- Verified Loaded Data ---")
    print(df)


if __name__ == "__main__":
    create_marketing_database()
    verify_database_data()
