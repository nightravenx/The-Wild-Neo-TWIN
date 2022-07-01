# TWIN-The Wild Neo by NEOGEE
# cobain

# Karakter Protagonis
define mika = Character("Mika", color="#51d4eb", who_bold=True, who_outlines=[(1, "#000")])
define miko = Character("Miko", color="#b470ec", who_bold=True, who_outlines=[(1, "#000")])
define intro = Character("", color="#B6AAA6", window_yalign=0.5,who_bold=True, who_outlines=[(1, "#000")])
define gui.dialogue_xpos = 0.5

# Karakter Antagonis
define tb = Character("Time Bandit", color="#F18E76", who_bold=True, who_outlines=[(1, "#000")])
define tb2 = Character("Time Bandit Green ", color="#6afaab", who_bold=True, who_outlines=[(1, "#000")])
define tb3 = Character("Time Bandit Biru", color="#7e96ff", who_bold=True, who_outlines=[(1, "#000")])
define tb2dan3 = Character("Time Bandit Hijau & Biru ", color="#6ad9e7", who_bold=True, who_outlines=[(1, "#000")])

# Karakter NPC
define polisi = Character("Polisi", color="#b4b4b4", who_bold=True, who_outlines=[(1, "#000")])
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

# Fade to black and back.
define fade = Fade(0.5, 0.0, 0.5)
# Hold at black for a bit.
define fadehold = Fade(0.5, 1.0, 0.5)
# Camera flash - quickly fades to white, then back to the scene.
define whiteflash = Fade(0.1, 0.0, 0.5, color="#fff")
define redflash = Fade(0.1, 0.0, 0.5, color="#f00")

# image miko
image miko biasa = "Character/MIKO/biasa.png"
image miko senang = "Character/MIKO/senang.png"
image miko marah = "Character/MIKO/marah.png"
image miko sedih = "Character/MIKO/sedih.png"

image miko diam biasa = "Character/MIKO/diam/biasa.png"
image miko diam senang = "Character/MIKO/diam/senang.png"
image miko diam marah = "Character/MIKO/diam/marah.png"
image miko diam sedih = "Character/MIKO/diam/sedih.png"

# image mika
image mika biasa = "Character/MIKA/biasa.png"
image mika senang = "Character/MIKA/senang.png"
image mika marah = "Character/MIKA/marah.png"
image mika sedih = "Character/MIKA/sedih.png"

image mika diam biasa = "Character/MIKA/diam/biasa.png"
image mika diam senang = "Character/MIKA/diam/senang.png"
image mika diam marah = "Character/MIKA/diam/marah.png"
image mika diam sedih = "Character/MIKA/diam/sedih.png"

# image tb
image tb c biasa = "Character/tb/commonFire/biasa.png"
image tb c marah = "Character/tb/commonFire/marah.png"
image tb c senang = "Character/tb/commonFire/senang.png"
image tb c sedih = "Character/tb/commonFire/sedih.png"
image tb c defense = "Character/tb/commonFire/defense.png"

image tb c diam biasa = "Character/tb/commonFire/diam/biasa.png"
image tb c diam marah = "Character/tb/commonFire/diam/marah.png"
image tb c diam senang = "Character/tb/commonFire/diam/senang.png"
image tb c diam sedih = "Character/tb/commonFire/diam/sedih.png"
image tb c diam defense = "Character/tb/commonFire/diam/defense.png"

image tb2 c biasa = "Character/tb/commonWind/biasa.png"
image tb2 c marah = "Character/tb/commonWind/marah.png"
image tb2 c senang = "Character/tb/commonWind/senang.png"
image tb2 c sedih = "Character/tb/commonWind/sedih.png"
image tb2 c defense = "Character/tb/commonWind/defense.png"

image tb2 c diam biasa = "Character/tb/commonWind/diam/biasa.png"
image tb2 c diam marah = "Character/tb/commonWind/diam/marah.png"
image tb2 c diam senang = "Character/tb/commonWind/diam/senang.png"
image tb2 c diam sedih = "Character/tb/commonWind/diam/sedih.png"
image tb2 c diam defense = "Character/tb/commonWind/diam/defense.png"

image tb3 c biasa = "Character/tb/commonWater/biasa.png"
image tb3 c marah = "Character/tb/commonWater/marah.png"
image tb3 c senang = "Character/tb/commonWater/senang.png"
image tb3 c sedih = "Character/tb/commonWater/sedih.png"
image tb3 c defense = "Character/tb/commonWater/defense.png"

image tb3 c diam biasa = "Character/tb/commonWater/diam/biasa.png"
image tb3 c diam marah = "Character/tb/commonWater/diam/marah.png"
image tb3 c diam senang = "Character/tb/commonWater/diam/senang.png"
image tb3 c diam sedih = "Character/tb/commonWater/diam/sedih.png"
image tb3 c diam defense = "Character/tb/commonWater/diam/defense.png"

#flip

image mika biasa flip= im.Flip("Character/MIKA/biasa.png", horizontal=True)
image mika senang flip= im.Flip("Character/MIKA/senang.png", horizontal=True)
image mika marah flip= im.Flip("Character/MIKA/marah.png", horizontal=True)
image mika sedih flip= im.Flip("Character/MIKA/sedih.png", horizontal=True)

