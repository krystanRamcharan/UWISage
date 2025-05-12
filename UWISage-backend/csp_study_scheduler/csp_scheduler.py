def generate_schedule(available_slots, course_hours, constraints):
    schedule = {}
    used_slots = set()
    max_per_day = constraints.get("max_hours_per_day", None)
    no_days = constraints.get("no_days", set())
    preferred = constraints.get("preferred_time", None)

 
    filtered_slots = [
        slot for slot in available_slots
        if slot[:3] not in no_days
    ]

    if preferred == "evening":
        filtered_slots = [s for s in filtered_slots if "pm" in s]
    elif preferred == "morning":
        filtered_slots = [s for s in filtered_slots if "am" in s and not s.startswith(("12", "11"))]

    for course, hours_needed in course_hours.items():
        hours_assigned = 0
        for slot in filtered_slots:
            day = slot.split("_")[0]
            if slot in used_slots:
                continue
            if max_per_day:
                slots_today = [s for s in schedule if s.startswith(day)]
                if len(slots_today) >= max_per_day:
                    continue
            schedule[slot] = course
            used_slots.add(slot)
            hours_assigned += 1
            if hours_assigned == hours_needed:
                break

    return schedule
