# Parkinson's Disease Prediction using Decision Tree Classifier

## Introduction
This repository contains a Python project that utilizes a Decision Tree Classifier to predict the presence of Parkinson's disease in individuals based on various vocal measurements. The model is trained on a dataset comprising biomedical voice measurements from people with and without Parkinson's disease.

## Features
- Utilizes a Decision Tree Classifier with the Gini index.
- Predicts Parkinson's disease status based on voice measurement inputs.
- Includes a Streamlit-based user interface for easy interaction.
- Provides a clear visualization of the decision tree for understanding the prediction logic.

## Installation
To run this project, you will need Python installed on your system. The project is built using Python 3.x. Follow these steps to set up the project:

1. **Clone the Repository**

 - git clone https://github.com/N-O-U-R/Data-Mining-Gini-Parkinson-s.git
 - cd Data-Mining-Gini-Parkinson-s
 
2. **Set Up a Virtual Environment** (Optional but recommended)
 python -m venv venv

## Windows
v- env\Scripts\activate

## Unix or MacOS
- source venv/bin/activate

3. **Install Required Packages**
- pip install -r requirements.txt


## Running the Application
To run the Streamlit app, execute:

- streamlit run app.py

The application should now be running on your local server (typically `http://localhost:8501`). Open the link in a web browser to interact with the application.

## Usage
The user interface allows you to input various vocal measurements. Once you provide all the required inputs, the application will use the pre-trained decision tree model to predict whether these measurements indicate the presence of Parkinson's disease.

## Contributing
Contributions to this project are welcome! To contribute, please fork the repository, make your changes, and create a pull request.


