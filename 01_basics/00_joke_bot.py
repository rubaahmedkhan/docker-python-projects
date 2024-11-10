import streamlit as st

# constants for the bot 
prompt: str = "What do you want ? "
joke: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies:' because they had eggs'"
sorry: str = "Sorry I only tell jokes. "

def main() -> None:
    """Main function to run the joke bot."""

    # title for the web page
    st.title("Simple Joke Bot")

    # prompt to ask user input
    user_input = st.text_input(prompt)

    # If the user enters "Joke", display the joke
    if st.button("Submit"):
        if user_input.strip().lower() == "joke":
            st.success(joke)    # Display the joke
        else:
            st.error(sorry)     # Display sorry message

if __name__ == "__main__":
    main()          