from datetime import datetime

events = []


def add_event():
    name = input("\nEnter event name: ")
    date_text = input("Enter event date (YYYY-MM-DD): ")

    try:
        event_date = datetime.strptime(date_text, "%Y-%m-%d").date()

        events.append({
            "name": name,
            "date": event_date
        })

        print("Event added successfully!")

    except ValueError:
        print("Invalid date format!")


def view_events():
    print("\n========== EVENTS ==========")

    if not events:
        print("No events available.")
        return

    today = datetime.today().date()

    events.sort(key=lambda event: event["date"])

    for event in events:
        difference = (event["date"] - today).days

        if difference > 0:
            status = f"{difference} days remaining"
        elif difference == 0:
            status = "Today"
        else:
            status = "Event completed"

        print(f"{event['date']} - {event['name']} ({status})")


def main():
    print("========== CALENDAR EVENT PLANNER ==========")

    while True:
        print("\n1. Add Event")
        print("2. View Events")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_event()

        elif choice == "2":
            view_events()

        elif choice == "3":
            print("\nThank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()