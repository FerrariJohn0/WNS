import streamlit as st
import requests
import pandas as pd

if "selected_seat" not in st.session_state:
    st.session_state.selected_seat = None

BASE_URL = "http://127.0.0.1:8000"

st.title("Movie Booking App")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Register User",
        "View Movies",
        "View Theatres",
        "View Shows",
        #"View Available Seats",
        "Book Ticket",
        "View Bookings"
    ]
)
if menu == "Register User":

    st.header("👤 Register User")

    st.markdown(
        """
        Create your account to start booking
        movie tickets instantly.
        """
    )

    st.divider()

    # -----------------------------
    # Layout Columns
    # -----------------------------

    left_col, right_col = st.columns([2, 1])

    # -----------------------------
    # Registration Form
    # -----------------------------

    with left_col:

        with st.container(border=True):

            st.subheader("📝 User Details")

            name = st.text_input(
                "Enter Full Name",
                placeholder="John Doe"
            )

            email = st.text_input(
                "Enter Email Address",
                placeholder="john@gmail.com"
            )

            st.write("")

            register_btn = st.button(
                "🚀 Register Account",
                use_container_width=True
            )

            if register_btn:

                if not name or not email:

                    st.warning(
                        "Please fill all fields"
                    )

                else:

                    payload = {
                        "name": name,
                        "email": email
                    }

                    response = requests.post(
                        f"{BASE_URL}/users/",
                        json=payload
                    )

                    if response.status_code == 200:

                        user = response.json()

                        st.success(
                            "✅ Registration Successful"
                        )

                        st.balloons()

                        st.json(user)

                    else:

                        st.error(
                            response.json()
                        )

    # -----------------------------
    # Side Information Panel
    # -----------------------------

    with right_col:

        with st.container(border=True):

            st.subheader("🎬 Benefits")

            st.markdown(
                """
                ✅ Book movie tickets instantly
                
                ✅ Access multiple theatres
                
                ✅ Real-time seat availability
                
                
                ✅ Personalized booking history
                """
            )

            st.info(
                "Start exploring movies after registration.")
    
                
elif menu == "View Movies":

    st.header("🎬 Movies Catalog")

    response = requests.get(
        f"{BASE_URL}/movies/"
    )

    if response.status_code == 200:

        movies = response.json()

        if movies:

            search = st.text_input(
                "Search Movie"
            )

            genre_filter = st.selectbox(
                "Filter by Genre",
                ["All"] + list(
                    set(
                        movie["genre"]
                        for movie in movies
                    )
                )
            )

            filtered_movies = []

            for movie in movies:

                matches_search = (
                    search.lower()
                    in movie["title"].lower()
                )

                matches_genre = (
                    genre_filter == "All"
                    or movie["genre"] == genre_filter
                )

                if matches_search and matches_genre:

                    filtered_movies.append(movie)
            if not filtered_movies:
                st.warning("No Movies Found")
            else:
                

                cols = st.columns(2)
                

                for index, movie in enumerate(filtered_movies):

                    with cols[index % 2]:

                        st.container(border=True)

                        st.subheader(
                            movie["title"]
                        )

                        st.write(
                            f"🎭 Genre: {movie['genre']}"
                        )

                        st.write(
                            f"⏱ Duration: {movie['duration']} mins"
                        )

                        st.write(
                            f"🌐 Language: {movie['language']}"
                        )

                        st.success(
                            "Now Showing"
                        )

        else:

            st.warning("No Movies Found")

    else:

        st.error(
            "Failed to fetch movies"
        )
