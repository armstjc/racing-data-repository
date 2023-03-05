import pandas as pd
import json
from datetime import datetime
import time
from urllib.request import urlopen
from tqdm import tqdm
#import numpy as np

def nascar_series_identification(series: str):
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
		raise Exception(f"{series} is not a known series in the NASCAR API.")

def parse_nascar_schedule(season: int, series="Cup"):
	def parser(section: str, json_data=None):
		main_df = pd.DataFrame()
		row_df = pd.DataFrame()

		for i in json_data[section]:
			row_df = pd.DataFrame()
			race_id = i['race_id']
			row_df = pd.DataFrame(columns=['race_id'], data=[race_id])
			row_df['series_id'] = i['series_id']
			row_df['race_season'] = i['race_season']
			row_df['race_name'] = i['race_name']
			row_df['race_type_id'] = i['race_type_id']

			if i['restrictor_plate'] == True:
				row_df['restrictor_plate'] = 1
			elif i['restrictor_plate'] == False:
				row_df['restrictor_plate'] = 0
			else:
				raise Exception(
					"There is something teribly wrong with your computer.")

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
			# row_df['race_comments'] = i['race_comments']
			row_df['attendance'] = i['attendance']
			row_df['radio_broadcaster'] = i['radio_broadcaster']
			row_df['television_broadcaster'] = i['television_broadcaster']
			row_df['master_race_id'] = i['master_race_id']

			try:
				if row_df['inspection_complete'] == True:
					row_df['inspection_complete'] = 1
				elif row_df['inspection_complete'] == False:
					row_df['inspection_complete'] = 0
			except:
				row_df['inspection_complete'] = None

			try:
				row_df['playoff_round'] = i['playoff_round']
			except:
				row_df['playoff_round'] = None

			try:
				if row_df['is_qualifying_race'] == True:
					row_df['is_qualifying_race'] = 1
				elif row_df['is_qualifying_race'] == False:
					row_df['is_qualifying_race'] = 0
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
				if row_df['has_qualifying'] == True:
					row_df['has_qualifying'] = 1
				elif row_df['has_qualifying'] == False:
					row_df['has_qualifying'] = 0
			except:
				row_df['has_qualifying'] = None

			try:
				row_df['winner_driver_id'] = i['winner_driver_id']
			except:
				row_df['winner_driver_id'] = None
			row_df['pole_winner_laptime'] = i['pole_winner_laptime']
			main_df = pd.concat([main_df, row_df], ignore_index=True)
			del row_df
		return main_df

	# Validate that the inputted season is valid.
	if season < 2015:
		raise Exception("NASCAR API does not have schedule data before 2015.")
	elif season > datetime.now().year + 1:
		raise Exception(
		"You are attempting to get a schedule that does not exist right now.\nCheck your input for the season.")
	section = nascar_series_identification(series)

	url = f"https://cf.nascar.com/cacher/{season}/race_list_basic.json"
	response = urlopen(url)
	json_data = json.loads(response.read())

	schedule_df = pd.DataFrame()
	series_one_df = pd.DataFrame()
	series_two_df = pd.DataFrame()
	series_three_df = pd.DataFrame()

	if section == "all" or section == "series_1":
		series_one_df = parser("series_1", json_data)
	else:
		series_one_df = pd.DataFrame()

	if section == "all" or section == "series_2":
		series_two_df = parser("series_2", json_data)
	else:
		series_two_df = pd.DataFrame()

	schedule_df = pd.concat([series_one_df, series_two_df], ignore_index=True)

	if section == "all" or section == "series_3":
		series_three_df = parser("series_3", json_data)
	else:
		series_three_df = pd.DataFrame()

	schedule_df = pd.concat([schedule_df, series_three_df], ignore_index=True)
	# print(schedule_df)
	time.sleep(5)
	return schedule_df

