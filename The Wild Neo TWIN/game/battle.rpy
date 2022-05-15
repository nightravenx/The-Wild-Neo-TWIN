#Battle Script
#Fire > Wind > Earth > Water > Fire

#Style
style move_button:
    background Frame("images/Button/buttonmove_idle.png")
    hover_background Frame("images/Button/buttonmove_hover.png")
style button_font:
    font "fonts/Bryndan_Write.ttf"
    size 30
    color "#000000"
    hover_color "#b96900"

#Stats
define playerhp = 200
default playersp = 100
default playeratk = 100
default playerdef = 100
default playerspd = 100

default enemyhp = 200
default enemyatk = 100
default enemydef = 50
default enemyspd = 50

default skilldmg = 40


#Calculation Variables

define weak = 0.7
define effective = 1
define supereffective = 1.3
define critdmg = [1,2]
default crit = False
default crt = 0

default atk = "" #["fire", "water", "wind", "earth", "normal"]
default defe = "" #["fire", "water", "wind", "earth", "normal"]
default enemydefelement = "normal" #["fire", "water", "wind", "earth", "normal"]

default damage = 1
default multiplier = 1
default enemydamage = 1
default movedmg = 1

default x = 10
default y = 30

default turn = True

default dmgto = 0

label bttle:
    show bg wild battle
    show kanon o:
        xalign 0.85
        yalign 1.0
        zoom 1.5
    show screen playerstatbar
    show screen mainbattle
    window hide
    pause
    

label bttlestart:
    show screen mainbattle
    window hide
    pause    

label attackmove:
    show screen moves
    window hide
    pause

screen playerstatbar:
    vbox:
        xalign 0.85
        yalign 0.6
        bar value AnimatedValue(playerhp, range=100.0):
            xalign 0.0
            yalign 0.0
            xmaximum 500
            left_bar Frame("images/Bar/health_full.png", 10, 0)
            right_bar Frame("images/Bar/health_empty.png", 0, 0, 10)
            thumb None
            bar_vertical False
    
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
                text "Attack" xalign 0.5 yalign 0.5 style ("button_font")
                xysize(242,43)
                style "move_button"
                action Hide("mainbattle"), Jump("attackmove")
            button:
                text "Items" xalign 0.5 yalign 0.5 style ("button_font")
                xysize(242,43)
                style "move_button"
                action Hide("mainbattle"), Jump("attackmove")
            button:
                text "Heal" xalign 0.5 yalign 0.5 style ("button_font")
                xysize(242,43)
                style "move_button"
                action Hide("mainbattle"), Jump("attackmove")
            button:
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
            xalign 0.06
            yalign 0.08
            text "Back" xalign 0.5 yalign 0.5 style ("button_font")
            xysize(242,43)
            style "move_button"
            action Hide("moves"), Jump("bttlestart")
        vbox:
            xalign 0.2
            yalign 0.6
            spacing 0.05
            hbox:
                spacing 40
                button:
                    text "Fireball" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), Jump("test"), SetVariable("atk", "fire")
                button:
                    text "Wind Blade" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), Jump("bttlestart"), SetVariable("atk", "wind")
            hbox:
                spacing 40
                button:
                    text "Rock Throw" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), Jump("bttlestart"), SetVariable("atk", "earth")
                button:
                    text "Bubble Gun" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), Jump("bttlestart"), SetVariable("atk", "water")

label test:
    $playerhp -= 20
    jump bttlestart

label checkeffective: #calculates effectiveness of an attack
    call critrate #look if the attack crits or not
    if atk == "water":
        if defe == "fire":
            $multiplier = supereffective
            $damage *= multiplier
        elif defe == "earth":
            $multiplier = weak
            $damage *= multiplier
        else:
            $multiplier = effective
            $damage *= multiplier

    elif atk == "fire":
        if defe == "wind":
            $multiplier = supereffective
            $damage *= multiplier
        elif defe == "water":
            $multiplier = weak
            $damage *= multiplier
        else:
            $multiplier = effective
            $damage *= multiplier

    elif atk == "wind":
        if defe == "earth":
            $multiplier = supereffective
            $damage *= multiplier
        elif defe == "fire":
            $multiplier = weak
            $damage *= multiplier
        else:
            $multiplier = effective
            $damage *= multiplier
        
    elif atk == "earth":
        if defe == "water":
            $multiplier = supereffective
            $damage *= multiplier
        elif defe == "wind":
            $multiplier = weak
            $damage *= multiplier
        else:
            $multiplier = effective
            $damage *= multiplier
    
    else:
        $multiplier = effective
        $damage *= multiplier

    if crit == True:
        $damage *= critdmg[1]

    jump attack

label critrate: #calculates crit
    $crt = renpy.random.randint(1, 20) # 5% Crit rate

    if crt == 5:
        $crit = True

    else:
        $crit = False

    return

label attack: #damaging part
    if turn == True: #player turn
        $dmgto = playeratk + damage + movedmg - enemydef
        $enemyhp -= dmgto

    else: #enemy turn
        $dmgto = playeratk + damage + movedmg - enemydef
        $enemyhp -= dmgto
    jump bttle


label autodmg: #for enemy atk dmg (dmg randomized according to x min and y max range)
    $dmgto = renpy.random.randint(x, y)
    call checkeffective

label switch: #switch turn
    if turn == True:
        $turn = False
    else:
        $turn = True
    jump bttle



    

    
