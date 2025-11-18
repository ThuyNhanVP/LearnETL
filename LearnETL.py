import pandas as pd

# Extract: đọc dữ liệu
titanic_data = pd.read_csv('titanic.csv')

# Transform: xử lý giá trị thiếu ở cột Age
mean_age = titanic_data['Age'].mean()
titanic_data['Age'].fillna(mean_age, inplace=True)

# Tạo cột nhóm tuổi
def age_group(age):
    if age < 12:
        return 'Child'
    elif age < 18:
        return 'Teenager'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

titanic_data['AgeGroup'] = titanic_data['Age'].apply(age_group)

# Load: lưu dữ liệu ra file mới
titanic_data.to_csv('titanic_transformed.csv', index=False)
