import team_Info_Pulled
import PrintsInfo
#========================================================================================================================
#Roster Managment For User_Team
#========================================================================================================================
#swaps two players on the roster
def roster_swapper(indx_Mvr,indx_Mvr2):
    #variables for specific cases
    while True:
        if indx_Mvr == 9 or indx_Mvr2 == 9:
            if team_Info_Pulled.u_teamDF.at[indx_Mvr, 'Pos'] != 'P' and team_Info_Pulled.u_teamDF.at[indx_Mvr2, 'Pos'] == 'P' or team_Info_Pulled.u_teamDF.at[indx_Mvr, 'Pos'] == 'P' and team_Info_Pulled.u_teamDF.at[indx_Mvr2, 'Pos'] != 'P':
                print('Cannot make this swap')
                break
            elif team_Info_Pulled.u_teamDF.at[indx_Mvr, 'Pos'] == 'P' and team_Info_Pulled.u_teamDF.at[indx_Mvr2, 'Pos'] == 'P':
                team_Info_Pulled.u_teamDF.loc[indx_Mvr], team_Info_Pulled.u_teamDF.loc[indx_Mvr2] =  team_Info_Pulled.u_teamDF.loc[indx_Mvr2].copy(), team_Info_Pulled.u_teamDF.loc[indx_Mvr].copy()
                print("Swapped")
                break
        elif indx_Mvr > len(team_Info_Pulled.u_teamDF) or indx_Mvr2 > len(team_Info_Pulled.u_teamDF):
            print("Input exceeds Teams Index")
            break
        else:
            team_Info_Pulled.u_teamDF.loc[indx_Mvr], team_Info_Pulled.u_teamDF.loc[indx_Mvr2] =  team_Info_Pulled.u_teamDF.loc[indx_Mvr2].copy(), team_Info_Pulled.u_teamDF.loc[indx_Mvr].copy()
            break
    return team_Info_Pulled.u_teamDF

#Section that deals with roster managment flow
def Roster_Managment():
    while True:
        while True:
            print("Reminder: index 9 acts as the pitcher! Team Roster:")
            print("===============================================================")
            print(team_Info_Pulled.u_teamDF)
            print("===============================================================")
            print("Make Change:(1)")
            print("Back:(2)")
            print("----------------")
            user_Manage_Choice = input()
            if user_Manage_Choice == '1':
                print("Index # to move:")
                indx_Mvr = float(input())
                print("Second Index to move")
                indx_Mvr2 = float(input())
                roster_swapper(indx_Mvr,indx_Mvr2)
            elif user_Manage_Choice == '2':
                break
            elif user_Manage_Choice != 1 and user_Manage_Choice != 2:
                print("Invalid Input")
        break
#================================================================================================================================
#Trade Managment between two teams
#================================================================================================================================
#Makes the swap between user's team and opponents team
def trade_swapper(idx_trd,idx_trd2):
    #variables for specific cases
    while True:
        if idx_trd == 9 or idx_trd2 == 9:
            if team_Info_Pulled.u_teamDF.at[idx_trd, 'Pos'] != 'P' and team_Info_Pulled.opp_team_df.at[idx_trd2,'Pos'] == 'P' or team_Info_Pulled.u_teamDF.at[idx_trd, 'Pos'] == 'P' and team_Info_Pulled.opp_team_df.at[idx_trd2, 'Pos'] != 'P':
                print('Cannot make this swap')
                break
            elif idx_trd > len(team_Info_Pulled.u_teamDF) or idx_trd2 > len(team_Info_Pulled.u_teamDF):
                print("Input exceeds Teams Index")
                break
            elif team_Info_Pulled.u_teamDF.at[idx_trd, 'Pos'] == 'P' and team_Info_Pulled.opp_team_df.at[ idx_trd2, 'Pos'] == 'P':
                team_Info_Pulled.u_teamDF.loc[idx_trd], team_Info_Pulled.opp_team_df.loc[idx_trd2] =  team_Info_Pulled.opp_team_df.loc[idx_trd2].copy(), team_Info_Pulled.u_teamDF.loc[idx_trd].copy()
                print("Swapped")
                break
        elif idx_trd > len(team_Info_Pulled.u_teamDF) or idx_trd2 > len(team_Info_Pulled.u_teamDF):
            print("Input exceeds Teams Index")
            break
        else:
            team_Info_Pulled.u_teamDF.loc[idx_trd], team_Info_Pulled.opp_team_df.loc[idx_trd2] =  team_Info_Pulled.opp_team_df.loc[idx_trd2].copy(), team_Info_Pulled.u_teamDF.loc[idx_trd].copy()
            print("Swapped")
            break
    return team_Info_Pulled.u_teamDF

#Section that deals with trade managment flow
def Trade_Managment():
    print(PrintsInfo.Print_Team_ID_and_Name())
    print("Trade with what team ID?--Give Team ID ")
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
    while True:
        print("-----------------------------------------------------------")
        print("Team Roster:")
        print(team_Info_Pulled.u_teamDF)
        print("-----------------------------------------------------------")
        print("Opposing Team:")
        print(team_Info_Pulled.opp_team_df)
        print("-----------------------------------------------------------")
        print("Make Change:(1)")
        print("Back:(2)")
        print("----------------")
        user_Manage_Choice = input()
        if user_Manage_Choice == '1':
            print("Player to Give:")
            idx_trd = float(input())
            print("Player to recieve:")
            idx_trd2 = float(input())
            trade_swapper(idx_trd,idx_trd2)
        elif user_Manage_Choice == '2':
            break
        elif user_Manage_Choice != 1 and user_Manage_Choice != 2:
            print("Invalid Input")
