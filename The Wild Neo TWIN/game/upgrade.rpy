transform pluszoom:
    zoom 0.7
transform statmenuzoom:
    zoom 0.9

style stattext:
    font "fonts/rexlia rg.otf"
    size 20
    color "#000000"

style aptext:
    font "fonts/rexlia rg.otf"
    size 40
    color "#ffffff"

define clickstat = ""
default maxFireball = 50 #IPA
default maxWind_Blade = 50 #Math
default maxRock_Throw = 50 #IPS
default maxWater_Stream = 50 #Indo
default maxPunch = 50
default maxCrit = 100
default tempHp = 200
default tempDef = 100
default imagebutton_enabled_state = True

label upstart:
    show screen upgrade
    $renpy.pause(None,hard=True)
    return

label upstart1:
    show screen upgrade1
    if curap == 0:
        $imagebutton_enabled_state = False
        
    else:
        $imagebutton_enabled_state = True
    $renpy.pause(None,hard=True)
    return

screen upgrade:
    
    frame at alpha_dissolve:
        xalign 0.5
        yalign 0.5
        xsize 1820
        ysize 980
        background Frame("images/UI/3.png")
        add "images/Character/[user!u]/biasa.png" xalign 0.1 yalign 0.5

        
        
        add "images/UI/Upgrade/hpup.png" zoom 0.8 xalign 0.35 yalign 0.3
        text "HP: [playermaxhp]" style "stattext" xalign 0.359 yalign 0.448
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.405 yalign 0.22 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "HP"), Hide("upgrade"), Call("increase")]

        add "images/UI/Upgrade/defup.png" zoom 0.8 xalign 0.525 yalign 0.3
        text "DEF: [playerdef]" style "stattext" xalign 0.525 yalign 0.448
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.565 yalign 0.22 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "DEF"), Hide("upgrade"), Call("increase")]

        add "images/UI/Upgrade/critup.png" zoom 0.8 xalign 0.7 yalign 0.3
        text "Crit: [critdmg1]%" style "stattext" xalign 0.69 yalign 0.448
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.729 yalign 0.22 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Crit"), Hide("upgrade"), Call("increase")]
        
        add "images/UI/Upgrade/critup.png" zoom 0.8 xalign 0.875 yalign 0.3
        text "Phys: [Punch]" style "stattext" xalign 0.854 yalign 0.448
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.895 yalign 0.22 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Physical"), Hide("upgrade"), Call("increase")]
        
##################################### Bottom ############################################

        add "images/UI/Upgrade/fireup.png" zoom 0.8 xalign 0.35 yalign 0.7
        text "Fire: [Fireball]" style "stattext" xalign 0.359 yalign 0.75
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.405 yalign 0.56 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Fire"), Hide("upgrade"), Call("increase")]

        add "images/UI/Upgrade/windup.png" zoom 0.8 xalign 0.525 yalign 0.7
        text "Wind: [Wind_Blade]" style "stattext" xalign 0.525 yalign 0.75
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.568 yalign 0.56 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Wind"), Hide("upgrade"), Call("increase")]

        add "images/UI/Upgrade/earthup.png" zoom 0.8 xalign 0.7 yalign 0.7
        text "Earth: [Rock_Throw]" style "stattext" xalign 0.69 yalign 0.75
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.729 yalign 0.56 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Earth"), Hide("upgrade"), Call("increase")]
        
        add "images/UI/Upgrade/waterup.png" zoom 0.8 xalign 0.875 yalign 0.7
        text "Water: [Water_Stream]" style "stattext" xalign 0.857 yalign 0.75
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.895 yalign 0.56 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Water"), Hide("upgrade"), Call("increase")]
        
#####################################Final Button########################################

        imagebutton:
            auto "images/UI/button/cross_%s.png" xalign 0.44 yalign 0.9 at pluszoom
            action [Hide("upgrade"), Call("cancelup")]
        imagebutton:
            auto "images/UI/button/reload_%s.png" xalign 0.605 yalign 0.9 at pluszoom
            action [Hide("upgrade"), Call("resetup")]
        imagebutton:
            auto "images/UI/button/check_%s.png" xalign 0.77 yalign 0.9 at pluszoom
            action [Hide("upgrade"), Call("confirmup")]
        
    frame at alpha_dissolve:
        xalign 0.5
        yalign 0.09
        xsize 500
        ysize 100
        background Frame("images/UI/5.png")
        text "AP: [curap]" style "aptext" xalign 0.5 yalign 0.5

