#Battle Script
#Fire > Wind > Earth > Water > Fire

#Style
style move_button:
    background Frame("images/Button/buttonmove_idle.png", 500, 200)
    hover_background Frame("images/Button/buttonmove_hover.png", 500, 200)
style button_font:
    font "fonts/rexlia rg.otf"
    size 25
    color "#000000"
    hover_color "#b96900"
style black_font:
    color "#000000"

#Transforms
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

#Stats
#Player Stats
define playermaxhp = 200
define playercurhp = 200
define playersp = 100
define playeratk = 100
define playerdef = 100
define playerspd = 100

#Enemy Stats
define enemymaxhp = 200
define enemycurhp = 200
define enemyatk = 100
define enemydef = 100
define enemyspd = 50

#Move dmg temp
define Fireball = 30 #IPA
define Wind_blade = 25 #Math
define rock_throw = 35 #IPS
define bubble_stream = 40 #Indo


#Calculation Variables

#Effectiveness and Crit Rates
define weak = 0.7
define effective = 1
define supereffective = 1.3
define critdmg = [1,2]
define crit = False
define crt = 0

#Elements
define atk = "" #["Fire", "Water", "Wind", "Earth", "normal"]
define defe = "Wind" #["Fire", "Water", "Wind", "Earth", "normal"]
define enemydefelement = "Wind" #["Fire", "Water", "Wind", "Earth", "normal"]
define movename = ""

#Effectiveness dialogue var
define effectivedesc = ""

#Dmg Calculations
define damage = 1
define multiplier = 1
define enemydamage = 1
define movedmg = 20

#Enemy Min and Max Move DMG
define x = 30
define y = 40

#Turn Switch
define turn = True

#Final dmg
define dmgto = 0

#Trivia Vars
define dummy = False #Question dummy
default quizquestion = 0
default z = 0
default asks = ""
default answers = ""
default corrects = ""
default answers1 = ""
default answers2 = ""
default answers3 = ""
default answercheck = ""

#Screens
#Timer bar
$ time = 800 # time in ticks (eg. 800 = 8 seconds)
$ timer_range = 800
$ timer_jump = 'checkquiz1'

screen countdown:
    text "Time Limit" xalign 0.5 yalign 0.65 style ("black_font")
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.7 xmaximum 600 at alpha_dissolve:
        left_bar Frame("images/Bar/health_full.png") right_bar Frame("images/Bar/health_empty.png")



#HP Bars Animations
screen hpbar:
    text "HP: [playercurhp]/[playermaxhp]" xalign 0.98 yalign 0.65 style ("black_font")
    bar value AnimatedValue(playercurhp, range=playermaxhp):
        xalign 0.98 yalign 0.70 xmaximum 300 left_bar Frame("images/Bar/health_full.png") right_bar Frame("images/Bar/health_empty.png")

    text "Enemy HP: [enemycurhp]/[enemymaxhp]" xalign 0.02 yalign 0.05 style ("black_font")
    bar value AnimatedValue(enemycurhp, range=enemymaxhp):
        xalign 0.02 yalign 0.10 xmaximum 300 left_bar Frame("images/Bar/health_full.png") right_bar Frame("images/Bar/health_empty.png")

#Ability Menu
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
    
#Attack Menu
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
                    action Hide("moves"), SetVariable("atk", "Fire"), SetVariable("movename", "Fireball"), SetVariable("movedmg", Fireball), Jump("trivia")
                button:
                    text "Wind Blade" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), SetVariable("atk", "Wind"), SetVariable("movename", "Wind Blade"), SetVariable("movedmg", Wind_blade), Jump("checkeffective1")
            hbox:
                spacing 40
                button:
                    text "Rock Throw" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), SetVariable("atk", "Earth"), SetVariable("movename", "Rock Throw"), SetVariable("movedmg", rock_throw), Jump("checkeffective1")
                button:
                    text "Bubble Stream" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(242,43)
                    style "move_button"
                    action Hide("moves"), SetVariable("atk", "Water"), SetVariable("movename", "Bubble Stream"), SetVariable("movedmg", bubble_stream), Jump("checkeffective1")


