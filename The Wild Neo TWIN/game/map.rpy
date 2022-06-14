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
            yalign 0.3 xalign 0.5
            hbox:
                spacing 50
                vbox:
                    text "{b}Grind Area 1{/b}" style ("grindArea_font1") size 30 at alpha_dissolve
                    text "Rekomendasi Level: 1" style ("grindArea_font1") size 25 at alpha_dissolve
                button:
                    text "Battle" xalign 0.5 yalign 0.5 size 25 style ("grindArea_font")
                    xysize(200,60)
                    style "grindArea_button"
                    action Hide("grindAreaPage", transition=dissolve), SetVariable("moveend", movename2), Jump("initmovevar")
        
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
    $renpy.pause(None,hard=True)


        
    




