#Battle Script
#Fire > Wind > Earth > Water > Fire

#Style
style move_button:
    background Frame("images/Button/buttonmove_idle.png", 500, 200)
    hover_background Frame("images/Button/buttonmove_hover.png", 500, 200)
style button_font:
    font "fonts/Bryndan_Write.ttf"
    size 30
    color "#000000"
    hover_color "#b96900"
style black_font:
    color "#000000"

#Stats

define playermaxhp = 200
define playercurhp = 200
define playersp = 100
define playeratk = 100
define playerdef = 100
define playerspd = 100

define enemymaxhp = 200
define enemycurhp = 200
define enemyatk = 100
define enemydef = 100
define enemyspd = 50

#Move dmg temp
define fireball = 30
define wind_blade = 25
define rock_throw = 35
define bubble_stream = 40


#Calculation Variables

define weak = 0.7
define effective = 1
define supereffective = 1.3
define critdmg = [1,2]
define crit = False
define crt = 0

define atk = "" #["fire", "water", "wind", "earth", "normal"]
define defe = "wind" #["fire", "water", "wind", "earth", "normal"]
define enemydefelement = "wind" #["fire", "water", "wind", "earth", "normal"]
define movename = ""
define effectivedesc = ""

define damage = 1
define multiplier = 1
define enemydamage = 1
define movedmg = 20

define x = 30
define y = 60

define turn = True

define dmgto = 0

label battle:
    show bg wild battle
    show kanon o:
        xalign 0.83
        yalign 1.0
        zoom 1.5
    show screen hpbar
    show screen mainbattle
    window hide
    pause
    

label battlestart:
    show screen mainbattle
    window hide
    pause    

label attackmove:
    show screen moves
    window hide
    pause


screen hpbar:
    text "HP: [playercurhp]/[playermaxhp]" xalign 0.98 yalign 0.65 style ("black_font")
    bar value AnimatedValue(playercurhp, range=playermaxhp):
        xalign 0.98 yalign 0.70 xmaximum 300 left_bar Frame("images/Bar/health_full.png") right_bar Frame("images/Bar/health_empty.png")

    text "Enemy HP: [enemycurhp]/[enemymaxhp]" xalign 0.02 yalign 0.05 style ("black_font")
    bar value AnimatedValue(enemycurhp, range=enemymaxhp):
        xalign 0.02 yalign 0.10 xmaximum 300 left_bar Frame("images/Bar/health_full.png") right_bar Frame("images/Bar/health_empty.png")

# screen playerstatbar:
#     vbox:
#         xalign 0.85
#         yalign 0.6
#         bar value AnimatedValue(playerhp, range=100):
#             xalign 0.0
#             yalign 0.0
#             xmaximum 500
#             left_bar Frame("images/Bar/health_full.png", 10, 0)
#             right_bar Frame("images/Bar/health_empty.png", 0, 0, 10)
#             thumb None
#             bar_vertical False
    
screen mainbattle:
    frame:
        xalign 0.5
        yalign 1.0
        xsize 1980
        ysize 300
        background Frame("images/Screen/platform.png")
        vbox:
            xalign 0.2
            yalign 0.5
            spacing 0.05
            button:
                focus_mask True
                text "Attack" xalign 0.5 yalign 0.5 style ("button_font")
                xysize(242,43)
                style "move_button"
                action Hide("mainbattle"), Jump("attackmove")
            button:
                focus_mask True
                text "Items" xalign 0.5 yalign 0.5 style ("button_font")
                xysize(242,43)
                style "move_button"
                action Hide("mainbattle"), Jump("attackmove")
            button:
                focus_mask True
                text "Heal" xalign 0.5 yalign 0.5 style ("button_font")
                xysize(242,43)
                style "move_button"
                action Hide("mainbattle"), Jump("attackmove")
            button:
                focus_mask True
                text "Run" xalign 0.5 yalign 0.5 style ("button_font")
                xysize(242,43)
                style "move_button"
                action Hide("mainbattle"), Jump("attackmove")
    
            
