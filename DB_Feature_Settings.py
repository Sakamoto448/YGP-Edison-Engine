
# These are all columns names for the features that will be used
def Add_Feature_Headers():
    Feature_Names= ['Action','Turn_Count','Phase','Player1_Action','Player2_Action','Player1_Turn','Player2_Turn',
    'Hand_Size_P1','Hand_Size_P2',
    'Deck_Size_P1','Deck_Size_P2',
    'Gy_P1','Gy_P2',
    'Banish_P1','Banish_P2',
    'Monsters_on_Field_P1','Monsters_on_Field_P2',
    'Highest_Atk_P1','Highest_Atk_P2',
    'S/T_on_Field_P1','S/T_on_Field_P2',
    'Face_up_S/T_P1','Face_up_S/T_P2',
    'Total_Atk_on_Field_P1','Total_Atk_on_Field_P2','P1_LP','P2_LP','P1First','P2First']
    return Feature_Names


def Clean_Action (Action):
        if 'Turn' in Action:
            return Action

        if Action[0] != ' ':
            return Clean_Action(Action[1:])
        else:
            return Action[1:]


def Player_Action(ws1,row,Player):

    # Mark 1 for Player Action, 0 for not there Action based on Text Color
    if Player == 'FF0000FF':
        ws1.cell(row + 1, 4, value=1)
        ws1.cell(row + 1, 5, value=0)

    if Player == 'FFFF0000':
        ws1.cell(row + 1, 4, value=0)
        ws1.cell(row + 1, 5, value=1)