import pandas as pd
import os

# ===============================
# STEP 1 — Load file summary dan data utama
# ===============================
file_path = "transactions.csv"
df = pd.read_csv(file_path)

df["Transaction_Time"] = pd.to_datetime(df["Transaction_Time"], errors="coerce")

# Filter hanya transaksi sukses
df_success = df[df["Status"].str.lower() == "success"].copy()

# ===============================
# STEP 2 — Deteksi Anomali berdasarkan Amount_IDR
# ===============================
Q1 = df_success["Amount_IDR"].quantile(0.25)
Q3 = df_success["Amount_IDR"].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + 1.5 * IQR

anomalies = df_success[df_success["Amount_IDR"] > upper_limit].copy()

# ===============================
# STEP 3 — Simpan hasil anomali
# ===============================
os.makedirs("output", exist_ok=True)
anomalies.to_csv("output/anomalies.csv", index=False)

# ===============================
# STEP 4 — Tampilkan hasil
# ===============================
print("\n=== ⚠️ Potential Anomalies (Amount_IDR) ===")
if anomalies.empty:
    print("Tidak ada anomali terdeteksi.")
else:
    print(anomalies[["Transaction_ID", "Transaction_Type", "Amount_IDR", "Device_Type"]].to_string(index=False))

print("\n✅ Hasil disimpan ke: output/anomalies.csv")
