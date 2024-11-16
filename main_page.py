import streamlit as st
import time
import pickle
import numpy as np
import pandas as pd
from streamlit_extras.let_it_rain import rain

#Importing the trained ML models and One Hot Encoder

pickle_in = open('random_forest_full.pkl', 'rb')
full_classifier = pickle.load(pickle_in)

pickle_in = open('random_forest_short.pkl', 'rb')
simple_classifier = pickle.load(pickle_in)

pickle_in = open('OHE_Encoder.pkl', 'rb')
encoder = pickle.load(pickle_in)

#Defining the Function that makes emojis rain

def emoji_rain_safe():
    rain(
        emoji="😋",
        font_size=64,
        falling_speed=3,
        animation_length="1",
    )
def emoji_rain_unsafe():
    rain(
        emoji="🍄☠️",
        font_size=64,
        falling_speed=3,
        animation_length="1",
    )

#Defining the Function showing the input fields for the "Full Model". For each feature a select box is created.
#The input in the selectbox is stored in a variable and returned. These variables are later one hot encoded using 
#the OHE function previously imported.

def full_model_toggle():
	col1, col2 = st.columns(2)
	with col1:
		cap_shape = st.selectbox('Cap Shape', ("b", "c", "x", "f", "k", "s"))
		cap_surface = st.selectbox('Cap Surface', ("f", "g", "y", "s"))
		cap_color = st.selectbox('Cap Color', ("n", "b", "c", "g", "r", "p", "u", "e", "w", "y"))
		bruises = st.selectbox('Bruises', ("t", "f"))
		odor = st.selectbox('Odor', ("a", "l", "c", "y", "f", "m", "n", "p", "s"))
		gill_attachment = st.selectbox('Gill Attachment', ("a", "d", "f", "n"))
		gill_spacing = st.selectbox('Gill Spacing', ("c", "w", "d"))
		gill_size = st.selectbox('Gill Size', ("b", "n"))
		gill_color = st.selectbox('Gill Color', ("k", "n", "b", "h", "g", "r", "o", "p", "u", "e", "w", "y"))
		stalk_shape = st.selectbox('Stalk Shape', ("e", "t"))
		stalk_root = st.selectbox('Stalk Root', ("b", "c", "u", "e", "z", "r", "?"))

	with col2:	
		stalk_surface_above_ring = st.selectbox('Stalk Surface Above Ring', ("f", "y", "k", "s"))
		stalk_surface_below_ring = st.selectbox('Stalk Surface Below Ring', ("f", "y", "k", "s"))
		stalk_color_above_ring = st.selectbox('Stalk Color Above Ring', ("n", "b", "c", "g", "o", "p", "e", "w", "y"))
		stalk_color_below_ring = st.selectbox('Stalk Color Below Ring', ("n", "b", "c", "g", "o", "p", "e", "w", "y"))
		veil_type = st.selectbox('Veil Type', ("p", "u"))
		veil_color = st.selectbox('Veil Color', ("n", "o", "w", "y"))
		ring_number = st.selectbox('Ring Number', ("n", "o", "t"))
		ring_type = st.selectbox('Ring Type', ("c", "e", "f", "l", "n", "p", "s", "z"))
		spore_print_color = st.selectbox('Spore Print Color', ("k", "n", "b", "h", "r", "o", "u", "w", "y"))
		population = st.selectbox('Population', ("a", "c", "n", "s", "v", "y"))
		habitat = st.selectbox('Habitat', ("g", "l", "m", "p", "u", "w", "d"))

	return [cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment,
	gill_spacing, gill_size, gill_color, stalk_shape, stalk_root,
	stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring,
	stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type,
	spore_print_color, population, habitat]


#This function collects input data from the user for the simplified model and converts it into a compatible dataframe that can be 
#input into the ML model to receive an output. The format of this DF could be considered to already be one-hot-encoded due to 
#its binary nature. As such the imported OHE model will not be applied to this dataframe.
def simple_model_toggle():

	#Defining list of columns that are used below to initialize the dataframe.
	columns = ['cap-color_y', 
	'bruises_t', 
	'odor_l', 
	'odor_n', 
	'odor_p', 
	'gill-size_n',
	'stalk-root_c', 
	'stalk-surface-below-ring_y', 
	'spore-print-color_r',
	'spore-print-color_u']

	#A database with all zeros is initialized.
	input_df = pd.DataFrame(np.zeros((1, len(columns))), columns=columns) 

	#Based on the selection of the box, the respective column in the dataframe is set to 1.
	#This is done for all 7 unique variables in the model. The modified "input_df" is returned.
	spore_print_color = st.selectbox("Spore Print Color", ("Purple (u)", "Green (r)","Other"))
	if spore_print_color == 'Purple (u)':
		input_df['spore-print-color_u'] = 1
	elif spore_print_color == 'Green (r)':
		input_df['spore-print-color_r'] = 1

	odor = st.selectbox("Odor", ("Anise (l)", "None (n)", "Pungent (p)", "Other"))
	if odor == "Anise (l)":
		input_df["odor_l"] = 1
	elif odor == "None (n)":
		input_df["odor_n"] = 1
	elif odor == "Pungent (p)":
		input_df["odor_p"] = 1

	cap_color = st.selectbox("Cap Color", ("Yellow (y)", "Other"))
	if cap_color == "Yellow (y)":
		input_df["cap-color_y"] = 1

	stalk_surface_below_ring = st.selectbox("Stalk surface below ring", ("Scaly (y)", "Other"))
	if stalk_surface_below_ring == "Scaly (y)":
		input_df["stalk-surface-below-ring_y"] =1

	stalk_root = st.selectbox("Stalk root", ("Club (c)", "Other"))
	if stalk_root == "Club (c)":
		input_df["stalk-root_c"] = 1

	gill_size = st.selectbox("Gill size", ("Narrow (n)", "Broad (b)"))
	if gill_size == "Narrow (n)":
		input_df["gill-size_n"] = 1

	bruises = st.selectbox("Does the Mushroom show bruises?", ("Yes", "No"))
	if bruises == "Yes":
		input_df["bruises_t"] == 1

	return input_df


