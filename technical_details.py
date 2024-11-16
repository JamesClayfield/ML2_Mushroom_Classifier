import streamlit as st
import time
import numpy as np
import pandas as pd

	# Read the jupyter notebook to be downloadable through the download button
with open("individual.ipynb", "rb") as file:
    notebook_data = file.read()




def technical_details():
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


	st.title('Technical Details')


	st.header("Model Training")
	st.markdown("""
The process of training the Random Forest model and the methodology applied can be found by downloading the following notebook:


		""")

	# Display download button
	st.download_button(
	    label="Download Explanatory Jupyter Notebook",
	    data=notebook_data,
	    file_name='individual.ipynb',
	    mime='application/json'
	)
	st.header("Model Performance")
	st.markdown("""
 Eating a poisonous mushroom, classified as safe could have fatal consequences. As such the most important metric for this model is recall in order to 
 minimze false negatives.

As can be seen from the below confusion matrices, the model classifies perfectly on train and test:
		""")
		# Create two columns
	col1, col2 = st.columns(2)

	# Add content to the first column
	with col1:
	    st.image("Train_Matrix.png", caption="Training Confusion Matrix")

	# Add content to the second column
	with col2:
	    st.image("Test_Matrix.png", caption="Test Confusion Matrix")


		##Provide here information about model performance and they key metrics.


	st.header("Model Selection")
	st.markdown("""
For the Mushroom Edibility Classifier, the Random Forest Classifier was chosen. This is a type of ensemble algorithm. The algorithm works by creating a set
of decision trees and combining their predicitions to improve accurancy and reduce overfitting. The random forest algorithm is a bagging technique 
as it combines multiple models into one to obtain a better prediction.

#### How Random Forest Works

##### 1) Building Multiple Decision Trees with Bootstrapping
Each decision tree in the forest is constructed using a different random subset of the training data. Each one of these subsets is created using **Bootstrapping**.
Bootstrapping is a bagging technique whereby datapoints are randomly sampled to create diverse training subsets for each tree. This ensures that every tree in 
a random forest is trained on a unique part of the data. 

##### 2) Random Feature Selection at Every Split (Bagging)
As the Random Forest Algorithm trains each decision tree, it randomly selects a subset of features from the features available for each split in the tree. 
The use of different features further increases the diversity of the trees by reducing correlation between them. As such the ensemble is more robust, preventing 
any single feature from dominating the model.

##### 3) Trees Grow until Stopping Criterion is Reached
In the forest, each tree is allowed to grow until a stopping criteria is reached. These include minimum number of samples per node, maximum depth etc.. 
These hyperparameters can be experimented with and the best identified through hyperparameter tuning methods like grid and random search.

##### 4) Aggregation and Prediction
Once all trees are trained the Random forest Algorithm conbines them through aggregation. Each tree then "votes" for a class. The forest's final prediction is 
the class that receives the majority vote across all trees.


#### Benefits of Random Forest
The Random Forest algorithm was selected for the following key reasons:

##### Reduced Overfitting
The aggregation of diverse decision trees, with the output being a majority vote or averaging, reduces individual biases 
and errors, reducing the risk of overfitting. This provides a more generalized, robust and thus accurate model.
risk of overfitting.

##### Inate Feature Selection
The random forest algorithm employs a technique called **"bagging"**. This refers to where at each split in the tree, 
only a certain number of features is considered. This is controlled by the ***max_features*** parameter in Sci-kit learn. As such the model 
inherently reduces the dominance of individual features, enabling a diverse set of trees and feature combinations.

##### Feature Importance
Random forest provide feature importance score after training based on how effectively and 
often each feature is used across all trees.

##### Handling of Higly Dimensional Data
Random forest algorithms are effective at handling datasets with high dimensionality, such as the 96 OHE encoded 
variable dataset in our example. This makes them robust to irrelevant features.

		""", unsafe_allow_html=True)