elif menu == "View Theatres":

    st.header("Theatres List")

    response = requests.get(
        f"{BASE_URL}/theatres/"
    )

    if response.status_code == 200:

        theatres = response.json()

        if theatres:
            search = st.text_input(
                "Search Theatre"
            )
            filtered_theatres = []
            for theatre in theatres:
                if search.lower() in theatre["name"].lower():

                    filtered_theatres.append(theatre)
            # Metrics Section
            total_theatres = len(filtered_theatres)
            total_seats = sum(
                theatre["total_seats"]
                for theatre in filtered_theatres)
            cities = len(
                set(
                    theatre["location"]
                    for theatre in filtered_theatres
                )
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Theatres",
                    total_theatres
                )

            with col2:
                st.metric(
                    "Total Seats",
                    total_seats
                )

            with col3:
                st.metric(
                    "Cities Covered",
                    cities
                )

            st.divider()
            # Theatre Cards
            cols = st.columns(2)

            for index, theatre in enumerate(filtered_theatres):

                with cols[index % 2]:

                    with st.container(border=True):

                        st.subheader(
                            f"🎭 {theatre['name']}"
                        )

                        st.write(
                            f"📍 Location: {theatre['location']}"
                        )

                        st.write(
                            f"💺 Total Seats: {theatre['total_seats']}"
                        )

                        st.success(
                            "Available for Booking"
                        )
        else:

            st.warning(
                "No Theatres Found"
            )

    else:

        st.error("Failed to fetch theatres")

        '''df = pd.DataFrame(theatres)

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning("No Theatres Found")

    else:

        st.error("Failed to fetch theatres")'''
elif menu == "View Shows":

    st.header("🎬 Shows List")

    response = requests.get(
        f"{BASE_URL}/shows/"
    )

    if response.status_code == 200:

        shows = response.json()

        if shows:

            # -----------------------------
            # Search by Show ID
            # -----------------------------

            search = st.text_input(
                "Search Show by ID"
            )

            filtered_shows = []

            for show in shows:

                if search == "" or search in str(show["id"]):

                    filtered_shows.append(show)

            # -----------------------------
            # Metrics Section
            # -----------------------------

            total_shows = len(filtered_shows)

            avg_price = (
                sum(
                    show["price"]
                    for show in filtered_shows
                ) / total_shows
                if total_shows > 0 else 0
            )

            max_price = (
                max(
                    show["price"]
                    for show in filtered_shows
                )
                if total_shows > 0 else 0
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Shows",
                    total_shows
                )

            with col2:
                st.metric(
                    "Average Price",
                    f"₹{avg_price:.0f}"
                )

            with col3:
                st.metric(
                    "Highest Price",
                    f"₹{max_price:.0f}"
                )

            st.divider()

            # -----------------------------
            # Show Cards
            # -----------------------------

            cols = st.columns(2)

            for index, show in enumerate(filtered_shows):

                with cols[index % 2]:

                    with st.container(border=True):

                        st.subheader(
                            f"🎟 Show ID: {show['id']}"
                        )

                        st.write(
                            f"🎬 Movie ID: {show['movie_id']}"
                        )

                        st.write(
                            f"🏢 Theatre ID: {show['theatre_id']}"
                        )

                        st.write(
                            f"🕒 Show Time: {show['show_time']}"
                        )

                        st.write(
                            f"💰 Ticket Price: ₹{show['price']}"
                        )

                        if show["price"] >= 250:

                            st.error(
                                "Premium Show"
                            )

                        elif show["price"] >= 180:

                            st.warning(
                                "Popular Show"
                            )

                        else:

                            st.success(
                                "Budget Friendly"
                            )

        else:

            st.warning(
                "No Shows Available"
            )

    else:

        st.error("Failed to fetch shows")  
       
        '''st.header("Shows List")

    response = requests.get(
        f"{BASE_URL}/shows/"
    )

    if response.status_code == 200:

        shows = response.json()

        if shows:

            df = pd.DataFrame(shows)

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning("No Shows Found")

    else:

        st.error("Failed to fetch shows")'''
        
        
elif menu == "View Available Seats":

    st.header("Available Seats")

    show_id = st.number_input(
        "Enter Show ID",
        min_value=1,
        step=1
    )

    if st.button("Fetch Seats"):

        response = requests.get(
            f"{BASE_URL}/seats/{show_id}"
        )

        if response.status_code == 200:

            seats = response.json()

            if seats:

                df = pd.DataFrame(seats)

                st.dataframe(
                    df,
                    use_container_width=True
                )

            else:

                st.warning(
                    "No Available Seats"
                )

        else:

            st.error(
                "Failed to fetch seats"
            )
