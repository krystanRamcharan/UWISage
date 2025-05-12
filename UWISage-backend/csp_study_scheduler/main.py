# main.py  (simplified command-line version)

from scheduler_utils import generate_weekly_slots, read_busy_slots
from busy_time_parser import parse_busy_text
from course_utils import get_study_hours_from_credits
from restriction_parser import parse_text_constraints
from csp_scheduler import generate_schedule


use_csv = input("Do you want to upload a class schedule CSV? (yes/no): ").strip().lower()

if use_csv == "yes":
    file_path = input("Enter CSV file path (e.g., class_schedule.csv): ").strip()
    busy_slots = read_busy_slots(file_path)
else:
    text_input = input("Describe your class schedule (e.g. 'Monday 9-11, Tuesday 1-3'): ")
    busy_slots = parse_busy_text(text_input)

all_slots = generate_weekly_slots()                     
available_slots = list(set(all_slots) - busy_slots)


course_hours = get_study_hours_from_credits("courses.csv", hours_per_credit=1)


pref_text = input("Any study constraints? (e.g. 'no weekends, evenings only')\n> ")
constraints = parse_text_constraints(pref_text)

schedule = generate_schedule(available_slots, course_hours, constraints)


print("\n---- Your Personalized Study Schedule ----")
for slot, course in sorted(schedule.items()):
    print(f"{slot}: {course}")

# if __name__ == "__main__":
#     from scheduler_utils import generate_weekly_slots

  
#     available = generate_weekly_slots()

    
#     course_hours = {
#         "COMP2140": 3,
#         "INFO2100": 2
#     }

#     # Sample constraints (none for now)
#     constraints = {
#         "no_weekends": True,
#         "preferred_times": ["evening"],
#         "max_per_day": 2
#     }

#     from pprint import pprint
#     schedule = generate_schedule(available, course_hours, constraints)
#     pprint(schedule)
