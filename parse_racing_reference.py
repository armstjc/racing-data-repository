import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime

def get_racing_reference_schedule(season:int,series_id:str) -> pd.DataFrame():
    if series_id.upper() == "W":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_cup/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Cup season.')
    ## Xfinity (Busch) series
    elif series_id.upper() == "B":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_busch/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} Xfinity (Busch) season.')
    ## Craftsman Truck series
    elif series_id.upper() == "C":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_trucks/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} Craftsman Truck season.')
    ## ARCA series
    elif series_id.upper() == "A":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} ARCA season.')
    ## ARCA East series
    elif series_id.upper() == "P":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca_east/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} ARCA East season.')
    ## ARCA West series
    elif series_id.upper() == "E":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca_west/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} ARCA West season.')
    ## Modified series
    elif series_id.upper() == "N":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Modified season.')
    ## NASCAR Pinty's series
    elif series_id.upper() == "T":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_pintys/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Pinty\'s season.')
    ## NASCAR Convertable series
    elif series_id.upper() == "V":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_convertible/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Convertible season.')
    ## NASCAR Grand National East series
    elif series_id.upper() == "G":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_grand_national_east/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Grand National East season.')
    ## NASCAR North Tour series
    elif series_id.upper() == "NN":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_north_tour/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR North Tour season.')
    ## IndyCar Series
    elif series_id.upper() == "O":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} IndyCar season.')
    ## Championship Auto Racing Teams (CART)
    elif series_id.upper() == "R":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_arca/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} IndyCar season.')
    ## United States Auto Club (USAC) Championship Car Series
    elif series_id.upper() == "UO":
        try:
            sched_df = pd.read_csv(f'racing_reference/usac_champ_car/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} USAC Championship Car Series season.')
    ## International Race of Champions (IROC)
    elif series_id.upper() == "I":
        try:
            sched_df = pd.read_csv(f'racing_reference/iroc/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} International Race of Champions (IROC) season.')
    ## Indy NXT (Indy Lights)
    elif series_id.upper() == "IL":
        try:
            sched_df = pd.read_csv(f'racing_reference/indy_lights/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} Indy NXT (Indy Lights) season.')
    ## ACT Late Model Tour
    elif series_id.upper() == "AC":
        try:
            sched_df = pd.read_csv(f'racing_reference/act_late_model/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} ACT Late Model Tour season.')
    ## A1 Grand Prix
    elif series_id.upper() == "A1":
        try:
            sched_df = pd.read_csv(f'racing_reference/a1_grand_prix/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} A1 Grand Prix season.')
    ## North American Touring Car Championship (NATCC)
    elif series_id.upper() == "NA":
        try:
            sched_df = pd.read_csv(f'racing_reference/natcc/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} North American Touring Car Championship (NATCC) season.')
    ## NASCAR Whelen Southern Modified Tour (WSMT)
    elif series_id.upper() == "M":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_whelen_southern_modified/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Whelen Southern Modified Tour (WSMT) season.')
    ## CARS Tour
    elif series_id.upper() == "US":
        try:
            sched_df = pd.read_csv(f'racing_reference/cars_tour/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} CARS Tour season.')
    ## NASCAR Southeast Series
    elif series_id.upper() == "SE":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_southeast_series/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Southeast Series season.')
    ## NASCAR Midwest Series
    elif series_id.upper() == "MW":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_midwest_series/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Midwest Series season.')
    ## NASCAR Southwest Series
    elif series_id.upper() == "SW":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_southwest_series/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Southwest Series season.')
    ## NASCAR Northwest Series
    elif series_id.upper() == "NW":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_northwest_series/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Northwest Series season.')
    ## ASA National Tour
    elif series_id.upper() == "AS":
        try:
            sched_df = pd.read_csv(f'racing_reference/asa_national_tour/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} ASA National Tour season.')
    ## ASA National Tour
    elif series_id.upper() == "AS":
        try:
            sched_df = pd.read_csv(f'racing_reference/asa_national_tour/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} ASA National Tour season.')
    ## NASCAR Peak Mexico Series
    elif series_id.upper() == "MX":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_peak_mexico/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR Peak Mexico Series season.')
    ## NASCAR FedEx Challenge
    elif series_id.upper() == "M2":
        try:
            sched_df = pd.read_csv(f'racing_reference/nascar_fedex_challenge/schedule/{season}_schedule.csv')
            return sched_df
        except:
            raise FileNotFoundError(f'Could not find a schedule file for the {season} NASCAR FedEx Challenge.')

    else:
        raise ValueError("The input for series_id is invalid.")


