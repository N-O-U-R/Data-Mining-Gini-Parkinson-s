import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
data = pd.read_csv('parkinsons.data')  # Make sure to replace with the correct path
features = data.drop(['name', 'status'], axis=1)
labels = data['status']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Create a Decision Tree model using the Gini index
model = DecisionTreeClassifier(criterion='gini')
model.fit(X_train, y_train)

def make_prediction(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0]
