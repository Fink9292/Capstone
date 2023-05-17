import mlbstatsapi
import pandas
import csv
global opp_team_df
global u_teamDF

mlb = mlbstatsapi.Mlb()

#======================================================================================================================================================================
#Small Pandas DB that assigns Teams their values
#======================================================================================================================================================================
team_Name_List = ["Oakland Athletics","Pittsburg Pirates","San Diego Padres","Seattle Mariners","San Francisco Giants","St.Louis Cardinals","Tampa Bay Rays","Texas Rangers","Toronto Blue Jays","Minnesota Twins","Philadelphia Phillies","Atlanta Braves","Chicago White Sox", "Miami Marlins","New York Yankees","Milwalkee Brewers", "Los Angeles Angles","Arizona Diamondbacks","Baltimore Orioles","Boston Red Sox", "Chicago Cubs","Cincinatti Reds","Cleveland Guardians","Colorado Rockies","Detroit Tigers","Houston Astros","Kansas City Royals","Los Angeles Dodgers", "Washington Nationals","New York Mets"]
team_ID_List =  ['133','134','135','136','137','138','139','140','141','142','143','144','145','146','147','158','108','109','110','111','112','113','114','115','116','117','118','119','120','121']
team_Df = pandas.DataFrame({'Team ID': team_ID_List, 'Team Name': team_Name_List})
#======================================================================================================================================================================
#Checks if selected team ID is in the list or not
#======================================================================================================================================================================
def checkID():
    global utID
    while True:
        try:
            userteamID = input()
            if userteamID in team_ID_List:
                utID = userteamID
                tID = team_Df[team_Df['Team ID'] == userteamID].index[0]
                tno = team_Df.at[tID, 'Team Name']
                print("You have selected the" + " " + tno + "!")
                break
            else:
                print("This Number does not correspond to a team! Input a valid team:")
        except:
            continue

