import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('parkinsons.data')  # Make sure to replace with the correct path
features = data.drop(['name', 'status'], axis=1)
labels = data['status']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2,random_state=42)

# Create a Decision Tree model using the Gini index
model = DecisionTreeClassifier(criterion='gini')
model.fit(X_train, y_train)

def make_prediction(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0]

def plot_decision_tree():
    # Predict on test set and calculate accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_percent = accuracy * 100  # Convert to percentage

    # Plot the decision tree
    plt.figure(figsize=(20,15))  # Adjust the figure size if necessary
    plot_tree(model, filled=True, feature_names=features.columns, class_names=['Healthy', 'Parkinson'])
    plt.title(f"Decision Tree for Parkinson's Disease Prediction\nAccuracy: {accuracy_percent:.2f}%", fontsize=16)
    plt.show()

if __name__ == "__main__":
    plot_decision_tree()
