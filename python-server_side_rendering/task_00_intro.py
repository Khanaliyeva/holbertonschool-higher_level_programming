import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Check empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        # For each placeholder, get value or "N/A" if missing or None
        filled_template = template
        for ph in placeholders:
            val = attendee.get(ph)
            if val is None:
                val = "N/A"
            filled_template = filled_template.replace("{" + ph + "}", str(val))

        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w") as f:
                f.write(filled_template)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