def parse_basic_race_results(season: int):
	race_info_df = pd.DataFrame()
	race_results_df = pd.DataFrame()
	race_cautions_df = pd.DataFrame()
	race_leaders_df = pd.DataFrame()
	race_stage_results_df = pd.DataFrame()
	race_infractions_df = pd.DataFrame()
	race_pit_reports_df = pd.DataFrame()
	row_df = pd.DataFrame()

	if season < 2018:
		raise Exception("\nNASCAR API does not have live race data before 2018.")
	elif season > datetime.now().year + 1:
		raise Exception("\nYou are attempting to get a race that does not exist right now.\nCheck your input for the season.")

	schedule_df = parse_nascar_schedule(season, "all")
	
	race_ids_list = schedule_df['race_id'].to_numpy()
	race_levels_list = schedule_df['series_id'].to_numpy()
	race_seasons_list = schedule_df['race_season'].to_numpy()

	for i in tqdm(range(0,len(race_ids_list))):
		row_df = pd.DataFrame()

		has_race_data = True
		race_id = int(race_ids_list[i])
		race_level = int(race_levels_list[i])
		race_season = int(race_seasons_list[i])
		'https://cf.nascar.com/cacher/2015/1/4389/weekend-feed.json'
		print(f'\n{race_id}')
		'https://cf.nascar.com/cacher/2021/1/5087/weekend-feed.json',
		url = f'https://cf.nascar.com/cacher/{race_season}/{race_level}/{race_id}/weekend-feed.json'
		try:
			response = urlopen(url)
			has_race_data = True
			json_data = json.loads(response.read())
			time.sleep(1)
		except:
			time.sleep(3)
			has_race_data = False

		if has_race_data == True:
			for j in json_data['weekend_race']:
				row_df = pd.DataFrame(columns=['race_id'], data=[race_id])
				row_df['series_id'] = race_level
				row_df['race_season'] = race_season
				row_df['race_name'] = j['race_name']
				row_df['race_type_id'] = j['race_type_id']
				row_df['restrictor_plate'] = j['restrictor_plate']
				row_df['track_id'] = j['track_id']
				row_df['track_name'] = j['track_name']
				row_df['date_scheduled'] = j['date_scheduled']
				row_df['race_date'] = j['race_date']
				row_df['qualifying_date'] = j['qualifying_date']

				try:
					row_df['tunein_date'] = j['tunein_date']
				except:
					row_df['tunein_date']= None
				
				row_df['scheduled_distance'] = j['scheduled_distance']
				row_df['actual_distance'] = j['actual_distance']
				row_df['scheduled_laps'] = j['scheduled_laps']
				row_df['actual_laps'] = j['actual_laps']
				row_df['stage_1_laps'] = j['stage_1_laps']
				row_df['stage_2_laps'] = j['stage_2_laps']
				row_df['stage_3_laps'] = j['stage_3_laps']
				
				try:
					row_df['stage_4_laps'] = j['stage_4_laps']
				except:
					row_df['stage_4_laps'] = None
				
				row_df['number_of_cars_in_field'] = j['number_of_cars_in_field']
				row_df['pole_winner_driver_id'] = j['pole_winner_driver_id']
				row_df['pole_winner_speed'] = j['pole_winner_speed']
				row_df['number_of_lead_changes'] = j['number_of_lead_changes']
				row_df['number_of_leaders'] = j['number_of_leaders']
				row_df['number_of_cautions'] = j['number_of_cautions']
				row_df['number_of_caution_laps'] = j['number_of_caution_laps']
				row_df['average_speed'] = j['average_speed']
				row_df['total_race_time'] = j['total_race_time']
				row_df['margin_of_victory'] = j['margin_of_victory']
				row_df['race_purse'] = j['race_purse']
				row_df['attendance'] = j['attendance']
				row_df['radio_broadcaster'] = j['radio_broadcaster']
				row_df['television_broadcaster'] = j['television_broadcaster']
				row_df['master_race_id'] = j['master_race_id']

				try:
					row_df['inspection_complete'] = j['inspection_complete']
				except:
					row_df['inspection_complete'] = None

				try:
					row_df['playoff_round'] = j['playoff_round']
				except:
					row_df['playoff_round'] = None

				race_info_df = pd.concat([race_info_df,row_df],ignore_index=True)
				
				del row_df

				for k in j['results']:
					row_df = pd.DataFrame(columns=['race_id'], data=[race_id])
					row_df['series_id'] = race_level
					row_df['race_season'] = race_season
					row_df['result_id'] = k['result_id']
					row_df['finishing_position'] = k['finishing_position']
					row_df['starting_position'] = k['starting_position']
					row_df['car_number'] = str(k['car_number'])
					row_df['driver_fullname'] = k['driver_fullname']

					try:
						row_df['driver_hometown'] = k['driver_hometown']
					except:
						row_df['driver_hometown'] = None

					row_df['hometown_city'] = k['hometown_city']
					row_df['hometown_state'] = k['hometown_state']

					try:
						row_df['hometown_country'] = k['hometown_country']
					except:
						row_df['hometown_country'] = None

					row_df['team_id'] = k['team_id']
					row_df['team_name'] = k['team_name']
					row_df['qualifying_order'] = k['qualifying_order']
					row_df['qualifying_position'] = k['qualifying_position']
					row_df['qualifying_speed'] = k['qualifying_speed']
					row_df['laps_led'] = k['laps_led']
					row_df['times_led'] = k['times_led']
					row_df['car_make'] = k['car_make']
					row_df['car_model'] = k['car_model']
					row_df['sponsor'] = k['sponsor']
					row_df['points_earned'] = k['points_earned']

					try:
						row_df['playoff_points_earned'] = k['playoff_points_earned']
					except:
						row_df['playoff_points_earned'] = None

					row_df['laps_completed'] = k['laps_completed']
					row_df['finishing_status'] = k['finishing_status']
					row_df['winnings'] = k['winnings']
					row_df['series_id'] = k['series_id']
					row_df['race_season'] = k['race_season']
					row_df['race_id'] = k['race_id']
					row_df['owner_fullname'] = k['owner_fullname']

					try:
						row_df['crew_chief_id'] = k['crew_chief_id']
					except:
						row_df['crew_chief_id'] = None

					row_df['crew_chief_fullname'] = k['crew_chief_fullname']
					row_df['points_position'] = k['points_position']
					row_df['points_delta'] = k['points_delta']
					row_df['owner_id'] = k['owner_id']
					row_df['official_car_number'] = str(k['official_car_number'])

					try:
						row_df['disqualified'] = k['disqualified']
					except:
						row_df['disqualified'] = None
					
					try:
						row_df['diff_laps'] = k['diff_laps']
					except:
						row_df['diff_laps'] = None

					try:
						row_df['diff_time'] = k['diff_time']
					except:
						row_df['diff_time'] = None

					race_results_df = pd.concat(
						[race_results_df,row_df],
						ignore_index=True
					)
					del row_df

				for k in j['caution_segments']:
					row_df = pd.DataFrame(columns=['race_id'], data=[race_id])
					row_df['start_lap'] = k['start_lap']
					row_df['end_lap'] = k['end_lap']
					row_df['reason'] = k['reason']
					row_df['comment'] = k['comment']
					row_df['beneficiary_car_number'] = str(k['beneficiary_car_number'])
					row_df['flag_state'] = k['flag_state']

					race_cautions_df = pd.concat(
						[race_cautions_df,row_df],
						ignore_index=True
					)

					del row_df

				for k in j['race_leaders']:
					row_df = pd.DataFrame(columns=['race_id'], data=[race_id])
					row_df['start_lap'] = k['start_lap']
					
					row_df['end_lap'] = k['end_lap']
					row_df['car_number'] = str(k['car_number'])

					race_leaders_df = pd.concat(
						[race_leaders_df,row_df],
						ignore_index=True
					)
					
					del row_df

				if season >= 2020:
					try:
						for k in j['stage_results']:
							stage_num = k['stage_number']
							for d in k['results']:
								row_df = pd.DataFrame(
									columns=['race_id'],
									data=[race_id])
								row_df['stage_number'] = stage_num
								row_df['driver_fullname'] = d['driver_fullname']
								row_df['driver_id'] = d['driver_id']
								row_df['car_number'] = str(d['car_number'])
								row_df['finishing_position'] = d['finishing_position']
								row_df['stage_points'] = d['stage_points']

								race_stage_results_df = pd.concat(
									[race_stage_results_df,row_df],
									ignore_index=True
								)
								del row_df
					except:
						print('No Stage results found in this race.')

				if season >= 2021:
					for k in j['infractions']:
						row_df = pd.DataFrame(columns=['race_id'], data=[race_id])
						row_df['car_number'] = str(k['car_number'])
						row_df['driver_fullname'] = k['driver_fullname']
						row_df['driver_id'] = k['driver_id']
						row_df['lap'] = k['lap']
						row_df['lap_assessed'] = k['lap_assessed']
						row_df['penalty'] = k['penalty']
						row_df['notes'] = k['notes']

						race_infractions_df = pd.concat([race_infractions_df,row_df],
							ignore_index=True
						)
						
						del row_df

					for k in j['pit_reports']:
						row_df = pd.DataFrame(columns=['race_id'], data=[race_id])
						row_df['infraction'] = k['infraction']
						row_df['vehicle_number'] = str(k['vehicle_number'])
						row_df['driver_name'] = k['driver_name']
						row_df['vehicle_manufacturer'] = k['vehicle_manufacturer']
						row_df['leader_lap'] = k['leader_lap']
						row_df['lap_count'] = k['lap_count']
						row_df['pit_in_flag_status'] = k['pit_in_flag_status']
						row_df['pit_out_flag_status'] = k['pit_out_flag_status']
						row_df['pit_in_race_time'] = k['pit_in_race_time']
						row_df['pit_out_race_time'] = k['pit_out_race_time']
						row_df['total_duration'] = k['total_duration']
						row_df['box_stop_race_time'] = k['box_stop_race_time']
						row_df['box_leave_race_time'] = k['box_leave_race_time']
						row_df['pit_stop_duration'] = k['pit_stop_duration']
						row_df['in_travel_duration'] = k['in_travel_duration']
						row_df['out_travel_duration'] = k['out_travel_duration']
						row_df['pit_stop_type'] = k['pit_stop_type']
						row_df['left_front_tire_changed'] = k['left_front_tire_changed']
						row_df['left_rear_tire_changed'] = k['left_rear_tire_changed']
						row_df['right_front_tire_changed'] = k['right_front_tire_changed']
						row_df['right_rear_tire_changed'] = k['right_rear_tire_changed']
						row_df['previous_lap_time'] = k['previous_lap_time']
						row_df['next_lap_time'] = k['next_lap_time']
						
						race_pit_reports_df = pd.concat(
							[race_pit_reports_df,row_df],
							ignore_index=True
						)

						del row_df

	return race_info_df, race_results_df, race_cautions_df, \
		race_leaders_df, race_stage_results_df, race_infractions_df, \
		race_pit_reports_df

