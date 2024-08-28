import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # df = pd.DataFrame(users)
    df = patients[(patients['conditions'].str.len()>4)
    & ((patients['conditions'].str.contains(' DIAB1', regex=False) | (patients['conditions'].str[:5] == 'DIAB1')))]
    return df