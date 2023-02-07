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
        row_df['race_num'] = int(str(i.find('div',{'class':'race-number','role':'cell'}).text).replace(" ",""))
        row_df['race_date'] = i.find('div',{'class':f'date {series_id}','role':'cell'}).text
        
        row_df['race_track_name'] = i.find('div',{'class':f'track {series_id}','role':'cell'}).text
        race_track_url = i.find('div',{'class':f'track {series_id}'}).find('a').get("href")
        row_df['race_track_id'] = str(race_track_url).replace('https://www.racing-reference.info/tracks/','').replace(' ','')
        
        row_df['race_car_count'] = int(str(i.find('div',{'class':'cars no-mobile','role':'cell'}).text).replace(' ',''))
        row_df['race_winner_name'] = i.find('div',{'class':f'winners {series_id}','role':'cell'}).text
        race_winner_url = i.find('div',{'class':f'winners {series_id}'}).find('a').get("href")
        row_df['race_winner_real_id'] = race_winner_url.replace('https://www.racing-reference.info/driver/','').replace('/','')
        
        try:
            row_df['race_winner_starting_pos'] = int(str(i.find('div',{'class':'st no-mobile','role':'cell'}).text).replace(' ',''))
        except:
            row_df['race_winner_starting_pos'] = None

        row_df['race_winner_make'] = i.find('div',{'class':f'manufacturer {series_id} no-mobile landscape','role':'cell'}).text
        row_df['race_lap_len'] = i.find('div',{'class':'len no-mobile','role':'cell'}).text
        row_df['race_track_surface'] = i.find('div',{'class':'sfc no-mobile','role':'cell'}).text
        row_df['race_miles_completed'] = i.find('div',{'class':f'miles no-mobile {series_id} no-right-border','role':'cell'}).text
        
        try:
            row_df['race_purse_completed'] = int(str(i.find('div',{'class':f'purse no-mobile {series_id}','role':'cell'}).text).replace(' ','').replace(',',''))
        except:
            row_df['race_purse_completed'] = None

        row_df['race_pole_time'] = i.find('div',{'class':'pole no-mobile no-tablet','role':'cell'}).text
        row_df['race_cautions'] = str(i.find('div',{'class':'cautions no-mobile no-tablet','role':'cell'}).text).replace(' ','')
        row_df['race_speed'] = i.find('div',{'class':'speed no-mobile no-tablet','role':'cell'}).text
        row_df['race_lead_changes'] = i.find('div',{'class':'lc no-mobile no-tablet','role':'cell'}).text
        
        row_df['race_url'] = str(i.find('div',{'class':'race-number'}).find("a").get("href")).replace(' ','')
        row_df['race_track_url'] = race_track_url
        row_df['race_winner_url'] = race_winner_url

        #print(race_num,race_winner_real_id)
        #print('\n')
        main_df = pd.concat([main_df,row_df],ignore_index=True)

    print(main_df)
    time.sleep(1)
    #main_df.to_csv('test.csv',index=False)
    return main_df


def main():

    for i in range(1996,2024):
        ## Cup Series
        if i >= 1949:
            df = get_racing_reference_standings(season=i,series_id="W")
            if len(df) > 0:
                df.to_csv(f"racing_reference/nascar_cup/schedule/{i}_schedule.csv",index=False)

        ## Xfinity (Busch) Series
        if i >= 1984:
            df = get_racing_reference_standings(season=i,series_id="B")
            if len(df) > 0:
                df.to_csv(f"racing_reference/nascar_busch/schedule/{i}_schedule.csv",index=False)

        ## Truck Series
        if i >= 1995:
            df = get_racing_reference_standings(season=i,series_id="C")
            if len(df) > 0:
                df.to_csv(f"racing_reference/nascar_trucks/schedule/{i}_schedule.csv",index=False)

        ## ARCA Series
        if i >= 1979:
            df = get_racing_reference_standings(season=i,series_id="A")
            if len(df) > 0:
                df.to_csv(f"racing_reference/nascar_arca/schedule/{i}_schedule.csv",index=False)

        ## Modified Series
        if i >= 1948:
            df = get_racing_reference_standings(season=i,series_id="N")
            if len(df) > 0:
                df.to_csv(f"racing_reference/nascar_modified/schedule/{i}_schedule.csv",index=False)

        ## IndyCar Series
        if i >= 1996:
            df = get_racing_reference_standings(season=i,series_id="O")
            if len(df) > 0:
                df.to_csv(f"racing_reference/indycar/schedule/{i}_schedule.csv",index=False)

        time.sleep(5)

if __name__ == "__main__":
    main()