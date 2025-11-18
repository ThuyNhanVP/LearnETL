import pandas as pd

# Extract: đọc dữ liệu
def Extract_data(filename):
    return pd.read_csv(filename)

# Transform: xử lý giá trị thiếu ở cột Age
def Transform_data(df):
    titanic_data = df.copy()
    mean_age = titanic_data['Age'].mean()
    titanic_data['Age'].fillna(mean_age, inplace=True)
    
    # Áp dụng hàm age_group để tạo cột mới
    titanic_data['AgeGroup'] = titanic_data['Age'].apply(age_group)
    
    return titanic_data
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

# Load: lưu dữ liệu ra file mới
def load_data(df, filename):
    df.to_csv(filename, index=False)

# Chạy ETL
if __name__ == "__main__":
    # Bước 1: Extract
    data = Extract_data('titanic.csv')
    
    # Bước 2: Transform
    transformed_data = Transform_data(data)
    
    # Bước 3: Load
    load_data(transformed_data, 'titanic_transformed.csv')



