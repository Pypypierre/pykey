import tkinter 

LST_Index = [ 0 ]

def FNC_Command ( ) :
    MNU_Command.add ( "command" , label = "Nouveau" )

def FNC_Cascade ( ) :
    MNU_Nouveau = tkinter.Menu ( MNU_MenuCommand )
    MNU_Nouveau.add ( "command" , label = "Nouveau Choix 1" )
    MNU_Nouveau.add ( "command" , label = "Nouveau Choix 2" )
    MNU_Nouveau.add ( "command" , label = "Nouveau Choix 3" )
    MNU_Command.add ( "cascade" , label = "Nouveau cascade" , menu = MNU_Nouveau )

def FNC_Separator ( Q ) :
    if Q == 0 : MNU_Command.add ( "separator" )
    if Q == 1 : MNU_Check.add ( "separator" )
    if Q == 2 : MNU_Radio.add ( "separator" )

def FNC_Checkbutton ( ) :
    LST_Index [ 0 ] += 1
    MNU_Check.add ( "checkbutton" , label = "Nouveau" , onvalue = LST_Index [ 0 ] , variable = TKV_Checkbutton )

def FNC_Radiobutton ( ) :
    LST_Index [ 0 ] += 1
    MNU_Radio.add ( "radiobutton" , label = "Nouveau" , value = LST_Index [ 0 ] )

TKI_Principal = tkinter.Tk ( )
TKV_Checkbutton = tkinter.IntVar ( )
TKV_Radiobutton = tkinter.IntVar ( )

FRA_Menu = tkinter.Frame ( TKI_Principal )
MNU_MenuCommand = tkinter.Menubutton ( FRA_Menu , text = "Command" )
MNU_MenuCheck = tkinter.Menubutton ( FRA_Menu , text = "Checkbutton" )
MNU_MenuRadio = tkinter.Menubutton ( FRA_Menu , text = "Radiobutton" )
MNU_MenuQuitter = tkinter.Menubutton ( FRA_Menu , text = "Quitter" )

MNU_Command = tkinter.Menu ( MNU_MenuCommand )
MNU_Command.add ( "command" , label = "Ajouter command" , command = FNC_Command )
MNU_Command.add ( "command" , label = "Ajouter cascade" , command = FNC_Cascade )
MNU_Command.add ( "command" , label = "Ajouter separator" , command = lambda : FNC_Separator ( 0 ) )
MNU_Command.add ( "separator" )

MNU_Check = tkinter.Menu ( MNU_MenuCheck )
MNU_Check.add ( "command" , label = "Ajouter checkbutton" , command = FNC_Checkbutton )
MNU_Check.add ( "command" , label = "Ajouter separator" , command = lambda : FNC_Separator ( 1 ) )
MNU_Check.add ( "separator" )

MNU_Radio = tkinter.Menu ( MNU_MenuRadio )
MNU_Radio.add ( "command" , label = "Ajouter radiobutton" , command = FNC_Radiobutton )
MNU_Radio.add ( "command" , label = "Ajouter separator" , command = lambda : FNC_Separator ( 2 ) )
MNU_Radio.add ( "separator" )

MNU_Quitter = tkinter.Menu ( MNU_MenuQuitter , postcommand = TKI_Principal.destroy )

MNU_MenuCommand [ "menu" ] = MNU_Command
MNU_MenuCheck [ "menu" ] = MNU_Check
MNU_MenuRadio [ "menu" ] = MNU_Radio
MNU_MenuQuitter [ "menu" ] = MNU_Quitter

FRA_Menu.grid ( row = 0 , column = 0 , sticky = "ew" )
MNU_MenuCommand.grid ( row = 0 , column = 0 )
MNU_MenuCheck.grid ( row = 0 , column = 1 )
MNU_MenuRadio.grid ( row = 0 , column = 2 )
MNU_MenuQuitter.grid ( row = 0 , column = 3 )

TKI_Principal.mainloop ( )