def parse_weekend_runs(season: int):

	weekend_runs_df = pd.DataFrame()
	row_df = pd.DataFrame()

	if season < 2018:
		raise Exception("NASCAR API does not have live race data before 2018.")
	elif season > datetime.now().year + 1:
		raise Exception(
		"You are attempting to get a race that does not exist right now.\nCheck your input for the season.")

	schedule_df = parse_nascar_schedule(season, "all")
	
	race_ids_list = schedule_df['race_id'].to_numpy()
	race_levels_list = schedule_df['series_id'].to_numpy()
	race_seasons_list = schedule_df['race_season'].to_numpy()

	for i in tqdm(range(0,len(race_ids_list))):
		row_df = pd.DataFrame()

		race_id = int(race_ids_list[i])
		race_level = int(race_levels_list[i])
		race_season = int(race_seasons_list[i])
		print(race_id)
		url = f'https://cf.nascar.com/cacher/{race_season}/{race_level}/{race_id}/weekend-feed.json'
		
		response = urlopen(url)
		json_data = json.loads(response.read())

		for j in json_data['weekend_runs']:
			weekend_run_id = j['weekend_run_id']
			timing_run_id = j['timing_run_id']
			run_type = j['run_type']
			run_name = j['run_name']
			run_date = j['run_date']

			try:
				run_date_utc = j['run_date_utc']
			except:
				run_date_utc = None

			for k in j['results']:
				row_df = pd.DataFrame(columns=['race_id'], data=[race_id])

				row_df['weekend_run_id'] = weekend_run_id
				row_df['timing_run_id'] = timing_run_id
				row_df['run_type'] = run_type
				row_df['run_name'] = run_name
				row_df['run_date'] = run_date
				row_df['run_date_utc'] = run_date_utc

				row_df['run_id'] = k['run_id']
				row_df['car_number'] = str(k['car_number'])
				
				try:
					row_df['vehicle_number'] = str(k['vehicle_number'])
				except:
					row_df['vehicle_number'] = None
				
				try:
					row_df['manufacturer'] = k['manufacturer']
				except:
					row_df['manufacturer'] = None

				row_df['driver_id'] = k['driver_id']

				try:
					row_df['driver_name'] = k['driver_name']
				except:
					row_df['driver_name'] = None

				row_df['finishing_position'] = k['finishing_position']
				row_df['best_lap_time'] = k['best_lap_time']
				row_df['best_lap_speed'] = k['best_lap_speed']
				row_df['best_lap_number'] = k['best_lap_number']
				row_df['laps_completed'] = k['laps_completed']
				row_df['comment'] = k['comment']
				row_df['delta_leader'] = k['delta_leader']

				try:
					row_df['disqualified'] = k['disqualified']
				except:
					row_df['disqualified'] = None
				
				weekend_runs_df = pd.concat(
					[weekend_runs_df,row_df],
					ignore_index=True
				)

				del row_df
		return weekend_runs_df

