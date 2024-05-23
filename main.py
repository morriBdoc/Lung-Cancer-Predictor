import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def add_new_data():
	file = open("survey lung cancer.csv", "a")
	file.write(f"{gender},{age},{smoking},{yellow_fingers},{anxiety},{peer_pressure},{chronic_disease},{fatigue},{allergy},{wheezing},{alcohol_consuming},{coughing},{shortness_of_breath},{swallowing_difficulty},{chest_pain},{prediction[0]}\n")
	file.close()


data = pd.read_csv("survey lung cancer.csv")

features = ['AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE', 'CHRONIC DISEASE', 'FATIGUE', 'ALLERGY', 'WHEEZING', 'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH', 'SWALLOWING DIFFICULTY', 'CHEST PAIN']

X = data[features]
y = data["LUNG_CANCER"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("\nPlease note that even though this test is anonymous, it still saves your answers in the data for better models.")
print("\nAlso note that this test does not represent a medical diagnosis. If you think you have Lung Cancer, please contact your doctor.")

print(f"\nModel Accuracy: {round(accuracy * 100, 2)}%")

gender = input("\nWhat is your gender (M for Male and F for Female): ").upper()

while gender != "M" and gender != "F":

	print("Only M and F are accepted")
	gender = input("What is your gender: ").upper()

else:

	print("\nPlease enter the following details (1 for NO and 2 for YES)\n")

	try:

		age = int(input("How old are you: "))

		if age < 18 or age > 80:
			print("You are not eligible for this test")
			exit()
		else:
			print("You are eligible for this test\n")

		smoking = int(input("Are you a smoker: "))
		yellow_fingers = int(input("Do you have yellow fingers: "))
		anxiety = int(input("Do you have anxiety: "))
		peer_pressure = int(input("Have you experience peer pressure: "))
		chronic_disease = int(input("Do you have a chronic disease: "))
		fatigue = int(input("Do you experience fatigue: "))
		allergy = int(input("Do you have an allergy: "))
		wheezing = int(input("Do you have wheezing: "))
		alcohol_consuming = int(input("Are you consuming alcohol: "))
		coughing = int(input("Do you have a cough: "))
		shortness_of_breath = int(input("Do you have shortness of breath: "))
		swallowing_difficulty = int(input("Do you have difficulty swallowing: "))
		chest_pain = int(input("Do you have chest pain: "))

	except ValueError:

		print("Please only enter numbers")
		exit()

	prediction = model.predict([[age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]])

	if accuracy * 100 > 90:
		add_new_data()
	else:
		pass

	print("\nRemember that this test is just for experimental use and does not represent a medical diagnosis. If you think you have Lung Cancer, please contact your doctor.\n")

	if prediction[0] == "YES":
		print("Based on the information given, you might have Lung Cancer")
	else:
		print("Based on the information given, it does not seem like you have Lung Cancer")
