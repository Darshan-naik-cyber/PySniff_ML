import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import argparse

# Parse the command-line argument for the data file path
parser = argparse.ArgumentParser()
parser.add_argument('--data_file', type=str, required=True, help='/upload')
args = parser.parse_args()

# Load data from the provided CSV file
data = pd.read_excel(args.data_file)


# Encode categorical features (IP addresses)
label_encoder = LabelEncoder()
data['Source_IP'] = label_encoder.fit_transform(data['Source IP'])
data['Destination_IP'] = label_encoder.fit_transform(data['Destination IP'])

X = data[['Source_IP', 'Destination_IP', 'Source Port', 'Destination Port']]
y = data['Source Port']  # Use 'Source Port' as the label column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Machine Learning Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate the Model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)

# Visualization 1: Confusion Matrix Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# Visualization 2: Source IP vs. Destination IP Scatterplot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Source_IP', y='Destination_IP', hue='Source Port', data=data)
plt.title('Source IP vs. Destination IP Scatterplot')
plt.show()

# Visualization 3: Source Port vs. Destination Port Scatterplot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Source Port', y='Destination Port', hue='Source IP', data=data)
plt.title('Source Port vs. Destination Port Scatterplot')
plt.show()

# Visualization 4: Source Port Distribution Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Source Port', data=data)
plt.title('Source Port Distribution')
plt.xlabel('Source Port')
plt.show()

# Visualization 5: Destination Port Distribution Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Destination Port', data=data)
plt.title('Destination Port Distribution')
plt.xlabel('Destination Port')
plt.show()

# Visualization 6: Pairplot of All Features
data_to_plot = data[['Source_IP', 'Destination_IP', 'Source Port', 'Destination Port']]
data_to_plot['Label'] = y
sns.pairplot(data_to_plot, hue='Label')
plt.title('Pairplot of All Features')
plt.show()

# Visualization 7: Countplot of Source IP
plt.figure(figsize=(10, 6))
sns.countplot(x='Source_IP', data=data)
plt.title('Count of Source IP')
plt.xlabel('Source IP')
plt.ylabel('Count')
plt.show()

# Visualization 8: Countplot of Destination IP
plt.figure(figsize=(10, 6))
sns.countplot(x='Destination_IP', data=data)
plt.title('Count of Destination IP')
plt.xlabel('Destination IP')
plt.ylabel('Count')
plt.show()

# Visualization 9: Countplot of Source Port
plt.figure(figsize=(10, 6))
sns.countplot(x='Source Port', data=data)
plt.title('Count of Source Port')
plt.xlabel('Source Port')
plt.ylabel('Count')
plt.show()

# Visualization 10: Countplot of Destination Port
plt.figure(figsize=(10, 6))
sns.countplot(x='Destination Port', data=data)
plt.title('Count of Destination Port')
plt.xlabel('Destination Port')
plt.ylabel('Count')
plt.show()

# Visualization 11: Violin Plot of Source Port vs. Destination Port
plt.figure(figsize=(10, 6))
sns.violinplot(x='Source Port', y='Destination Port', data=data)
plt.title('Violin Plot of Source Port vs. Destination Port')
plt.xlabel('Source Port')
plt.ylabel('Destination Port')
plt.show()

# Visualization 12: Swarm Plot of Source Port vs. Destination Port
plt.figure(figsize=(10, 6))
sns.swarmplot(x='Source Port', y='Destination Port', data=data, hue='Source_IP')
plt.title('Swarm Plot of Source Port vs. Destination Port')
plt.xlabel('Source Port')
plt.ylabel('Destination Port')
plt.show()

# Visualization 13: KDE Plot of Source Port vs. Destination Port
plt.figure(figsize=(10, 6))
sns.kdeplot(data=data[['Source Port', 'Destination Port']], shade=True)
plt.title('KDE Plot of Source Port vs. Destination Port')
plt.xlabel('Source Port / Destination Port')
plt.ylabel('Density')
plt.show()

# Visualization 14: Histogram of Source IP
plt.figure(figsize=(10, 6))
sns.histplot(data['Source_IP'], bins=20, kde=True)
plt.title('Histogram of Source IP')
plt.xlabel('Source IP')
plt.ylabel('Frequency')
plt.show()

# Visualization 15: Histogram of Destination IP
plt.figure(figsize=(10, 6))
sns.histplot(data['Destination_IP'], bins=20, kde=True)
plt.title('Histogram of Destination IP')
plt.xlabel('Destination IP')
plt.ylabel('Frequency')
plt.show()