#This function runs the prediction using the full_classifer using the inputs from the full_model_toggle() function.
def full_prediction(encoded_input):
	prediction = full_classifier.predict(encoded_input)
	if prediction == 0:
		pred = 'Not Poisonous'
	else:
		pred = 'Poisonous'
	return pred

#This function runs the preduction using the simple_classifier using the inputs from the simple_model_toggle() function.
def simple_prediction(input_df):
	prediction = simple_classifier.predict(input_df)
	if prediction == 0:
		pred = 'Not Poisonous'
	else:
		pred = 'Poisonous'
	return pred

#This function combines all the above functions to visualize the main page when it is selected in the sidebar in app.py
def main_page():
	st.image("mushrooms-Banner.jpeg", use_column_width=True)
	
	# This CSS code sets the background color of the page and forces lightmode to be used in the browser. This prevents the font color from changing at night.
	st.markdown(
		"""
		<style>
			/* Force light mode */
        	:root {
        	color-scheme: light;
			/* Change the background color of the main content */
			[data-testid="stAppViewContainer"] {
				background-color: #ffeed6; /* Set to any color you prefer */

		    /* Style for the dropdown menu */
		    .stSelectbox .css-26l3qy-menu {
		        background-color: #F4E1C4; /* Background color for the dropdown menu */
		        color: black; /* Text color for options */
		    }


			}
		</style>
		""",
		unsafe_allow_html=True
	)


#The below pieces of code provide the main body of text of information for the user.
	st.title("🍄Mushroom Edibility Classifier🍄‍🟫")
	st.write("""

Have you ever wondered if you could eat a random mushroom in a forest? The Mushroom Edibility Classifier (MEC) employs
a sophisticated Random Forest Classification algorithm to determine whether the mushroom you have found is indeed
poisonous or not.

The Mushroom Edibility Classifier uses data from the Audobon Society Field Guide and can be used to identify the edibility 
of 23 species of gilled mushrooms in the Agaricus and Lepiota Family. More information about the dataset can be found 
[here](https://archive.ics.uci.edu/ml/datasets/Mushroom).

#### *"You can eat every mushroom on earth, however some you can eat only once."* - A wise man.

In light of this proverb highlighting the dangers of unknown mushrooms, **DO NOT** rely on this model to determine mushroom edibility.
Please consult an expert for reliable information.

	""")

	st.subheader("Please select a Model:")
	st.write("""
The MEC provides two separate models for classifying gilled mushrooms based on edibility. 

The **Simplified Model** was trained using cutting edge feature selection algorithms with the aim of creating a model requiring less input variables
but maintaining the same level of accuracy.

The **Full Model** uses all variables available
to make the most accurate classification possible.


		""")

	#This select box lets users to select which model they would like to use. This result is later passed used in the if-statement of the select button
	#so the app knows which prediction to run when the button is pressed.
	model_select = st.selectbox('Model Version', ('Simplified Model','Full Model'))

	st.subheader("Please enter the Mushroom's Characteristics")	

	#This container seems redundant. Can remove.

	if model_select == 'Full Model':
		inputs = full_model_toggle()
	else:
		inputs = simple_model_toggle()		

	# Depending on the Model Selection toggle, different functions should be called when the button is pressed.
	if st.button("Predict",use_container_width=True): 
	    if model_select == "Full Model":
	        encoded_inputs = encoder.transform([inputs])
	        result = full_prediction(encoded_inputs)

	        if result == 'Not Poisonous':
	            st.success('The Mushroom is {}!'.format(result))
	            emoji_rain_safe()
	        else:
	            st.error('The Mushroom is {}!'.format(result))
	            emoji_rain_unsafe()
	    elif model_select == "Simplified Model":
	        result = simple_prediction(inputs)

	        if result == 'Not Poisonous':
	            st.success('The Mushroom is {}!'.format(result))
	            emoji_rain_safe()
	        else:
	            st.error('The Mushroom is {}!'.format(result))
	            emoji_rain_unsafe()



def party_time():
	with st.container():
		balloon_select=st.selectbox('Is it Party Time?',
							['No', 'Yes']
							)
		while balloon_select=='Yes':
			st.balloons()
			time.sleep(1)
