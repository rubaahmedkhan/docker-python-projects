# import random
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Title for the Streamlit app
# st.title("Enhanced Random Number Generator")

# # User inputs for number of random numbers, min and max range
# num_count = st.slider("How many numbers?", min_value=1, max_value=20, value=10)
# min_val = st.number_input("Minimum value:", min_value=1, max_value=100, value=1)
# max_val = st.number_input("Maximum value:", min_value=min_val, max_value=100, value=100)

# # Button to generate random numbers
# if st.button("Generate Random Numbers"):
#     random_numbers = [random.randint(min_val, max_val) for _ in range(num_count)]
    
#     # Display the random numbers
#     random_numbers_str = ' '.join([str(x) for x in random_numbers])
#     st.write("Here are your random numbers:")
#     st.write(random_numbers_str)

#     # Add statistics
#     st.write(f"Sum: {sum(random_numbers)}")
#     st.write(f"Average: {sum(random_numbers)/len(random_numbers):.2f}")
#     st.write(f"Max: {max(random_numbers)}")
#     st.write(f"Min: {min(random_numbers)}")
    
#     # Display histogram
#     fig, ax = plt.subplots()
#     ax.hist(random_numbers, bins=10, range=(min_val, max_val), color='blue', edgecolor='black')
#     st.pyplot(fig)
    
#     # Allow download as CSV
#     csv = pd.DataFrame(random_numbers, columns=["Random Numbers"]).to_csv(index=False)
#     st.download_button("Download CSV", csv, "random_numbers.csv", "text/csv")

#     # Track history of generated numbers
#     if 'history' not in st.session_state:
#         st.session_state['history'] = []
#     st.session_state['history'].append(random_numbers)
#     st.write("History of Generated Numbers:", st.session_state['history'])
