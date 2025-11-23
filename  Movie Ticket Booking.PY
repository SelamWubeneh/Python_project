
# 4. Movie Ticket Booking Simulation
# Simulate a movie theater booking system that:
# Shows a list of available movie titles, showtimes, and seat prices.
# Asks the user to choose a movie and number of tickets.
# Confirms total price and asks if they want to book another movie.
# Ends when they say “no” and displays total bookings and cost.
# Skills practiced: loops, input, conditionals, calculations, nested dictionaries



# Step-1: Welcome message
print("   ============== Welcome to MovieTime! Grab your tickets. ==============")
print()

# Step-2: Initialize available movies with title, showtime and prices.
movies = {
    'The Lion King' : {'showtime':['12:00', '15:00'], 'price': 15},
    'Brave' : {'showtime':['13:00', '16:00'], 'price': 20},
    'The Help' : {'showtime':['14:00', '17:00'], 'price': 10},
    'Rango' : {'showtime':['11:00', '14:00'], 'price': 30}
}

# Step-3: Display for the available movies from the movies list
print("     ====================== Today's Movie List ======================")
for movie, movie_details in movies.items():
    showtime, price = movie_details['showtime'], movie_details['price']
    print(f'Name: {movie:20}: ----     Showtime: {showtime} ----       Unit-price: ${price:.2f}')
print()

total_movie_booked = []
total_cost = 0

while True:
    # Step-4: Get input from the user for movie selection
    selected_movie = input('Please enter the movie name from the list or done to finish: ').strip().title()
    if selected_movie == "done":
        break
    if selected_movie in movies:
        print(f'You selected a movie titled: {selected_movie} from the list')
    else:
        print(f"{selected_movie} movie is not in today's list. Please enter again from the list. ")
        continue
    # Step-5: Get input from the user for number of movie tickets
    while True:
        
        ticket_qty = input('How many tickets do you want?: ')
        if ticket_qty.isdigit():
            ticket_qty_int = int(ticket_qty)
            if ticket_qty_int <= 0:
                print('Ticket quantity must be breater than zero. Please enter a valid number.')
                print()
            else:
                break
        else:
            print('Invalid input. Please enter a valid input for the selected movie.')
            print()
            continue

    # Step-6: Get input from the user for showtime
    print(f"The showtime for the movie {selected_movie} is {movies[selected_movie]['showtime']}")
    while True:
        selected_showtime = input('Please enter the showtime you want from the list: ').strip()
        if selected_showtime in movies[selected_movie]['showtime']:
            #print(f'Your {selected_movie} movie is at {selected_showtime}.')
            break
            print()
        else:
            print(f"{selected_showtime} is not in the showtime list. Please try again from the list.")
            continue

    # Step-7: Determine total price for the booking by using tichet_qty_int times price
    # Access the price from the movies list
    price_per_selected_movie = movies[selected_movie]['price']
    subtotal = ticket_qty_int * price_per_selected_movie
    total_cost += subtotal

    # Step-8: Append selected movie booking to the total  movie booking list
    total_movie_booked.append({'movie':selected_movie, 'showtime':selected_showtime, 'ticket':ticket_qty_int,
                               'price':price_per_selected_movie, 'subtotal':subtotal})
    print(f'You booked a movie name {selected_movie} at {selected_showtime} with {ticket_qty_int} number of tickets and total cost of {total_cost}')

    # Step-9: Check if the user wants to book additional movie from the list
    additional_booking = input('Do you want to add new booking? (y/n): ')
    additional_booking = additional_booking.lower()
    if additional_booking == 'n':
        break

# Step-10: Printing Receipt
print()
print('          ======================= RECEIPT ======================= ')
for ticket_booked in total_movie_booked:
    movie_name = ticket_booked['movie']
    ticket = ticket_booked['ticket']
    selected_time = ticket_booked['showtime']
    unit_price = ticket_booked['price']
    subtotal = ticket_booked['subtotal']

    print(f'You booked: Movie Title:{movie_name} --- Qty:{ticket} --- Showtime:{selected_time} --- Unit price:${price} --- Subtotal:${subtotal}')
print('_' * 80)
print(f"{'Total Cost':15} ------------------------------------------------------    ${total_cost:.2f}")
print('_' * 80)
print('        ****************  Thank you for coming!  ****************')