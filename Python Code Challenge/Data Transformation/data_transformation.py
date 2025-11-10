import pandas as pd
import re
from io import StringIO

def transform_checkin_logs(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform check-in logs:
    1. Calculate Stay_Duration_Hours from Duration_String.
    2. Standardize Guest_Type.
    3. Filter records with Check_In_Date >= 2024-01-01.
    """
    
    # Convert Check_In_Date to datetime
    df["Check_In_Date"] = pd.to_datetime(df["Check_In_Date"], errors="coerce")
    
    # Filter by date (only 2024 and later)
    df = df[df["Check_In_Date"] >= pd.Timestamp("2024-01-01")].copy()

    # Parse Duration_String into total hours
    def parse_duration(duration_str):
        if pd.isna(duration_str):
            return None
        days = 0
        hours = 0
        match_days = re.search(r"(\d+)\s*day", duration_str)
        match_hours = re.search(r"(\d+)\s*hour", duration_str)
        if match_days:
            days = int(match_days.group(1))
        if match_hours:
            hours = int(match_hours.group(1))
        return days * 24 + hours

    df["Stay_Duration_Hours"] = df["Duration_String"].apply(parse_duration)

    # Standardize Guest_Type
    def standardize_guest_type(x):
        if not isinstance(x, str):
            return x
        x_lower = x.strip().lower()
        if any(k in x_lower for k in ["new", "first", "baru"]):
            return "New"
        elif any(k in x_lower for k in ["return", "repeat", "kembali"]):
            return "Returning"
        else:
            return x  # leave unchanged if not matched

    df["Guest_Type"] = df["Guest_Type"].apply(standardize_guest_type)

    return df.reset_index(drop=True)


# =======================
#  Example Usage
# =======================

data = """Log_ID,Guest_ID,Check_In_Date,Duration_String,Location_ID,Guest_Type
1001,G1234,2024-03-15,"2 days, 10 hours",LOC01,New_User
1002,G5678,2023-12-28,"1 day, 5 hours",LOC03,returning
1003,G9012,2024-06-01,"4 days, 0 hours",LOC01,Returning Guest
1004,G3456,2024-01-05,"10 hours",LOC02,new
1005,G7890,2024-07-20,"5 days, 15 hours",LOC04,Returning
1006,G1122,2024-02-14,"1 day, 2 hours",LOC05,Repeat
1007,G3344,2024-08-01,"18 hours",LOC01,First-Time
1008,G5566,2024-04-22,"3 days, 6 hours",LOC02,new
1009,G7788,2023-11-10,"7 hours",LOC03,Returning Guest
1010,G9900,2024-05-19,"2 days, 20 hours",LOC04,New_User
1011,G0011,2024-01-01,"1 day, 0 hours",LOC05,kembali
1012,G2233,2024-07-25,"9 hours",LOC01,Repeat
1013,G4455,2024-03-08,"3 days, 12 hours",LOC02,new
1014,G6677,2023-10-05,"2 days, 1 hours",LOC03,New_User
1015,G8899,2024-06-15,"14 hours",LOC04,Returning
1016,G1212,2024-02-29,"4 days, 4 hours",LOC05,First-Time
1017,G3434,2024-08-20,"1 day, 16 hours",LOC01,Returning Guest
1018,G5656,2024-04-01,"5 days, 0 hours",LOC02,new
1019,G7878,2023-09-01,"8 hours",LOC03,New_User
1020,G9090,2024-05-05,"2 days, 18 hours",LOC04,Repeat
1021,G1357,2024-01-10,"1 day, 4 hours",LOC05,Returning
1022,G2468,2024-07-04,"11 hours",LOC01,new
1023,G3579,2024-03-20,"3 days, 8 hours",LOC02,First-Time
1024,G4680,2023-07-17,"20 hours",LOC03,Returning Guest
1025,G5791,2024-06-30,"1 day, 13 hours",LOC04,Repeat
1026,G6802,2024-02-01,"4 days, 16 hours",LOC05,New_User
1027,G7913,2024-08-15,"6 hours",LOC01,returning
1028,G8024,2024-04-10,"2 days, 22 hours",LOC02,new
1029,G9135,2023-06-01,"1 day, 1 hour",LOC03,Returning
1030,G0246,2024-05-25,"3 days, 10 hours",LOC04,First-Time
1031,G1468,2024-01-22,"12 hours",LOC05,New_User
1032,G2579,2024-07-11,"5 days, 1 hour",LOC01,returning
1033,G3680,2024-03-01,"1 day, 7 hours",LOC02,Repeat
1034,G4791,2024-05-15,"16 hours",LOC03,Baru
1035,G5802,2024-06-08,"2 days, 19 hours",LOC04,New_User
1036,G6913,2024-02-08,"3 days, 0 hours",LOC05,Returning Guest
1037,G7024,2024-08-25,"1 day, 19 hours",LOC01,returning
1038,G8135,2024-04-18,"4 days, 5 hours",LOC02,new
1039,G9246,2023-04-04,"15 hours",LOC03,First-Time
1040,G0357,2024-05-01,"2 days, 3 hours",LOC04,Repeat
1041,G1479,2024-01-29,"1 day, 23 hours",LOC05,New_User
1042,G2591,2024-07-28,"17 hours",LOC01,returning
1043,G3602,2024-03-25,"3 days, 14 hours",LOC02,First-Time
1044,G4713,2023-03-20,"2 days, 6 hours",LOC03,Returning Guest
1045,G5824,2024-06-20,"1 day, 9 hours",LOC04,Repeat
1046,G6935,2024-02-18,"5 hours",LOC05,new
1047,G7046,2024-16-05,"4 days, 1 hour",LOC01,New_User
1048,G8157,2024-04-29,"2 days, 7 hours",LOC02,returning
1049,G9268,2023-02-01,"1 day, 10 hours",LOC03,First-Time
1050,G0379,2024-05-10,"3 days, 5 hours",LOC04,Repeat
"""

# Load data into DataFrame
df_raw = pd.read_csv(StringIO(data))

# Transform the logs
df_transformed = transform_checkin_logs(df_raw)

# Show result
print(df_transformed.head(10))

# (Opsional) simpan ke CSV
# df_transformed.to_csv("checkin_transformed.csv", index=False)