elif menu == "Book Ticket":

    st.header("🎟 Book Movie Ticket")


    # Fetch Shows

    shows_response = requests.get(
        f"{BASE_URL}/shows/"
    )

    if shows_response.status_code == 200:

        shows = shows_response.json()

        if shows:

            show_options = {
                f"Show {show['id']} | ₹{show['price']} | {show['show_time']}": show["id"]
                for show in shows
            }

            selected_show = st.selectbox(
                "Select Show",
                list(show_options.keys())
            )

            show_id = show_options[selected_show]

            
            # Fetch Available Seats
            

            seats_response = requests.get(
                f"{BASE_URL}/seats/{show_id}"
            )

            if seats_response.status_code == 200:

                seats = seats_response.json()

                if seats:

                    st.subheader(
                        "Available Seats"
                    )

                    seat_map = {}

                    for seat in seats:

                        row = seat["seat_number"][0]

                        if row not in seat_map:
                            seat_map[row] = []

                        seat_map[row].append(seat)


                    for row_name, row_seats in seat_map.items():

                        st.write(f"### Row {row_name}")

                        cols = st.columns(5)

                        for index, seat in enumerate(row_seats):

                            with cols[index % 5]:

                                if seat["is_booked"]:
                                    st.button(f"🟥 {seat['seat_number']}",disabled=True,key=f"booked_{seat['id']}")
                                else:
                                    if st.button(f"🟩 {seat['seat_number']}",key=f"available_{seat['id']}"):

                                        st.session_state.selected_seat = seat
                                    
                    # User Selection
                    
                    user_id = st.number_input(
                        "Enter User ID",
                        min_value=1,
                        step=1
                    )

                    if st.session_state.selected_seat:

                        st.success(
                            f"Selected Seat: {st.session_state.selected_seat['seat_number']}"
                        )

                        if st.button(
                            "Confirm Booking"
                        ):

                            payload = {
                                "user_id": int(user_id),
                                "show_id": int(show_id),
                                "seat_id": st.session_state.selected_seat["id"]
                            }

                            booking_response = requests.post(
                                f"{BASE_URL}/bookings/",
                                json=payload
                            )

                            if booking_response.status_code == 200:

                                st.success(
                                    "🎉 Ticket Booked Successfully"
                                )

                                st.json(
                                    booking_response.json()
                                )

                            else:

                                st.error(
                                    booking_response.json()
                                )

                else:

                    st.warning(
                        "No Available Seats"
                    )

            else:

                st.error(
                    "Failed to fetch seats"
                )

        else:

            st.warning(
                "No Shows Available"
            )

    else:

        st.error(
            "Failed to fetch shows")
        
elif menu == "View Bookings":

    st.header("🎟 Booking History")

    response = requests.get(
        f"{BASE_URL}/bookings/"
    )

    if response.status_code == 200:

        bookings = response.json()

        if bookings:

            # -----------------------------
            # Search Booking
            # -----------------------------

            search = st.text_input(
                "Search by User ID"
            )

            filtered_bookings = []

            for booking in bookings:

                if (
                    search == ""
                    or search in str(booking["user_id"])
                ):

                    filtered_bookings.append(
                        booking
                    )

            # -----------------------------
            # Metrics Section
            # -----------------------------

            total_bookings = len(
                filtered_bookings
            )

            unique_users = len(
                set(
                    booking["user_id"]
                    for booking in filtered_bookings
                )
            )

            total_seats_booked = len(
                filtered_bookings
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Bookings",
                    total_bookings
                )

            with col2:
                st.metric(
                    "Users",
                    unique_users
                )

            with col3:
                st.metric(
                    "Seats Booked",
                    total_seats_booked
                )

            st.divider()

            # -----------------------------
            # Booking Cards
            # -----------------------------

            cols = st.columns(2)

            for index, booking in enumerate(
                filtered_bookings
            ):

                with cols[index % 2]:

                    with st.container(border=True):

                        st.subheader(
                            f"🎫 Booking #{booking['id']}"
                        )

                        st.write(
                            f"👤 User ID: {booking['user_id']}"
                        )

                        st.write(
                            f"🎬 Show ID: {booking['show_id']}"
                        )

                        st.write(
                            f"💺 Seat ID: {booking['seat_id']}"
                        )

                        st.success(
                            "Booking Confirmed"
                        )

        else:

            st.warning(
                "No Booking History Found"
            )

    else:

        st.error(
            "Failed to fetch bookings")
        '''st.header("Booking History")

    response = requests.get(
        f"{BASE_URL}/bookings/"
    )

    if response.status_code == 200:

        bookings = response.json()

        if bookings:

            df = pd.DataFrame(bookings)

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning(
                "No Bookings Found"
            )

    else:

        st.error(
            "Failed to fetch bookings"
        )'''