screen moves:
    frame:
        xalign 0.5
        yalign 1.0
        xsize 1980
        ysize 300
        background Frame("images/Screen/platform.png")
        button:
            xalign 0.75
            yalign 0.5
            text "Back" xalign 0.5 yalign 0.5 style ("button_font")
            xysize(242,43)
            style "move_button"
            action Hide("moves"), Jump("battlestart")
        vbox:
            xalign 0.2
            yalign 0.5
            spacing 0.05
            hbox:
                spacing 40
                button:
                    text "Fireball" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), SetVariable("atk", "fire"), SetVariable("movename", "Fireball"), SetVariable("movedmg", fireball), Jump("checkeffective1")
                button:
                    text "Wind Blade" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), SetVariable("atk", "wind"), SetVariable("movename", "Wind Blade"), SetVariable("movedmg", wind_blade), Jump("checkeffective1")
            hbox:
                spacing 40
                button:
                    text "Rock Throw" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), SetVariable("atk", "earth"), SetVariable("movename", "Rock Throw"), SetVariable("movedmg", rock_throw), Jump("checkeffective1")
                button:
                    text "Bubble Stream" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), SetVariable("atk", "water"), SetVariable("movename", "Bubble Stream"), SetVariable("movedmg", bubble_stream), Jump("checkeffective1")

label test:
    $playercurhp -= 20
    jump battlestart

label checkeffective1: #calculates effectiveness of an attack
    call critrate #look if the attack crits or not
    if atk == "water":
        if defe == "fire":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"
        elif defe == "earth":
            $multiplier = weak
            $movedmg *= multiplier
            $effectivedesc = "not very effective"
        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"

    elif atk == "fire":
        if defe == "wind":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"
        elif defe == "water":
            $multiplier = weak
            $movedmg *= multiplier
            $effectivedesc = "not very effective"
        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"

    elif atk == "wind":
        if defe == "earth":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"
        elif defe == "fire":
            $multiplier = weak
            $movedmg *= multiplier
            $effectivedesc = "not very effective"
        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"
        
    elif atk == "earth":
        if defe == "water":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"
        elif defe == "wind":
            $multiplier = weak
            $movedmg *= multiplier
            $effectivedesc = "not very effective"
        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"
    
    else:
        $multiplier = effective
        $movedmg *= multiplier
        $effectivedesc = "effective"

    if crit == True:
        $movedmg *= critdmg[1]
    jump attack



label critrate: #calculates crit
    $crt = renpy.random.randint(1, 20) # 5% Crit rate

    if crt == 5:
        $crit = True

    else:
        $crit = False

    return

label attack: #damaging part
    window show
    
    if turn == True: #player turn
        "You used [movename]."
        $dmgto = playeratk + movedmg - enemydef
        $dmgto = int(dmgto)
        $enemycurhp -= dmgto
        if enemycurhp <= 0:
            $enemycurhp = 0
    else: #enemy turn
        $dmgto = enemyatk + movedmg - playerdef
        $dmgto = int(dmgto)
        $playercurhp -= dmgto
        if playercurhp <= 0:
            $playercurhp = 0

    if turn == False:
        "Enemy deals [dmgto]."
    else:
        "You deal [dmgto]."
        if effectivedesc == "not very effective":
            "It's not very effective."
        elif effectivedesc == "very effective":
            "It's very effective."
    
    if crit == True:
        "It's critical hit."
    $movedmg = 1

    $renpy.restart_interaction()

    if playercurhp <= 0:
        "You lost."
        $playercurhp = playermaxhp
        $enemycurhp = enemymaxhp
        hide screen hpbar
        jump start
    elif enemycurhp <= 0:
        "You won."
        $playercurhp = playermaxhp
        $enemycurhp = enemymaxhp
        hide screen hpbar
        jump start
    else:
        call switch
        if turn == False:
            jump autodmg
        else:
            jump battlestart


label autodmg: #for enemy atk dmg (dmg randomized according to x min and y max range)
    $movedmg = renpy.random.randint(x, y)
    jump checkeffective1

label switch: #switch turn
    if turn == True:
        $turn = False
    else:
        $turn = True
    return



    

    
