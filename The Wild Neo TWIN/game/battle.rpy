#Battle Script
#Fire > Wind > Earth > Water > Fire

#Style
style move_button:
    background Frame("images/UI/button 2.png", 0, 0)
    hover_background Frame("images/UI/button 2.png", 0, 0)
style button_font:
    font "fonts/rexlia rg.otf"
    size 35
    color "#eeeeee"
    hover_color "#9fbbf0"
    italic True
style black_font:
    color "#000000"
    font "fonts/Rounded_Elegance.ttf"
style white_font:
    color "#FFFFFF"
    font "fonts/Rounded_Elegance.ttf"

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
define playeratk = 100
define playerdef = 100

#Enemy Stats
define enemymaxhp = 200
define enemycurhp = 200
define enemyatk = 100
define enemydef = 100

#Move dmg temp
define Fireball = 30 #IPA
define Wind_Blade = 32 #Math
define Rock_Throw = 40 #IPS
define Water_Stream = 38 #Indo
define Punch = 40


#Calculation Variables

#Effectiveness and Crit Rates
define weak = 0.7
define effective = 1
define supereffective = 1.3
define critdmg = [1,2]
define crit = False
define crt = 0

#Elements
define movelist = ["Fireball", "Wind Blade", "Rock Throw", "Water Stream", "Punch"]
define tempmovelist = ["Fireball", "Wind Blade", "Rock Throw", "Water Stream", "Punch"]
define atklist = ["Fire", "Wind", "Earth", "Water", "Physical"]
define atk = ""
define defelist = ["Fire", "Wind", "Earth", "Water", "Physical"]
define defe = ""
define enemydefe = "Physical" #["Fire", "Wind", "Earth", "Water", "Physical"]
define movename = ""

#Other
define effectivedesc = ""
define turndesc = "YOUR TURN"
define turndesccol = "#81ee57" #"#81ee57" "#a13e3e" "#E25822"
define atkcol = ""

#Dmg Calculations
define damage = 1
define multiplier = 1
define enemydamage = 1
define movedmg = 20

#Enemy Min and Max Move DMG
define x = 20
define y = 30
define a = 0

#Turn Switch
define turn = True

#Final dmg
define dmgto = 0

#Trivia Vars
define dummy = False #Question dummy
define canAttack = False
default quizquestion = 0
default z = 0
default asks = ""
default answers = ""
default corrects = ""
default answers1 = ""
default answers2 = ""
default answers3 = ""
default answercheck = ""

define movename = ""
define movename1 = ""
define movename2 = ""
define movename3 = ""
define movename4 = ""
define moveend = ""

label moveinit:
    $renpy.random.shuffle(tempmovelist)
    $movename = tempmovelist[0]
    $movename1 = tempmovelist[1]
    $movename2 = tempmovelist[2]
    $movename3 = tempmovelist[3]
    $movename4 = tempmovelist[4]
    return

#Screens
#Timer bar
$ time = 800 # time in ticks (eg. 800 = 8 seconds)
$ timer_range = 800
$ timer_jump = 'checkquiz1'

screen countdown:
    text "Time Limit" xalign 0.5 yalign 0.70 style ("black_font") at alpha_dissolve
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.75 xmaximum 600 at alpha_dissolve:
        left_bar Frame("images/Bar/health_full.png") right_bar Frame("images/Bar/health_empty.png")



#HP Bars Animations
screen hpbar:
    text "{b}HP{/b}" xalign 0.085 yalign 0.1 style ("white_font") at alpha_dissolve
    text "[playercurhp]/[playermaxhp]" xalign 0.33 yalign 0.145 style ("white_font") at alpha_dissolve
    bar value AnimatedValue(playercurhp, range=playermaxhp) at alpha_dissolve:
        xalign 0.15 yalign 0.1 xmaximum 500 left_bar Frame("images/Bar/health_full.png") right_bar Frame("images/Bar/health_empty.png")

    text "{b}EXP{/b}" xalign 0.085 yalign 0.1 style ("white_font") at alpha_dissolve
    text "[curexp]/[maxexp]" xalign 0.33 yalign 0.145 style ("white_font") at alpha_dissolve
    bar value AnimatedValue(playercurhp, range=playermaxhp) at alpha_dissolve:
        xalign 0.15 yalign 0.1 xmaximum 500 left_bar Frame("images/Bar/health_full.png") right_bar Frame("images/Bar/health_empty.png")

    text "{b}HP{/b}" xalign 0.9185 yalign 0.1 style ("white_font") at alpha_dissolve
    bar value AnimatedValue(enemycurhp, range=enemymaxhp) at alpha_dissolve:
        xalign 0.85 yalign 0.1 xmaximum 500 left_bar Frame("images/Bar/health_full.png") right_bar Frame("images/Bar/health_empty.png")

