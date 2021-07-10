import Extract as et
import pandas as pd
access_token = et.accesstoken('c0ab671cf54e43ce914a8aa5b116f8d6','392dbc90b09046339e0a3816d79433cd')
df1=et.get_track_data(access_token)


def getdataglobal():
    return(et.get_track_data(access_token))
    


def check_if_valid_data(df1):
    # Check if dataframe is empty
    if df1.empty:
        print("No songs extracted. failure...")
        return False 

    # Primary Key Check
    if pd.Series(df1['id']).is_unique:
        pass
    else:
        raise Exception("Primary Key check is violated")

    # Check for nulls
    if df1.isnull().values.any():
        raise Exception("Null values found")
    
if __name__ == "__main__":    
    # Validate
    if check_if_valid_data(df1):
        print("Data valid, proceed to Load stage")
