import re

def parse_text_constraints(text):
    text = text.lower()
    constraints = {
        "no_days": set(),
        "preferred_time": None,
        "max_hours_per_day": None,
    }

    if "no weekends" in text:
        constraints["no_days"].update({"Sat", "Sun"})
    if "no friday" in text:
        constraints["no_days"].add("Fri")

    if "mornings" in text:
        constraints["preferred_time"] = "morning"
    elif "evenings" in text or "after 5" in text or "after 6" in text:
        constraints["preferred_time"] = "evening"

    match = re.search(r'(\d+)\s*(hours|hrs)\s*(per day|a day)', text)
    if match:
        constraints["max_hours_per_day"] = int(match.group(1))

    return constraints
