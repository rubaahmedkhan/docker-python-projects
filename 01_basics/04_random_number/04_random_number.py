import random
import streamlit as st

# Constants
N_NUMBERS: int = 10  # Number of random numbers to generate
MIN_VALUE: int = 1   # Minimum value of the random numbers
MAX_VALUE: int = 100 # Maximum value of the random numbers

def main():
    """
    The main function to generate and display random numbers.
    """
    # Title for the Streamlit app
    st.title("Random Number Generator")
    
    # Button to generate random numbers when clicked
    if st.button("Generate Random Numbers"):
        random_numbers = []
        
        # Generate N_NUMBERS random integers between MIN_VALUE and MAX_VALUE
        for _ in range(N_NUMBERS):
            num = random.randint(MIN_VALUE, MAX_VALUE)
            random_numbers.append(num)
        
        # Convert the list of numbers to a string for display purposes
        random_numbers_str = ' '.join([str(x) for x in random_numbers])

        # Display the random numbers
        st.write("Here are your random numbers:")
        st.write(random_numbers_str)

if __name__ == '__main__':
    main()
