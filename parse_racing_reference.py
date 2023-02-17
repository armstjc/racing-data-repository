import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_racing_reference_standings(season:int,series_id="W"):
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

def get_racing_reference_race_results(season:int,series_id="W"):
    """
    
    """
    sched_df = pd.DataFrame()
    ## Cup series
    if series_id.upper() == "W":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_cup/schedule/{season}_schedule.csv')
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Cup season.')
    ## Xfinity (Busch) series
    elif series_id.upper() == "B":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_busch/schedule/{season}_schedule.csv')
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} Xfinity (Busch) season.')
    ## Craftsman Truck series
    elif series_id.upper() == "C":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_trucks/schedule/{season}_schedule.csv')
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} Craftsman Truck season.')
    ## ARCA series
    elif series_id.upper() == "A":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca/schedule/{season}_schedule.csv')
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} ARCA season.')
    ## ARCA East series
    elif series_id.upper() == "P":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca_east/schedule/{season}_schedule.csv')
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} ARCA East season.')
    ## ARCA West series
    elif series_id.upper() == "E":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca_west/schedule/{season}_schedule.csv')
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} ARCA West season.')
    ## Modified series
    elif series_id.upper() == "N":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca/schedule/{season}_schedule.csv')
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Modified season.')
    ## IndyCar Series
    elif series_id.upper() == "O":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca/schedule/{season}_schedule.csv')
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} IndyCar season.')
    else:
        raise ValueError("The input for series_id is invalid.")

    race_url_arr = sched_df['race_url'].to_list()
    race_num_arr = sched_df['race_num'].to_list()
    #main_df = pd.DataFrame()
    race_df = pd.DataFrame()
    row_df = pd.DataFrame()

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    for i in tqdm(range(0,len(race_url_arr))):
        url = race_url_arr[i]
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')

        # table 0: Race info table.
        # table 1: Header table (links to stuff like race results, loop data, and pit stop data).
        html_table = soup.find_all('table',{'class':'tb race-results-tbl'})[0]
        #print(f"\n{html_table}")

        race_id = str(url).replace("https://www.racing-reference.info/race-results/","").replace(f"/{series_id.upper()}","")
        if race_num_arr[i] < 10:
            race_id_short = f"{season}_0{race_num_arr[i]}_{series_id}"
        else:
            race_id_short = f"{season}_{race_num_arr[i]}_{series_id}"
        
        for j in html_table.find_all('tr'):
            row_df = pd.DataFrame({'season':season,'series_id':series_id,'race_id':race_id,'race_id_short':race_id_short},index=[0])
            row = j.find_all('td')

            if len(row) < 2:
                ## If this is less than 2, this is the header.
                ## We don't need the header.
                pass
            else:
                #print(race_id)
                row_df['finish_position'] = row[0].text.strip()
                row_df['starting_position'] = row[1].text.strip()
                row_df['driver_number'] = str(row[2].text.strip())
                row_df['driver_nationality'] = str(row[3].find("img").get("src")).replace('//www.racing-reference.info/wp-content/themes/ndms/images/racing-reference/flags/','').replace('.png','')
                try:
                    row_df['driver_id'] = str(row[3].find("a").get("href")).replace('https://www.racing-reference.info/driver/','').replace('/','')
                except:
                    row_df['driver_id'] = None
                row_df['driver_name'] = row[3].text.strip()
                sponsor_owner = row[4].text.strip()
                row_df['sponsor'] = sponsor_owner.split('   ')[0]
                try:
                    row_df['owner_id'] = str(row[4].find("a").get("href")).replace('https://www.racing-reference.info/owner/','')
                except:
                    row_df['owner_id'] = None
                try:                    
                    row_df['car'] = row[5].text.strip()
                except:
                    row_df['car'] = None
                row_df['race_laps_run'] = row[6].text.strip()
                row_df['race_status'] = row[7].text.strip()
                row_df['race_laps_lead'] = row[8].text.strip()
                try:
                    row_df['points_earned'] = row[9].text.strip()
                except:
                    row_df['points_earned'] = None
                try:
                    row_df['playoff_points_earned'] = row[10].text.strip()
                except:
                    row_df['playoff_points_earned'] = None
                race_df = pd.concat([race_df,row_df],ignore_index=True)
        #print(race_df)
        time.sleep(1)

    return race_df


def main():
    for i in range(1958,2024):
        ## Cup Series
        if i >= 1949:
            sched_df = get_racing_reference_standings(season=i,series_id="W")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_cup/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="W")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_cup/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR Cup season.')

        ## Xfinity (Busch) Series
        if i >= 1984:
            sched_df = get_racing_reference_standings(season=i,series_id="B")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_busch/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="B")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_busch/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR Xfinity season.')

        ## Truck Series
        if i >= 1995:
            sched_df = get_racing_reference_standings(season=i,series_id="C")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_trucks/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="C")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_trucks/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR Trucks season.')

        ## ARCA Series
        if i >= 1979:
            sched_df = get_racing_reference_standings(season=i,series_id="A")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_arca/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="A")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_arca/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR ARCA season.')
        
        ## ARCA East Series
        if i >= 1954:
            sched_df = get_racing_reference_standings(season=i,series_id="P")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_arca_east/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="P")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_arca_east/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR ARCA East season.')

        ## ARCA West Series
        if i >= 1987:
            sched_df = get_racing_reference_standings(season=i,series_id="E") # Yes, this is the actual leauge ID for ARCA West.
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_arca_west/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="E")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_arca_west/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR ARCA West season.')

        ## Modified Series
        if i >= 1948:
            sched_df = get_racing_reference_standings(season=i,series_id="N")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_modified/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="N")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_modified/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR Modifieds season.')

        ## IndyCar Series
        if i >= 1996:
            sched_df = get_racing_reference_standings(season=i,series_id="O")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/indycar/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="O")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/indycar/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} IndyCar season.')

if __name__ == "__main__":
    main()