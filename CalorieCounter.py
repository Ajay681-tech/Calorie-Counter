
from datetime import date

class CalorieCounter:
    def __init__(self):
        self.log = {}

    def log_food(self, food_name, calories):
        """Logs a food item with calorie count for today's date."""
        today = date.today().isoformat()
        if today not in self.log:
            self.log[today] = []
        self.log[today].append({"food": food_name, "calories": calories})
        print(f"Logged: {food_name} ({calories} calories) for {today}")

    def view_day_entries(self, day):
        """Displays the food entries and total calories for a given day."""
        day_str = day.isoformat()
        if day_str in self.log:
            print(f"Calorie log for {day_str}:")
            total_calories = 0
            for entry in self.log[day_str]:
                print(f"  - {entry['food']}: {entry['calories']} calories")
                total_calories += entry['calories']
            print(f"Total calories for {day_str}: {total_calories} calories")
        else:
            print(f"No entries found for {day_str}.")

# Example usage
if __name__ == "__main__":
    calorie_counter = CalorieCounter()

    while True:
        print("\nOptions:")
        print("1. Log Food")
        print("2. View Day Entries")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            food_name = input("Enter the food name: ")
            try:
                calories = int(input("Enter calories: "))
                calorie_counter.log_food(food_name, calories)
            except ValueError:
                print("Please enter a valid number for calories.")
        elif choice == "2":
            try:
                year = int(input("Enter year (YYYY): "))
                month = int(input("Enter month (MM): "))
                day = int(input("Enter day (DD): "))
                calorie_counter.view_day_entries(date(year, month, day))
            except ValueError:
                print("Please enter a valid date.")
        elif choice == "3":
            print("Exiting the program. Stay healthy!")
            break
        else:
            print("Invalid choice. Please try again.")
