import random

# Global variable for backward navigation tracking
f = 0


class MovieBookingSystem:
    def __init__(self, rows=5, cols=5):
        # Movie name will be set dynamically based on user choice
        self.movie_name = ""
        self.seats = [[False for _ in range(cols)] for _ in range(rows)]  # False = free

    def display_seats(self):
        """Displays seat grid (O=Open, X=Booked)."""
        print(f"\n--- SEATING LAYOUT FOR {self.movie_name.upper()} ---")
        # Print column numbers header
        print("   " + " ".join([str(i + 1) for i in range(len(self.seats[0]))]))
        for r, row in enumerate(self.seats):
            print(f"{chr(65 + r)}: {' '.join(['X' if s else 'O' for s in row])}")

    def book_ticket(self, seat_code):
        """Processes input 'A1' and prints ticket."""
        try:
            row = ord(seat_code[0].upper()) - 65
            col = int(seat_code[1:]) - 1
            if not self.seats[row][col]:
                self.seats[row][col] = True  # Mark as booked
                self.print_ticket(seat_code.upper())
                return True
            else:
                print("Seat taken. Please try another seat.")
                return False
        except:
            print("Invalid seat code format. Use formats like A1, B3.")
            return False

    def print_ticket(self, seat):
        """Outputs formatted ticket with seat info."""
        print("\n" + "=" * 40)
        print(f"  MOVIE TICKET GENERATED SUCCESSFULLY")
        print("" + "=" * 40)
        print(f"  Movie : {self.movie_name}")
        print(f"  Seat  : {seat}")
        print(f"  ID    : {random.randint(100, 999)}")
        print("=" * 40 + "\n")

    def t_movie(self):
        global f
        f = f + 1
        print("\nWhich movie do you want to watch?")
        print("1, Karuppu ")
        print("2, Drishyam 3 ")
        print("3, Kara")
        print("4, Back")
        movie_choice = int(input("Choose your movie: "))

        # Map indices to names
        movie_names = {1: "Karuppu", 2: "Drishyam 3", 3: "Kara"}

        if movie_choice == 4:
            self.center()
            self.theater()
            return 0

        if movie_choice in movie_names:
            self.movie_name = movie_names[movie_choice]

        if f == 1:
            self.theater()

    def theater(self):
        print("\nWhich screen do you want to watch movie: ")
        print("1, SCREEN 1")
        print("2, SCREEN 2")
        print("3, SCREEN 3")
        a = int(input("Choose your screen: "))
        ticket_count = int(input("Number of tickets do you want?: "))
        self.timing(a, ticket_count)

    def timing(self, a, ticket_count):
        time1 = {"1": "10.00-1.00", "2": "1.10-4.10", "3": "4.20-7.20", "4": "7.30-10.30"}
        time2 = {"1": "10.15-1.15", "2": "1.25-4.25", "3": "4.35-7.35", "4": "7.45-10.45"}
        time3 = {"1": "10.30-1.30", "2": "1.40-4.40", "3": "4.50-7.50", "4": "8.00-10.45"}

        if a == 1:
            active_time = time1
        elif a == 2:
            active_time = time2
        elif a == 3:
            active_time = time3
        else:
            print("Invalid screen selection.")
            return

        print("\nChoose your time:")
        print(active_time)
        t = input("Select your time slot key (1-4): ")
        x = active_time[t]
        print(f"\nTime confirmed! Enjoy the movie at {x}")

        # Trigger the seat booking phase for each ticket requested
        for i in range(ticket_count):
            print(f"\nBooking ticket {i + 1} of {ticket_count}:")
            while True:
                self.display_seats()
                seat_choice = input("Enter seat code (e.g., A1): ")
                if self.book_ticket(seat_choice):
                    break  # Break inner loop when ticket books successfully

    def movie(self, theater_choice):
        if theater_choice in [1, 2, 3]:
            self.t_movie()
        elif theater_choice == 4:
            self.city()
        else:
            print("Wrong choice")

    def center(self):
        print("\nWhich theater do you wish to see movie? ")
        print("1, Inox")
        print("2, Icon")
        print("3, pvp")
        print("4, Back")
        a = int(input("Choose your option: "))
        self.movie(a)

    def city(self):
        print("\nHi welcome to movie ticket booking: ")
        print("Where you want to watch movie?:")
        print("1, Chennai")
        print("2, Madurai ")
        print("3, Coimbatore ")
        place = int(input("Choose your option: "))
        if place in [1, 2, 3]:
            self.center()
        else:
            print("Wrong choice")


# Main Execution block
if __name__ == "__main__":
    # Create system object instance
    system = MovieBookingSystem()
    # Call the initial city selection function through the instance
    system.city()