#Ability Menu
# screen mainbattle:
#     frame:
#         xalign 0.5
#         yalign 1.0
#         xsize 1980
#         ysize 300
#         background Frame("images/UI/nn.png")
#         vbox:
#             xalign 0.2
#             yalign 0.5
#             spacing 0.05
#             button:
#                 focus_mask True
#                 text "Attack" xalign 0.5 yalign 0.5 style ("button_font")
#                 xysize(242,43)
#                 style "move_button"
#                 action Hide("mainbattle"), Jump("attackmove")
#             button:
#                 focus_mask True
#                 text "Items" xalign 0.5 yalign 0.5 style ("button_font")
#                 xysize(242,43)
#                 style "move_button"
#                 action Hide("mainbattle"), Jump("attackmove")
#             button:
#                 focus_mask True
#                 text "Heal" xalign 0.5 yalign 0.5 style ("button_font")
#                 xysize(242,43)
#                 style "move_button"
#                 action Hide("mainbattle"), Jump("attackmove")
#             button:
#                 focus_mask True
#                 text "Run" xalign 0.5 yalign 0.5 style ("button_font")
#                 xysize(242,43)
#                 style "move_button"
#                 action Hide("mainbattle"), Jump("attackmove")
#Screen untuk menu
screen menu_frame:
    frame at alpha_dissolve:
        xalign 0.5 yalign 0.5
        xsize 1500
        ysize 800
        background Frame("images/UI/3.png")
#Screen Health
screen healths:
    frame at alpha_dissolve:
        xalign 0.5 yalign 0
        xsize 1980
        ysize 210
        background Frame("images/UI/3.png")
        text "{i}Player{/i}" xalign 0.135 yalign 0.35 font "fonts/rexlia rg.otf"
        text "{i}Enemy{/i}" xalign 0.87 yalign 0.35 font "fonts/rexlia rg.otf"
        text "{color=[turndesccol]}[turndesc]{/color}" xalign 0.5 yalign 0.5 size 50 font "fonts/rexlia rg.otf"
#Attack Menu
screen moves:
    frame at alpha_dissolve:
        xalign 0.5
        yalign 1.02
        xsize 1980
        ysize 360
        background Frame("images/UI/nn.png")
        text "Skill apa yang ingin digunakan?" xalign 0.32 yalign 0.21 color "#000000" font "fonts/rexlia rg.otf" size 30
        vbox:
            xalign 0.23
            yalign 0.82
            spacing 0
                
            hbox:
                spacing 0
                button:
                    text "[movename]" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("moves"), SetVariable("moveend", movename), Jump("initmovevar")
                button:
                    text "[movename1]" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("moves"), SetVariable("moveend", movename1), Jump("initmovevar")
            hbox:
                spacing 0
                button:
                    text "[movename2]" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("moves"), SetVariable("moveend", movename2), Jump("initmovevar")
                button:
                    text "[movename3]" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("moves"), SetVariable("moveend", movename3), Jump("initmovevar")

label initmovevar:
    if moveend == "Fireball":
        $atk = "Fire"
        $movename = moveend
        $movedmg = Fireball
        $atkcol = "#E25822"
    elif moveend == "Wind Blade":
        $atk = "Wind"
        $movename = moveend
        $movedmg = Wind_Blade
        $atkcol = "#61ffb0"
    elif moveend == "Rock Throw":
        $atk = "Earth"
        $movename = moveend
        $movedmg = Rock_Throw
        $atkcol = "#b17837"
    elif moveend == "Water Stream":
        $atk = "Water"
        $movename = moveend
        $movedmg = Water_Stream
        $atkcol = "#55bbff"
    else:
        $atk = "Physical"
        $movename = moveend
        $movedmg = Punch
        $atkcol = "#cccccc"
    jump trivia
            

screen shield:
    frame at alpha_dissolve:
        xalign 0.5
        yalign 1.02
        xsize 1980
        ysize 360
        background Frame("images/UI/nn.png")
        text "Shield elemen apa yang ingin digunakan?" xalign 0.32 yalign 0.21 color "#000000" font "fonts/rexlia rg.otf" size 30
        vbox:
            xalign 0.23
            yalign 0.82
            spacing 0
            hbox:
                spacing 100
                button:
                    text "Fire" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("shield"), SetVariable("defe", "Fire"), Jump("autodmg")
                button:
                    text "Wind" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("shield"), SetVariable("defe", "Wind"), Jump("autodmg")
            hbox:
                spacing 100
                button:
                    text "Earth" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("shield"), SetVariable("defe", "Earth"), Jump("autodmg")
                button:
                    text "Water" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("shield"), SetVariable("defe", "Water"), Jump("autodmg")


