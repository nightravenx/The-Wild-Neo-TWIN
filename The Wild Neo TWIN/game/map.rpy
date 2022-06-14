define placeUnlocked = 1

#animations
image chibi animated a:
    "chibi together"
    xpos 887 ypos 830
    xpos 887
    linear 1.0 ypos 805
    xpos 887
    linear 1.0 ypos 830
    repeat

    

image chibi animated b:
    "chibi together"
    xpos 665 ypos 700
    xpos 665
    linear 1.0 ypos 725
    xpos 665
    linear 1.0 ypos 700
    repeat

style grindArea_button:
    background Frame("images/UI/button/button 3_idle.png", 0, 0)
    hover_background Frame("images/UI/button/button 3_hover.png", 0, 0)
style grindArea_font:
    font "fonts/Rounded_Elegance.ttf"
    size 35
    color "#000000"
    hover_color "#000000"
style grindArea_font1:
    font "fonts/Rounded_Elegance.ttf"
    color "#FFFFFF"

label mapStart:
    scene black with fade
    $renpy.pause(1.0,hard=True)
    scene game map with fade

    $renpy.pause(1.0,hard=True)

    window hide dissolve

    call unlockMap

    show screen buttonMap with dissolve
    show chibi animated a with dissolve
    
    
    $renpy.pause(None,hard=True)

label mapStart1:
    call unlockMap

    show screen buttonMap
    show chibi animated a
    with dissolve
    $renpy.pause(None,hard=True)

label unlockMap:
    if placeUnlocked >= 1:
        $ch1Map = True
    return

# xpos 837  ypos 700

screen buttonMap:
    button:
        xalign 1.0 yalign 0.0
        text "Grind Area" xalign 0.5 yalign 0.5 style ("grindArea_font")
        xysize(400,90)
        style "grindArea_button"
        action Hide("buttonMap", transition=dissolve), Jump("grindArea")
    button:
        xalign 0.73 yalign 0.0
        text "Upgrade Stat" xalign 0.5 yalign 0.5 style ("grindArea_font")
        xysize(400,90)
        style "grindArea_button"
        action Hide("buttonMap", transition=dissolve), Call("upstart")
    imagebutton:
        auto "images/Game map/jawa surabaya button_%s.png" xpos 615  ypos 590
        sensitive ch1Map
        action Hide("buttonMap", transition=dissolve), Jump("ch1Move")

screen grindAreaPage:
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 900
        background Frame("images/UI/2.png")
        
        text "{b}Grind Area{/b}" xalign 0.5 yalign 0.11 size 50 style("grindArea_font")
        vbox:
            yalign 0.4 xalign 0.5
            spacing 20
            hbox:
                spacing 50

                #Enemy Stats
                # define enemymaxhp = 200
                # define enemycurhp = 200
                # define enemyatk = 100
                # define enemydef = 100
                vbox:
                    text "{b}Grind Area 1{/b}" style ("grindArea_font1") size 30 at alpha_dissolve
                    text "Rekomendasi Level: 1" style ("grindArea_font1") size 25 at alpha_dissolve
                button:
                    text "Battle" xalign 0.5 yalign 0.5 size 25 style ("grindArea_font")
                    xysize(200,60)
                    style "grindArea_button"
                    action Hide("grindAreaPage", transition=dissolve), SetVariable("enemymaxhp", 200), SetVariable("enemycurhp", 200), SetVariable("enemyatk", 100), SetVariable("enemydef", 100), SetVariable("expmulti", 1), SetVariable("grinding", True), Jump("battle")
            hbox:
                spacing 50

                #Enemy Stats lvl3
                # define enemymaxhp = 250
                # define enemycurhp = 250
                # define enemyatk = 120
                # define enemydef = 100
                vbox:
                    text "{b}Grind Area 2{/b}" style ("grindArea_font1") size 30 at alpha_dissolve
                    text "Rekomendasi Level: 3" style ("grindArea_font1") size 25 at alpha_dissolve
                button:
                    text "Battle" xalign 0.5 yalign 0.5 size 25 style ("grindArea_font")
                    xysize(200,60)
                    style "grindArea_button"
                    action Hide("grindAreaPage", transition=dissolve), SetVariable("enemymaxhp", 225), SetVariable("enemycurhp", 225), SetVariable("enemyatk", 110), SetVariable("enemydef", 100), SetVariable("expmulti", 5), SetVariable("grinding", True), Jump("battle")
            hbox:
                spacing 50

                #Enemy Stats lvl5
                # define enemymaxhp = 300
                # define enemycurhp = 300
                # define enemyatk = 150
                # define enemydef = 120
                vbox:
                    text "{b}Grind Area 3{/b}" style ("grindArea_font1") size 30 at alpha_dissolve
                    text "Rekomendasi Level: 5" style ("grindArea_font1") size 25 at alpha_dissolve
                button:
                    text "Battle" xalign 0.5 yalign 0.5 size 25 style ("grindArea_font")
                    xysize(200,60)
                    style "grindArea_button"
                    action Hide("grindAreaPage", transition=dissolve), SetVariable("enemymaxhp", 300), SetVariable("enemycurhp", 300), SetVariable("enemyatk", 150), SetVariable("enemydef", 120), SetVariable("expmulti", 8), SetVariable("grinding", True), Jump("battle")
        
        button:
            xalign 0.5 yalign 0.9
            text "Back" xalign 0.5 yalign 0.5 size 25 style ("grindArea_font")
            xysize(200,60)
            style "grindArea_button"
            action Hide("grindAreaPage", transition=dissolve), Jump("mapStart1")


label grindArea:
    show screen grindAreaPage with dissolve 
    $renpy.pause(None,hard=True)


label ch1Move:
    show chibi animated b with MoveTransition(2.0)
    $renpy.pause(1.0,hard=True)
    scene black with fade
    window show
    jump surabaya


        
    




