import time
import pandas
import random
import PrintsInfo
import team_Info_Pulled
import Roster_and_Trades
#Wins and Losses
global game_num
game_num = 1
global losses
global wins
wins = 0
losses = 0
#Outs for Game
global outs
global outs2
outs = 0
outs2 = 0
#Hitting Loop for lineup
global indx
indx = 0 
global indx2
indx2 = 0
#Home and Away Scores
global home_Score
global away_Score
home_Score = 0
away_Score = 0
global game_Num
game_num = 1
#Inning
global Inning
Inning = 1
#What hit happened
global Hit_Type
Hit_Type = ''
#Is there Runner on base
global runner_on_first
global runner_on_second
global runner_on_third
runner_on_first = 0
runner_on_second = 0
runner_on_third = 0
#Prints Teams Total Record
def TeamRecord():
    print("You have ", wins, " " "wins and " ,losses , "losses.")

#Player Has Drawn a walk
def player_Walks_A():
    #Variables To update game
    global away_Score
    global Hit_Type
    global runner_on_first
    global runner_on_second
    global runner_on_third
    #Set Hit Type
    Hit_Type = 'Walked'
    #Update Runners
    if runner_on_first == 0 and runner_on_second == 0 and runner_on_third == 0:
        runner_on_first = 1
    elif runner_on_first == 1 and runner_on_second == 0 and runner_on_third == 0:
        runner_on_first = 1
        runner_on_second = 1
    elif runner_on_first == 0 and runner_on_second == 1 and runner_on_third == 0:
        runner_on_first = 1
    elif runner_on_first == 1 and runner_on_second == 1 and runner_on_third == 0:
        runner_on_first = 1
        runner_on_second = 1
        runner_on_third = 1
    elif runner_on_first == 1 and runner_on_second == 1 and runner_on_third == 1:
        runner_on_first = 1
        runner_on_second = 1
        runner_on_third = 1
        away_Score = away_Score + 1

#Player Has Drawn a walk
def player_Walks_H():
    #Variables To update game
    global home_Score
    global Hit_Type
    global runner_on_first
    global runner_on_second
    global runner_on_third
    #Set Hit Type
    Hit_Type = 'Walked'
    #Update Runners
    if runner_on_first == 0 and runner_on_second == 0 and runner_on_third == 0:
        runner_on_first = 1
    elif runner_on_first == 1 and runner_on_second == 0 and runner_on_third == 0:
        runner_on_first = 1
        runner_on_second = 1
    elif runner_on_first == 1 and runner_on_second == 1 and runner_on_third == 0:
        runner_on_first = 1
        runner_on_second = 1
        runner_on_third = 1
    elif runner_on_first == 0 and runner_on_second == 1 and runner_on_third == 0:
        runner_on_first = 1
    elif runner_on_first == 1 and runner_on_second == 0 and runner_on_third == 1:
        runner_on_first = 1
        runner_on_second = 1
        runner_on_third = 1
    elif runner_on_first == 1 and runner_on_second == 1 and runner_on_third == 1:
        runner_on_first = 1
        runner_on_second = 1
        runner_on_third = 1
        home_Score = home_Score + 1