#====================================================================================================================================
#Attempt to get team roster to csv
# os.environ['MLB_API_KEY'] = 'b0b7a7b0-7f1a-4b1e-8b0e-2b9b5b'
#====================================================================================================================================
def getroster():
    #Global user team DF
    global u_teamDF
    #Gets Teams Information
    #response = mlb.get_team_roster(139)
    response = mlb.get_team_roster(utID)
    team = {}
    for i in response:
        player = {}
        for k, v in i.__dict__.items():
            player[k] = v
        primaryposition = {}
        for m, n in player["primaryposition"].__dict__.items():
            primaryposition[m] = n
        player["primaryposition"] = primaryposition
        player["stats"] = mlb.get_player_stats(player["id"], ["season"], ["hitting", "pitching", "fielding", "running"]) 
        try: 
            for split in player["stats"]["hitting"]["season"].splits:
                for k, v in split.stat.__dict__.items():
                    player["stats"]["hitting"][k] = v
        except:
            pass
        try:
            for split in player["stats"]["pitching"]["season"].splits:
                for k, v in split.stat.__dict__.items():
                    player["stats"]["pitching"][k] = v
        except:
            pass
        try:
            for split in player["stats"]["fielding"]["season"].splits:
                for k, v in split.stat.__dict__.items():
                    player["stats"]["fielding"][k] = v
        except:
            pass
        team[player["id"]] = player

    #=============================================================
    #Write the CSV
    #=============================================================
    #Opens csv file and writes down the information called from API into the file
    with open('User_Team.csv', mode='w', newline='') as csvfile:
        fieldnames = ['Name', 'Pos', '|', 'PA','Avg', 'OBP', 'Walks','Hits', 'Doubles', 'Triples', 'Home Runs', 'SO', 'GO', 'FO', '|||', 'ABa','BAa', 'OBPa', 'Wa', 'Ha', '2Ba', '3Ba', 'HRa', 'SOf','GOf','FOf'] #['Pitching Stats', 'Fielding Stats', 'Running Stats']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for player_id, player_info in team.items():
            team_stats = team.get(player_id, {}).get('stats', {})
            hitting_stats = team_stats.get('hitting', {})
            pitching_stats = team_stats.get('pitching',{})
            #fielding_stats = team_stats.get('fielding',{})
            #running_stats = team_stats.get('running',{})
            #================================================
            #Cases for Hitting
            #================================================
            if 'avg' in hitting_stats:
                plyr_avg = hitting_stats['avg']
            else:
                plyr_avg = 0
            if 'obp' in hitting_stats:
                plyr_OBP = hitting_stats['obp']  
            else:
                plyr_OBP = 0
            if 'strikeouts' in hitting_stats:
                plyr_SO = hitting_stats['strikeouts']  
            else:
                plyr_SO = 0
            if 'doubles' in hitting_stats:
                plyr_doubles = hitting_stats['doubles']  
            else:
                plyr_doubles = 0  
            if 'triples' in hitting_stats:
                plyr_triples = hitting_stats['triples']  
            else:
                plyr_triples = 0    
            if 'homeruns' in hitting_stats:
                plyr_home_runs = hitting_stats['homeruns']  
            else:
                plyr_home_runs = 0
            if 'hits' in hitting_stats:
                plyr_hits = hitting_stats['hits']
            else:
                plyr_hits = 0
            if 'plateappearances' in hitting_stats:
                plyr_PA = hitting_stats['plateappearances']
            else:
                plyr_PA = 0
            if 'groundouts' in hitting_stats:
                plyr_GO = hitting_stats['groundouts']  
            else:
                plyr_GO = 0
            if 'airouts' in hitting_stats:
                plyr_FO = hitting_stats['airouts']  
            else:
                plyr_FO = 0
            if 'baseonballs' in hitting_stats:
                plyr_walks = hitting_stats['baseonballs']  
            else:
                plyr_walks = 0 
            #================================================                      
            #Cases for Pitching
            #================================================
            if 'atbats' in pitching_stats:
                plyr_ABA = pitching_stats['atbats']
            else:
                plyr_ABA = 0
            if 'avg' in pitching_stats:
                plyr_BAA = pitching_stats['avg']
            else:
                plyr_BAA = 0
            if 'strikeouts' in pitching_stats:
                plyr_SO_p = pitching_stats['strikeouts']  
            else:
                plyr_SO_p = 0
            if 'doubles' in pitching_stats:
                plyr_doubles_p = pitching_stats['doubles']  
            else:
                plyr_doubles_p = 0   
            if 'triples' in pitching_stats:
                plyr_triples_p = pitching_stats['triples']  
            else:
                plyr_triples_p = 0  
            if 'homeruns' in pitching_stats:
                plyr_home_runs_p = pitching_stats['homeruns']  
            else:
                plyr_home_runs_p = 0
            if 'hits' in pitching_stats:
                plyr_hits_p = pitching_stats['hits']
            else:
                plyr_hits_p = 0
            if 'obp' in pitching_stats:
                plyr_obp_p = pitching_stats['obp']
            else:
                plyr_obp_p = 0
            if 'baseonballs' in pitching_stats:
                plyr_walks_p = pitching_stats['baseonballs']  
            else:
                plyr_walks_p = 0
            if 'groundouts' in pitching_stats:
                plyr_GO_p = pitching_stats['groundouts']  
            else:
                plyr_GO_p = 0
            if 'airouts' in pitching_stats:
                plyr_FO_p = pitching_stats['airouts']  
            else:
                plyr_FO_p = 0
            #================================================
            #Basic Player Info
            #================================================
            name = team[player_id]['fullname']
            plyr_position = team[player_id]['primaryposition']['abbreviation']
            #================================================
            #Writes Rows of player information
            #================================================
            writer.writerow({
                'Name': name,
                'Pos': plyr_position,
                '|': '|',
                'PA':plyr_PA,
                'Avg': plyr_avg,
                'OBP': plyr_OBP,
                'Walks': plyr_walks,
                'Hits':plyr_hits,
                'Doubles': plyr_doubles,
                'Triples': plyr_triples,
                'Home Runs': plyr_home_runs,
                'SO': plyr_SO,
                'GO': plyr_GO,
                'FO': plyr_FO,
                '|||': '|||',
                'ABa': plyr_ABA,
                'BAa': plyr_BAA,
                'OBPa': plyr_obp_p,
                'Wa': plyr_walks_p,
                'Ha': plyr_hits_p,
                '2Ba': plyr_doubles_p,
                '3Ba': plyr_triples_p,
                'HRa': plyr_home_runs_p,
                'SOf': plyr_SO_p,
                'GOf': plyr_GO_p,
                'FOf': plyr_FO_p
            })

    #====================================================
    #Get CSV into pandas DF
    #====================================================
    u_teamDF_csv_read = pandas.read_csv('User_Team.csv')
    u_teamDF = u_teamDF_csv_read
    print(u_teamDF)  

