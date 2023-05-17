import PrintsInfo
import team_Info_Pulled
import Roster_and_Trades
import BaseballGameSim
import SimsMultGames

#Checks ID to make sure it corresponds to a team
def IDcheck():
    team_Info_Pulled.checkID()

#Prints Menu Options and takes users input to what is desired
def menu_Options():
    PrintsInfo.Print_Menu_Options()
    procSelc = input()
    while True:
        if procSelc == '6':
            exit()
        elif procSelc == '1':
            BaseballGameSim.Game_Simulation()
            break
        elif procSelc == '2':
            BaseballGameSim.TeamRecord()
            break
        elif procSelc == '4':
            Roster_and_Trades.Trade_Managment()
            break
        elif procSelc == '3':
            Roster_and_Trades.Roster_Managment()
            break
        elif procSelc == '5':
            SimsMultGames.Game_Simulation()
            break
        else:
            print("Invalid Input")
            break

#Main Starts the Code, goes through general contorl flow
class Main:   
    PrintsInfo.Print_Team_ID_and_Name()
    print("Input Team ID:")
    IDcheck()
    print("Getting your team's roster...")
    team_Info_Pulled.getroster()
    while True:
        menu_Options()
    