#Hitting for away
def hit_result_A():
    global away_Score
    global Hit_Type
    global runner_on_first
    global runner_on_second
    global runner_on_third
    rc_hit = random.uniform(0,100)
    if rc_hit <= 3:
        #Triple + Runs Scored (If runners on base)
        Hit_Type = 'Triple'
        triple_runs = runner_on_first + runner_on_second + runner_on_third
        away_Score = away_Score + triple_runs
        #Clear bases (Except third, stays or sets)
        runner_on_first = 0
        runner_on_second = 0
        runner_on_third = 1
    elif 3 < rc_hit <= 17 :
        #Home Run + Runs Scored
        Hit_Type = 'Home Run'
        hr_runs = runner_on_first + runner_on_second + runner_on_third + 1
        away_Score = away_Score + hr_runs
        #Clear Bases
        runner_on_first = 0
        runner_on_second = 0
        runner_on_third = 0
    elif 17 < rc_hit < 38:
        #Double + Runs Scored (If runners on base)
        Hit_Type = 'Double'
        #Double Cases
        if runner_on_first == 1 and runner_on_second == 0 and runner_on_third == 0:
            runner_on_third = 1
            runner_on_first = 0
        elif runner_on_first == 1 and runner_on_second == 1 and runner_on_third == 0:
            away_Score = away_Score + 1
            runner_on_third = 1
        elif runner_on_first == 0 and runner_on_second == 0 and runner_on_third == 1:
            away_Score = away_Score + 1
            runner_on_third = 0
        elif runner_on_first == 0 and runner_on_second == 1 and runner_on_third == 1:
            away_Score = away_Score + 2 
            runner_on_third = 0 
        elif runner_on_first == 1 and runner_on_second == 1 and runner_on_third == 1:
            away_Score = away_Score + 2
            runner_on_first = 0 
        runner_on_second = 1

    elif 38 < rc_hit < 100:
        #Single + Hit Cases
        Hit_Type = 'Single'
        #Advancing Runners on first, second with nobody on third
        if runner_on_third != 1:
            if runner_on_first == 0 and runner_on_second == 0:
                runner_on_first = 1
            elif runner_on_first == 1 and runner_on_second == 0:
                runner_on_first = 1
                runner_on_second = 1
            elif runner_on_first == 1 and runner_on_second == 1:
                runner_on_first = 1
                runner_on_second = 1
                runner_on_third = 1
            elif runner_on_first == 0 and runner_on_second == 1:
                runner_on_first = 1
                runner_on_second = 0
                runner_on_third = 1
        #Advances Runners on first and second, and scores the run on third
        elif runner_on_third == 1:
            if runner_on_first == 0 and runner_on_second == 0:
                away_Score = away_Score + 1
                runner_on_third = 0
                runner_on_first = 1
            elif runner_on_first == 1 and runner_on_second == 0:
                away_Score = away_Score + 1
                runner_on_third = 0
                runner_on_first = 1
                runner_on_second = 1
            elif runner_on_first == 0 and runner_on_second == 1:
                away_Score = away_Score + 1
                runner_on_first = 1
                runner_on_second = 0
                runner_on_third = 1
            elif runner_on_first == 1 and runner_on_second == 1:
                away_Score = away_Score + 1
                runner_on_first = 1
                runner_on_second = 1
                runner_on_third = 1
        runner_on_first = 1

#Hit % for player
def home_calculations():
    plyr_hits = team_Info_Pulled.u_teamDF.at[indx2,'Hits']
    plyr_doubles = team_Info_Pulled.u_teamDF.at[indx2,'Doubles']
    plyr_triples = team_Info_Pulled.u_teamDF.at[indx2,'Triples']
    plyr_homeruns = team_Info_Pulled.u_teamDF.at[indx2,'Home Runs']
    plyr_singles = plyr_hits - plyr_doubles - plyr_triples - plyr_homeruns
    single = plyr_singles / plyr_hits
    double = plyr_doubles / plyr_hits
    triple = plyr_triples / plyr_hits
    homerun = plyr_homeruns / plyr_hits
    return single,double,triple,homerun