image mika diam biasa flip= im.Flip("Character/MIKA/diam/biasa.png", horizontal=True)
image mika diam senang flip= im.Flip("Character/MIKA/diam/senang.png", horizontal=True)
image mika diam marah flip= im.Flip("Character/MIKA/diam/marah.png", horizontal=True)
image mika diam sedih flip= im.Flip("Character/MIKA/diam/sedih.png", horizontal=True)

image splashTWIN = "splashTWIN.png"
image splashNEOGEE = "splashNEOGEE.png"

# music and audio
define audio.explode1 = "audio/explosion.mp3"
define audio.dangerAlarm = "audio/alarm.ogg"

define audio.awalStart = "audio/Teddy.mp3"
define audio.dangerBGM = "audio/danger.mp3"
define audio.afterBoom = "audio/panic.mp3"
define audio.mm_bgm = "audio/main_menu.mp3"

style game_tb:
    background Frame("images/button_idle.png")
    hover_background Frame("images/button_hover.png")

transform charButton:
    zoom 0.9
transform eneZoom:
    zoom 0.75

default user = "Miko"
default sib = "Mika"

label charSelect:
    window hide dissolve
    show screen karakter with dissolve 
    
    $renpy.pause(None,hard=True)

screen karakter:
    frame at alpha_dissolve:
        xalign 0.5 yalign 0.5
        xsize 1500 ysize 1050
        background Frame("images/UI/6.png")
        vbox:
            xalign 0.5 ypos 0.063
            spacing 20
            text "Pilihlah karakter Anda" color "#000000" size 48 minwidth 100 xalign 0.5 yalign 1.0 style "black_font"
            hbox:
                spacing 200
                vbox:
                    # text "MIKO" size 36 xalign 0.5 ypos 100
                    imagebutton:
                        auto "images/Character/MIKO/miko_%s.png"
                        xalign 0.3 ypos 100
                        action [SetVariable("user", "Miko"), SetVariable("sib", "Mika"), Hide("karakter", transition=dissolve), Hide("displayNameText", transition=dissolve), Jump("next")]
                        at charButton

                        hovered Show("displayNameText", displayName = "Miko")
                        unhovered Hide("displayNameText")

                vbox:
                    # text "MIKA" size 36 xalign 0.5 ypos 100
                    imagebutton:
                        auto "images/Character/MIKA/mika_%s.png"
                        xalign 0.3 ypos 100
                        action [SetVariable("user", "Mika"), SetVariable("sib", "Miko"), Hide("karakter", transition=dissolve), Hide("displayNameText", transition=dissolve), Jump("next")]
                        at charButton

                        hovered Show("displayNameText", displayName = "Mika")
                        unhovered Hide("displayNameText")

label eneSelect:
    window hide dissolve
    show screen chooseEnemy with dissolve 
    $renpy.pause(None,hard=True)
    return

screen chooseEnemy:
    frame at alpha_dissolve:
        xalign 0.5 yalign 0.5
        xsize 1500 ysize 1050
        background Frame("images/UI/6.png")
        vbox:
            xalign 0.5 ypos 0.063
            spacing 20
            text "Pilih musuh yang akan dilawan" color "#000000" size 48 minwidth 100 xalign 0.5 yalign 1.0 style "black_font"
            hbox:
                spacing 200
                vbox:
                    # text "MIKA" size 36 xalign 0.5 ypos 100
                    imagebutton:
                        auto "images/Character/tb/commonWind/tb_%s.png"
                        xalign 0.3 ypos 100
                        action [SetVariable("enemydefe", "Wind"), SetVariable("tbType", "Wind"), Hide("chooseEnemy", transition=dissolve), Hide("displayNameText1", transition=dissolve), Call("battle")]
                        at eneZoom

                        hovered Show("displayNameText1", displayName = "Time Bandit Hijau")
                        unhovered Hide("displayNameText1")
                vbox:
                    # text "MIKO" size 36 xalign 0.5 ypos 100
                    imagebutton:
                        auto "images/Character/tb/commonWater/tb_%s.png"
                        xalign 0.3 ypos 100
                        action [SetVariable("enemydefe", "Water"), SetVariable("tbType", "Water"), Hide("chooseEnemy", transition=dissolve), Hide("displayNameText1", transition=dissolve), Call("battle")]
                        at eneZoom

                        hovered Show("displayNameText1", displayName = "Time Bandit Biru")
                        unhovered Hide("displayNameText1")

                
                    
screen displayNameText:
    default displayName = ""
    vbox:
        xalign 0.5
        yalign 0.22
        frame:
            xsize 350
            ysize 100
            background Frame("images/UI/5.png")
            vbox:
                xalign 0.5
                yalign 0.5
                text displayName color "#FFFFFF"

screen displayNameText1:
    default displayName = ""
    vbox:
        xalign 0.5
        yalign 0.22
        frame:
            xsize 450
            ysize 100
            background Frame("images/UI/5.png")
            vbox:
                xalign 0.5
                yalign 0.5
                text displayName color "#FFFFFF"

label splashscreen:
    scene black
    $renpy.pause(1.0,hard=True)
    scene splashNEOGEE with Dissolve(2.0)
    $renpy.pause(2.0,hard=True)
    scene black with dissolve
    $renpy.pause(1.0,hard=True)
    scene splashTWIN with Dissolve(2.0)
    $renpy.pause(2.0,hard=True)
    scene black with dissolve
    $renpy.pause(1.0,hard=True)
    return

define dismissTime = 1
screen noDismiss:
    key 'dismiss' action NullAction()
    timer 1 repeat True action If(dismissTime > 0, true=SetVariable('dismissTime', dismissTime - 1), false=[Hide('noDismiss')])

label start:
    stop music fadeout 2
    scene expression "#000"
    with Dissolve(1.0) #untuk smooth transition setelah klik new game

    # action Preference("auto-forward", "disable")
#################################################################################
# SEQUENCE 01 - PROLOG
#################################################################################
# shot no 1
    show screen noDismiss
    intro "Bumi\nTahun 7047"

# shot no 2
    show screen noDismiss
    intro "Indonesia"
# shot no 3
    show screen noDismiss
    intro "Dunia penuh dengan teknologi, bermacam perangkat digital selalu ada disetiap kegiatan sehari-hari.\n\nKemakmuran dan kemudahan dirasakan oleh setiap manusia."

# shot no 4
    show screen noDismiss
    intro "Namun, teknologi tidak bisa memberikan kestabilan alam.\n\nTeknologi tidak bisa merubah perilaku manusia yang sering merusak kondisi alam.\n\nBanyak hewan yang telah punah karena sifat tamak yang dimiliki manusia."

# shot no 5
    scene bg lab with fade
    play music awalStart fadein 3
    show miko biasa:
        xalign 0.05
        yalign 1.0
    show mika biasa:
        xalign 0.95
        yalign 1.0
    with dissolve

    show mika diam biasa
    with dissolve
    show screen noDismiss
    miko "Mika, coba lihat ini. Ini hewan apa? Aku tidak pernah lihat sebelumnya."
    $ renpy.pause(0.5, hard=True)

    show miko diam biasa
    show mika biasa
    with dissolve
    show screen noDismiss
    mika "Hmmm, ini benar hewan? Aku tidak tahu kalau ada hewan seperti ini."
    $ renpy.pause(0.5, hard=True)

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Bisakah kamu scan gambar ini? Mungkin ada informasi yang cocok di database."
    $ renpy.pause(0.5, hard=True)


    show miko diam biasa
    show mika biasa
    with dissolve
    show screen noDismiss
    mika "Sebentar Miko, coba aku teliti dengan kacamataku."
    $ renpy.pause(0.5, hard=True)

    hide mika
    hide miko
    with dissolve
# shot no 6
    show screen noDismiss
    "(Mika memindai gambar dengan kacamata yang dipakainya. Kacamata canggih yang setara dengan supercomputer)"

# shot no 7
    scene bg lab with dissolve

    show mika senang flip:
        xalign 0.95
        yalign 1.0
    show miko biasa:
        xalign 0.05
        yalign 1.0
    with dissolve

    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Ketemu! Berdasarkan data, ini adalah orang utan. Hewan jenis kera yang hidup di hutan tropis seperti pulau Kalimantan dan Sumatera."


    show miko biasa
    show mika diam senang flip
    with dissolve
    show screen noDismiss
    miko "Orang utan? Memang mirip dengan orang ya, tetapi badannya penuh bulu."


    show mika biasa
    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Iya benar sekali, memang dinamakan orang utan karena mirip orang. Di sini tertulis hewan ini sudah punah pada tahun 4262."


    show miko sedih
    show mika diam biasa
    with dissolve
    show screen noDismiss
    miko "Sudah punah tahun 4262? Pantas saja aku tidak tahu dan tidak pernah lihat hewan ini."
     

    show miko biasa
    show mika diam biasa
    with dissolve
    show screen noDismiss
    miko "Sayang sekali sekarang hewan tidak beragam, paling banyak hanya kucing dan anjing."

    hide mika 
    hide miko
    with dissolve

# shot no 8
    show screen noDismiss
    "Miko dan Mika, adalah sepasang saudara kembar yang merupakan genius teknologi di Surabaya, Indonesia"
    show screen noDismiss
    "Di usia ke-17, tahun ini, mereka sudah menciptakan banyak alat teknologi yang dipakai di penjuru dunia"
    show screen noDismiss
    "Dengan niat mengembalikan keanekaragaman hewan di Indonesia, mereka berniat menciptakan mesin waktu"


# shot no 9
    jump charSelect

# shot no 10
label next:
    window show dissolve
    scene bg lab with dissolve
    show mika biasa:
        xalign 0.95
        yalign 1.0
    show miko biasa:
        xalign 0.05
        yalign 1.0
    with dissolve

    show mika diam biasa
    with dissolve
    show screen noDismiss
    miko "Hey Mika, aku punya ide! Bagaimana jika kita membuat mesin waktu untuk menarik hewan dari masa lalu ke masa sekarang?"

    show mika senang flip
    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Ide yang menarik! Tapi kamu tahu kan, time-travelling itu tidak mungkin bisa dilakukan? Kita tidak bisa kembali ke masa lalu, Miko."

    show mika diam senang flip
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Iya benar, kita tidak bisa kembali ke masa lalu. Tetapi kita bisa menarik yang ada di masa lalu ke masa sekarang bukan?"

    show miko diam biasa
    show mika senang flip
    with dissolve
    show screen noDismiss
    mika "Ah! Jika kita mengunci sesuatu di sebuah ruang dan memanipulasi waktu secara temporal..."

    show mika diam senang flip
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Mik..."

    show miko diam biasa
    show mika senang flip
    with dissolve
    show screen noDismiss
    mika "Lalu membatasi progresi metabolisme biologis objek pada ruang tersebut..."

    show mika diam senang flip
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Mika..."

    show miko diam biasa
    show mika senang flip
    with dissolve
    show screen noDismiss
    mika "Digabungkan dengan data lokasi dan waktu setiap hewan yang cukup dari database..."

    show mika diam senang flip
    show miko marah
    with dissolve
    show screen noDismiss
    miko "Mika!"

    show miko diam marah
    show mika senang flip
    with dissolve
    show screen noDismiss
    mika "Ah! Maaf aku terlalu bersemangat dengan ide dan teori yang tiba-tiba muncul, jadi tidak sadar lingkungan, hehe."

    show mika diam senang flip
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Dasar kebiasaan kamu. Tapi berarti ide ini bisa dilakukan kan?"

    show miko diam biasa
    show mika senang flip
    with dissolve
    show screen noDismiss
    mika "Berdasarkan pemikiranku dan teknologi yang sekarang, seharusnya bisa!"

    show mika diam senang flip
    show miko senang
    with dissolve
    show screen noDismiss
    miko "Ayo buat mesin waktu?"

    show miko diam senang
    show mika senang flip
    with dissolve
    show screen noDismiss
    mika "Ayo! Dan kita kembalikan keanekaragaman hewan!"


    hide miko
    hide mika
    with dissolve

# shot no 11
    show screen noDismiss
    "(Miko dan Mika mulai membentuk portal waktu di lab mereka)"
    show screen noDismiss
    "(Clink! Clank!)"
    show screen noDismiss
    "(Beberapa waktu kemudian...)"

# shot no 12
    scene bg portal with fade

    show mika senang flip:
        xalign 0.95
        yalign 1.0
    show miko senang:
        xalign 0.05
        yalign 1.0
    
    show mika diam senang flip
    with dissolve
    show screen noDismiss
    miko "Portal waktu selesai!"

    show miko diam senang
    show mika senang flip
    with dissolve
    show screen noDismiss
    mika "Yeay!"

    show mika diam senang flip
    show miko senang
    with dissolve
    show screen noDismiss
    miko "Ayo segera aktifkan portalnya Mika!"

    show miko diam senang
    show mika biasa
    with dissolve
    show screen noDismiss
    mika "Sebentar, aku atur pengaturannya terlebih dahulu."

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Oke! Aku suka angka 7, jadi ayo kita coba tarik 7 hewan kesini!"

    show miko diam biasa
    show mika biasa
    with dissolve
    show screen noDismiss
    mika "7 hewan... data hewan... Orangutan... Harimau... Komodo... Kasuari... Anoa... Gajah... Kakatua...."
    show screen noDismiss
    mika "Pengaturan selesai!"

    hide miko
    hide mika
    with dissolve

# shot no 13
    show screen noDismiss
    "Portal waktu telah diaktifkan"
    show screen noDismiss
    "Cahaya biru berpendar terang dari portal waktu. Miko dan Mika menyaksikan mesin yang mereka buat dengan antusias"
# shot no 14
    scene bg portal1 with dissolve
    stop music
    play music dangerBGM fadein 2
    play sound dangerAlarm loop

    show screen noDismiss
    "Tiba-tiba, layar mesin berubah menjadi merah dan menampilkan pesan kesalahan"
    show screen noDismiss
    "WARNING! PORTAL UNSTABLE!"

# shot no 15
    scene bg portal2 with dissolve
    stop sound fadeout 5
    play sound explode1

    show screen noDismiss
    "*shiiiing* *BAAAM*"
    show screen noDismiss
    "Sinar putih yang begitu terang disertai dentuman besar mengisi lab."
    stop music fadeout 2
# shot no 16
    scene bg portal with Dissolve(2.0)
    
    show screen noDismiss
    "Kondisi lab kembali tenang, portal waktu tidak mengeluarkan cahaya dan suara yang bising lagi"

    play music afterBoom fadein 2
    show screen noDismiss
    "Miko dan Mika yang sempat terlempar ke lantai, berdiri lagi dan langsung mengecek mesin"
    $ renpy.pause(0.5, hard=True)
# shot no 17
    show miko biasa:
        xalign 0.05
        yalign 1.0
    show mika biasa:
        xalign 0.95
        yalign 1.0
    with dissolve

    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Oh tidak! Apa yang terjadi?"

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Ugh, apakah portal waktu kita gagal berfungsi?"

    show miko diam biasa
    show mika biasa
    with dissolve
    show screen noDismiss
    mika "Berdasarkan statistik mesin, portal waktu berhasil menarik 7 hewan kok Miko..."

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Umm... Mika..."

    show miko diam biasa
    show mika biasa
    with dissolve
    show screen noDismiss
    mika "Tapi kenapa tidak ada hewan yang muncul disini? Hmm... detail statistik... lokasi portal..."

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Mika... dia itu siapa?"

    show miko diam biasa
    show mika biasa
    with dissolve
    show screen noDismiss
    mika "Hah?!"
    show screen noDismiss
    mika "Portalnya terpecah jadi 7 dan tersebar di lokasi yang berbeda?!"
    show screen noDismiss
    mika "Ada beberapa portal kecil lain juga yang terdeteksi dan entitas lain terhubung melalui portal tersebut?!"
    
    show mika diam biasa
    show miko marah
    with dissolve
    show screen noDismiss
    miko "MIKA!"

    show mika biasa
    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Hah?! Kenapa Miko?"

    show miko biasa
    show mika diam biasa
    with dissolve
    show screen noDismiss
    miko "Itu ada orang asing di dekat portal waktu!"



# shot no 18
    scene bg portal with dissolve

    show screen noDismiss
    "Tanpa disadari sebelumnya, ada orang asing yang tiba-tiba muncul di lab mereka"
    show screen noDismiss
    "Seorang pemuda kisaran usia 20 tahun yang memiliki tampilan unik, mengenakan pakaian yang dilengkapi banyak peralatan memburu"
    show screen noDismiss
    "Kelihatannya orang tersebut datang dari era yang berbeda dari Bumi tahun 7047"

# shot no 19
    show miko biasa:
        xalign 0.05
        yalign 1.0
    show mika biasa behind miko:
        xalign 0.2
        yalign 1.0
    show tb c biasa:
        xalign 0.9
        yalign 1.0


    show miko diam biasa
    show mika diam biasa
    with dissolve
    show screen noDismiss
    tb "Ahahahaha!"
    show screen noDismiss
    tb "Bos memang hebat! Tidak sia-sia aku mendukung bos membentuk portal waktu!"
    show screen noDismiss
    tb "Hahahaha!"
    show screen noDismiss
    tb "Ah, sebentar ini dimana dan tahun berapa?"
    show screen noDismiss
    tb "Oh, Bumi 7047."
    show screen noDismiss
    tb "Wahahaha! Bos hebat bisa membuka portal ke 100 tahun yang lalu!"

    show mika diam biasa
    show tb c diam biasa
    show miko marah
    with dissolve
    show screen noDismiss
    miko "Hei siapa kamu?!"


    show miko diam marah
    show mika diam biasa
    show tb c biasa
    with dissolve
    show screen noDismiss
    tb "Ah, ada orang disini ternyata. Halo penduduk bumi tahun 7047!"


    show miko diam marah behind mika
    show tb c diam biasa
    show mika marah
    with dissolve
    show screen noDismiss
    mika "Ya! Siapa kamu dan kenapa ada disini?!"


    show mika diam marah
    show miko diam marah
    show tb c biasa
    with dissolve
    show screen noDismiss
    tb "Hei tenang anak muda. Kami disini tidak akan mengganggu kalian. Target kami hanyalah memburu dan menangkap hewan."


    show mika diam marah behind miko
    show tb c diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Kami?"

    show mika diam marah
    show miko diam biasa
    show tb c biasa
    with dissolve
    show screen noDismiss
    tb "Iya, kami adalah Time Bandit yang setia mengikuti bos besar. Bos ingin memburu hewan dari masa lalu, kami siap beraksi!"

    show miko diam biasa behind mika
    show tb c diam biasa
    show mika biasa
    with dissolve
    show screen noDismiss
    mika "Tapi, kamu kan sendirian..."

    show mika diam biasa
    show miko diam biasa
    show tb c biasa
    show screen noDismiss
    tb "Sendiri?"
    show screen noDismiss
    tb "Eh?"
    show screen noDismiss
    tb "Hei! Kenapa aku sendirian?! Dimana bos?! Dimana Time Bandit yang lain?!"
    hide tb with dissolve

# shot no 20

    show mika biasa
    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Miko, setelah aku analisis menggunakan kacamataku, alat yang digunakan di tangan orang itu adalah alat seperti mesin waktu yang kita buat, tapi lebih canggih."

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Oh ya? Berarti dia benar dari masa depan? Perjalanan waktu benar bisa dilakukan?"

    show miko diam biasa
    show mika biasa
    with dissolve
    show screen noDismiss
    mika "Nampaknya begitu. Jika dia bisa pergi ke masa sekarang, maka dia bisa juga dikembalikan ke masa asalnya menggunakan alat yang sama."

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Oke, kalau begitu ayo kita kembalikan dia ke masa depan!"

    show miko diam biasa
    show mika senang flip
    with dissolve
    show screen noDismiss
    mika "Miko, kita bisa menggunakan alat invensi kita sebelumnya, Elemental Gauntlet, untuk mengalahkan dia."

    show mika diam senang flip
    show miko senang
    with dissolve
    show screen noDismiss
    miko "Ide yang bagus Mika!"


# shot no 21
    scene bg portal with dissolve

    show mika biasa behind miko:
        xalign 0.2
        yalign 1.0
    show miko marah:
        xalign 0.05
        yalign 1.0
    show tb c biasa:
        xalign 0.9
        yalign 1.0
    
    show mika diam biasa 
    show tb c diam biasa
    with dissolve
    show screen noDismiss
    miko "Hei! Kami tidak tahu kamu siapa dan darimana, tapi kami tau kamu bukan orang yang baik!"
    show screen noDismiss
    miko "Tidak akan kami biarkan kamu memburu dan menangkap hewan di bumi ini!"
    
    hide mika
    hide tb
    hide miko
    with dissolve

    # TB stat beginner
    $ enemymaxhp = 200
    $ enemycurhp = 200
    $ enemyatk = 100
    $ enemydef = 100
    $ tbType = "Fire"
    call battle from _call_battle #pindah ke battle screen
    
    jump afterBattle0

label afterBattle0:
# shot no 1
    play music awalStart fadein 2
    scene bg portal with fade

    show screen noDismiss
    "Miko dan Mika berhasil mengalahkan Time Bandit hingga membuatnya terjatuh dan tidak berdaya."

# shot no 2
    show mika biasa behind miko:
        xalign 0.2
        yalign 1.0
    show miko biasa:
        xalign 0.05
        yalign 1.0
    show tb c marah :
        xalign 0.9
        yalign 1.0
    with dissolve

    show mika diam biasa
    show miko diam biasa
    with dissolve
    show screen noDismiss
    tb "Ughhh..."

    show mika diam biasa
    show miko biasa
    show tb c diam biasa
    with dissolve
    show screen noDismiss
    miko "Dia sudah tidak berdaya! Ayo kita kembalikan dia ke masa depan!"

    show mika biasa
    show miko diam biasa behind mika
    show tb c diam biasa
    with dissolve
    show screen noDismiss
    mika "Oke!"


# shot no 3
    scene bg portal with dissolve
    show screen noDismiss
    "Miko dan Mika berhasil mengalahkan Time Bandit hingga membuatnya terjatuh dan tidak berdaya."
    show screen noDismiss
    "Mika mulai menganalisa alat di tangan Time Bandit yang dicurigai sebagai mesin waktu."

# shot no 4
    show mika biasa behind miko:
        xalign 0.2
        yalign 1.0
    show miko biasa:
        xalign 0.05
        yalign 1.0
    show tb c biasa:
        xalign 0.9
        yalign 1.0
    with dissolve
    
    show miko diam biasa
    show mika diam biasa
    with dissolve
    show screen noDismiss
    tb "Ugh, apa yang kalian lakukan?"

    show mika diam biasa
    show miko marah
    show tb c diam biasa
    with dissolve
    show screen noDismiss
    miko "Mengembalikan kamu ke waktu asalmu! Tidak akan kubiarkan kamu memburu dan menangkap hewan disini!"

    show mika diam biasa
    show miko diam marah
    show tb c biasa
    with dissolve
    show screen noDismiss
    tb "Hah, kamu kira aku datang kesini sendirian? Bos membawa pasukan Time Bandit yang sangat banyak tahu!"

    show mika biasa
    show miko diam marah behind mika
    show tb c diam biasa
    with dissolve
    show screen noDismiss
    mika "Tapi faktanya kamu kan sendirian disini."

    show mika diam biasa
    show miko diam marah
    show tb c biasa
    with dissolve
    show screen noDismiss
    tb "Uhh...benar juga sih."
    show screen noDismiss
    tb "Tapi aku yakin dan aku tahu Bos dan Time Bandit yang lain ada di tahun ini! Hahahaha!"

    show mika diam biasa behind miko
    show miko biasa
    show tb c diam biasa
    with dissolve
    show screen noDismiss
    miko "Tidak masalah! Akan kami cari dan kami kembalikan kalian semua ke tempat asal! Lihat saja!"

    show mika diam biasa
    show miko diam biasa
    show tb c biasa
    with dissolve
    show screen noDismiss
    tb "Hahaha, bisa apa kalian hei anak kecil. Kalian kira kalian bisa menemukan Time Bandit dengan mudah? Kami adalah pasukan yang..."

    show mika biasa
    show miko diam biasa behind mika
    show tb c diam biasa
    with dissolve
    show screen noDismiss
    mika "Ada 21 koordinat lokasi Time Bandit lainnya Miko. Tersebar di berbagai pulau di Indonesia."

    show mika diam biasa
    show miko diam biasa
    show tb c biasa
    with dissolve
    show screen noDismiss
    tb "Hei hei hei! Kalian jangan anggap remeh kami Time..."

    show mika biasa 
    show miko diam biasa behind mika
    show tb c diam biasa
    with dissolve
    show screen noDismiss
    mika "Kebetulan lokasi terdekat ada di kota kita Miko. Patung Sura dan Baya, 5 kilometer dari sini."

    show mika diam biasa behind miko
    show miko biasa
    show tb c diam biasa
    with dissolve
    show screen noDismiss
    miko "Nice info Mika! Oke, sekarang saatnya kamu kembali ke tempat asalmu Time Bandit!"

    show mika biasa
    show miko diam biasa behind mika
    show tb c diam biasa
    with dissolve
    show screen noDismiss
    mika "Oke! Alatnya sudah kuatur untuk kembali ke waktu asalnya. Menjauh Miko!"

    show mika diam biasa
    show miko diam biasa
    show tb c marah
    with dissolve
    show screen noDismiss
    tb "Aaaah kenapa Time Gauntletnya tidak bisa dihentikan?!"

    show mika senang
    show miko diam biasa behind mika
    show tb c diam marah
    with dissolve
    show screen noDismiss
    mika "Hehe, sudah kukunci alatnya sehingga hanya bisa digunakan untuk terakhir kali ini saja."

    show mika diam senang
    show miko diam biasa
    show tb c marah
    with dissolve
    show screen noDismiss
    tb "Ugh! Kalian!"

    show tb c defense
    with dissolve
    show screen noDismiss
    tb "Eh? Miko dan Mika? Kalian kembar genius Miko dan Mika?!"

    show mika diam biasa behind miko
    show miko biasa
    show tb c diam defense
    with dissolve
    show screen noDismiss
    miko "Ya! Kenapa memangnya?!"

    show mika diam biasa
    show miko diam biasa
    show tb c biasa
    with dissolve
    show screen noDismiss
    tb "Ha ha ha...Tidak kusangka ternyata aku bertemu kalian."
    show screen noDismiss
    tb "Kenapa aku tidak sadar sejak awal."
    show screen noDismiss
    tb "Ini akan menarik, bos pasti akan kaget saat melihat kalian."
    show screen noDismiss
    tb "Kalian harus tau, bos itu adalah..."



# shot no 5
    scene bg portal with dissolve
    show screen noDismiss
    "Alat yang ternyata dinamakan Time Gauntlet itu mulai berpendar mengeluarkan cahaya yang sangat terang."
    show screen noDismiss
    "Sedetik kemudian, Time Bandit yang semula ada di depan Miko dan Mika seketika hilang tanpa jejak."
    show screen noDismiss
    "Sesuai prediksi dan rencana Mika, seharusnya Time Bandit tersebut sudah kembali ke asal tempatnya kembali di masa depan."


# shot no 6

    show mika biasa:
        xalign 0.95
        yalign 1.0
    show miko biasa:
        xalign 0.05
        yalign 1.0
    with dissolve

    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Tadi dia bilang apa Miko?"

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Entahlah, tidak terdengar dengan jelas."

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Dia sudah kembali ke waktu asalnya kan?"

    show mika biasa
    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Seharusnya iya, dari hasil simulasi yang aku lakukan tadi sekitar 98%% akurat."

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Oke! Sekarang saatnya kita cari Time Bandit yang lain! Tujuan pertama, Patung Sura dan Baya!"

# shot no 7
    scene bg portal with dissolve

    show screen noDismiss
    "Miko dan Mika mempersiapkan peralatan dan barang lain yang perlu dibawa untuk berpergian."
    show screen noDismiss
    "Kemudian Miko dan Mika bergegas pergi dari workshop untuk mencari Time Bandit lainnya."

    stop music fadeout 2
    $placeUnlocked = 1
    jump mapStart

#################################################################################
# SEQUENCE 02 - ACT JAVA: 01 SURABAYA
#################################################################################
label surabaya:
# shot no 8
    play music awalStart fadein 2
    scene bg jawa surabaya with fade

    show screen noDismiss
    "Dengan mengendarai hoverboard, Miko dan Mika sampai ke lokasi Time Bandit terdekat, Patung Sura dan Baya."

    show screen noDismiss
    "Patung Sura dan Baya adalah patung yang terkenal dan menjadi ikon dari kota Surabaya."

    show screen noDismiss
    "Berdasarkan legenda, patung ini menceritakan tentang Sura si ikan hiu dan Baya si buaya yang saling memperebutkan lokasi kekuasaan di kota Surabaya."


# shot no 9

    show mika biasa:
        xalign 0.95
        yalign 1.0
    show miko biasa:
        xalign 0.05
        yalign 1.0
    with dissolve

    show mika diam biasa
    with dissolve
    show screen noDismiss
    miko "Oke, kita sudah sampai. Kira-kira dimana ya Time Banditnya?"


    show mika biasa
    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Sayangnya lokasi yang bisa dideteksi tidak spesifik Miko, aku hanya tau lokasinya di sekitar sini."


    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Hmmm."


    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Hei lihat ada keributan di depan patung Sura!"


# shot no 10
    scene bg jawa surabaya with dissolve

    show screen noDismiss
    "Terjadi keributan di depan patung Sura dan Baya."
    show screen noDismiss
    "Terlihat ada dua pemuda yang mengenakan baju mirip dengan Time Bandit sebelumnya."
    show screen noDismiss
    "Kedua pemuda tersebut sedang berargumen satu sama lain."
    show screen noDismiss
    "Keadaan semakin ramai dengan adanya petugas keamanan yang berusaha menghentikan mereka."
    show screen noDismiss
    "Miko dan Mika bergerak mendekati mereka."

