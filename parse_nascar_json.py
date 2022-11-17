import pandas as pd
import json
from datetime import datetime
import time
from urllib.request import urlopen
from tqdm import tqdm

def nascar_series_identification(series:str):
    if str.lower(series) == str.lower("series_1") \
        or str.lower(series) == str.lower("series_2") \
        or str.lower(series) == str.lower("series_3"):
        return series
    elif str.lower(series) == str.lower("Cup") or \
        str.lower(series) == str.lower("Cup Series") or \
        str.lower(series) == str.lower("Strictly Stock") or \
        str.lower(series) == str.lower("Strictly Stock Division") or \
        str.lower(series) == str.lower("Grand National") or \
        str.lower(series) == str.lower("Grand National Division") or \
        str.lower(series) == str.lower("Winston") or \
        str.lower(series) == str.lower("Winston Cup") or \
        str.lower(series) == str.lower("Winston Cup Series") or \
        str.lower(series) == str.lower("Nextel") or \
        str.lower(series) == str.lower("Nextel Cup") or \
        str.lower(series) == str.lower("Nextel Cup Series") or \
        str.lower(series) == str.lower("Monster") or \
        str.lower(series) == str.lower("Monster Cup") or \
        str.lower(series) == str.lower("Sprint") or \
        str.lower(series) == str.lower("Sprint Cup") or \
        str.lower(series) == str.lower("Sprint Cup Series") or \
        str.lower(series) == str.lower("Monster Cup Series") or \
        str.lower(series) == str.lower("Monster Energy Cup") or \
        str.lower(series) == str.lower("Monster Energy Cup Series"):
        return "series_1"
    elif str.lower(series) == str.lower("Xfinity") or \
        str.lower(series) == str.lower("Xfinity Series") or \
        str.lower(series) == str.lower("Budweiser") or \
        str.lower(series) == str.lower("Budweiser Series") or \
        str.lower(series) == str.lower("Late") or \
        str.lower(series) == str.lower("Late Model") or \
        str.lower(series) == str.lower("Late Model Series") or \
        str.lower(series) == str.lower("Sportsman") or \
        str.lower(series) == str.lower("Sportsman Series") or \
        str.lower(series) == str.lower("Budweiser Late Series") or \
        str.lower(series) == str.lower("Budweiser Late Model Series") or\
        str.lower(series) == str.lower("Budweiser Sportsman") or \
        str.lower(series) == str.lower("Budweiser Sportsman Series") or \
        str.lower(series) == str.lower("Budweiser Late Sportsman Series") or \
        str.lower(series) == str.lower("Budweiser Late Model Sportsman Series") or \
        str.lower(series) == str.lower("Busch") or \
        str.lower(series) == str.lower("Busch Series") or \
        str.lower(series) == str.lower("Grand National") or \
        str.lower(series) == str.lower("Busch Grand National") or \
        str.lower(series) == str.lower("Busch Grand National Series") or \
        str.lower(series) == str.lower("Buschwhack") or \
        str.lower(series) == str.lower("Buschwhacker") or \
        str.lower(series) == str.lower("Buschwhacker Series") or \
        str.lower(series) == str.lower("Nationwide") or \
        str.lower(series) == str.lower("Nationwide Series"):
        return "series_2"
    elif str.lower(series) == str.lower("Truck") or \
        str.lower(series) == str.lower("Truck Series") or \
        str.lower(series) == str.lower("Craftsman") or \
        str.lower(series) == str.lower("Craftsman Truck") or \
        str.lower(series) == str.lower("Craftsman Truck Series") or \
        str.lower(series) == str.lower("SuperTruck") or \
        str.lower(series) == str.lower("SuperTruck Series") or \
        str.lower(series) == str.lower("Camping World") or \
        str.lower(series) == str.lower("Camping World Truck") or \
        str.lower(series) == str.lower("Camping World Truck Series") or \
        str.lower(series) == str.lower("Camping World Series") or \
        str.lower(series) == str.lower("Camping") or \
        str.lower(series) == str.lower("Camping Truck") or \
        str.lower(series) == str.lower("Camping Truck Series") or \
        str.lower(series) == str.lower("Camping Series") or \
        str.lower(series) == str.lower("Gander") or \
        str.lower(series) == str.lower("Gander RV") or \
        str.lower(series) == str.lower("Gander RV Truck") or \
        str.lower(series) == str.lower("Gander RV Series") or \
        str.lower(series) == str.lower("Gander RV Truck Series") or \
        str.lower(series) == str.lower("Gander RV and Outdoors") or \
        str.lower(series) == str.lower("Gander RV and Outdoors Series") or \
        str.lower(series) == str.lower("Gander RV and Outdoors Truck") or \
        str.lower(series) == str.lower("Gander RV and Outdoors Truck Series") or \
        str.lower(series) == str.lower("Gander RV & Outdoors") or \
        str.lower(series) == str.lower("Gander RV & Outdoors Series") or \
        str.lower(series) == str.lower("Gander RV & Outdoors Truck") or \
        str.lower(series) == str.lower("Gander RV & Outdoors Truck Series") or \
        str.lower(series) == str.lower("Gander Outdoors") or \
        str.lower(series) == str.lower("Gander Outdoors Series") or \
        str.lower(series) == str.lower("Gander Outdoors Truck") or \
        str.lower(series) == str.lower("Gander Outdoors Truck Series"):
        return "series_3"
    elif str.lower(series) == str.lower("all"):
        return "all"
    else:
        raise Exception(f"{series} is not a known series in NASCAR.")
    