#==================================================================================================
#Get Opposing Teams Roster
#==================================================================================================
def getopproster(opptID):
    global opp_team_df
    response = mlb.get_team_roster(opptID)
    team = {}
    for i in response:
        player = {}
        for k, v in i.__dict__.items():
            player[k] = v
        primaryposition = {}
        for m, n in player["primaryposition"].__dict__.items():
            primaryposition[m] = n
        player["primaryposition"] = primaryposition
        player["stats"] = mlb.get_player_stats(player["id"], ["season"], ["hitting", "pitching", "fielding", "running"]) 
        try: 
            for split in player["stats"]["hitting"]["season"].splits:
                for k, v in split.stat.__dict__.items():
                    player["stats"]["hitting"][k] = v
        except:
            pass
        try:
            for split in player["stats"]["pitching"]["season"].splits:
                for k, v in split.stat.__dict__.items():
                    player["stats"]["pitching"][k] = v
        except:
            pass
        try:
            for split in player["stats"]["fielding"]["season"].splits:
                for k, v in split.stat.__dict__.items():
                    player["stats"]["fielding"][k] = v
        except:
            pass
        team[player["id"]] = player

    #=============================================================
    #Write the CSV
    #=============================================================
    #Opens csv file and writes down the information called from API into the file
    with open('Opp_Team.csv', mode='w', newline='') as csvfile:
        fieldnames = ['Name', 'Pos', '|', 'PA','Avg', 'OBP', 'Walks','Hits', 'Doubles', 'Triples', 'Home Runs', 'SO', 'GO', 'FO', '|||', 'ABa','BAa', 'OBPa', 'Wa', 'Ha', '2Ba', '3Ba', 'HRa', 'SOf','GOf','FOf'] #['Pitching Stats', 'Fielding Stats', 'Running Stats']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for player_id, player_info in team.items():
            team_stats = team.get(player_id, {}).get('stats', {})
            hitting_stats = team_stats.get('hitting', {})
            pitching_stats = team_stats.get('pitching',{})
            #fielding_stats = team_stats.get('fielding',{})
            #running_stats = team_stats.get('running',{})
            #================================================
            #Cases for Hitting
            #================================================
            if 'avg' in hitting_stats:
                plyr_avg = hitting_stats['avg']
            else:
                plyr_avg = 0
            if 'obp' in hitting_stats:
                plyr_OBP = hitting_stats['obp']  
            else:
                plyr_OBP = 0
            if 'strikeouts' in hitting_stats:
                plyr_SO = hitting_stats['strikeouts']  
            else:
                plyr_SO = 0
            if 'doubles' in hitting_stats:
                plyr_doubles = hitting_stats['doubles']  
            else:
                plyr_doubles = 0  
            if 'triples' in hitting_stats:
                plyr_triples = hitting_stats['triples']  
            else:
                plyr_triples = 0    
            if 'homeruns' in hitting_stats:
                plyr_home_runs = hitting_stats['homeruns']  
            else:
                plyr_home_runs = 0
            if 'hits' in hitting_stats:
                plyr_hits = hitting_stats['hits']
            else:
                plyr_hits = 0
            if 'plateappearances' in hitting_stats:
                plyr_PA = hitting_stats['plateappearances']
            else:
                plyr_PA = 0
            if 'groundouts' in hitting_stats:
                plyr_GO = hitting_stats['groundouts']  
            else:
                plyr_GO = 0
            if 'airouts' in hitting_stats:
                plyr_FO = hitting_stats['airouts']  
            else:
                plyr_FO = 0
            if 'baseonballs' in hitting_stats:
                plyr_walks = hitting_stats['baseonballs']  
            else:
                plyr_walks = 0 
            #================================================                      
            #Cases for Pitching
            #================================================
            if 'atbats' in pitching_stats:
                plyr_ABA = pitching_stats['atbats']
            else:
                plyr_ABA = 0
            if 'avg' in pitching_stats:
                plyr_BAA = pitching_stats['avg']
            else:
                plyr_BAA = 0
            if 'strikeouts' in pitching_stats:
                plyr_SO_p = pitching_stats['strikeouts']  
            else:
                plyr_SO_p = 0
            if 'doubles' in pitching_stats:
                plyr_doubles_p = pitching_stats['doubles']  
            else:
                plyr_doubles_p = 0   
            if 'triples' in pitching_stats:
                plyr_triples_p = pitching_stats['triples']  
            else:
                plyr_triples_p = 0  
            if 'homeruns' in pitching_stats:
                plyr_home_runs_p = pitching_stats['homeruns']  
            else:
                plyr_home_runs_p = 0
            if 'hits' in pitching_stats:
                plyr_hits_p = pitching_stats['hits']
            else:
                plyr_hits_p = 0
            if 'obp' in pitching_stats:
                plyr_obp_p = pitching_stats['obp']
            else:
                plyr_obp_p = 0
            if 'baseonballs' in pitching_stats:
                plyr_walks_p = pitching_stats['baseonballs']  
            else:
                plyr_walks_p = 0
            if 'groundouts' in pitching_stats:
                plyr_GO_p = pitching_stats['groundouts']  
            else:
                plyr_GO_p = 0
            if 'airouts' in pitching_stats:
                plyr_FO_p = pitching_stats['airouts']  
            else:
                plyr_FO_p = 0
            #================================================
            #Basic Player Info
            #================================================
            name = team[player_id]['fullname']
            plyr_position = team[player_id]['primaryposition']['abbreviation']
            #================================================
            #Writes Rows of player information
            #================================================
            writer.writerow({
                'Name': name,
                'Pos': plyr_position,
                '|': '|',
                'PA':plyr_PA,
                'Avg': plyr_avg,
                'OBP': plyr_OBP,
                'Walks': plyr_walks,
                'Hits':plyr_hits,
                'Doubles': plyr_doubles,
                'Triples': plyr_triples,
                'Home Runs': plyr_home_runs,
                'SO': plyr_SO,
                'GO': plyr_GO,
                'FO': plyr_FO,
                '|||': '|||',
                'ABa': plyr_ABA,
                'BAa': plyr_BAA,
                'OBPa': plyr_obp_p,
                'Wa': plyr_walks_p,
                'Ha': plyr_hits_p,
                '2Ba': plyr_doubles_p,
                '3Ba': plyr_triples_p,
                'HRa': plyr_home_runs_p,
                'SOf': plyr_SO_p,
                'GOf': plyr_GO_p,
                'FOf': plyr_FO_p
            })

    #====================================================
    #Get CSV into pandas DF
    #====================================================
    opp_teamDF_csv_read = pandas.read_csv('Opp_Team.csv')
    opp_team_df = opp_teamDF_csv_read  






