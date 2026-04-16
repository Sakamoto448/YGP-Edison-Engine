import openpyxl as ox
from DB_Feature_Settings import Add_Feature_Headers, Clean_Action
import Player_Settings as P


#GLOBALS
Turn_Player = ""
Turn_Count = 0

#Create Players
P1 = P.Player()
P2 = P.Player()

P1.set_Deck_Size(40)
P2.set_Deck_Size(41)

# Read the Dueling Book Log Excel
wb = ox.load_workbook("Db_Test.xlsx")
ws = wb.worksheets[0]

#This worksheet will have the setup with all the data
wb.create_sheet(title='Db_Log', index=None)
ws1 = wb['Db_Log']
ws1.append(Add_Feature_Headers())

# Get DB Log Action Length
Log_length = int(len(ws['A:A']))

# The Check color of the Text in cell, Looking for:
# Blue: FF0000FF
# Red:  FFFF0000

# Add what Player is each action
for row in range(1,Log_length+1):
    r = str(row)
    Check_row = 'A' + r
    #current_row = 'B' + r

    #Value of the Action (Cell)
    Action = Clean_Action(ws[Check_row].value)

    #Move Action to Db_Log Sheet
    ws1.cell(row + 1, 1, value=Action)

    #Color of the Action (Cell)
    Player = ws[Check_row].font.color.rgb

    #Turn Count
    ws1.cell(row + 1, 2, value=Turn_Count)

    # Mark 1 for Player Action, 0 for not there Action based on Text Color
    #Blue (Player 1)
    if Player == 'FF0000FF':
        #ws[current_row] = 'Player1'
        ws1.cell(row + 1, 4, value=1)
        ws1.cell(row + 1, 5, value=0)

        # Find out who is Turn Player then alternate from there
        if Action.lower() == 'Chose to go first'.lower():
            Turn_Player = 'Player1'

        # Game State Actions:
        if Action.lower() == 'Drew a card'.lower():
            P1.Increase_Hand_Size(1)
            P1.Decrease_Deck_Size(1)

#-------------------------------------------------------------------------------------------------#

    #Red (Player 2)
    if Player == 'FFFF0000':
        #ws[current_row] = 'Player2'
        ws1.cell(row + 1, 4, value=0)
        ws1.cell(row + 1, 5, value=1)

        #Turn Player
        if Action.lower() == 'Chose to go first'.lower():
            Turn_Player = 'Player2'

        # Game State Actions:
        if Action.lower() == 'Drew a card'.lower():
            P2.Increase_Hand_Size(1)
            P2.Decrease_Deck_Size(1)

    #Keep track of Turn Player until the end there turn

    if Turn_Player == 'Player1':
        ws1.cell(row + 1, 6, value=1)
        ws1.cell(row + 1, 7, value=0)
    else:
        ws1.cell(row + 1, 6, value=0)
        ws1.cell(row + 1, 7, value=1)

    if Action.lower() == 'Ended turn'.lower():
        if Turn_Player == 'Player1':
            Turn_Player = 'Player2'
            Turn_Count += 1
        else:
            Turn_Player = 'Player1'
            Turn_Count += 1

    #Current Game State

    # Hand Size
    ws1.cell(row + 1, 8, value=P1.Hand_Size)
    ws1.cell(row + 1, 9, value=P2.Hand_Size)

    # Deck Size
    ws1.cell(row + 1, 8, value=P1.Deck_Size)
    ws1.cell(row + 1, 9, value=P2.Deck_Size)

# Save the file
wb.save("Db_Test.xlsx")
print("DONE")
