import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df_left = pd.DataFrame(employees['employee_id'])
    df_right = employees[(employees['employee_id']%2==1) & (employees['name'].str[0] != 'M')]
    df_right = df_right[['employee_id', 'salary']].rename(columns ={'salary': 'bonus'})
    df_right = df_right.fillna(0)
    df = pd.merge(df_left, df_right, on='employee_id', how = 'left').sort_values(by=['employee_id'])
    return df.fillna(0)