#Hitting for home
def hit_result_H():
    global home_Score
    global Hit_Type
    global runner_on_first
    global runner_on_second
    global runner_on_third

    #single,double,triple,homerun = home_calculations() 

    rc_hit = random.uniform(0,1)

    if rc_hit <= 3:
        #Triple + Runs Scored (If runners on base)
        Hit_Type = 'Triple'
        triple_runs = runner_on_first + runner_on_second + runner_on_third
        home_Score = home_Score + triple_runs
        #Clear bases (Except third, stays or sets)
        runner_on_first = 0
        runner_on_second = 0
        runner_on_third = 1
    elif 3 < rc_hit <= 17 :
        #Home Run + Runs Scored
        Hit_Type = 'Home Run'
        hr_runs = runner_on_first + runner_on_second + runner_on_third + 1
        home_Score = home_Score + hr_runs
        #Clear Bases
        runner_on_first = 0
        runner_on_second = 0
        runner_on_third = 0
    elif 17 < rc_hit < 38:
        #Double + Runs Scored (If runners on base)
        Hit_Type = 'Double'
        double_runs = runner_on_second + runner_on_third
        home_Score = home_Score + double_runs
        #Double Cases
        if runner_on_first == 1 and runner_on_second == 0 and runner_on_third == 0:
            runner_on_third = 1
            runner_on_first = 0
        elif runner_on_first == 1 and runner_on_second == 1 and runner_on_third == 0:
            home_Score = home_Score + 1
            runner_on_third = 1
        elif runner_on_first == 0 and runner_on_second == 0 and runner_on_third == 1:
            home_Score = home_Score + 1
            runner_on_third = 0
        elif runner_on_first == 0 and runner_on_second == 1 and runner_on_third == 1:
            home_Score = home_Score + 2 
            runner_on_third = 0 
        elif runner_on_first == 1 and runner_on_second == 1 and runner_on_third == 1:
            home_Score = home_Score + 2
            runner_on_first = 0 
        runner_on_second = 1

    elif 38 < rc_hit < 100:
        #Single + Hit Cases
        Hit_Type = 'Single'
        #Advancing Runners on first, second with nobody on third
        if runner_on_third != 1:
            if runner_on_first == 0 and runner_on_second == 0:
                runner_on_first = 1
            elif runner_on_first == 1 and runner_on_second == 0:
                runner_on_first = 1
                runner_on_second = 1
            elif runner_on_first == 1 and runner_on_second == 1:
                runner_on_first = 1
                runner_on_second = 1
                runner_on_third = 1
            elif runner_on_first == 0 and runner_on_second == 1:
                runner_on_first = 1
                runner_on_second = 0
                runner_on_third = 1
        #Advances Runners on first and second, and scores the run on third
        elif runner_on_third == 1:
            if runner_on_first == 0 and runner_on_second == 0:
                home_Score = home_Score + 1
                runner_on_third = 0
                runner_on_first = 1
            elif runner_on_first == 1 and runner_on_second == 0:
                home_Score = home_Score + 1
                runner_on_third = 0
                runner_on_first = 1
                runner_on_second = 1
            elif runner_on_first == 0 and runner_on_second == 1:
                home_Score = home_Score + 1
                runner_on_first = 1
                runner_on_second = 0
                runner_on_third = 1
            elif runner_on_first == 1 and runner_on_second == 1:
                home_Score = home_Score + 1
                runner_on_first = 1
                runner_on_second = 1
                runner_on_third = 1

