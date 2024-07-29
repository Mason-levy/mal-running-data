import pandas as pd
from datetime import datetime
from pathlib import Path
from src.api_methods import get_methods
from src.api_methods import authorize
from src.data_preprocessing import main as data_prep

# Constants
ACTIVITIES_PER_PAGE = 200
PAGE_NUMBER = 1

GET_ALL_ACTIVITIES_PARAMS = {
    'per_page': ACTIVITIES_PER_PAGE,
    'page': PAGE_NUMBER
}

def main():
    # Get the access token
    token = authorize.get_access_token()
    
    # Fetch activity and athlete data
    activitydata = get_methods.access_activity_data(token, params=GET_ALL_ACTIVITIES_PARAMS)
    athletedata = get_methods.access_athlete_data(token, params=GET_ALL_ACTIVITIES_PARAMS)
    
    # Preprocess the data
    activitydf = data_prep.preprocess_data(activitydata)
    athletedf = data_prep.preprocess_data(athletedata)
    
    # Create data directory if it doesn't exist
    data_dir = Path('data')
    data_dir.mkdir(parents=True, exist_ok=True)
    
    
    # Save data to CSV files
    activitydf.to_csv(data_dir / f'my_activity_data.csv', index=False)
    athletedf.to_csv(data_dir / f'my_athlete_data.csv', index=False)
    
    # # Process and save splits data
    # if getsplits(activitydf):
    #     print("Splits data processed and saved successfully.")
    
    return activitydf

# def getsplits(activities):
#     ids = activities['id']
#     all_splits = []  # Initialize an empty list to collect all activity splits

#     for id in ids:
#         token = authorize.get_access_token()
#         splitdata = get_methods.access_activity_splits(id, token)
        
#         # Preprocess the split data
#         activitydf = data_prep.preprocess_data(splitdata)
        
#         # Add the processed data to the list
#         all_splits.append(activitydf)
    
#     # Concatenate all dataframes in the list into a single dataframe
#     all_splits_df = pd.concat(all_splits, ignore_index=True)
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
#     # Export the dataframe to a CSV file
#     data_dir = Path('data')
#     all_splits_df.to_csv(data_dir / f'my_splits_data_{timestamp}.csv', index=False)
    
#     return True

if __name__ == '__main__':
    main()