def parse_nascar_schedule(season:int,series="Cup"):
    def parser(section:str,json_data=None):
            main_df = pd.DataFrame()
            row_df = pd.DataFrame()

            for i in json_data[section]:
                row_df = pd.DataFrame()
                race_id = i['race_id']
                row_df = pd.DataFrame(columns=['race_id'],data=[race_id])
                row_df['series_id'] = i['series_id']
                row_df['race_season'] = i['race_season']
                row_df['race_name'] = i['race_name']
                row_df['race_type_id'] = i['race_type_id']
                
                if i['restrictor_plate'] == True:
                    row_df['restrictor_plate'] = 1
                elif i['restrictor_plate'] == False:
                    row_df['restrictor_plate'] = 1
                else:
                    raise Exception("There is something teribly wrong with your computer.")

                row_df['track_id'] = i['track_id']
                row_df['track_name'] = i['track_name']
                row_df['date_scheduled'] = i['date_scheduled']
                row_df['race_date'] = i['race_date']

                if i['qualifying_date'] == "1900-01-01T00:00:00":
                    row_df['qualifying_date'] = None
                else:
                    row_df['qualifying_date'] = i['qualifying_date']
                
                try:
                    row_df['tunein_date'] = i['tunein_date']
                except:
                    row_df['tunein_date'] = None
                
                row_df['scheduled_distance'] = i['scheduled_distance']
                row_df['actual_distance'] = i['actual_distance']
                row_df['scheduled_laps'] = i['scheduled_laps']
                row_df['actual_laps'] = i['actual_laps']
                
                try:
                    row_df['stage_1_laps'] = i['stage_1_laps']
                except:
                    row_df['stage_1_laps'] = None
                
                try:
                    row_df['stage_2_laps'] = i['stage_2_laps']
                except:
                    row_df['stage_2_laps'] = None
                
                try:
                    row_df['stage_3_laps'] = i['stage_3_laps']
                except:
                    row_df['stage_3_laps'] = None

                row_df['number_of_cars_in_field'] = i['number_of_cars_in_field']
                row_df['pole_winner_driver_id'] = i['pole_winner_driver_id']
                row_df['pole_winner_speed'] = i['pole_winner_speed']
                row_df['number_of_lead_changes'] = i['number_of_lead_changes']
                row_df['number_of_leaders'] = i['number_of_leaders']
                row_df['number_of_cautions'] = i['number_of_cautions']
                row_df['number_of_caution_laps'] = i['number_of_caution_laps']
                row_df['average_speed'] = i['average_speed']
                row_df['total_race_time'] = i['total_race_time']

                try:
                    row_df['margin_of_victory'] = i['margin_of_victory']
                except:
                    row_df['margin_of_victory'] = None

                row_df['race_purse'] = i['race_purse']
                row_df['race_comments'] = i['race_comments']
                row_df['attendance'] = i['attendance']
                row_df['radio_broadcaster'] = i['radio_broadcaster']
                row_df['television_broadcaster'] = i['television_broadcaster']
                row_df['master_race_id'] = i['master_race_id']

                try:
                    row_df['inspection_complete'] = i['inspection_complete']
                except:
                    row_df['inspection_complete'] = None
                
                try:
                    row_df['playoff_round'] = i['playoff_round']
                except:
                    row_df['playoff_round'] = None

                try:
                    row_df['is_qualifying_race'] = i['is_qualifying_race']
                except:
                    row_df['is_qualifying_race'] = None
                
                try:
                    row_df['qualifying_race_no'] = i['qualifying_race_no']
                except:
                    row_df['qualifying_race_no'] = None

                try:
                    row_df['qualifying_race_id'] = i['qualifying_race_id']
                except:
                    row_df['qualifying_race_id'] = None

                try:
                    row_df['has_qualifying'] = i['has_qualifying']
                except:
                    row_df['has_qualifying'] = None

                try:
                    row_df['winner_driver_id'] = i['winner_driver_id']
                except:
                    row_df['winner_driver_id'] = None
                row_df['pole_winner_laptime'] = i['pole_winner_laptime']
                main_df = pd.concat([main_df,row_df],ignore_index=True)
                del row_df
            return main_df


    
    ## Validate that the inputted season is valid.
    if season < 2015:
        raise Exception("NASCAR API does not have schedule data before 2015.")
    elif season > datetime.now().year +1:
        raise Exception("You are attempting to get a schedule that does not exist right now.\nCheck your input for the season.")
    section = nascar_series_identification(series)

    
        
    url = f"https://cf.nascar.com/cacher/{season}/race_list_basic.json"
    response = urlopen(url)
    json_data = json.loads(response.read())
    
    schedule_df = pd.DataFrame()
    series_one_df = pd.DataFrame()
    series_two_df = pd.DataFrame()
    series_three_df = pd.DataFrame()

    if section == "all" or section == "series_1":
        series_one_df = parser("series_1",json_data)
    else:
        series_one_df = pd.DataFrame()

    if section == "all" or section == "series_2":
        series_two_df = parser("series_2",json_data)
    else:
        series_two_df = pd.DataFrame()

    schedule_df = pd.concat([series_one_df,series_two_df],ignore_index=True)

    if section == "all" or section == "series_3":
        series_three_df = parser("series_3",json_data)
    else:
        series_three_df = pd.DataFrame()

    schedule_df = pd.concat([schedule_df,series_three_df],ignore_index=True)
    #print(schedule_df)
    time.sleep(5)
    return schedule_df


def parse_race_results():
    pass

def main():
    for i in range(2015,2024):
        print(f'Getting the NASCAR Schedule for the {i} season.')
        df = parse_nascar_schedule(i,"all")
        df.to_csv(f"nascar_api/races/{i}_schedule.csv",index=False)

if __name__ == "__main__":
    main()