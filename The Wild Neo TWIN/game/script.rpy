# TWIN-The Wild Neo by NEOGEE

# Karakter Protagonis
define mika = Character("Mika", color="#CD6247", who_bold=True, who_outlines=[(1, "#000")])
define miko = Character("Miko", color="#EE8A79", who_bold=True, who_outlines=[(1, "#000")])
define intro = Character("", color="#B6AAA6", window_yalign=0.5,who_bold=True, who_outlines=[(1, "#000")])
define gui.dialogue_xpos = 0.5

# Karakter Antagonis
define tb = Character("Time Bandit", color="#F18E76", who_bold=True, who_outlines=[(1, "#000")])

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

image mika biasa flip= im.Flip("Character/MIKA/biasa.png", horizontal=True)
image mika senang flip= im.Flip("Character/MIKA/senang.png", horizontal=True)
image mika marah flip= im.Flip("Character/MIKA/marah.png", horizontal=True)
image mika sedih flip= im.Flip("Character/MIKA/sedih.png", horizontal=True)

image mika diam biasa flip= im.Flip("Character/MIKA/diam/biasa.png", horizontal=True)
image mika diam senang flip= im.Flip("Character/MIKA/diam/senang.png", horizontal=True)
image mika diam marah flip= im.Flip("Character/MIKA/diam/marah.png", horizontal=True)
image mika diam sedih flip= im.Flip("Character/MIKA/diam/sedih.png", horizontal=True)

style game_tb:
    background Frame("images/button_idle.png")
    hover_background Frame("images/button_hover.png")

default user = "MIKO"
default sib = "MIKA"

label start:

#################################################################################
# Prolog
#################################################################################
# shot no 1
    intro "Bumi\nTahun 7047{w=3}{nw}"
    with Dissolve(1)
    $ renpy.pause(1, hard=True)
# shot no 2
    intro "Indonesia{w=3}{nw}"
    with Dissolve(1)
    $ renpy.pause(1, hard=True)
# shot no 3
    intro "Dunia penuh dengan teknologi, bermacam perangkat digital selalu ada disetiap kegiatan sehari-hari.{p=4.0}\nKemakmuran dan kemudahan dirasakan oleh setiap manusia.{w=4}{nw}"
    with Dissolve(1)
    $ renpy.pause(1, hard=True)
# shot no 4
    intro "Namun, teknologi tidak bisa memberikan kestabilan alam.{p=4.0}\nTeknologi tidak bisa merubah perilaku manusia yang sering merusak kondisi alam.{p=4.0}\nBanyak hewan yang telah punah karena sifat tamak yang dimiliki manusia.{w=4}{nw}"
    with Dissolve(1)
    $ renpy.pause(1, hard=True)
# shot no 5
    scene bg lab
    show miko biasa at left:
        xalign 0.05
    show mika biasa at right:
        xalign 0.95

    show mika diam biasa at right:
        xalign 0.95
    with dissolve
    miko "Mika, coba lihat ini. Ini hewan apa? Aku tidak pernah lihat sebelumnya."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa with dissolve

    show miko diam biasa at left:
        xalign 0.05
    with dissolve
    mika "Hmmm, ini benar hewan? Aku tidak tahu kalau ada hewan seperti ini."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa with dissolve

    show mika diam biasa at right:
        xalign 0.95
    with dissolve
    miko "Bisakah kamu scan gambar ini? Mungkin ada informasi yang cocok di database."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa with dissolve

    show miko diam biasa at left:
        xalign 0.05
    with dissolve
    mika "Sebentar Miko, coba aku teliti dengan kacamataku."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa with dissolve

    hide mika biasa with dissolve
    hide miko biasa with dissolve
# shot no 6
    "(Mika memindai gambar dengan kacamata yang dipakainya. Kacamata canggih yang setara dengan supercomputer){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
# shot no 7
    scene bg lab

    show mika senang flip at right:
        xalign 0.95
    show miko diam biasa at left:
        xalign 0.05
    mika "Ketemu! Berdasarkan data, ini adalah orang utan. Hewan jenis kera yang hidup di hutan tropis seperti pulau Kalimantan dan Sumatera."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika senang flip

    show miko biasa at left:
        xalign 0.05
    show mika diam senang flip at right:
        xalign 0.95
    miko "Orang utan? Memang mirip dengan orang ya, tetapi badannya penuh bulu."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam senang flip
    hide miko biasa

    show mika biasa at right:
        xalign 0.95
    show miko diam biasa at left:
        xalign 0.05
    mika "Iya benar sekali, memang dinamakan orang utan karena mirip orang. Di sini tertulis hewan ini sudah punah pada tahun 4262."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika biasa

    show miko sedih at left:
        xalign 0.05
    show mika diam biasa at right:
        xalign 0.95
    miko "Sudah punah tahun 4262? Pantas saja aku tidak tahu dan tidak pernah lihat hewan ini."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko sedih

    show miko biasa at left:
        xalign 0.05

    show mika diam biasa at right:
        xalign 0.95

    miko "Sayang sekali sekarang hewan tidak beragam, paling banyak hanya kucing dan anjing."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko biasa

