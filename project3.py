import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the data with correct delimiter
data = pd.read_csv(r"C:\\Users\\dhanu\\Downloads\\bank-additional-full.csv", delimiter=';')

# Display basic information about the data
print(data.head())
print(data.info())

# Identify categorical and numerical columns
categorical_columns = data.select_dtypes(include=['object']).columns.tolist()
numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Ensure 'y' column is treated properly
if 'y' in categorical_columns:
    categorical_columns.remove('y')

print("Categorical columns:", categorical_columns)
print("Numerical columns:", numerical_columns)

# Define feature and target variables
X = data.drop(columns='y')
y = data['y'].apply(lambda x: 1 if x == 'yes' else 0)

# Define preprocessor
preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_columns)],
    remainder='passthrough'
)

# Create and fit the pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier(random_state=42))
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

pipeline.fit(X_train, y_train)

# Predict and evaluate
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(report)
print("Confusion Matrix:")
print(conf_matrix)

# Extract the preprocessor and classifier from the pipeline
model = pipeline.named_steps['classifier']
preprocessor = pipeline.named_steps['preprocessor']

# Transform training data to get feature names
X_transformed = preprocessor.transform(X_train)
feature_names = preprocessor.get_feature_names_out()

# Plot the tree
plt.figure(figsize=(20,10))
plt.title("Decision Tree")
plot_tree(model, filled=True, feature_names=feature_names, class_names=['No', 'Yes'])
plt.show()