def parse_live_points(season:int):
	points_df = pd.DataFrame()
	row_df = pd.DataFrame()

	if season < 2019:
		raise Exception("\nNASCAR API does not have live race data before 2018.")
	elif season > datetime.now().year + 1:
		raise Exception(
		"You are attempting to get a race that does not exist right now.\nCheck your input for the season.")
	
	schedule_df = parse_nascar_schedule(season, "all")
	
	race_ids_list = schedule_df['race_id'].to_numpy()
	race_levels_list = schedule_df['series_id'].to_numpy()
	#race_seasons_list = schedule_df['race_season'].to_numpy()

	for i in tqdm(range(0,len(race_ids_list))):
		row_df = pd.DataFrame()

		race_id = int(race_ids_list[i])
		race_level = int(race_levels_list[i])
		print(race_id)
		url = f'https://cf.nascar.com/live/feeds/series_{race_level}/{race_id}/live_points.json'
		try:
			response = urlopen(url)
			json_data = json.loads(response.read())

			for j in json_data:
				row_df = pd.DataFrame(columns=['race_id'], data=[race_id])
				row_df['series_id'] = race_level
				row_df['run_id'] = j['run_id']
				row_df['car_number'] = str(j['car_number'])
				row_df['bonus_points'] = j['bonus_points']
				row_df['delta_leader'] = j['delta_leader']
				row_df['delta_next'] = j['delta_next']
				row_df['first_name'] = j['first_name']
				row_df['driver_id'] = j['driver_id']
				row_df['is_in_chase'] = j['is_in_chase']
				row_df['is_points_eligible'] = j['is_points_eligible']
				row_df['is_rookie'] = j['is_rookie']
				row_df['last_name'] = j['last_name']
				row_df['membership_id'] = j['membership_id']
				row_df['points'] = j['points']
				row_df['points_position'] = j['points_position']
				row_df['points_earned_this_race'] = j['points_earned_this_race']
				row_df['stage_1_points'] = j['stage_1_points']
				row_df['stage_1_winner'] = j['stage_1_winner']
				row_df['stage_2_points'] = j['stage_2_points']
				row_df['stage_2_winner'] = j['stage_2_winner']
				row_df['stage_3_points'] = j['stage_3_points']
				row_df['stage_3_winner'] = j['stage_3_winner']
				row_df['wins'] = j['wins']
				row_df['top_5'] = j['top_5']
				row_df['top_10'] = j['top_10']
				row_df['poles'] = j['poles']

				points_df = pd.concat([points_df,row_df],ignore_index=True)

				del row_df
		except:
			time.sleep(1)
	return points_df

