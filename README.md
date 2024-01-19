## Introduction:
- The primary objective of this project is to provide farmers with easily comprehensible knowledge in their native language about crops, ngo and government schemes regarding farmers.
- The HomePage, NGOPage,India's Map View Of Crops which are grown mostly in each state and Crop-Recommendation System on our website allow users to access our content in their local tongue. There is also a language change option available on every page.

## Tech-Stack:
- HTML/CSS, Python-Django, Flask, ML Algorithms, scikit-learn, numpy, pandas, kaggle 

## Logic:
- The Crops-Recommendation-System is a Python-based project built on the Flask framework. It applies Machine Learning to determine the best crop to be grown in a specific condition. 
- The system uses a trained model (`model.pkl`) based on crop recommendation datasets retrieved from Kaggle.
- The system takes into user inputs for Nitrogen, Phosporus, Potassium, Temperature, Humidity, pH, and Rainfall. 
- These conditions are then processed by a preloaded machine learning model to predict a suitable crop for the given conditions.

```bash
N = int(request.form['Nitrogen'])
P = int(request.form['Phosporus'])
K = int(request.form['Potassium'])
temp = float(request.form['Temperature'])
humidity = float(request.form['Humidity'])
ph = float(request.form['pH'])
rainfall = float(request.form['Rainfall'])

feature_list = [N, P, K, temp, humidity, ph, rainfall]
single_pred = np.array(feature_list).reshape(1, -1)

prediction = loaded_model.predict(single_pred)
```

- Once a prediction is determined, the output is matched against a dictionary to retrieve the crop's name and deliver a readable and user-friendly output.
```bash
crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
             8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
             14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
             19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee
```

## Installation Guide:


