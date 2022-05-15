# The Wild Neo (TWIN) by Meta7
# Karakter Protagonis
define ra = Character("[ra]", color="#CD6247", who_bold=True, who_outlines=[(1, "#000")])
define ro = Character("[ro]", color="#EE8A79", who_bold=True, who_outlines=[(1, "#000")])

# Karakter Antagonis
define s = Character("Sadi", color="#B6AAA6", who_bold=True, who_outlines=[(1, "#000")])
define a = Character("Anji", color="#F8DC71", who_bold=True, who_outlines=[(1, "#000")])
define b = Character("Bili", color="#99DAEC", who_bold=True, who_outlines=[(1, "#000")])
define c = Character("Cali", color="#F18E76", who_bold=True, who_outlines=[(1, "#000")])

# Karakter NPC
define jan = Character("Janu", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define feb = Character("Febri", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define mar = Character("Maria", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define apr = Character("Aprilia", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define mei = Character("Mey", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define jun = Character("Yunia", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define jul = Character("Julio", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define agu = Character("Agus", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define sep = Character("Septian", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define okt = Character("Okta", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define nov = Character("Novian", color="#EF6C3A", who_bold=True, who_outlines=[(1, "#000")])

label start:
    # play music
    # play sound
    # stop music
    # scene bg
    # show a at right
    # show a at center
    # show a at left

    #For battle screen testing
    # "..."
    # jump bttle



    "Hey nak, bangun, pakaianmu sangat kumuh, aku bahkan tidak tau kamu itu laki-laki atau perempuan"
    menu:
        "Laki-laki":
            python:
                ro = renpy.input("Owh laki-laki? Siapa nama kamu?", length=8)
                ro = ro.strip()

                if not ro:
                    ro = "Rivero"
            ro "Namaku [ro]"
        "Perempuan":
            python:
                ra = renpy.input("Owh perempuan? Siapa nama kamu?", length=8)
                ra = ra.strip()

                if not ra:
                    ra = "Rivera"
            ra "Namaku [ra]"

    "Tamat."

    return