#Start Mechanism
#Start battle (called only once from script.rpy)
label battle:
    scene bg wild battle with fade
    show kanon o:
        xalign 0.83
        yalign 1.0
        zoom 1.5
    window hide
    show screen hpbar
    show screen mainbattle

    $renpy.random.shuffle(trivIPA) #Randomize the trivia beforehand

    $renpy.pause(None,hard=True)
    
#Ability Menu (Attack, Items, etc.)
label battlestart:
    window hide
    show screen mainbattle
    $renpy.pause(None,hard=True)    

#Attack Menu
label attackmove:
    window hide
    show screen moves
    $renpy.pause(None,hard=True)

#Trivia initiations
label trivia:
    $ quizquestion = trivIPA[z]
    $ asks = quizquestion["question"]
    $ answers = quizquestion["answer"]
    $ corrects = quizquestion["correct"]
    $ renpy.random.shuffle(answers) #reshuffle answers
    $ answers1 = answers[0]
    $ answers2 = answers[1]
    $ answers3 = answers[2]
    $ answercheck = ""
    jump trivia1

#Trivia gui
label trivia1:
    $ time = 800
    $ timer_range = 800
    $ timer_jump = 'checkquiz1'
    show screen countdown
    menu:
        "{color=#E25822}{b}[atk] Trivia{/b}{/color}\n
        {color=#FFFFFF}[asks]{/color}" if dummy == True:
            "Oops. How'd you get here?"
        "[answers1]":
            $answercheck = answers1
            jump checkquiz1
        "[answers2]":
            $answercheck = answers2
            jump checkquiz1
        "[answers3]":
            $answercheck = answers3
            jump checkquiz1

#Answer check
label checkquiz1:
    #If correct
    if answercheck == corrects:
        hide screen countdown
        window show
        $movedmg *= 1.1
        $movedmg = int(movedmg)
        "Trivia answer is correct! Move DMG increased by 10%%"

    #If incorrect
    else:
        hide screen countdown
        window show
        $movedmg *= 0.5
        $movedmg = int(movedmg)
        "Trivia answer is incorrect! Move DMG decreased by 50%%"

    #Questions Index
    $z +=1
    
    jump checkeffective1

label checkeffective1: #calculates effectiveness of an attack
    call critrate #look if the attack crits or not
    if atk == "Water":
        if defe == "Fire":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"
        elif defe == "Earth":
            $multiplier = weak
            $movedmg *= multiplier
            $effectivedesc = "not very effective"
        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"

    elif atk == "Fire":
        if defe == "Wind":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"
        elif defe == "Water":
            $multiplier = weak
            $movedmg *= multiplier
            $effectivedesc = "not very effective"
        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"

    elif atk == "Wind":
        if defe == "Earth":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"
        elif defe == "Fire":
            $multiplier = weak
            $movedmg *= multiplier
            $effectivedesc = "not very effective"
        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"
        
    elif atk == "Earth":
        if defe == "Water":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"
        elif defe == "Wind":
            $multiplier = weak
            $movedmg *= multiplier
            $effectivedesc = "not very effective"
        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"
    
    #Physical
    else:
        $multiplier = effective
        $movedmg *= multiplier
        $effectivedesc = "effective"

    #Crit DMG Calculations
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

    #Dialogue on enemy's turn
    if turn == False:
        "Enemy deals [dmgto]."

    #Dialogue on player's turn
    else:
        "You deal [dmgto]."
        if effectivedesc == "not very effective":
            "It's not very effective."
        elif effectivedesc == "very effective":
            "It's very effective."
    
    #Dialogue if crits
    if crit == True:
        "It's critical hit."
    $movedmg = 1 #reset the move dmg (i forgot why i put this here)

    #Refresh HP Bar
    $renpy.restart_interaction()

    #Going back to script.rpy if either sides died
    if playercurhp <= 0:
        "You lost."
        $playercurhp = playermaxhp
        $enemycurhp = enemymaxhp
        hide screen hpbar
        return
    elif enemycurhp <= 0:
        "You won."
        $playercurhp = playermaxhp
        $enemycurhp = enemymaxhp
        hide screen hpbar
        return

    #If neither sides died yet
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



    

    
