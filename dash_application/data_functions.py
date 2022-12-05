import os

import pandas as pd
import requests
import datetime


# TOKEN = os.getenv('TOKEN')
TOKEN = 'a37062a36393726f3911dde489fe88e8'
PROJECT_ID = 2615506
headers = {
    'X-TrackerToken': f'{TOKEN}',
}
today = datetime.datetime.now()
now = today.isoformat()
print(now, type(now))

def story_transitions_data():
    response = requests.get('https://www.pivotaltracker.com/services/v5/projects/2615506/story_transitions',
                            headers=headers)
    #  получаем список изменений статусов историй
    # в виде: user_id, story_id, Datetime, new_status
    # итерируемся по списку - получаем дикты
    result_data_list = []
    for dict in response.json():
        temp_dict = {}
        temp_dict['user_id'] = dict['performed_by_id']
        temp_dict['story_id'] = dict['story_id']
        temp_dict['occurred_at'] = dict['occurred_at']
        temp_dict['new_status'] = dict['state']
        result_data_list.append(temp_dict)
    story_transitions_df = pd.DataFrame(result_data_list)
    story_transitions_df['occurred_at_dt'] = pd.to_datetime(story_transitions_df['occurred_at'],
                                                            # format='%Y-%m-%dT%H:%M:%SZ'
                                                            )
    # print(story_transitions_df)
    return story_transitions_df
# story_transitions()

def current_tasks():
    """список задач в Current"""

    params = {
        'date_format': 'millis',
        'accepted_before': now
    }

    response = requests.get(
        'https://www.pivotaltracker.com/services/v5/projects/2615506/stories',
        headers=headers,
        params=params
    )

    print(response.json())
current_tasks()
