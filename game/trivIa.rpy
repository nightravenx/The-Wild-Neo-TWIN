# Trivia Bank

define question = 1
define trivListEl = ["ipa", "ips", "math", "bi"]
define trivListPhys = ["ppkn", "pjok", "sbdp"]
define Triv = ""
# define fireTriv = trivListEl[0]
# define windTriv = trivListEl[1]
# define earthTriv = trivListEl[2]
# define waterTriv = trivListEl[3]
# define physTriv = trivListPhys[0]
define realQuestion = ""
define typeQuestion = ""
define foundQuestion = False
define ind = -1 #index
define indPhys = 0

define color0 = ""
define color1 = ""
define color2 = ""
define color3 = ""

label randomtriv:
    $renpy.random.shuffle(trivListEl)
    $renpy.random.shuffle(trivListPhys)
    $renpy.random.shuffle(allTriv)
    return

label initTriv:
    
    while foundQuestion == False:
        $Triv = allTriv[ind]
        $typeQuestion = Triv["type"]
        $ind += 1
        if atk == "Fire" and trivListEl[0] == typeQuestion:
            $foundQuestion = True
        elif atk == "Wind" and trivListEl[1] == typeQuestion:
            $foundQuestion = True
        elif atk == "Earth" and trivListEl[2] == typeQuestion:
            $foundQuestion = True
        elif atk == "Water" and trivListEl[3] == typeQuestion:
            $foundQuestion = True
        elif atk == "Physical" and trivListPhys[indPhys] == typeQuestion:
            $foundQuestion = True
            $indPhys += 1
            if indPhys == 3:
                $indPhys = 0
        if ind >= 117:
            $ind = -1

    $foundQuestion = False
    jump trivia

label initTrivDef:
    
    while foundQuestion == False:
        $Triv = allTriv[ind]
        $typeQuestion = Triv["type"]
        $ind += 1
        if defe == "Fire" and trivListEl[0] == typeQuestion:
            $foundQuestion = True
        elif defe == "Wind" and trivListEl[1] == typeQuestion:
            $foundQuestion = True
        elif defe == "Earth" and trivListEl[2] == typeQuestion:
            $foundQuestion = True
        elif defe == "Water" and trivListEl[3] == typeQuestion:
            $foundQuestion = True
        if ind >= 117:
            $ind = -1

    $foundQuestion = False
    jump trivia

label trivia:
    $ quizquestion = Triv
    $ asks = quizquestion["question"]
    $ answers = quizquestion["answer"]
    $ corrects = quizquestion["correct"]
    $ renpy.random.shuffle(answers) #reshuffle answers
    $ answers1 = answers[0]
    $ answers2 = answers[1]
    $ answers3 = answers[2]
    $ answers4 = answers[3]
    $ answercheck = ""

    if answers1 == corrects:
        $color0 = "#00FF00"
        $color1 = "#FF0000"
        $color2 = "#FF0000"
        $color3 = "#FF0000"
    elif answers2 == corrects:
        $color0 = "#FF0000"
        $color1 = "#00FF00"
        $color2 = "#FF0000"
        $color3 = "#FF0000"
    elif answers3 == corrects:
        $color0 = "#FF0000"
        $color1 = "#FF0000"
        $color2 = "#00FF00"
        $color3 = "#FF0000"
    elif answers4 == corrects:
        $color0 = "#FF0000"
        $color1 = "#FF0000"
        $color2 = "#FF0000"
        $color3 = "#00FF00"

    jump trivia1




