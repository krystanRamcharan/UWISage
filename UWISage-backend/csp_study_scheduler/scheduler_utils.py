from datetime import datetime, timedelta
import pandas as pd

def generate_weekly_slots(start_hour=8, end_hour=20):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    slots = []
    for day in days:
        for hour in range(start_hour, end_hour):
            time_str = datetime.strptime(str(hour), "%H").strftime("%I%p").lstrip("0").lower()
            slots.append(f"{day}_{time_str}")
    return slots

def read_busy_slots(csv_path):
    df = pd.read_csv(csv_path)
    busy_slots = set()

    for _, row in df.iterrows():
        day = row['Day'][:3]  # 'Monday' → 'Mon'
        start = datetime.strptime(row['Start'], "%H:%M")
        end = datetime.strptime(row['End'], "%H:%M")

        while start < end:
            time_str = start.strftime("%I%p").lstrip("0").lower()
            busy_slots.add(f"{day}_{time_str}")
            start += timedelta(hours=1)

    return busy_slots
