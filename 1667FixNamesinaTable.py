import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df1 = pd.DataFrame(users)
    df1['name'] = users['name'].str[1:].str.lower()
    df1['name'] = users['name'].str[0].str.upper() + df1['name']

    # # Apply the str.capitalize() function to fix the names
    # users['name'] = users['name'].str.capitalize()
    return pd.DataFrame(df1.sort_values(by=['user_id']))