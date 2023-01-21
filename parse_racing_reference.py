import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_racing_reference_standings(season = 2022,series_id = "W"):
    main_df = pd.DataFrame()
    row_df = pd.DataFrame()
    url = f"https://www.racing-reference.info/season-stats/{season}/{series_id}/"
    #driver.get(url)
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, features='lxml')


    table_rows = soup.find_all("div", {"itemprop":"SportsEvent","class":"table-row","role":"row"})
    #print(table_rows)



    for i in tqdm(table_rows):
        #print('\n')
        #print(i)
        row_df = pd.DataFrame(columns=['season'],data=[season])
        row_df['series_id'] = series_id
        row_df['race_num'] = i.find('div',{'class':'race-number','role':'cell'}).text
        row_df['race_date'] = i.find('div',{'class':f'date {series_id}','role':'cell'}).text
        
        row_df['race_track_name'] = i.find('div',{'class':f'track {series_id}','role':'cell'}).text
        race_track_url = i.find('div',{'class':f'track {series_id}'}).find('a').get("href")
        row_df['race_track_id'] = str(race_track_url).replace('https://www.racing-reference.info/tracks/','').replace(' ','')
        
        row_df['race_car_count'] = i.find('div',{'class':'cars no-mobile','role':'cell'}).text
        row_df['race_winner_name'] = i.find('div',{'class':f'winners {series_id}','role':'cell'}).text
        race_winner_url = i.find('div',{'class':f'winners {series_id}'}).find('a').get("href")
        row_df['race_winner_real_id'] = race_winner_url.replace('https://www.racing-reference.info/driver/','').replace('/','')

        row_df['race_winner_starting_pos'] = i.find('div',{'class':'st no-mobile','role':'cell'}).text
        row_df['race_winner_make'] = i.find('div',{'class':f'manufacturer {series_id} no-mobile landscape','role':'cell'}).text
        row_df['race_lap_len'] = i.find('div',{'class':'len no-mobile','role':'cell'}).text
        row_df['race_track_surface'] = i.find('div',{'class':'sfc no-mobile','role':'cell'}).text
        row_df['race_miles_completed'] = i.find('div',{'class':f'miles no-mobile {series_id} no-right-border','role':'cell'}).text
        row_df['race_purse_completed'] = i.find('div',{'class':f'purse no-mobile {series_id}','role':'cell'}).text
        row_df['race_pole_time'] = i.find('div',{'class':'pole no-mobile no-tablet','role':'cell'}).text
        row_df['race_cautions'] = i.find('div',{'class':'cautions no-mobile no-tablet','role':'cell'}).text
        row_df['race_speed'] = i.find('div',{'class':'cautions no-mobile no-tablet','role':'cell'}).text
        row_df['race_lead_changes'] = i.find('div',{'class':'lc no-mobile no-tablet','role':'cell'}).text
        
        row_df['race_url'] = i.find('div',{'class':'race-number'}).find("a").get("href")
        row_df['race_track_url'] = race_track_url
        row_df['race_winner_url'] = race_winner_url

        #print(race_num,race_winner_real_id)
        #print('\n')
        main_df = pd.concat([main_df,row_df],ignore_index=True)

    print(main_df)
    main_df.to_csv('test.csv',index=False)



#get_racing_reference_standings(series_id="W")