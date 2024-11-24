import streamlit as st
import random

# Constants
NUM_ROUNDS: int = 5  # Type hint for number of rounds

def main() -> None:
    # Title of the app
    st.title("High-Low Game")
    st.write('--------------------------------')

    # Initialize session state variables if they don't exist
    if 'score' not in st.session_state:
        st.session_state.score = 0  
    if 'round' not in st.session_state:
        st.session_state.round = 1  
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False  

    # Display current round and score
    st.write(f"Round {st.session_state.round}")
    st.write(f"Current Score: {st.session_state.score}")

    # Exit Game button (this button will be available at any point in the game)
    if st.button("Exit Game"):
        # When the game is exited, display the current score and stop further interactions
        st.session_state.game_over = True
        st.write(f"You have exited the game. Your final score is {st.session_state.score}.")
        return

    # If game is over, show the final score and provide an exit button
    if st.session_state.game_over:
        st.write(f"Game Over! Your final score is {st.session_state.score}")
        if st.button('Exit Game'):
            st.session_state.game_over = False
            st.session_state.round = 1
            st.session_state.score = 0
        return

    # Generate random numbers for the round
    computer_num: int = random.randint(1, 100)  # Type hint for computer's number
    your_num: int = random.randint(1, 100)  # Type hint for user's number

    # Display the user's number
    st.write(f"Your number is: {your_num}")

    # Dropdown to select "higher" or "lower"
    choice: str = st.selectbox("Do you think your number is higher or lower than the computer's?", ["higher", "lower"])

    # Button to submit the guess
    if st.button("Submit Guess"):
        # Type casting: choice is a string, but we'll use it directly as it's needed in the if statements
        higher_and_correct: bool = choice == "higher" and your_num > computer_num
        lower_and_correct: bool = choice == "lower" and your_num < computer_num

        # Check if the guess is correct and update score
        if higher_and_correct or lower_and_correct:
            st.write(f"You were right! The computer's number was {computer_num}")
            st.session_state.score += 1
        else:
            st.write(f"Aww, that's incorrect. The computer's number was {computer_num}")

        # Move to next round
        st.session_state.round += 1

    # Button to continue playing after each guess
    if st.button("Continue Playing"):
        st.session_state.game_over = False

# Run the app
if __name__ == "__main__":
    main()
