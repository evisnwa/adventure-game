import streamlit as st
from PIL import Image

import streamlit as st

st.header("ADVENTURE GAME")

img = Image.open('13.jpeg')
st.image(img)



# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 'start'

if 'choice1' not in st.session_state:
    st.session_state.choice1 = ''

if 'choice2' not in st.session_state:
    st.session_state.choice2 = ''

# Function to reset the game
def reset_game():
    st.session_state.step = 'start'
    st.session_state.choice1 = ''
    st.session_state.choice2 = ''

# Function to handle first choice
def handle_choice1(choice):
    st.session_state.choice1 = choice
    if choice == 'left':
        st.session_state.step = 'left_path'
    elif choice == 'right':
        st.session_state.step = 'right_path'
    else:
        st.session_state.step = 'invalid_choice1'

# Function to handle second choice
def handle_choice2(choice):
    st.session_state.choice2 = choice
    if st.session_state.choice1 == 'left':
        if choice == 'sword':
            st.session_state.step = 'left_sword'
        elif choice == 'potion':
            st.session_state.step = 'left_potion'
        else:
            st.session_state.step = 'invalid_choice2_left'
    elif st.session_state.choice1 == 'right':
        if choice == 'enter':
            st.session_state.step = 'right_enter'
        elif choice == 'continue':
            st.session_state.step = 'right_continue'
        else:
            st.session_state.step = 'invalid_choice2_right'

# Start of the game
if st.session_state.step == 'start':
    st.write("You find yourself in a forest. You can see a path to the left and a path to the right.")
    st.write("Which way do you go, left or right?")
    img = Image.open('1.jpeg')
    st.image(img)

    choice1 = st.radio("Choose a path", ('left', 'right'))
    if st.button('Submit'):
        handle_choice1(choice1)

# Left path
if st.session_state.step == 'left_path':
    st.write("\nYou walk to the left path and encounter a friendly elf.")
    st.write("The elf offers you a choice between a magic sword and a health potion.")
    choice2 = st.radio("Choose an item", ('sword', 'potion'))
    img = Image.open('5.jpeg')
    st.image(img)
    if st.button('Submit', key='left'):
        handle_choice2(choice2)

# Right path
if st.session_state.step == 'right_path':
    st.write("\nYou walk down the right path and find a mysterious cave.")
    img = Image.open('8.jpeg')
    st.image(img)
    st.write("Do you want to enter the cave or continue walking?")
    choice2 = st.radio("Choose an action", ('enter', 'continue'))
    if st.button('Submit', key='right'):
        handle_choice2(choice2)

# Left path results
if st.session_state.step == 'left_sword':
    st.write("\nYou choose the magic sword and it strikes the elf in the chest.")
    st.write("The elf is now dead.")
    st.write("You have killed a friendly elf. You lose!")
    img = Image.open('6.jpeg')
    st.image(img)

    img = Image.open('12.jpeg')
    st.image(img)
     
    if st.button('Restart'):
        reset_game()

if st.session_state.step == 'left_potion':
    st.write("\nYou drink the health potion and the elf is now healthy.")
    st.write("You have saved the elf. You win!")
    img = Image.open('7.jpeg')
    st.image(img)
    if st.button('Restart'):
        reset_game()

# Right path results
if st.session_state.step == 'right_enter':
    st.write("\nYou enter the cave and find a sleeping dragon.")
    img = Image.open('9.jpeg')
    st.image(img)
    st.write("You find a treasure behind the sleeping dragon.")
    st.write("You are rewarded for your bravery. You win!")
    img = Image.open('11.jpeg')
    st.image(img)
    if st.button('Restart'):
        reset_game()

if st.session_state.step == 'right_continue':
    st.write("\nYou are kidnapped by a wild eagle and dumped in a volcano.")
    img = Image.open('2.jpg')
    st.image(img)

    st.write("You lose!") 

    img = Image.open('12.jpeg')
    st.image(img)

    if st.button('Restart'):
        reset_game()

# Invalid choices
if st.session_state.step == 'invalid_choice1':
    st.write("Your choice is not a valid choice. You lose!")
    img = Image.open('12.jpeg')
    st.image(img)
    if st.button('Restart'):
        reset_game()

if st.session_state.step == 'invalid_choice2_left':
    st.write("Your choice is not a valid choice. You lose!")
    img = Image.open('12.jpeg')
    st.image(img)
    if st.button('Restart'):
        reset_game()

if st.session_state.step == 'invalid_choice2_right':
    st.write("Your choice is not a valid choice. You lose!")
    img = Image.open('12.jpeg')
    st.image(img)
    if st.button('Restart'):
        reset_game()

