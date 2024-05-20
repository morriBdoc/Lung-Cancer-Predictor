import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def check_val(val):
	if type(val) != int:
		return "Please enter a valid value"
	elif val < 1 or val > 2:
		return "Please enter a valid value"
	else:
		pass


data = pd.read_csv("survey lung cancer.csv")

features = ['AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'CHRONIC DISEASE', 'FATIGUE', 'ALLERGY', 'WHEEZING', 'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH', 'CHEST PAIN']

X = data[features]
y = data["LUNG_CANCER"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

score = model.score(X_test, y_test)

print(f"Model Accuracy: {round(score * 100, 2)}%")

print("Please enter the following details (1 for NO and 2 for YES)\n")
age = int(input("How old are you: "))

if age < 18:
	print("You are not eligible to test for Lung Cancer")
	exit()
elif age > 80:
	print("You are not eligible to test for Lung Cancer")
	exit()
elif type(age) != int:
	print("Please enter a valid age")
	exit()
else:
	print("You are eligible to test for Lung Cancer")

smoking = int(input("Are you a smoker: "))
check_val(smoking)
yellow_fingers = int(input("Do you have yellow fingers: "))
check_val(yellow_fingers)
anxiety = int(input("Do you have anxiety: "))
check_val(anxiety)
chronic_disease = int(input("Do you have a chronic disease: "))
check_val(chronic_disease)
fatigue = int(input("Do you experience fatigue: "))
check_val(fatigue)
allergy = int(input("Do you have an allergy: "))
check_val(allergy)
wheezing = int(input("Do you have wheezing: "))
check_val(wheezing)
alcohol_consuming = int(input("Are you consuming alcohol: "))
check_val(alcohol_consuming)
coughing = int(input("Do you have a cough: "))
check_val(coughing)
shortness_of_breath = int(input("Do you have shortness of breath: "))
check_val(shortness_of_breath)
chest_pain = int(input("Do you have chest pain: "))
check_val(chest_pain)

prediction = model.predict([[age, smoking, yellow_fingers, anxiety, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, chest_pain]])

print("\nThis test is just for experimental use and does not represent a medical diagnosis. If you think you have Lung Cancer, please contact your doctor.\n")
if prediction[0] == "YES":
	print("Based on the information given, you might have Lung Cancer")
else:
	print("Based on the information given, it does not seem like you have Lung Cancer")
