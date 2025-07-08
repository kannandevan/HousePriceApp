# 1. Import the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Load the dataset
data = pd.read_csv('USA_Housing.csv')

# 3. Prepare the Data
X = data[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
          'Avg. Area Number of Bedrooms', 'Area Population']]
y = data['Price']

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# 5. Create and Train the AI Model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Save the Trained Model
joblib.dump(model, 'house_price_model.pkl')

print("Model trained and saved successfully!")

# --- NEW CODE TO CREATE AND SAVE THE GRAPH ---

# 7. Create a scatter plot
plt.figure(figsize=(10, 6)) # Set the figure size
sns.scatterplot(x=data['Avg. Area Income'], y=data['Price'])
plt.title('House Price vs. Average Area Income')
plt.xlabel('Average Area Income')
plt.ylabel('Price')
plt.grid(True)

# 8. Save the plot to the 'static' folder
plt.savefig('static/income_vs_price.png')

print("Graph saved successfully as static/income_vs_price.png!")