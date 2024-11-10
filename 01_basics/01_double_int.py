import streamlit as st


def double_numbers(curr_value: int) -> list:
   """Doubles the input number until it reachesor exceeds 100."""
   results = []

#  Continue doubling the number untill it reaches or exceeds 100
   while curr_value < 100:
         curr_value *= 2  # Correctly double the value
         results.append(curr_value)

   return results    # Return results after the loop finishes 
def main() -> None:
      st.title("Number Doubler")
      curr_value: int = st.number_input("Enter a number:", min_value=0)    
      if st.button("Double it!"):
          results = double_numbers(curr_value)

         # Display result 
          st.write("Doubled values:", " ".join(map(str, results)))
if __name__ == "__main__":
     main()        

