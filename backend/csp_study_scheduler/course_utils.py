import pandas as pd

def get_study_hours_from_credits(csv_path, hours_per_credit=1):
   
    df = pd.read_csv(csv_path)
    study_hours = {}

    for _, row in df.iterrows():
        code = row.get("courseCode")
        credits = row.get("credits")

        try:
            hours = int(credits) * hours_per_credit
        except:
            hours = hours_per_credit  # fallback default

        if code:
            study_hours[code] = hours

    return study_hours
