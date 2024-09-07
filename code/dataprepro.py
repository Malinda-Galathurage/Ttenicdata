import pandas as pd
file_path = '../data/malinda_data.csv'
data = pd.read_csv(file_path)
data.head()

from sklearn.preprocessing import LabelEncoder, StandardScaler

data['Age'].fillna(data['Age'].median(), inplace=True)

data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

data.drop(columns=['Cabin'], inplace=True)

label_encoder = LabelEncoder()


data['Sex'] = label_encoder.fit_transform(data['Sex'])


data['Embarked'] = label_encoder.fit_transform(data['Embarked'])

data.drop(columns=['PassengerId', 'Name', 'Ticket'], inplace=True)


scaler = StandardScaler()


data[['Fare', 'Age']] = scaler.fit_transform(data[['Fare', 'Age']])

output_file_path = '../data/preprocessed_malinda_data.csv'
data.to_csv(output_file_path, index=False)


print("Job DONE")

