import re
from datetime import datetime, timedelta

def parse_busy_text(text):
    day_map = {
        'monday': 'Mon', 'tuesday': 'Tue', 'wednesday': 'Wed',
        'thursday': 'Thu', 'friday': 'Fri'
    }

    # Pattern: "Monday from 9 to 11", "Tuesday 1pm to 3pm", etc.
    pattern = r"(?P<day>monday|tuesday|wednesday|thursday|friday)[^\d]*(?P<start>\d{1,2})(?:[:.]?\d{0,2})?\s*(am|pm)?[^\d]*(?P<end>\d{1,2})(?:[:.]?\d{0,2})?\s*(am|pm)?"
    matches = re.findall(pattern, text, re.IGNORECASE)

    busy_slots = set()

    for match in matches:
        day_raw, start_hr, start_ampm, end_hr, end_ampm = match
        day = day_map.get(day_raw.lower(), None)
        if not day:
            continue

        try:
            start_hr = int(start_hr)
            end_hr = int(end_hr)

            # Convert to 24-hour format
            if start_ampm == 'pm' and start_hr != 12:
                start_hr += 12
            if end_ampm == 'pm' and end_hr != 12:
                end_hr += 12

            current = datetime.strptime(f"{start_hr}", "%H")
            stop = datetime.strptime(f"{end_hr}", "%H")

            while current < stop:
                time_label = current.strftime("%I%p").lstrip("0").lower()
                busy_slots.add(f"{day}_{time_label}")
                current += timedelta(hours=1)

        except Exception as e:
            print(f"Error parsing match {match}: {e}")
            continue

    return busy_slots
