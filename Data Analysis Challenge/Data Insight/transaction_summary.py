import pandas as pd
import os

===============================
STEP 1 — Load CSV file
===============================
file_path = "transactions.csv"
df = pd.read_csv(file_path)

expected_cols = [
    "Transaction_ID", "User_ID", "Location_ID",
    "Transaction_Type", "Amount_IDR", "Transaction_Time",
    "Status", "Device_Type"
]
missing_cols = [c for c in expected_cols if c not in df.columns]
if missing_cols:
    raise ValueError(f"Missing columns in CSV: {missing_cols}")

df["Transaction_Time"] = pd.to_datetime(df["Transaction_Time"], errors="coerce")

===============================
STEP 2 — Filter hanya transaksi sukses
===============================
df_success = df[df["Status"].str.lower() == "success"].copy()

===============================
STEP 3 — Ringkasan per Device
===============================
summary = (
    df_success.groupby("Device_Type")
    .agg(
        Total_Transactions=("Transaction_ID", "count"),
        Total_Amount_IDR=("Amount_IDR", "sum"),
        Avg_Amount_IDR=("Amount_IDR", "mean")
    )
    .reset_index()
)

# Jenis transaksi dominan per device
dominant_type = (
    df_success.groupby(["Device_Type", "Transaction_Type"])
    .size()
    .reset_index(name="Count")
    .sort_values(["Device_Type", "Count"], ascending=[True, False])
    .drop_duplicates("Device_Type")[["Device_Type", "Transaction_Type"]]
)

summary = summary.merge(dominant_type, on="Device_Type", how="left")
summary.rename(columns={"Transaction_Type": "Dominant_Transaction_Type"}, inplace=True)

===============================
STEP 4 — Simpan hasil ringkasan
===============================
os.makedirs("output", exist_ok=True)
summary.to_csv("output/summary.csv", index=False)

print("\n=== Summary by Device (Success Only) ===")
print(summary.to_string(index=False))
print("\n Hasil disimpan ke: output/summary.csv")