#Start Mechanism
#Start battle (called only once from script.rpy)
label battle:
    scene bg portal with fade
    show timebandit merah:
        xalign 0.85 #78
        yalign 1.0 #15
        zoom 1.2
    show mika:
        xalign 0.15
        yalign 1.0
        zoom 1.2
    window hide dissolve
    show screen healths
    show screen hpbar
    call moveinit
    show screen moves

    $renpy.random.shuffle(trivIPA) #Randomize the trivia beforehand

    $renpy.pause(None,hard=True)
    
#Ability Menu (Attack, Items, etc.)
# label battlestart:
#     window hide
#     show screen mainbattle
#     $renpy.pause(None,hard=True)    

#Attack Menu
label attackmove:
    window hide dissolve
    call moveinit
    show screen moves
    $renpy.pause(None,hard=True)

label defensemove:
    window hide dissolve
    show screen shield
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
    show screen menu_frame
    show screen countdown
    menu:
        "{color=[atkcol]}{b}[atk] Trivia{/b}{/color}\n
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
        $Hide("countdown", transition=Dissolve(1.0))()
        $Hide("menu_frame", transition=Dissolve(1.0))()
        
        window show dissolve
        $movedmg *= 1
        $movedmg = int(movedmg)
        $canAttack = True
        "Trivia benar! Serangan berhasil menyerang musuh."

    #If incorrect
    elif answercheck == "":
        $Hide("countdown", transition=Dissolve(1.0))()
        $Hide("menu_frame", transition=Dissolve(1.0))()

        window show dissolve
        $canAttack = False
        "Waktu habis! Serangan gagal menyerang musuh."
    else:
        $Hide("countdown", transition=Dissolve(1.0))()
        $Hide("menu_frame", transition=Dissolve(1.0))()
       
        window show dissolve
        $canAttack = False
        "Trivia salah! Serangan gagal menyerang musuh."

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
    window show dissolve
    if turn == True: #player turn
        if canAttack == True: #decide if the player can attack or not (set from whether the trivia is correct or not)
            "Kamu menggunakan [movename]."
            $dmgto = playeratk + movedmg - enemydef
            $dmgto = int(dmgto)
            $enemycurhp -= dmgto
            if enemycurhp <= 0:
                $enemycurhp = 0
    else: #enemy turn
        "Kamu menggunakan perisai [defe]."
        "Musuh menggunakan serangan [atk]."

        if effectivedesc == "not very effective":
            "Tangkis berhasil menahan elemen! Serangan musuh dilemahkan."
        elif effectivedesc == "very effective":
            "Tangkis gagal menahan elemen! Serangan musuh lebih efektif."
        $dmgto = enemyatk + movedmg - playerdef
        $dmgto = int(dmgto)
        $playercurhp -= dmgto
        if playercurhp <= 0:
            $playercurhp = 0

    #Dialogue on enemy's turn
    # if turn == False:
    #     "Enemy memberikan serangan sebesar [dmgto]."

    #Dialogue on player's turn
    if turn == True:
        if canAttack == True: #decide if the player can attack or not (set from whether the trivia is correct or not)
            if dmgto > 0:
                if effectivedesc == "not very effective":
                    "Serangan tidak efektif."
                elif effectivedesc == "very effective":
                    "Serangan sangat efektif."
    
    #Dialogue if crits
    if crit == True:
        "Serangan kritis!"
    $movedmg = 0 #reset the move dmg
    $canAttack = False #reset

    #Refresh HP Bar
    $renpy.restart_interaction()

    #Going back to script.rpy if either sides died
    if playercurhp <= 0:
        "Kamu kalah!"
        $playercurhp = playermaxhp
        $enemycurhp = enemymaxhp
        $Hide("hpbar", transition=Dissolve(1.0))()
        scene black with fade
        return
    elif enemycurhp <= 0:
        "Kamu menang!"
        $playercurhp = playermaxhp
        $enemycurhp = enemymaxhp
        $curexp += 15
        $renpy.restart_interaction()
        $Hide("hpbar", transition=Dissolve(1.0))()
        scene black with fade
        return

    #If neither sides died yet
    else:
        call switch
        if turn == False:
            jump defensemove
        else:
            jump attackmove

label defense:


label autodmg: #for enemy atk dmg (dmg randomized according to x min and y max range)
    $movedmg = renpy.random.randint(x, y)
    $a = renpy.random.randint(0,4)
    $atk = atklist[a]
    jump checkeffective1

label switch: #switch turn
    $renpy.pause(2.0,hard=True) #for damage animation interval
    if turn == True:
        $turn = False
        $turndesc = "ENEMY TURN"
        $turndesccol = "#a13e3e"
    else:
        $turn = True
        $turndesc = "YOUR TURN"
        $turndesccol = "#81ee57"
        $defe = enemydefe
    return

define curexp = 0
define maxexp = 100
define lvl = 1
define bonusap = 3
define curap = 0