def parse_lap_times(race_id,race_level,race_season):
	lap_times_df = pd.DataFrame()
	row_df = pd.DataFrame()

	url = f'https://cf.nascar.com/cacher/{race_season}/{race_level}/{race_id}/lap-times.json'
	
	try:
		response = urlopen(url)
		json_data = json.loads(response.read())
	except:
		raise Exception(f"Could not get lap data for {race_id} in the {race_level} level's {race_season} season.")

	for j in json_data['laps']:
		driver_number = str(j['Number'])
		driver_full_name = j['FullName']
		manufacturer = j['Manufacturer']
		running_position = j['RunningPos']
		NASCAR_driver_id = j['NASCARDriverID']

		for k in j['Laps']:
			row_df = pd.DataFrame(columns=['race_id'], data=[race_id])
			
			row_df['race_level'] = race_level
			row_df['race_season'] = race_season
			row_df['driver_number'] = driver_number
			row_df['driver_full_name'] = driver_full_name
			row_df['manufacturer'] = manufacturer
			row_df['finishing_position'] = running_position
			row_df['NASCAR_driver_id'] = NASCAR_driver_id
			row_df['lap_num'] = k['Lap']
			row_df['lap_time'] = k['LapTime']
			row_df['lap_speed'] = k['LapSpeed']
			row_df['lap_running_position'] = k['RunningPos']
			
			lap_times_df = pd.concat(
				[lap_times_df,row_df],
				ignore_index=True
			)

			del row_df

	return lap_times_df