init:
    $ timer_range = 0
    $ timer_jump = 0
    

    $allTriv = [
        # 1-10 IPA
        {"question" : "Proses yang disertai dengan pertambahan berat, besar, dan tinggi pada makhluk hidup disebut ...", 
        "answer" : ["Pertambahan", "Penggemukan", "Pertumbuhan", "Berkembang biak"], 
        "correct" : "Pertumbuhan",
        "type" : "ipa"},

        {"question" : "Alat perkembangbiakan generatif pada tumbuhan berupa ...", 
        "answer" : ["Bunga", "Batang", "Daun", "Akar"], 
        "correct" : "Bunga",
        "type" : "ipa"},
        
        {"question" : "Hewan yang bekembangbiakan dengan cara bertelur adalah", 
        "answer" : ["Angsa, itik, dan bebek", "Bebek, angsa, dan kelinci", "Ayam, hiu, dan cecak", "Kera, bebek, dan ayam"], 
        "correct" : "Angsa, itik, dan bebek",
        "type" : "ipa"},
        
        {"question" : "Burung elang berkembang biak dengan cara bertelur. Berarti, burung elang mengalami perkembangbiakan secara ...", 
        "answer" : ["Vegetatif", "Membelah diri", "Spora", "Generatif"], 
        "correct" : "Generatif",
        "type" : "ipa"},

        {"question" : "Perkembangbiakan secara bertelur dan beranak disebut juga dengan perkembangbiakan ...", 
        "answer" : ["Spora", "Ovipar", "Vivipar", "Ovovivipar"], 
        "correct" : "Ovovivipar",
        "type" : "ipa"},

        {"question" : "Hewan yang berkembang biak secara ovipar adalah ...", 
        "answer" : ["Kadal, hiu, dan ular", "Ayam, hiu, dan lumba-lumba", "Ayam, bebek, dan angsa", "Kambing, sapi, dan kelinci"], 
        "correct" : "Ayam, bebek, dan angsa",
        "type" : "ipa"},

        {"question" : "Sel kelamin betina yang terdapat pada bunga disebut ...", 
        "answer" : ["Kelopak", "Benang sari", "Mahkota", "Putik"], 
        "correct" : "Putik",
        "type" : "ipa"},

        {"question" : "Bambu berkembang biak dengan ...", 
        "answer" : ["Spora", "Rhizoma", "Tunas", "Tunas adventif"], 
        "correct" : "Tunas",
        "type" : "ipa"},

        {"question" : "Salah satu tumbuhan yang berkembang biak dengan umbi lapis yaitu ...", 
        "answer" : ["Rumput teki", "Sukun", "Bawang Merah", "Ubi jalar"], 
        "correct" : "Bawang Merah",
        "type" : "ipa"},

        # 10 - 20
        {"question" : "Serbuk sari yang jatuh ke kepala putik yang berasal dari bunga itu sendiri disebut penyerbukan ...", 
        "answer" : ["Silang", "Sendiri", "Tetangga", "Bastar"], 
        "correct" : "Sendiri",
        "type" : "ipa"},

        {"question" : "Perkembangbiakan generatif pada tumbuhan hanya bisa terjadi pada tumbuhan yang memiliki ...", 
        "answer" : ["Akar", "Bunga", "Daun", "Batang"], 
        "correct" : "Bunga",
        "type" : "ipa"},

        {"question" : "Berikut ini merupakan perkembangbiakan vegetatif alami adalah ...", 
        "answer" : ["Mencangkok", "Stek", "Umbi Batang", "Okulasi"], 
        "correct" : "Umbi Batang",
        "type" : "ipa"},

        {"question" : "Berikut adalah bagian-bagian yang terdapat pada bunga, kecuali ...", 
        "answer" : ["Putik", "Mahkota bunga", "Kepala sari", "Kelopak bunga"], 
        "correct" : "Kepala sari",
        "type" : "ipa"},

        {"question" : "Alat kelamin jantan pada bunga adalah ...", 
        "answer" : ["Benang sari", "Putik", "Mahkota bunga", "Benang mahkota"], 
        "correct" : "Benang sari",
        "type" : "ipa"},

        {"question" : "Penyerbukan yang terjadi jika serbuk sari yang jatuh di atas kepala putik berasal dari tanaman yang berbeda tetapi masih satu jenis dinamakan penyebukan ...", 
        "answer" : ["Sendiri", "Tetangga", "Silang", "Bartas"], 
        "correct" : "Silang",
        "type" : "ipa"},

        {"question" : "Perkembangan vegetatif terdiri menjadi dua macam, yaitu ...", 
        "answer" : ["Buatan dan fisika", "Alami dan buatan", "Biologi dan kimia ", "Alami dan biologi"], 
        "correct" : "Alami dan buatan",
        "type" : "ipa"},

        {"question" : "Hewan berikut ini yang dapat membantu penyerbukan pada tumbuhan adalah ...", 
        "answer" : ["Jangkrik", "Lebah", "Gajah", "Ayam"], 
        "correct" : "Lebah",
        "type" : "ipa"},

        {"question" : "Ovarium pada tubuh wanita melepaskan sel telur dengan jangka waktu ...", 
        "answer" : ["Setahun sekali", "Sebulan sekali", "Seminggu sekali", "Sehari sekali"], 
        "correct" : "Sebulan sekali",
        "type" : "ipa"},

        {"question" : "Batang yang akan dicangkok dipilih cabang yang ...", 
        "answer" : ["Besar", "Bengkok", "Kecil", "Lurus"], 
        "correct" : "Lurus",
        "type" : "ipa"},

        #20-30
        {"question" : "Perkembangbiakan tumbuhan dengan cara menimbun bagian cabang yang tumbuh memanjang dalam permukaan tanah dinamakan ...", 
        "answer" : ["Merunduk", "Okulasi", "Mengenten", "Stek"], 
        "correct" : "Merunduk",
        "type" : "ipa"},

        {"question" : "Perkembangbiakan vegatatif buatan yang dilakukan dengan menanam bagian tertentu dari tumbuhan tanpa menunggu tumbuhnya akar disebut ...", 
        "answer" : ["Geragih", "Stek", "Mencangkok", "Okulasi"], 
        "correct" : "Stek",
        "type" : "ipa"},

        {"question" : "Berikut adalah tumbuhan yang berkembang biak secara tunas ...", 
        "answer" : ["Pisang dan mangga", "Bambu dan mahoni", "Pisang dan padi", "Pisang dan bambu"], 
        "correct" : "Pisang dan bambu",
        "type" : "ipa"},

        {"question" : "Jamur, tumbuhan paku dan lumut adalah contoh tumbuhan yang tidak berbiji. Tumbuhan tersebut berkembang biak dengan cara ...", 
        "answer" : ["Spora", "Stek", "Okulasi", "Membelah diri"], 
        "correct" : "Spora",
        "type" : "ipa"},

        {"question" : "Contoh tumbuhan yang berkembang biak dengan cara umbi lapis adalah ...", 
        "answer" : ["Bawang merah, kentang, dan bawang putih", "Jambu, mangga, dan rambutan", "Tebu, bambu, dan pisang", "Bawang merah, bawang putih, dan bawang bombai"], 
        "correct" : "Bawang merah, bawang putih, dan bawang bombai",
        "type" : "ipa"},

        {"question" : "Di bawah ini yang merupakan ciri bunga yang penyerbukannya dibantu oleh hewan adalah ...", 
        "answer" : ["Kepala putik agak tersembunyi", "Mahkota tidak berwarna mencolok", "Serbuk sari kering", "Mahkota bunga kecil"], 
        "correct" : "Kepala putik agak tersembunyi",
        "type" : "ipa"},

        {"question" : "Setelah penyerbukan maka akan terjadi proses pembuahan (fertilisasi) yang terjadi di ...", 
        "answer" : ["Mahkota bunga", "Bakal biji", "Dasar bunga", "Kelopak"], 
        "correct" : "Dasar bunga",
        "type" : "ipa"},
        
        {"question" : "Pelestarian makhluk hidup bertujuan untuk menjaga agar makhluk hidup tidak ...", 
        "answer" : ["Punah", "Beranak", "Bertambah", "Berkembang Biak"], 
        "correct" : "Punah",
        "type" : "ipa"},
        
        {"question" : "Indonesia merupakan negara yang baik untuk pertumbuhan tumbuhan dan hewan karena memiliki iklim ...", 
        "answer" : ["Hujan", "Tropis", "Subtropis", "Panas"], 
        "correct" : "Tropis",
        "type" : "ipa"},
        
        {"question" : "Berikut pernyataan yang bukan merupakan pelestarian makhluk hidup adalah ...", 
        "answer" : ["Pembuatan cagar alam dan suaka margasatwa", "Perburuan dan penebangan liar", "Pengembangbiakan hewan dan tumbuhan", "Perlindungan hewan dan tumbuhan dari kepunahan"], 
        "correct" : "Perburuan dan penebangan liar",
        "type" : "ipa"},

##############################################################################################################################################

        # 1-10 IPS
        {"question" : "Negara di Asia Tenggara yang tidak mempunyai laut adalah ...", 
        "answer" : ["Laos", "Kamboja", "Thailand", "Vietnam"], 
        "correct" : "Laos",
        "type" : "ips"},

        {"question" : "Kuala Lumpur adalah ibu kota negara ...", 
        "answer" : ["Laos", "Kamboja", "Singapura", "Malaysia"], 
        "correct" : "Malaysia",
        "type" : "ips"},
        
        {"question" : "Di Asia Tenggara yang termasuk negara kepulauan adalah ...", 
        "answer" : ["Filipina dan Malaysia", "Indonesia dan Filipina", "Filipina dan Thailand", "Indonesia dan Thailand"], 
        "correct" : "Indonesia dan Filipina",
        "type" : "ips"},
        
        {"question" : "Wilayah yang berbatasan langsung dengan Indonesia adalah ...", 
        "answer" : ["Singapura dan Malaysia", "Malaysia dan Brunai Darussalam", "Papua Nugini dan Malaysia", "Filipina dan Malaysia"], 
        "correct" : "Papua Nugini dan Malaysia",
        "type" : "ips"},
        
        {"question" : "Gunung Fan Si Pan terletak di Negara ...", 
        "answer" : ["Vietnam", "Laos", "Kamboja", "India"], 
        "correct" : "Vietnam",
        "type" : "ips"},
        
        {"question" : "Provinsi Timor Timur berdiri sebagai negara baru pada tahun ...", 
        "answer" : ["1979", "1989", "2002", "2000"], 
        "correct" : "2002",
        "type" : "ips"},
        
        {"question" : "Pada masa awal kemerdekaan Kepulauan Nusa Tenggara disebut Provinsi ...", 
        "answer" : ["Sunda Kecil", "Sunda Besar", "Nusa Tenggara Barat", "Nusa Tenggara Timur"], 
        "correct" : "Sunda Kecil",
        "type" : "ips"},
        
        {"question" : "Provinsi Bangka Belitung merupakan pemekaran provinsi ...", 
        "answer" : ["Lampung", "Sumatera Selatan", "Bengkulu", "Riau"], 
        "correct" : "Sumatera Selatan",
        "type" : "ips"},
        
        {"question" : "Tanjung Pinang ibu kota Provinsi ...", 
        "answer" : ["Riau", "Kepulauan Riau", "Bangka Belitung", "Jambi"], 
        "correct" : "Kepulauan Riau",
        "type" : "ips"},
        
        {"question" : "Letak Indonesia secara geografis sangat strategis karena berada di persilangan dua benua yaitu Benua ...", 
        "answer" : ["Asia dan Afrika", "Australia dan Amerika", "Asia dan Eropa", "Asia dan Australia"], 
        "correct" : "Asia dan Australia",
        "type" : "ips"},
        
        #10-20
        {"question" : "Indonesia terletak diantara dua benua dan dua samudra sehingga mendapat sebutan ...", 
        "answer" : ["Nusantara", "Maritim", "Agraris", "Zamrud Khatulistiwa"], 
        "correct" : "Maritim",
        "type" : "ips"},
        
        {"question" : "Untuk mengatur jalannya pemerintahan wilayah NKRI dibagi atas beberapa ...", 
        "answer" : ["pulau", "provinsi", "wilayah", "daerah"], 
        "correct" : "provinsi",
        "type" : "ips"},
        
        {"question" : "Contoh sikap waspada terhadap masalah sosial di Indonesia adalah ...", 
        "answer" : ["menjaga keharmonisan", "bersikap menyendiri", "tidak bermasyarakat", "bergaul seenaknya"], 
        "correct" : "menjaga keharmonisan",
        "type" : "ips"},
        
        {"question" : "Secara astronomis wilayah Indonesia terletak antara ... (dalam derajat)", 
        "answer" : ["6 LU – 11 LS dan 95 BT – 141 BT", "6 LU – 11 LU dan 95 BT – 141 BT", "6 LU – 11 LU dan 95 BB – 141 BT", "6 LU – 11 LS dan 95 BB – 141 BT"], 
        "correct" : "6 LU – 11 LS dan 95 BT – 141 BT",
        "type" : "ips"},
        
        {"question" : "Negara di Asia Tenggara yang merupakan tujuan wisata yang paling populer adalah ...", 
        "answer" : ["Filipina", "Indonesia", "Singapura", "Laos"], 
        "correct" : "Singapura",
        "type" : "ips"},
        
        {"question" : "Negara ini mendapat sebutan “Macan Asia” kecuali ...", 
        "answer" : ["Jepang", "Korea Selatan", "Singapura", "Malaysia"], 
        "correct" : "Malaysia",
        "type" : "ips"},
        
        {"question" : "Gunung Fuji dianggap kramat oleh penduduk ...", 
        "answer" : ["Jepang", "India", "China", "Mesir"], 
        "correct" : "Jepang",
        "type" : "ips"},
        
        {"question" : "Penduduk asli Australia adalah ...", 
        "answer" : ["Aborijin", "Negro", "Eskimo", "Indian"], 
        "correct" : "Aborijin",
        "type" : "ips"},
        
        {"question" : "Antara Benua Asia dan Benua Afrika dibatasi oleh ...", 
        "answer" : ["Laut Kaspia", "Pegunungan Ural", "Laut Hitam", "Laut Merah"], 
        "correct" : "Laut Merah",
        "type" : "ips"},
        
        #20-29
        {"question" : "Negara berikut yang sangat sering dilanda angin topan adalah ...", 
        "answer" : ["Australia", "Singapura", "Malaysia", "Brunai Darussalam"], 
        "correct" : "Australia",
        "type" : "ips"},
        
        {"question" : "Salah satu usaha untuk mencegah terjadinya banjir adalah ...", 
        "answer" : ["Rehabilitasi", "Irigasi", "Reboisasi", "Urbanisasi"], 
        "correct" : "Reboisasi",
        "type" : "ips"},
        
        {"question" : "Keadaan cuaca di Indonesia selalu di pantau oleh badan yang disebut ...", 
        "answer" : ["KPK", "Bakornas", "LSM", "BMKG"], 
        "correct" : "BMKG",
        "type" : "ips"},

        {"question" : "Arti dari globalisasi adalah ....", 
        "answer" : ["Adanya ketergantungan satu negara dengan negara lain", "Proses hilangnya identitas suatu bangsa", "Proses mendunia dalam segala aspek kehidupan", "Proses hancurnya budaya lokal oleh budaya dunia"], 
        "correct" : "Proses mendunia dalam segala aspek kehidupan",
        "type" : "ips"},
        
        {"question" : "Gejala alam yang sering terjadi di Filipina adalah ...", 
        "answer" : ["Gunung meletus dan badai tropis", "Badai salju dan longsor", "Banjir dan erosi", "Gempa bumi dan Tsunami"], 
        "correct" : "Gunung meletus dan badai tropis",
        "type" : "ips"},
        
        {"question" : "Bila ada tanda-tanda akan terjadinya Tsunami, yang segera kita lakukan adalah ...", 
        "answer" : ["Mendekati pantai untuk mengukur besarnya gelombang", "Pergi menjauhi pantai dan mencari tempat yang tinggi", "Tinggal di dalam rumah", "Sembunyi di bawah tempat tidur"], 
        "correct" : "Pergi menjauhi pantai dan mencari tempat yang tinggi",
        "type" : "ips"},
        
        {"question" : "Membuang sampah di sungai dapat menyebabkan bencana ...", 
        "answer" : ["Banjir", "Gempa", "Longsor", "Kebakaran"], 
        "correct" : "Banjir",
        "type" : "ips"},
        
        {"question" : "Apabila terjadi gempa dan berada di dalam rumah, hal yang harus dilakukan adalah ...", 
        "answer" : ["Berlindung di bawah meja", "Lari ke kamar", "Menyelamatkan harta benda", "Lari ke luar"], 
        "correct" : "Berlindung di bawah meja",
        "type" : "ips"},
        
        {"question" : "Secara geografis Indonesia terletak di antara dua benua yaitu ...", 
        "answer" : ["Asia dan Eropa", "Eropa dan Afrika", "Asia dan Afrika", "Asia dan Australia"], 
        "correct" : "Asia dan Australia",
        "type" : "ips"},
        
        {"question" : "Alat untuk mencatat gempa bumi disebut ...", 
        "answer" : ["Seismometer", "Anemometer", "Seismologi", "Termometer"], 
        "correct" : "Seismometer",
        "type" : "ips"},

################################################################################################################################################

        # 1-10 BI
        {"question" : "Pengertian dari percakapan adalah ...", 
        "answer" : ["Kegiatan berkomunikasi secara tulisan", "Kegiatan berkomunikasi secara lisan antara dua orang atau lebih", "Kegiatan berkomunikasi melalui surat", "Kegiatan berkomunikasi melalui bacaan"], 
        "correct" : "Kegiatan berkomunikasi secara lisan antara dua orang atau lebih",
        "type" : "bi"},

        {"question" : "Kalimat berikut ini yang menyatakan tanggapan adalah ...", 
        "answer" : ["Ibu membawa keranjang dari plastik saat berbelanja di pasar.", "Sebaiknya kualitas pendidikan di Indonesia mulai ditingkatkan sejak saat ini.", "Jangan bermain terlalu jauh.", "Untuk saat ini, aku hanya ingin beristirahat"], 
        "correct" : "Sebaiknya kualitas pendidikan di Indonesia mulai ditingkatkan sejak saat ini.",
        "type" : "bi"},

        {"question" : "Berikut ini yang tidak perlu ditulis dalam laporan hasil pengamatan adalah ...", 
        "answer" : ["lokasi", "waktu", "objek", "perlengkapan"], 
        "correct" : "perlengkapan",
        "type" : "bi"},

        {"question" : "Kalimat berikut yang menjelaskan hasil pengamatan adalah ...", 
        "answer" : ["Setelah disiram, biarkanlah bunga-bunga itu melakukan proses fotosintesis", "Rumah-rumah di RT 02 tampak berjejer rapi dan menghadap ke sebelah timur.", "Mereka mengharapkan datangnya bantuan.", "Aku melewati jalan setapak ini pada waktu malam"], 
        "correct" : "Rumah-rumah di RT 02 tampak berjejer rapi dan menghadap ke sebelah timur.",
        "type" : "bi"},

        {"question" : "Isi percakapan pada kegiatan menyampaikan informasi adalah ...", 
        "answer" : ["tulisan", "cerita", "pertanyaan dan jawaban", "pepatah dan peribahasa"], 
        "correct" : "pertanyaan dan jawaban",
        "type" : "bi"},

        {"question" : "Hal-hal yang tidak boleh dilakukan ketika menyampaikan pesan kepada orang lain adalah ...", 
        "answer" : ["menyampaikan pesan apa adanya", "melebih-lebihkan pesan", "diulangi jika penerima pesan jika belum jelas", "disampaikan dengan kalimat yang jelas"], 
        "correct" : "melebih-lebihkan pesan",
        "type" : "bi"},

        {"question" : "Kalimat di bawah ini yang menyatakan laporan adalah ...", 
        "answer" : ["Dimana kalian berdarmawisata?", "Mengapa mereka ikut mendaki gunung?", "Lia dan Lala ingin pergi ke Bali", "Air terjun itu ada di lereng Gunung Lawu"], 
        "correct" : "Air terjun itu ada di lereng Gunung Lawu",
        "type" : "bi"},

        {"question" : "Langkah berikut ini yang tidak digunakan dalam menemukan informasi bacaan adalah ...", 
        "answer" : ["membaca bacaan dengan sungguh-sungguh", "menyimpulkan isi bacaan atau mengambil garis besar isi bacaan", "membaca bacaan cepat mungkin", "memahami isi bacaan"], 
        "correct" : "membaca bacaan cepat mungkin",
        "type" : "bi"},

        {"question" : "Di bawah ini yang termasuk pujian adalah ...", 
        "answer" : ["Baju kamu sangat bau!", "Wah, nakal betul anak itu.", "Wah, bagus benar tulisanmu seperti ceker ayam.", "Kamu cantik sekali hari ini."], 
        "correct" : "Kamu cantik sekali hari ini.",
        "type" : "bi"},

        {"question" : "Ada seorang temanmu yang memakai sepatu baru, tetapi warnanya tidak sesuai dengan aturan di sekolah. Tanggapan yang tepat untuk kondisi tersebut adalah ...", 
        "answer" : ["Wah, sepatumu bagus sekali. Pasti mahal, ya!", "Sepatumu bagus, pasti mahal ya!", "Sebaiknya kamu memakai sepatu yang warnanya sesuai aturan sekolah.", "Jangan memakai sepatu yang warnanya tidak sesuai aturan sekolah, dong!"], 
        "correct" : "Sebaiknya kamu memakai sepatu yang warnanya sesuai aturan sekolah.",
        "type" : "bi"},

        #10-18
        {"question" : "Berdasarkan hasil kunjungan kami di lokasi, ternyata kegagalan panen para petani tahun ini disebabkan oleh serangan hama tikus dan wereng. Pernyataan tersebut tepat untuk ...", 
        "answer" : ["laporan hasil pengamatan", "resensi buku", "laporan hasil kunjungan", "ringkasan"], 
        "correct" : "laporan hasil kunjungan",
        "type" : "bi"},

        {"question" : "Bacalah penggalan kalimat berikut! Akhir-akhir ini hama wereng banyak melanda daerah Pacitan dan sekitarnya, sehingga membuat petani gagal panen. Penggalan kalimat tersebut bertema ...", 
        "answer" : ["pertanian", "pendidikan", "peternakan", "kesehatan"], 
        "correct" : "pertanian",
        "type" : "bi"},

        {"question" : "Dalam sebuah cerpen yang dimaksud dengan tokoh utama ialah ...", 
        "answer" : ["tokoh yang jarang muncul", "tokoh yang kadang muncul", "tokoh yang sering muncul", "tokoh yang tidak pernah muncul"], 
        "correct" : "tokoh yang sering muncul",
        "type" : "bi"},

        {"question" : "Manfaat meringkas teks adalah ...", 
        "answer" : ["agar teks menjadi pendek", "agar mudah dipahami", "untuk mudah mengingat kembali isi teks", "agar teks semakin bermanfaat"], 
        "correct" : "untuk mudah mengingat kembali isi teks",
        "type" : "bi"},

        {"question" : "Berkut ini kalimat yang menunjukkan latar tempat adalah ...", 
        "answer" : ["Ayah menyiram tanaman.", "Adik bermain boneka.", "Budi mandi dua kali sehari.", "Hari ini, di Jakarta terjadi banjir"], 
        "correct" : "Hari ini, di Jakarta terjadi banjir",
        "type" : "bi"},

        {"question" : "Temanmu suka menyontek pekerjaan teman yang lain. Kritikan yang tepat untuk situasi tersebut adalah ...", 
        "answer" : ["Wah, ternyata kamu itu suka menyontek.", "Kamu itu seharusnya belajar yang rajin. Jangan suka menyontek !", "Pantas saja nilaimu bagus. Ternyata hasil menyontek.", "Daripada menyontek, lebih baik kamu belajar yang rajin"], 
        "correct" : "Daripada menyontek, lebih baik kamu belajar yang rajin",
        "type" : "bi"},

        {"question" : "Kalimat iklan yang tepat untuk menawarkan kamera adalah ...", 
        "answer" : ["Kamera berkualitas dengan harga pantas.", "Belilah kamera ini, dijamin Anda puas.", "Kamera zaman sekarang segera miliki!", "Kamera murah dan awet."], 
        "correct" : "Kamera berkualitas dengan harga pantas.",
        "type" : "bi"},

        {"question" : "Dalam mengisi daftar riwayat hidup setelah kata \"nama\" harus dilkuti dengan tanda ...", 
        "answer" : ["koma", "titik", "titik dua", "sama dengan"], 
        "correct" : "titik dua",
        "type" : "bi"},

################################################################################################################################################

        # 1-10 Math
        {"question" : "16/32 =", 
        "answer" : ["0.5", "0.2", "0.75", "0.8"], 
        "correct" : "0.5",
        "type" : "math"},

        {"question" : "3 3/4 + 2.5 - 3 1/2 =", 
        "answer" : ["2 3/4", "2 1/4", "1 3/4", "1 1/4"], 
        "correct" : "2 3/4",
        "type" : "math"},

        {"question" : "0.65 : 3/5 x 30% =", 
        "answer" : ["9/20", "3/10", "1/2", "3/12"], 
        "correct" : "9/20",
        "type" : "math"},

        {"question" : "Urutan pecahan 2,326; 2 5/8 ; 243%; 11/8 dari yang terbesar adalah ...", 
        "answer" : ["243% ; 2,326 ; 11/8 ; 2 5/8", "11/8; 2,326 ; 243% ; 2 5/8", "2 5/8; 2,326 ; 243% ; 11/8", "2 5/8; 243% ; 2,326 ; 11/8"], 
        "correct" : "243% ; 2,326 ; 11/8 ; 2 5/8",
        "type" : "math"},

        {"question" : "90 + 56 x 2 + 10 =", 
        "answer" : ["212", "192", "302", "302.5"], 
        "correct" : "212",
        "type" : "math"},

        {"question" : "48% =", 
        "answer" : ["12/25", "24/25", "48/50", "18/25"], 
        "correct" : "12/25",
        "type" : "math"},

        {"question" : "Volume tabung yang memiliki jari-jari 7 cm dan tinggi 20 cm adalah ...", 
        "answer" : ["3,080", "2,980", "3,280", "2,280"], 
        "correct" : "3,080",
        "type" : "math"},

        {"question" : "Luas lingkaran yang memiliki diameter 6 1/4 cm adalah ... (pembulatan ke atas)", 
        "answer" : ["35.77", "35.76", "35.67", "35.56"], 
        "correct" : "35.77",
        "type" : "math"},

        {"question" : "Luas segitiga yang memiliki tinggi 3 cm dan alas 2 1/2 cm adalah", 
        "answer" : ["3.75", "3.5", "3.25", "4"], 
        "correct" : "3.75",
        "type" : "math"},

        {"question" : "Hasil dari (-20) x (-2) : 10 x (-3) =", 
        "answer" : ["-12", "12", "-16", "16"], 
        "correct" : "-12",
        "type" : "math"},

        {"question" : "Hasil dari (10 x (-2) : 20 + 1) x (-3) =", 
        "answer" : ["0", "3", "-1", "-3"], 
        "correct" : "0",
        "type" : "math"},

        {"question" : "Luas lingkaran yang memiliki jari-jari 7 cm adalah ... (pembulatan ke atas)", 
        "answer" : ["154", "144", "164", "134"], 
        "correct" : "154",
        "type" : "math"},

        {"question" : "75% dari 120 =", 
        "answer" : ["90", "80", "100", "75"], 
        "correct" : "90",
        "type" : "math"},

        {"question" : "80% =", 
        "answer" : ["0.5", "0.8", "0.16", "8"], 
        "correct" : "0.8",
        "type" : "math"},

        {"question" : "125 + 65 + 30 - 120 =", 
        "answer" : ["100", "95", "90", "105"], 
        "correct" : "100",
        "type" : "math"},
############################################################################################################################################

        #1-10 PPKn
        {"question" : "Formulasi Pancasila yang resmi tercanntum dalam pembukaan UUD 1945, yaitu di alinea ...", 
        "answer" : ["Pertama", "Kedua", "Ketiga", "Keempat"], 
        "correct" : "Keempat",
        "type" : "ppkn"},

        {"question" : "Nilai pertempuran yang menonjol dalam menyatukan ketidaksepakatan dalam proses BPUPKI dan PPKI adalah nilai ...", 
        "answer" : ["keilahian", "Siap berkorban", "Kebersamaan", "Ketulusan"], 
        "correct" : "Siap berkorban",
        "type" : "ppkn"},

        {"question" : "Contoh sikap yang sesuai dengan sila kemanusiaan yang adil dan beradab adalah ...", 
        "answer" : ["beribadah tepat waktu", "memberi bantuan kepada korban bencana alam.", "selalu mengambil keputusan dengan musyawarah.", "memeluk agama sesuai kayakinan tanpa paksaan."], 
        "correct" : "memberi bantuan kepada korban bencana alam.",
        "type" : "ppkn"},

        {"question" : "Upacara tindik telinga upacara pemasangan anting-anting dilakukan oleh suku ...", 
        "answer" : ["Bali", "Sanda", "Dayak", "Tengger"], 
        "correct" : "Dayak",
        "type" : "ppkn"},

        {"question" : "Contoh wujud cinta tanah air di lingkungan sekolah adalah ...", 
        "answer" : ["belajar tekun saat menghadapi ujian", "menggunakan seragam sekolah dengan rapi", "mengikuti kegiatan ektra kurikuler dengan tertib", "mengikuti upacara bendera di sekolah dengan tertib"], 
        "correct" : "mengikuti upacara bendera di sekolah dengan tertib",
        "type" : "ppkn"},

        {"question" : "Manfaat menjaga persatuan di sekolah adalah ...", 
        "answer" : ["terjadi perselisihan", "membuat hidup tidak tenang", "menumbuhkan sikap acuh tak acuh", "menghindari perselisihan dan permusuhan"], 
        "correct" : "menghindari perselisihan dan permusuhan",
        "type" : "ppkn"},

        {"question" : "Contoh pelaksanaan sila Pancasila dengan lambang \"Kepala Banteng\" adalah ...", 
        "answer" : ["tidak bergaya hidup mewah", "menghargai hasil karya orang lain", "selalu menjaga kerukunan dengan teman", "tidak memaksakan kehendak kepada orang lain"], 
        "correct" : "tidak memaksakan kehendak kepada orang lain",
        "type" : "ppkn"},

        {"question" : "Beni mengendarai sepeda ketika berangkat dan pulang sekolah. Saat jalan macet Beni mengendarai sepedanya di trotoar. Perilaku Anton sudah melanggar hak orang lain yaitu ...", 
        "answer" : ["mengganggu lalu lintas", "mengganggu pejalan kaki", "mengganggu semua pengguna jalan", "mengganggu pengendara sepeda yang lain"], 
        "correct" : "mengganggu pejalan kaki",
        "type" : "ppkn"},

        {"question" : "Sesuatu yang harus kita lakukan dengan penuh tanggung jawab sebelum mendapatkan hak kita disebut ...", 
        "answer" : ["Kewajiban", "Hak", "Perintah", "Anjuran"], 
        "correct" : "Kewajiban",
        "type" : "ppkn"},

        {"question" : "Nilai kebersamaan yang tercermin dalam sidang panitia sembilan dalam perumusan Pancasila adalah ...", 
        "answer" : ["perdebatan yang seru", "saling beradu pendapat", "berjuang meraih kemerdekaan", "menghargai adanya perbedaan pendapat"], 
        "correct" : "menghargai adanya perbedaan pendapat",
        "type" : "ppkn"},

        {"question" : "Dasar Negara Kesatuan Republik Indonesia adalah", 
        "answer" : ["UUD1945", "Undang-Undang", "Pancasila", "Perpres"], 
        "correct" : "Pancasila",
        "type" : "ppkn"},
        
        {"question" : "Berikut ini yang termasuk dalam jenis-jenis peraturan perundang-undangan tingkat daerah adalah ....", 
        "answer" : ["PP", "Perpu", "UUD1945", "Perda Provinsi"], 
        "correct" : "Perda Provinsi",
        "type" : "ppkn"},

        {"question" : "Berikut ini yang merupakan pengaruh positif dari globalisasi adalah ....", 
        "answer" : ["pergaulan bebas", "perilaku individual", "penyalahgunaan narkoba", "kemudahan berkomunikasi"], 
        "correct" : "kemudahan berkomunikasi",
        "type" : "ppkn"},

        {"question" : "Budaya asing yang dapat ditiru adalah budaya yang ....", 
        "answer" : ["bertentangan dengan kepribadian bangsa", "sesuai dengan kepribadian bangsa", "sesuai dengan selera kita", "menjadi tren masa kini"], 
        "correct" : "sesuai dengan kepribadian bangsa",
        "type" : "ppkn"},

        {"question" : "Salah satu contoh organisasi sosial kemasyarakatan adalah ....", 
        "answer" : ["pemerintah desa", "karang taruna", "partai politik", "pramuka"], 
        "correct" : "karang taruna",
        "type" : "ppkn"},

##############################################################################################################################################

        #1-10 PJOK
        {"question" : "Senam yang terdiri atas gerakan tertentu yang dilakukan diatas matras adalah ...", 
        "answer" : ["senam Aerobik", "senam Lantai", "SKJ", "senam pagi"], 
        "correct" : "senam Lantai",
        "type" : "pjok"},

        {"question" : "Senam lantai merupakan salah satu nomor senam ...", 
        "answer" : ["anaerobik", "dinamik", "aerobik", "artistik"], 
        "correct" : "artistik",
        "type" : "pjok"},

        {"question" : "Contoh lain senam artistik adalah ...", 
        "answer" : ["kuda-kuda pelana", "yoga", "SKJ", "senam pagi"], 
        "correct" : "kuda-kuda pelana",
        "type" : "pjok"},

        {"question" : "Berikut unsur unsur gerakan senam artistik, kecuali ...", 
        "answer" : ["mengguling", "duduk", "melompat", "meloncat"], 
        "correct" : "duduk",
        "type" : "pjok"},

        {"question" : "Tiga elemen gerakan yang digabung menjadi satu gerakan yang berkesinambungan sehingga nampak indah bagi yang melihatnya disebut ...", 
        "answer" : ["senam aerobik", "senam artistik", "senam lantai tiga pola", "senam pagi"], 
        "correct" : "senam artistik",
        "type" : "pjok"},

        {"question" : "Gerak yang mendasari terbentuknya suatu ketrampilan dalam senam lantai yaitu ...", 
        "answer" : ["gerak dasar", "keseimbangan", "pola gerak dominan", "kekuatan"], 
        "correct" : "pola gerak dominan",
        "type" : "pjok"},

        {"question" : "Berikut macam pola gerak dominan, kecuali ...", 
        "answer" : ["lari zig zag (belak belok)", "posisi statis", "rotations (putaran)", "ayunan (swing)"], 
        "correct" : "lari zig zag (belak belok)",
        "type" : "pjok"},

        {"question" : "Dibawah ini contoh gerak lokomotor adalah ...", 
        "answer" : ["duduk", "berjalan", "berdiri satu kaki", "membungkuk"], 
        "correct" : "berjalan",
        "type" : "pjok"},

        {"question" : "Dibawah ini contoh gerak non lokomotor adalah...", 
        "answer" : ["mengayun lengan", "berlari", "melompat", "berjalan"], 
        "correct" : "mengayun lengan",
        "type" : "pjok"},

        {"question" : "Gerakan yang dilakukan secara memutar dan berada pada titik poros disebut ...", 
        "answer" : ["ayunan/swing", "posisi statis", "putaran", "springs"], 
        "correct" : "putaran",
        "type" : "pjok"},

        {"question" : "Bertumpu pada pundak dan kedua kaki diangkat lurus keatas kedua tangan membantu menopang pantat disebut ...", 
        "answer" : ["sikap lilin", "guling ke depan", "guling belakang", "meroda"], 
        "correct" : "sikap lilin",
        "type" : "pjok"},

        {"question" : "Gerakan awal pada sikap lilin adalah", 
        "answer" : ["Tubuh terlentang", "jongkok", "Berdiri tegak", "setengah jongkok"], 
        "correct" : "Tubuh terlentang",
        "type" : "pjok"},

        {"question" : "Pada saat tumpuan dibutuhkan keseimbangan yang baik. Tumpuan sikap lilin terletak pada…..", 
        "answer" : ["pundak", "kedua tangan", "kedua kaki", "kedua siku dan pundak"], 
        "correct" : "kedua siku dan pundak",
        "type" : "pjok"},

        {"question" : "Meloncati rintangan diawali dengan berlari sebagai awalan. Bagaimana posisi badan pada saat melakukan awalan?", 
        "answer" : ["Mengahadap ke depan", "duduk", "Membelakangi rintangan", "jongkok"], 
        "correct" : "Mengahadap ke depan",
        "type" : "pjok"},

        {"question" : "Tolakan dilakuakan dengan salah satu kaki. Kaki manakah yang digunakan untuk menolak agar menghasilkan tolakan yang optimal?", 
        "answer" : ["kanan", "kedua kaki", "kiri", "kaki terkuat"], 
        "correct" : "kaki terkuat",
        "type" : "pjok"},

        {"question" : "Lapangan kasti biasanya berbentuk ....", 
        "answer" : ["persegi", "segi lima", "segi enam", "segitiga"], 
        "correct" : "persegi",
        "type" : "pjok"},

###############################################################################################################################################

        #1-10 SBdP
        {"question" : "Contoh kota yang memproduksi batik adalah ...", 
        "answer" : ["Manokwari", "Pekalongan", "Banten", "Madiun"], 
        "correct" : "Pekalongan",
        "type" : "sbdp"},

        {"question" : "Alat untuk membuat batik adalah ...", 
        "answer" : ["pena", "menandai Pena", "canting", "krayon"], 
        "correct" : "canting",
        "type" : "sbdp"},

        {"question" : "Keringkan handuk batik yang masih basah di tempat teduh untuk ...", 
        "answer" : ["Sehingga warnanya menjadi lebih terang", "Agar warnanya tidak pudar", "Sehingga warnanya menjadi lebih gelap", "Warnanya cepat kohesif"], 
        "correct" : "Sehingga warnanya menjadi lebih terang",
        "type" : "sbdp"},

        {"question" : "Bentuk dasar apresiasi seni adalah melalui ...", 
        "answer" : ["pura-pura", "cuti", "pelepasan", "kagumi"], 
        "correct" : "kagumi",
        "type" : "sbdp"},

        {"question" : "Keunggulan orang yang menghargai seni adalah ...", 
        "answer" : ["Kebosanan dengan cepat", "Terkesan oleh orang tua", "Apakah Anda ingin membeli dengan boros", "Dapatkan kepuasan batin"], 
        "correct" : "Dapatkan kepuasan batin",
        "type" : "sbdp"},

        {"question" : "Orang yang menggambar ilustrasi disebut ...", 
        "answer" : ["ilusi", "direktur", "pencipta", "ilustrator"], 
        "correct" : "ilustrator",
        "type" : "sbdp"},

        {"question" : "Gambar ilustrasi dibagi menjadi ...", 
        "answer" : ["4", "7", "10", "13"], 
        "correct" : "7",
        "type" : "sbdp"},

        {"question" : "Ilustrasi dalam komik dibuat oleh ...", 
        "answer" : ["mix", "tunggal", "paralel", "bersama"], 
        "correct" : "paralel",
        "type" : "sbdp"},

        {"question" : "Gambar ilustrasi yang digunakan pada papan iklan termasuk jenis ...", 
        "answer" : ["tahu", "gambar kartun", "pengiklanan", "kesaksian"], 
        "correct" : "pengiklanan",
        "type" : "sbdp"},

        {"question" : "Yang tidak tergantung pada motif dekoratif adalah ...", 
        "answer" : ["simbolis", "dekorasi", "sumber sejarah", "melengkapi"], 
        "correct" : "melengkapi",
        "type" : "sbdp"}

    ]