#Hitting For Home and Away Team for the Inning            
def hitting_for_Inning():
    global outs
    global outs2
    global indx
    global indx2
    global home_Score
    global away_Score
    global runner_on_first
    global runner_on_second
    global runner_on_third
    #Plays out hitting for Inning
    while True:
        #Start Away Hittting
        while outs != 3:
            #time.sleep(.5)
            #Resets Batting Order
            if indx2 == 9:
                indx2 = 0
            #Away Team DF to get values
            plyr_avg= team_Info_Pulled.opp_team_df.at[indx2,'Avg']
            plyr_Name = team_Info_Pulled.opp_team_df.at[indx2,'Name']
            opp_plyr_OBP = team_Info_Pulled.opp_team_df.at[indx,'OBP']
            ptch_avg_own = team_Info_Pulled.u_teamDF.at[9,'BAa']#Users Pitchers BAA
            #Inital Math for AB
            hit_Chance = (plyr_avg *(ptch_avg_own/.243))/(plyr_avg*(ptch_avg_own/.243)+((1 - plyr_avg)*((1 - ptch_avg_own)/(1 - lg_hit_avg))))
            walk_math = opp_plyr_OBP - hit_Chance
            walk_Chance = walk_math + hit_Chance
            r_chance = random.uniform(0, 1)
            #Hit,Walk, or out result and print
            if hit_Chance > r_chance:
                hit_result_A()
                #print(plyr_Name, "Hit for:", Hit_Type)
                indx2 = indx2 + 1
            elif walk_Chance > r_chance:
                player_Walks_A()
                #print(plyr_Name, "Was", Hit_Type)
                indx2 = indx2 + 1
            else:
                #Out_Result_A()
                #print("An out for:", plyr_Name)
                outs = outs + 1
                outs2 = 0
                indx2 = indx2 + 1
        #Switch
        #print("-------------------------------------------------------------")
        #print("Switch Sides! " "Heading into the bottom of Inning", Inning)
        #print("-------------------------------------------------------------")
        #Clear Bases
        runner_on_first = 0
        runner_on_second = 0
        runner_on_third = 0
        #Start Home Hitting
        while outs2 != 3:
            #time.sleep(.5)
            #Specific case if home team is winning in the 9th they dont need to hit
            if Inning == 9 and home_Score > away_Score:
                walk_off_count = 0
                if walk_off_count == 0:
                    #print("------------------------------------------------------")
                    #print("Home Team doesn't need to hit because they are winning")
                    walk_off_count = walk_off_count + 1
                else:
                    #print("------------------------------------------------------")
                    #print("A Spectacular walkoff for ",plyr_Name,"with a game winning",Hit_Type)
                    outs = 0
                break
            elif Inning >= 9 and home_Score > away_Score:
                outs = 0
                #print("------------------------------------------------------")
                #print("A Spectacular walkoff for ",plyr_Name,"with a game winning",Hit_Type)
                break
            #resets batting order
            if indx == 9:
                indx = 0
            #Home Team DF to get values
            plyr_avg= team_Info_Pulled.u_teamDF.at[indx,'Avg']
            plyr_Name = team_Info_Pulled.u_teamDF.at[indx,'Name']
            plyr_OBP = team_Info_Pulled.u_teamDF.at[indx,'OBP']
            ptch_avg_opp = team_Info_Pulled.opp_team_df.at[9,'BAa']#Opposing Pitcher BAA
            #Inital Math determining values for hit chance and walk chance
            hit_Chance = (plyr_avg *(ptch_avg_opp/.243))/(plyr_avg*(ptch_avg_opp/.243)+((1 - plyr_avg)*((1 - ptch_avg_opp)/(1 - lg_hit_avg))))
            walk_math = plyr_OBP - hit_Chance
            walk_Chance = walk_math + hit_Chance
            r_chance = random.uniform(0, 1)
            #Outcome and print result
            if hit_Chance > r_chance:
                hit_result_H()
                #print(plyr_Name, "Hit for:", Hit_Type)
                indx = indx + 1
            elif walk_Chance > r_chance:
                player_Walks_H()
                #print(plyr_Name, "Was", Hit_Type)
                indx = indx + 1
            else:
                #Out_Result_H()
                #print("An Out for", plyr_Name)
                outs2 = outs2 + 1
                outs = 0
                indx = indx + 1
        #Clear Bases
        runner_on_first = 0
        runner_on_second = 0
        runner_on_third = 0
        break

#Manager Wants to make changes during the game
def make_Changes():
    while True:
        while True:
            current_depth = len(team_Info_Pulled.u_teamDF)
            print("--------------------------------------")
            print("Current Lineup:")
            current_lineup = team_Info_Pulled.u_teamDF.loc[0:9]
            print(current_lineup)
            print("----------------")
            print("Avalible Swaps:")
            print("----------------")
            current_bench = team_Info_Pulled.u_teamDF.loc[10:current_depth]
            print(current_bench)
            print("----------------")
            print("Make Changes:(1)")
            print("Return to game:(2)")
            print("----------------")
            user_desire_change = input()
            if user_desire_change == '1':
                print("Index # to move:")
                indx_Mvr = float(input())
                print("Second Index to move")
                indx_Mvr2 = float(input())
                print("Swapped")
                Roster_and_Trades.roster_swapper(indx_Mvr,indx_Mvr2)
            elif user_desire_change == '2':
                break
            elif user_desire_change != '1' and user_desire_change != '2':
                print("Invalid Input")
        break

