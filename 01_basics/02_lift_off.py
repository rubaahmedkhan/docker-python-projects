import streamlit as st

def countdown() -> None:
    """Print a countdown from 10 to 1 and out put 'Liftoff!'."""
    # Countdown numbers
    countdown_numbers = []

    # For loop for countdown from 10 to 1
    for i in range(10, 0, -1):
        countdown_numbers.append(str(i))  # Typecasting to string for display

    countdown_numbers.append("Liftoff!")  #  Adding 'Liftoff!' at the end 

    # Displaying the countdown
    st.write("Countdown:"," ".join(countdown_numbers))

def main() -> None:
    # Streamlit app title
    st.title("Spaceship Countdown") 

    # Button to start the countdown
    if st.button("Launch!") :
        countdown()  # Call countdown function on button click

if __name__ == "__main__" :
    main()      