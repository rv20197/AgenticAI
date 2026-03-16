railway_ticket_seat_info_input = input("Enter your railway ticket seat information (e.g., 'Sleeper', 'AC', 'General', 'Luxury'): ")

railway_ticket_seat_info = {
    "sleeper": "You have a Sleeper class ticket. Enjoy your journey with basic amenities.",
    "ac": "You have an AC class ticket. Enjoy your journey with air conditioning and comfortable seating.",
    "general": "You have a General class ticket. Enjoy your journey with basic seating arrangements.",
    "luxury": "You have a Luxury class ticket. Enjoy your journey with premium amenities and services."
}

seat_info = railway_ticket_seat_info.get(railway_ticket_seat_info_input.lower(), "Invalid seat information. Please enter a valid seat type.")
print(seat_info)