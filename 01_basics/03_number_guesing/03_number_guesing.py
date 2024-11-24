import random
import streamlit as st

def main():
    # Title for the Streamlit app
    st.title("Guess My Number Game")

    # Instructions for the user
    st.write("I am  thinking  of  a number  between  1 and 99...")

    # Generate the secret number only if it's not already generated
    if 'secret_number' not in st.session_state:
        st.session_state['secret_number'] = random.randint(1, 99)

    # Using Streamlit text input for user guesses
    guess = st.number_input("Enter your guess:", min_value=1, max_value=99, step=1, value=1)

    # Initial message
    if 'message' not in st.session_state:
        st.session_state['message'] = ''

    # Check user's guess
    if st.button("Submit"):
        if guess < st.session_state['secret_number']:
            st.session_state['message'] = "Your guess is too low."
        elif guess > st.session_state['secret_number']:
            st.session_state['message'] = "Your guess is too high."
        else:
            st.session_state['message'] = f"Congrats! The number was: {st.session_state['secret_number']}"
            # Reset the secret number for a new game
            st.session_state['secret_number'] = random.randint(1, 99)

    # Display the message
    st.write(st.session_state['message'])

# This line is required at the end of the python file to call the main() function.
if __name__ == '__main__':
    main()