'''
#===========================================================================================================================================================================
#Emergency DB's for Testing
#===========================================================================================================================================================================
#Home Team DB
own_player = ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6","Player 7","Player 8","Player 9","Player 10","Player 11","Player 12","Player 13","Player 14","Player 15"]
own_player_avg = [.312,.175,.286,.260,.190,.280,.216,.296,.250,.210,.230,.287,.180,.295,.390]
own_player_pos = ['CF','2B','SS','RF','LF','3B','DH','1B','C','P','DH','P','P','2B','LF']
own_player_OBP = [.322,.198,.321,.318,.195,.306,.220,.333,.296,.293,.340,.370,.200,.310,.420]
own_player_AB = [1000,1250,1500,1750,2000,2250,2500,2750,3000,100,5000,100,100,1000,1000]
own_team_df = pandas.DataFrame({'Player': own_player,'Position': own_player_pos,'Avg': own_player_avg,'OBP': own_player_OBP,'ABs': own_player_AB})
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Away Team DB
opp_player = ["Opponent 1","Opponent 2","Opponent 3","Opponent 4","Opponent 5","Opponent 6","Opponent 7","Opponent 8","Opponent 9","Opponent 10","Opponent 11","Opponent 12","Opponent 13","Opponent 14","Opponent 15"]
opp_player_pos = ['2B','C','CF','DH','LF','3B','RF','1B','SS','P','DH','LF','P','2B','P']
opp_player_avg = [.212,.264,.286,.260,.312,.280,.430,.296,.250,.210,.230,.222,.210,.295,.193]
opp_player_OBP = [.289,.314,.321,.318,.313,.306,.450,.333,.296,.293,.340,.370,.220,.296,.200]
opp_player_AB = [1250,1000,2000,1500,1750,2000,2250,2500,2750,100,4000,1000,100,3000,100]
opp_team_df = pandas.DataFrame({'Player': opp_player,'Position': opp_player_pos,'Avg': opp_player_avg,'OBP': opp_player_OBP,'ABs': opp_player_AB})
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