def get_racing_reference_standings(season:int,series_id="W") -> pd.DataFrame():
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
        race_num = int(str(i.find('div',{'class':'race-number','role':'cell'}).text).replace(" ",""))
        row_df['race_num'] = race_num
        row_df['race_date'] = i.find('div',{'class':f'date {series_id}','role':'cell'}).text
        
        if race_num < 10:
            row_df['race_short_id'] = f"{season}_0{race_num}"
        else:
            row_df['race_short_id'] = f"{season}_{race_num}"

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
    sched_df = get_racing_reference_schedule(season=season,series_id=series_id)

    race_url_arr = sched_df['race_url'].to_list()
    #race_num_arr = sched_df['race_num'].to_list()
    race_id_short_arr = sched_df['race_short_id'].to_list()
    #main_df = pd.DataFrame()
    race_results_df = pd.DataFrame()
    row_df = pd.DataFrame()

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    for i in tqdm(range(0,len(race_url_arr))):
        race_results_url = race_url_arr[i]
        response = requests.get(race_results_url,headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')

        # table 0: Race info table.
        # table 1: Header table (links to stuff like race results, loop data, and pit stop data).
        html_table = soup.find_all('table',{'class':'tb race-results-tbl'})[0]
        #print(f"\n{html_table}")

        race_id = str(race_results_url).replace("https://www.racing-reference.info/race-results/","").replace(f"/{series_id.upper()}","")
        race_id_short = race_id_short_arr[i]
        
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
                race_results_df = pd.concat([race_results_df,row_df],ignore_index=True)
        
                del row_df

        time.sleep(1)

    return race_results_df

def get_racing_reference_entry_lists(season:int,series_id="W") -> pd.DataFrame():
    """
    
    """
    sched_df = get_racing_reference_schedule(season=season,series_id=series_id)


    race_id_short_arr = sched_df['race_short_id'].to_list()
    #main_df = pd.DataFrame()
    race_entry_lists_df = pd.DataFrame()
    row_df = pd.DataFrame()
    has_entry_lists = False

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    for i in race_id_short_arr:
        url = f"https://www.racing-reference.info/race-results/?rType=cc&raceId={i}&series={series_id}"
        row_df = pd.DataFrame({'season':season,'series_id':series_id,'race_id_short':i},index=[0])
        try:
            response = requests.get(url,headers=headers)
            soup = BeautifulSoup(response.text, features='lxml')
            has_entry_lists = True
        except:
            print(f'No entry list found for {i}.\nseries ID:{series_id}')
            has_entry_lists = False

        table = soup.find_all("tbody")


        del row_df

    return race_entry_lists_df

def main():
    #current_year = datetime.now().year
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day


    for i in range(current_year,current_year+1):
        ## Cup Series
        if i >= 1949:
            sched_df = get_racing_reference_standings(season=i,series_id="W")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_cup/schedule/{i}_schedule.csv",index=False)
            #try:
            results_df = get_racing_reference_race_results(season=i,series_id="W")
            if len(results_df) > 0:
                results_df.to_csv(f"racing_reference/nascar_cup/race_results/{i}_race_results.csv",index=False)
            #except:
            #    print(f'Could not get race results for the {i} NASCAR Cup season.')

            #get_racing_reference_entry_lists(i,"W")

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

        # NASCAR Pinty's Series
        if i >= 2007:
            sched_df = get_racing_reference_standings(season=i,series_id="T")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_pintys/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="T")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_pintys/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR Pinty\'s season.')

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

        ## Indy NXT (Indy Lights)
        if i >= 1986:
            sched_df = get_racing_reference_standings(season=i,series_id="IL")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/indy_lights/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="IL")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/indy_lights/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} Indy NXT (Indy Lights) season.')

        # ACT Late Model Tour
        if i >= 2006:
            sched_df = get_racing_reference_standings(season=i,series_id="AC")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/act_late_model/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="AC")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/act_late_model/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} ACT Late Model Tour season.')

        # Needs diffrient parser for this leauge.
        ## Supercars Championship
        if i >= 1960:
            sched_df = get_racing_reference_standings(season=i,series_id="V8")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/supercars_championship/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="V8")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/supercars_championship/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} Supercars Championship season.')
        
        ## NASCAR Peak Mexico
        if i >= 2008:
            sched_df = get_racing_reference_standings(season=i,series_id="MX")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_peak_mexico/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="MX")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_peak_mexico/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} NASCAR Peak Mexico season.')

        ## NASCAR FedEx Challenge
        if i >= 2017:
            sched_df = get_racing_reference_standings(season=i,series_id="M2")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_fedex_challenge/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="M2")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_fedex_challenge/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} NASCAR FedEx Challenge season.')

        # #####################################################################################################################################3
        # ## Defunct Series
        # #####################################################################################################################################3

        ## NASCAR Convertible Series
        if i >= 1956 and i <= 1959:
            sched_df = get_racing_reference_standings(season=i,series_id="V")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_convertible/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="V")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_convertible/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR Convertible season.')

        ## NASCAR Grand National East Series
        if i >= 1972 and i <= 1973:
            sched_df = get_racing_reference_standings(season=i,series_id="G")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_grand_national_east/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="G")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_grand_national_east/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR Convertible season.')

        ## NASCAR North Tour
        if i >= 1979 and i <= 1985:
            sched_df = get_racing_reference_standings(season=i,series_id="NN")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_north_tour/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="NN")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_north_tour/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR North Tour season.')

        ## Championship Auto Racing Teams (CART)
        if i >= 1979 and i <= 2007:
            sched_df = get_racing_reference_standings(season=i,series_id="R")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/cart/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="R")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/cart/race_results/{i}_race_results.csv",index=False)
            except:
                print(f'Could not get race results for the {i} NASCAR Convertible season.')

        ## USAC Champ Car Series
        if i >= 1905 and i <= 1995:
            sched_df = get_racing_reference_standings(season=i,series_id="UO")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/usac_champ_car/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="UO")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/usac_champ_car/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} USAC Champ Car Series season.')

        ## International Race of Champions (IROC)
        if i >= 1974 and i <= 2006:
            sched_df = get_racing_reference_standings(season=i,series_id="I")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/iroc/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="I")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/iroc/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} USAC Champ Car Series season.')

        ## A1 Grand Prix
        if i >= 2005 and i <= 2008:
            sched_df = get_racing_reference_standings(season=i,series_id="A1")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/a1_grand_prix/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="A1")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/a1_grand_prix/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} A1 Grand Prix season.')

        ## North American Touring Car Championship (NATCC)
        if i >= 1996 and i <= 1997:
            sched_df = get_racing_reference_standings(season=i,series_id="NA")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/natcc/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="NA")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/natcc/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} North American Touring Car Championship (NATCC) season.')

        ## NASCAR Whelen Southern Modified Tour (WSMT)
        if i >= 2005 and i <= 2016:
            sched_df = get_racing_reference_standings(season=i,series_id="M")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_whelen_southern_modified/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="M")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_whelen_southern_modified/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} NASCAR Whelen Southern Modified Tour (WSMT) season.')

        ## CARS Tour
        if i >= 1997 and i <= 2014:
            sched_df = get_racing_reference_standings(season=i,series_id="US")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/cars_tour/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="US")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/cars_tour/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} CARS Tour season.')

        ## NASCAR Southeast Series
        if i >= 1991 and i <= 2006:
            sched_df = get_racing_reference_standings(season=i,series_id="SE")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_southeast_series/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="SE")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_southeast_series/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} NASCAR Southeast Series season.')

        ## NASCAR Midwest Series
        if i >= 1998 and i <= 2006:
            sched_df = get_racing_reference_standings(season=i,series_id="MW")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_midwest_series/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="MW")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_midwest_series/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} NASCAR Midwest Series season.')

        ## NASCAR Southwest Series
        if i >= 1986 and i <= 2006:
            sched_df = get_racing_reference_standings(season=i,series_id="SW")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_southwest_series/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="SW")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_southwest_series/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} NASCAR Southwest Series season.')
        
        ## NASCAR Northwest Series
        if i >= 1985 and i <= 2006:
            sched_df = get_racing_reference_standings(season=i,series_id="NW")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/nascar_northwest_series/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="NW")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/nascar_northwest_series/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} NASCAR Northwest Series season.')

        ## ASA National Tour
        if i >= 1998 and i <= 2004:
            sched_df = get_racing_reference_standings(season=i,series_id="NW")
            if len(sched_df) > 0:
                sched_df.to_csv(f"racing_reference/asa_national_tour/schedule/{i}_schedule.csv",index=False)
            try:
                results_df = get_racing_reference_race_results(season=i,series_id="MW")
                if len(results_df) > 0:
                    results_df.to_csv(f"racing_reference/asa_national_tour/race_results/{i}_race_results.csv",index=False)
            except:
               print(f'Could not get race results for the {i} ASA National Tour season.')


    with open('racing_reference_status.json','w+') as f:
        f.write(f"{{ \"year\":{current_year},\"month\":{current_month},\"day\":{current_day} }}")

if __name__ == "__main__":
    main()