# shot no 11
    show mika diam biasa behind miko:
        xalign 0.2
        yalign 1.0
    show miko diam biasa:
        xalign 0.05
        yalign 1.0
    show tb2 c biasa:
        xalign 0.8
        yalign 1.0
    show tb3 c diam biasa behind tb2:
        xalign 0.95
        yalign 1.0
    with dissolve
    show screen noDismiss
    tb2 "Aku yang akan menangkap hiu! Kamu saja yang menangkap buaya!"

    show mika diam biasa
    show miko diam biasa
    show tb2 c diam biasa behind tb3
    show tb3 c marah
    with dissolve
    show screen noDismiss
    tb3 "Gak mau! Aku saja yang menangkap hiu! Aku suka hiu karena dia lebih keren daripada buaya!"

    show mika diam biasa
    show miko diam biasa
    show tb2 c diam biasa
    show tb3 c diam marah
    with dissolve
    show screen noDismiss
    polisi "Hei hentikan kalian berdua! Kalian jangan merusak barang publik!"

    show mika diam biasa
    show miko diam biasa
    show tb2 c marah
    show tb3 c marah behind tb2
    with dissolve
    show screen noDismiss
    tb2dan3 "Jangan ikut campur!"

    show mika diam biasa behind miko
    show miko biasa
    show tb2 c diam marah
    show tb3 c diam marah
    with dissolve
    show screen noDismiss
    miko "Uhh, ada apa ini?"

    show mika diam biasa
    show miko diam biasa
    show tb2 c diam marah
    show tb3 c diam marah
    with dissolve
    show screen noDismiss
    polisi "Ini, ada dua orang asing yang meributkan ingin menangkap hiu dan buaya."


    show mika biasa
    show miko diam biasa behind mika
    show tb2 c diam marah
    show tb3 c diam marah
    with dissolve
    show screen noDismiss
    mika "Tapi itu kan patung ya? Bukan hiu dan buaya asli."

    show mika diam biasa
    show miko diam biasa
    show tb2 c diam biasa behind tb3
    show tb3 c biasa
    with dissolve
    show screen noDismiss
    tb3 "Haaah?! Apa katamu?! Ini adalah hiu dan buaya legendaris! Bukan patung! Lihat baik-baik, mereka sangat nyata!"

    show mika diam biasa
    show miko diam biasa
    show tb2 c senang
    show tb3 c diam biasa behind tb2
    with dissolve
    show screen noDismiss
    tb2 "Ya benar! Akan aku tangkap hiu ini lalu kulaporkan ke bos! Pasti dia akan sangat senang hahaha!"

    show mika diam biasa
    show miko diam biasa
    show tb2 c diam senang  behind tb3
    show tb3 c marah
    with dissolve
    show screen noDismiss
    tb3 "Hei! Aku yang akan menangkap hiu, bukan kamu!"

    show mika diam biasa behind miko
    show miko biasa
    show tb2 c diam biasa
    show tb3 c diam marah
    with dissolve
    show screen noDismiss
    miko "Ummm.... Mereka ini benar Time Bandit yang ingin menangkap dan memburu hewan itu Mika?"

    show mika biasa
    show miko diam biasa behind mika
    show tb2 c diam biasa
    show tb3 c diam biasa
    with dissolve
    show screen noDismiss
    mika "Dari tampilannya sih iya. Lihat, mereka juga menggunakan Time Gauntlet yang sama!"
    show screen noDismiss
    mika "Tapi... tidak kusangka mereka malah menyangka patung Sura dan Baya sebagai hewan beneran."


    show mika diam biasa behind miko
    show miko biasa
    show tb2 c diam biasa
    show tb3 c diam biasa
    with dissolve
    show screen noDismiss
    miko "Ha ha ha, Mereka agak aneh ya."
    show screen noDismiss
    miko "Walaupun begitu, mereka tetap Time Bandit yang sama. Sebelum mereka memburu hewan dan...merusak barang publik, ayo kita kembalikan mereka ke tempat asalnya!"

# shot no 13

    # TB stat beginner
    $ enemymaxhp = 250
    $ enemycurhp = 250
    $ enemyatk = 120
    $ enemydef = 90
    $ bgName = "surabaya"
    call resetAll from _call_resetAll_2
    call eneSelect from _call_eneSelect

# shot no 14
    scene bg jawa surabaya with dissolve
    play music awalStart fadein 2
    show screen noDismiss
    "Miko dan Mika berhasil mengalahkan Time Bandit."
    show screen noDismiss
    "Sebelum mengembalikan mereka ke tempat asalnya, Mika memindai lokasi Time Bandit berikutnya."


# shot no 15
    show mika diam biasa:
        xalign 0.95
        yalign 1.0
    show miko biasa:
        xalign 0.05
        yalign 1.0
    with dissolve
    show screen noDismiss
    miko "Oke, saatnya mengembalikan mereka ke masa depan."

    show mika biasa
    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Tunggu sebentar Miko, aku scan dulu dimana lokasi Time Bandit berikutnya"

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Oh iya, hampir lupa."

    show mika biasa
    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Umm, kasihan mereka berdua sampai pingsan begini."

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Hehe, maaf ya sepertinya tadi aku terlalu bersemangat."
# shot no 16
    scene bg jawa surabaya with dissolve

    show screen noDismiss
    "Mika selesai mendapatkan lokasi Time Bandit berikutnya."
    
    show screen noDismiss
    "Time Gauntlet Time Bandit juga sudah diatur untuk mengembalikan mereka ke tempat asalnya."
    

# shot no 17

    show mika biasa:
        xalign 0.95
        yalign 1.0
    show miko diam biasa:
        xalign 0.05
        yalign 1.0
    with dissolve
    show screen noDismiss
    mika "Oke, lokasi berikutnya adalah Candi Borobudur, Jawa Tengah."

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Hmm jauh juga ya."
    
    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Tapi tidak masalah, tadi aku sudah merecharge hoverboard kita sampai penuh."

    show mika biasa
    show miko diam biasa
    with dissolve
    show screen noDismiss
    mika "Terima kasih Miko."

    show mika diam biasa
    show miko biasa
    with dissolve
    show screen noDismiss
    miko "Sama-sama Mika. Oke! Ayo berangkat!"
    stop music fadeout 3
    jump end
# shot no 18
label end:
    show black with Fade(1.5, 0, 1.5)
    play music mm_bgm fadein 3
    show screen noDismiss
    intro "{b}{color=#ffbb00}Grind area telah terbuka.{/color}{/b}\n\nKamu bisa melakukan battle berulang kali disini untuk mendapatkan experience point."

# shot no 19
    show screen noDismiss
    intro "{b}{color=#ffbb00}Upgrade Elemental Gauntlet telah terbuka.{/color}{/b}\n\nSetelah mendapatkan experience yang cukup untuk naik level, kamu bisa meningkatkan kemampuan Elemental Gauntlet."

# shot no 20
    show screen noDismiss
    intro "{b}{size=40}Terima kasih sudah memainkan TWIN - The Wild Neo Demo version.{/size}{/b}"
# shot no 21
    show screen noDismiss
    intro "{b}{size=40}Petualangan Miko dan Mika akan berlanjut di versi berikutnya.{/size}{/b}"

# shot no 22
    stop music fadeout 1
    scene black with Fade(0.5,0,0.5)
    $placeUnlocked = 2
    jump mapStart
    return