# shot no 8
    "(Miko dan Mika, adalah sepasang saudara kembar yang merupakan genius teknologi di Surabaya, Indonesia){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    "(Di usia ke-17, tahun ini, mereka sudah menciptakan banyak alat teknologi yang dipakai di penjuru dunia){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    "(Dengan niat mengembalikan keanekaragaman hewan di Indonesia, mereka berniat menciptakan mesin waktu){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
# shot no 9
# Kalo bisa minta tolong @putu dan @angga
# shot no 10
    scene bg lab

    show mika diam biasa at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Hey Mika, aku punya ide! Bagaimana jika kita membuat mesin waktu untuk menarik hewan dari masa lalu ke masa sekarang?"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko biasa

    show mika senang flip at right:
        xalign 0.95
    show miko diam biasa at left:
        xalign 0.05
    mika "Ide yang menarik! Tapi kamu tahu kan, time-travelling itu tidak mungkin bisa dilakukan? Kita tidak bisa kembali ke masa lalu, Mika."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika senang flip

    show mika diam senang flip at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Iya benar, kita tidak bisa kembali ke masa lalu. Tetapi kita bisa menarik yang ada di masa lalu ke masa sekarang bukan?"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam senang flip
    hide miko biasa

    show miko diam biasa at left:
        xalign 0.05
    show mika senang flip at right:
        xalign 0.95
    mika "Ah! Jika kita mengunci sesuatu di sebuah ruang dan memanipulasi waktu secara temporal..."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika senang flip

    show mika diam senang flip at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Mik..."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam senang flip
    hide miko biasa

    show miko diam biasa at left:
        xalign 0.05
    show mika senang flip at right:
        xalign 0.95
    mika "Lalu membatasi progresi metabolisme biologis objek pada ruang tersebut..."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika senang flip

    show mika diam senang flip at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Mika..."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam senang flip
    hide miko biasa

    show miko diam biasa at left:
        xalign 0.05
    show mika senang flip at right:
        xalign 0.95
    mika "Digabungkan dengan data lokasi dan waktu setiap hewan yang cukup dari database..."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika senang flip

    show mika diam senang flip at right:
        xalign 0.95
    show miko marah at left:
        xalign 0.05
    miko "Mika!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam senang flip
    hide miko marah

    show miko diam marah at left:
        xalign 0.05
    show mika senang flip at right:
        xalign 0.95
    mika "Ah! Maaf aku terlalu bersemangat dengan ide dan teori yang tiba-tiba muncul, jadi tidak sadar lingkungan, hehe."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam marah
    hide mika senang flip

    show mika diam senang flip at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Dasar kebiasaan kamu. Tapi berarti ide ini bisa dilakukan kan?"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam senang flip
    hide miko biasa

    show miko diam biasa at left:
        xalign 0.05
    show mika senang flip at right:
        xalign 0.95
    mika "Berdasarkan pemikiranku dan teknologi yang sekarang, seharusnya bisa!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika senang flip

    show mika diam senang flip at right:
        xalign 0.95
    show miko senang at left:
        xalign 0.05
    miko "Ayo buat mesin waktu?"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam senang flip
    hide miko senang

    show miko diam senang at left:
        xalign 0.05
    show mika senang flip at right:
        xalign 0.95
    mika "Ayo! Dan kita kembalikan keanekaragaman hewan!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam senang
    hide mika senang flip

# shot no 11
    "(Miko dan Mika mulai membentuk portal waktu di lab mereka){w=3}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    "(Clink! Clank!){w=3}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    "(Beberapa waktu kemudian...){w=3}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
# shot no 12
    scene bg portal

    show mika diam senang flip at right:
        xalign 0.95
    show miko senang at left:
        xalign 0.05
    miko "Portal waktu selesai!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam senang flip
    hide miko senang

    show miko diam senang at left:
        xalign 0.05
    show mika senang flip at right:
        xalign 0.95
    mika "Yeay!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam senang
    hide mika senang flip

    show mika diam senang flip at right:
        xalign 0.95
    show miko senang at left:
        xalign 0.05
    miko "Ayo segera aktifkan portalnya Mika!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam senang flip
    hide miko senang

    show miko diam senang at left:
        xalign 0.05
    show mika biasa at right:
        xalign 0.95
    mika "Sebentar, aku atur pengaturannya terlebih dahulu."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam senang
    hide mika biasa

    show mika diam biasa at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Oke! Aku suka angka 7, jadi ayo kita coba tarik 7 hewan kesini!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko biasa

    show miko diam biasa at left:
        xalign 0.05
    show mika biasa at right:
        xalign 0.95
    mika "7 hewan... data hewan... Orangutan... Harimau... Komodo... Kasuari... Anoa... Gajah... Kakatua...."
    mika "Pengaturan selesai!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika biasa

# shot no 13
    "(Portal waktu telah diaktifkan){w=2}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    "(Cahaya biru berpendar terang dari portal waktu. Miko dan Mika menyaksikan mesin yang mereka buat dengan antusias){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
# shot no 14
# ga paham VFX di renpy gimana :v
    "(Tiba-tiba, layar mesin berubah menjadi merah dan menampilkan pesan kesalahan){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    "WARNING! PORTAL UNSTABLE!{w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
# shot no 15
# ga paham VFX di renpy gimana :v
    "*shiiiing* *BAAAM*{w=2}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    "(Sinar putih yang begitu terang disertai dentuman besar mengisi lab.){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
# shot no 16
    "(Kondisi lab kembali tenang, portal waktu tidak mengeluarkan cahaya dan suara yang bising lagi){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    "(Miko dan Mika yang sempat terlempar ke lantai, berdiri lagi dan langsung mengecek mesin){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
# shot no 17

    show miko diam biasa at left:
        xalign 0.05
    show mika biasa at right:
        xalign 0.95
    mika "Oh tidak! Apa yang terjadi?"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika biasa

    show mika diam biasa at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Ugh, apakah portal waktu kita gagal berfungsi?"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko biasa

    show miko diam biasa at left:
        xalign 0.05
    show mika biasa at right:
        xalign 0.95
    mika "Berdasarkan statistik mesin, portal waktu berhasil menarik 7 hewan kok Miko..."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika biasa

    show mika diam biasa at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Umm...Mika..."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko biasa

    show miko diam biasa at left:
        xalign 0.05
    show mika biasa at right:
        xalign 0.95
    mika "Tapi kenapa tidak ada hewan yang muncul disini? Hmm...detail statistik...lokasi portal..."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika biasa

    show mika diam biasa at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Mika...mereka itu siapa?"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa

    show miko diam biasa at left:
        xalign 0.05
    mika "Hah?!"
    mika "Portalnya terpecah jadi 7 dan tersebar di lokasi yang berbeda?!"
    mika "Ada beberapa portal kecil lain juga yang terdeteksi dan entitas lain terhubung melalui portal tersebut?!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide miko biasa
    hide mika biasa

    show mika diam biasa at right:
        xalign 0.95
    show miko marah at left:
        xalign 0.05
    miko "MIKA!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko marah

    show miko biasa at left:
        xalign 0.05
    show mika biasa at right:
        xalign 0.95

    show miko diam biasa at left:
        xalign 0.05
    mika "Hah?! Kenapa Miko?"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa

    show miko biasa at left:
        xalign 0.05
    show mika diam biasa at right:
        xalign 0.95
    miko "Itu ada orang asing di dekat portal waktu!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko biasa


# shot no 18
    scene bg portal
    "(Tanpa disadari sebelumnya, ada orang asing yang tiba-tiba muncul di lab mereka){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    "(Seorang pemuda kisaran usia 20 tahun yang memiliki tampilan unik, mengenakan pakaian yang dilengkapi banyak peralatan memburu){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    "(Kelihatannya orang tersebut datang dari era yang berbeda dari Bumi tahun 7047){w=4}{nw}"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
# shot no 19
    scene bg portal


    show miko diam biasa at left:
        xalign 0.05
    show mika diam biasa at left behind miko, diam, biasa:
        xalign 0.3
    show tb merah at right:
        xalign 0.9
    tb "Ahahahaha!"
    tb "Bos memang hebat! Tidak sia-sia aku mendukung bos membentuk portal waktu!"
    tb "Hahahaha!"
    tb "Ah, sebentar ini dimana dan tahun berapa?"
    tb "Oh, Bumi 7047."
    tb "Wahahaha! Bos hebat bisa membuka portal ke 100 tahun yang lalu!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko diam biasa
    hide tb merah

    show mika diam biasa at left behind miko, marah:
        xalign 0.3
    show diam tb merah at right:
        xalign 0.9
    show miko marah at left:
        xalign 0.05
    miko "Hei siapa kamu?!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide diam tb merah
    hide miko marah

    show miko diam marah at left:
        xalign 0.05
    show mika diam biasa at left behind miko, diam, marah:
        xalign 0.3
    show tb merah at right:
        xalign 0.9
    tb "Ah, ada orang disini ternyata. Halo penduduk bumi tahun 7047!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko diam marah
    hide tb merah

    show miko diam marah at left:
        xalign 0.05
    show diam tb merah at right:
        xalign 0.95
    show mika marah at left:
        xalign 0.3
    mika "Ya! Siapa kamu dan kenapa ada disini?!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam marah
    hide diam tb merah
    hide mika marah

    show mika diam marah at left:
        xalign 0.3
    show miko diam marah at left:
        xalign 0.05
    show tb merah at right:
        xalign 0.9
    tb "Hei tenang anak muda. Kami disini tidak akan mengganggu kalian. Target kami hanyalah memburu dan menangkap hewan."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam marah
    hide miko diam marah
    hide tb merah

    show mika diam marah at left:
        xalign 0.3
    show diam tb merah at right:
        xalign 0.9
    show miko biasa at left:
        xalign 0.05
    miko "Kami?"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam marah
    hide diam tb merah
    hide miko biasa

    show mika diam marah at left:
        xalign 0.3
    show miko diam biasa at left:
        xalign 0.05
    show tb merah at right:
        xalign 0.9
    tb "Iya, kami adalah Time Bandit yang setia mengikuti bos besar. Bos ingin memburu hewan dari masa lalu, kami siap beraksi!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam marah
    hide miko diam biasa
    hide tb merah

    show miko diam biasa at left:
        xalign 0.05
    show diam tb merah at right:
        xalign 0.9
    show mika biasa at left:
        xalign 0.3
    mika "Tapi, kamu kan sendirian..."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide diam tb merah
    hide mika biasa

    show mika diam biasa at left:
        xalign 0.3
    show miko diam biasa at left:
        xalign 0.05
    show tb merah at right:
        xalign 0.9
    tb "Sendiri?"
    tb "Eh?"
    tb "Hei! Kenapa aku sendirian?! Dimana bos?! Dimana Time Bandit yang lain?!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam
    hide miko diam
    hide tb merah

# shot no 20
    scene bg portal

    show miko diam biasa at left:
        xalign 0.05
    show mika biasa at right:
        xalign 0.95
    mika "Miko, setelah aku analisis menggunakan kacamataku, alat yang digunakan di tangan orang itu adalah alat seperti mesin waktu yang kita buat, tapi lebih canggih."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika biasa

    show mika diam biasa at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Oh ya? Berarti dia benar dari masa depan? Perjalanan waktu benar bisa dilakukan?"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko biasa

    show miko diam biasa at left:
        xalign 0.05
    show mika biasa at right:
        xalign 0.95
    mika "Nampaknya begitu. Jika dia bisa pergi ke masa sekarang, maka dia bisa juga dikembalikan ke masa asalnya menggunakan alat yang sama."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika biasa

    show mika diam biasa at right:
        xalign 0.95
    show miko biasa at left:
        xalign 0.05
    miko "Oke, kalau begitu ayo kita kembalikan dia ke masa depan!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide miko biasa

    show miko diam biasa at left:
        xalign 0.05
    show mika senang flip at right:
        xalign 0.95
    mika "Miko, kita bisa menggunakan alat invensi kita sebelumnya, Elemental Gauntlet, untuk mengalahkan dia."
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide miko diam biasa
    hide mika senang flip

    show mika diam senang flip at right:
        xalign 0.95
    show miko senang at left:
        xalign 0.05
    miko "Ide yang bagus Mika!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam senang flip
    hide miko senang

# shot no 21
    scene bg portal

    show mika diam biasa at left behind miko, marah:
        xalign 0.3
    show diam tb merah at right:
        xalign 0.9
    show miko marah at right:
        xalign 0.05
    miko "Hei! Kami tidak tahu kamu siapa dan darimana, tapi kami tau kamu bukan orang yang baik!"
    miko "Tidak akan kami biarkan kamu memburu dan menangkap hewan di bumi ini!"
    with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    hide mika diam biasa
    hide diam tb merah
    hide miko marah

    call battle #pindah ke battle screen

    hide tb merah with dissolve
    hide mika with dissolve
    hide miko with dissolve
    scene bg portal with fade()


    "Tamat."

    return