#Main Control for the Game
def Game_Simulation():
    PrintsInfo.Print_Team_ID_and_Name()
    print("Select team to play!")
    while True:
        try:
            opptID = input()
            if opptID in team_Info_Pulled.team_ID_List:
                pass
                break
            else:
                print("This Number does not correspond to a team! Input a valid team:")
        except:
            continue
    team_Info_Pulled.getopproster(opptID)
    global wins
    global losses
    global home_Score
    global away_Score
    global indx
    global indx2
    global Inning
    global game_num
    high_score = 0
    Inning = 1
    #Checks to make sure new pitcher is starting
    #after team selected roster is adjusted
    # Game can start
    print("=============================")
    print("Play Ball, Game:", game_num)
    print("=============================")
    #time.sleep(1.5)
    simgameCount = 0
    while simgameCount != 1000:
        #What is Inning/Score and Results
        #time.sleep(1.0)
        while True:
        #Go into Hitting for Inning
            if Inning < 9:
                #print("==============================================================")
                #print("Inning:", Inning, "The Score is:", home_Score, "-", away_Score)
                #print("==============================================================")
                #Asks if change is desired
                #print("Want to make changes?(y/n)")
                '''
                while True:
                    mk_change = input()
                    if mk_change == 'y':
                        make_Changes()
                        break
                    elif mk_change == 'n':
                        break
                    else:
                        print("Invalid input")
                print("------------------------------------------------------")
                '''
                hitting_for_Inning()
                Inning = Inning + 1
            elif Inning == 9:
                '''
                print("==============================================================")
                print("Inning:", Inning, "The Score is:", home_Score, "-", away_Score)
                print("==============================================================")
                #Asks if change is desired
                print("Want to make changes?(y/n)")
                while True:
                    mk_change = input()
                    if mk_change == 'y':
                        make_Changes()
                        break
                    elif mk_change == 'n':
                        break
                    else:
                        print("Invalid input")
                print("------------------------------------------------------")
                '''
                hitting_for_Inning()

                Inning = Inning + 1 
            elif Inning >= 10 and home_Score == away_Score:
                '''
                print("==============================================================")
                print("Extra Inning:", Inning, "The Score is:", home_Score, "-", away_Score)
                print("==============================================================")
                #Asks if change is desired
                print("Want to make changes?(y/n)")
                while True:
                    mk_change = input()
                    if mk_change == 'y':
                        make_Changes()
                        break
                    elif mk_change == 'n':
                        break
                    else:
                        print("Invalid input")
                print("------------------------------------------------------")
                '''
                hitting_for_Inning()
                Inning = Inning + 1
            else:
                if high_score < home_Score:
                    high_score = home_Score
                    highgame = game_num
                    team_high = 'The Home Team!'
                elif high_score < away_Score:
                    high_score = away_Score
                    highgame = game_num
                    team_high = 'The Away Team!'
                if home_Score > away_Score:
                    print("============================")
                    print("Secured the win!")
                    print("Home Score:", home_Score, " Away Score:", away_Score)
                    wins = wins + 1
                    simgameCount = simgameCount + 1
                elif away_Score > home_Score:
                    print("============================")
                    print("A devistating loss!")
                    print("Home Score:", home_Score, " Away Score:", away_Score)
                    losses = losses + 1
                    simgameCount = simgameCount + 1
                elif home_Score == away_Score:
                    print("How did this happen!!!")
                    pass
                break
        print("============================================================================================")
        print("Game:", game_num, "and the final score:", home_Score, '-',away_Score)
        print("============================================================================================")
        home_Score = 0
        away_Score = 0 
        indx = 0
        indx2 = 0
        game_num = game_num + 1
        Inning = 1
    print("Final Record:", wins, "-", losses)
    print("--------------------------------")
    print("The Highest Score was", high_score,"in game", highgame,"by",team_high)
    print("============================================================================================")


#League Average
lg_plyr = ["Avg Joe"]
lg_bat_avg = [.243]
lg_df = pandas.DataFrame({'Player': lg_plyr, 'lg avg': lg_bat_avg})
lg_hit_avg = lg_df.at[0,'lg avg']