def main():
	#current_year = datetime.now().year
	now = datetime.now()
	current_year = now.year
	current_month = now.month
	current_day = now.day

	for i in tqdm(range(current_year-1,current_year+1)):
		df = parse_nascar_schedule(i, "all")
		df = df.sort_values(by="date_scheduled")
		df.to_csv(f"nascar_api/schedule/{i}_schedule.csv", index=False)
		del df

	#parse_basic_race_results(current_year)
	for i in range(current_year-1,current_year+1):
		print(f'\nGetting the NASCAR race info for the {i} season.')
		info_df, results_df, cautions_df, leaders_df,\
			stage_df,infractions_df, pitstops_df,\
			 = parse_basic_race_results(i)

		info_df.to_csv(f"nascar_api/race_info/{i}_race_info.csv", index=False)
		results_df.to_csv(f"nascar_api/race_results/{i}_race_results.csv", index=False)
		cautions_df.to_csv(f"nascar_api/race_cautions/{i}_race_cautions.csv", index=False)
		leaders_df.to_csv(f"nascar_api/race_leaders/{i}_race_leaders.csv", index=False)
		stage_df.to_csv(f"nascar_api/race_stage_results/{i}_race_stage_results.csv", index=False)
		infractions_df.to_csv(f"nascar_api/race_infractions/{i}_race_infractions.csv", index=False)
		pitstops_df.to_csv(f"nascar_api/race_pit_stops/{i}_race_pit_stops.csv", index=False)
		#weekend_runs_df.to_csv(f"nascar_api/weekend_runs/{i}_weekend_runs.csv", index=False)

	for i in range(current_year-1,current_year+1):
		print(f'\nGetting the NASCAR weekend runs for the {i} season.')

		weekend_runs_df = parse_weekend_runs(i)
		weekend_runs_df.to_csv(f"nascar_api/weekend_runs/{i}_weekend_runs.csv", index=False)

		schedule_df = parse_nascar_schedule(i, "all")
		
		race_ids_list = schedule_df['race_id'].to_numpy()
		race_levels_list = schedule_df['series_id'].to_numpy()
		race_seasons_list = schedule_df['race_season'].to_numpy()
		
		for j in tqdm(range(0,len(race_ids_list))):
			try:
				race_df = parse_lap_times(race_ids_list[j],race_levels_list[j],race_seasons_list[j])
				race_df.to_csv(f"nascar_api/lap_times/{race_seasons_list[j]}_{race_ids_list[j]}_lap_times.csv",index=False)
				time.sleep(1)
			except:
				print('Couldn\'t parse the race. Breaking the loop.')
				time.sleep(2)
			#print(race_df)

	with open('nascar_api_status.json','w+') as f:
		f.write(f"{{ \"year\":{current_year},\"month\":{current_month},\"day\":{current_day} }}")

if __name__ == "__main__":
	main()