screen upgrade1:
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1820
        ysize 980
        background Frame("images/UI/3.png")
        add "images/Character/[user!u]/biasa.png" xalign 0.1 yalign 0.5

        
        
        add "images/UI/Upgrade/hpup.png" zoom 0.8 xalign 0.35 yalign 0.3
        text "HP: [playermaxhp]" style "stattext" xalign 0.359 yalign 0.448
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.405 yalign 0.22 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "HP"), Hide("upgrade1"), Call("increase")]

        add "images/UI/Upgrade/defup.png" zoom 0.8 xalign 0.525 yalign 0.3
        text "DEF: [playerdef]" style "stattext" xalign 0.525 yalign 0.448
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.565 yalign 0.22 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "DEF"), Hide("upgrade1"), Call("increase")]

        add "images/UI/Upgrade/critup.png" zoom 0.8 xalign 0.7 yalign 0.3
        text "Crit: [critdmg1]%" style "stattext" xalign 0.69 yalign 0.448
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.729 yalign 0.22 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Crit"), Hide("upgrade1"), Call("increase")]
        
        add "images/UI/Upgrade/critup.png" zoom 0.8 xalign 0.875 yalign 0.3
        text "Phys: [Punch]" style "stattext" xalign 0.854 yalign 0.448
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.895 yalign 0.22 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Physical"), Hide("upgrade1"), Call("increase")]
        
##################################### Bottom ############################################

        add "images/UI/Upgrade/fireup.png" zoom 0.8 xalign 0.35 yalign 0.7
        text "Fire: [Fireball]" style "stattext" xalign 0.359 yalign 0.75
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.405 yalign 0.56 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Fire"), Hide("upgrade1"), Call("increase")]

        add "images/UI/Upgrade/windup.png" zoom 0.8 xalign 0.525 yalign 0.7
        text "Wind: [Wind_Blade]" style "stattext" xalign 0.525 yalign 0.75
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.568 yalign 0.56 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Wind"), Hide("upgrade1"), Call("increase")]

        add "images/UI/Upgrade/earthup.png" zoom 0.8 xalign 0.7 yalign 0.7
        text "Earth: [Rock_Throw]" style "stattext" xalign 0.69 yalign 0.75
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.729 yalign 0.56 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Earth"), Hide("upgrade1"), Call("increase")]
        
        add "images/UI/Upgrade/waterup.png" zoom 0.8 xalign 0.875 yalign 0.7
        text "Water: [Water_Stream]" style "stattext" xalign 0.857 yalign 0.75
        imagebutton:
            auto "images/UI/button/plus2_%s.png" xalign 0.895 yalign 0.56 at pluszoom
            sensitive imagebutton_enabled_state
            action [SetVariable("clickstat", "Water"), Hide("upgrade1"), Call("increase")]
        
#####################################Final Button########################################

        imagebutton:
            auto "images/UI/button/cross_%s.png" xalign 0.44 yalign 0.9 at pluszoom
            action [Hide("upgrade1"), Call("cancelup")]
        imagebutton:
            auto "images/UI/button/reload_%s.png" xalign 0.605 yalign 0.9 at pluszoom
            action [Hide("upgrade1"), Call("resetup")]
        imagebutton:
            auto "images/UI/button/check_%s.png" xalign 0.77 yalign 0.9 at pluszoom
            action [Hide("upgrade1"), Call("confirmup")]
        
    frame:
        xalign 0.5
        yalign 0.09
        xsize 500
        ysize 100
        background Frame("images/UI/5.png")
        text "AP: [curap]" style "aptext" xalign 0.5 yalign 0.5
# 0.7 0.748 0.56        

label increase:

    if clickstat == "HP":
        $playermaxhp += 20
    elif clickstat == "DEF":
        $playerdef += 10
    elif clickstat == "Crit":
        $critdmg1 += 10
    elif clickstat == "Physical":
        $Punch += 10
    elif clickstat == "Fire":
        $Fireball += 10
    elif clickstat == "Wind":
        $Wind_Blade += 10
    elif clickstat == "Earth":
        $Rock_Throw += 10
    elif clickstat == "Water":
        $Water_Stream += 10

    $curap -= 1
    $renpy.restart_interaction()

    jump upstart1

label resetup:
    $curap = maxap
    $Fireball = maxFireball
    $Wind_Blade = maxWind_Blade
    $Rock_Throw = maxRock_Throw
    $Water_Stream = maxWater_Stream
    $Punch = maxPunch
    $critdmg1 = maxCrit
    $playermaxhp = tempHp
    $playerdef = tempDef

    $renpy.restart_interaction()
    jump upstart1

label confirmup:
    $maxap = curap
    $maxFireball = Fireball
    $maxWind_Blade = Wind_Blade
    $maxRock_Throw = Rock_Throw
    $maxWater_Stream = Water_Stream
    $maxPunch = Punch
    $maxCrit = critdmg1
    $ tempHp = playermaxhp
    $ playercurhp = playermaxhp
    $ tempDef = playerdef

    $renpy.restart_interaction()
    jump mapStart1

label cancelup:
    $curap = maxap
    $Fireball = maxFireball
    $Wind_Blade = maxWind_Blade
    $Rock_Throw = maxRock_Throw
    $Water_Stream = maxWater_Stream
    $Punch = maxPunch
    $critdmg1 = maxCrit
    $playermaxhp = tempHp
    $playerdef = tempDef

    $renpy.restart_interaction()
    jump mapStart1


# label finalconfirm:
#     scene black with dissolve
#     return