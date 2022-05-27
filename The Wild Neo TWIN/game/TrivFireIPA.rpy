# Trivia Bank

define question = 1
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ trivIPA = [

        # 1-10
        {"question" : "Proses yang disertai dengan pertambahan berat, besar, dan tinggi pada makhluk hidup disebut ....", 
        "answer" : ["Pertambahan", "Penggemukan", "Pertumbuhan", "Berkembang biak"], 
        "correct" : "Pertumbuhan"},

        {"question" : "Alat perkembangbiakan generatif pada tumbuhan berupa ....", 
        "answer" : ["Bunga", "Batang", "Daun", "Akar"], 
        "correct" : "Bunga"},
        
        {"question" : "Hewan yang bekembangbiakan dengan cara bertelur adalah", 
        "answer" : ["Angsa, itik, dan bebek", "Bebek, angsa, dan kelinci", "Ayam, hiu, dan cecak", "Kera, bebek, dan ayam"], 
        "correct" : "Angsa, itik, dan bebek"},
        
        {"question" : "Burung elang berkembang biak dengan cara bertelur. Berarti, burung elang mengalami perkembangbiakan secara ....", 
        "answer" : ["Vegetatif", "Membelah diri", "Spora", "Generatif"], 
        "correct" : "Generatif"},

        {"question" : "Perkembangbiakan secara bertelur dan beranak disebut juga dengan perkembangbiakan ....", 
        "answer" : ["Spora", "Ovipar", "Vivipar", "Ovovivipar"], 
        "correct" : "Ovovivipar"},

        {"question" : "Hewan yang berkembang biak secara ovipar adalah ....", 
        "answer" : ["Kadal, hiu, dan ular", "Ayam, hiu, dan lumba-lumba", "Ayam, bebek, dan angsa", "Kambing, sapi, dan kelinci"], 
        "correct" : "Ayam, bebek, dan angsa"},

        {"question" : "Ciri yang dapat diamati pada ayam dan kucing yang akan kawin adalah ....", 
        "answer" : ["Berkejar-kejaran", "Menari di hadapan betinanya", "Membuat sarang", "Mengeluarkan tarian khusus"], 
        "correct" : "Berkejar-kejaran"},

        {"question" : "Sel kelamin betina yang terdapat pada bunga disebut ....", 
        "answer" : ["Kelopak", "Benang sari", "Mahkota", "Putik"], 
        "correct" : "Putik"},

        {"question" : "Bambu berkembang biak dengan ....", 
        "answer" : ["Spora", "Rhizoma", "Tunas", "Tunas adventif"], 
        "correct" : "Tunas"},

        {"question" : "Salah satu tumbuhan yang berkembang biak dengan umbi lapis yaitu ....", 
        "answer" : ["Rumput teki", "Sukun", "Bunga bakung", "Ubi jalar"], 
        "correct" : "Bunga bakung"},

        # 10 - 20
        {"question" : "Serbuk sari yang jatuh ke kepala putik yang berasal dari bunga itu sendiri disebut penyerbukan ....", 
        "answer" : ["Silang", "Sendiri", "Tetangga", "Bastar"], 
        "correct" : "Sendiri"},

        {"question" : "Perkembangbiakan generatif pada tumbuhan hanya bisa terjadi pada tumbuhan yang memiliki ....", 
        "answer" : ["Akar", "Bunga", "Daun", "Batang"], 
        "correct" : "Bunga"},

        {"question" : "Berikut ini merupakan perkembangbiakan vegatatif alami adalah ....", 
        "answer" : ["Mencangkok", "Setek", "Geragih", "Okulasi"], 
        "correct" : "Geragih"},

        {"question" : "Berikut adalah bagian-bagian yang terdapat pada bunga, kecuali ....", 
        "answer" : ["Putik", "Mahkota bunga", "Kepala sari", "Kelopak bunga"], 
        "correct" : "Kepala sari"},

        {"question" : "Alat kelamin jantan pada bunga adalah ....", 
        "answer" : ["Benang sari", "Putik", "Mahkota bunga", "Benang mahkota"], 
        "correct" : "Benang sari"},

        {"question" : "Penyerbukan yang terjadi jika serbuk sari yang jatuh di atas kepala putik berasal dari tanaman yang berbeda tetapi masih satu jenis dinamakan penyebukan ....", 
        "answer" : ["Sendiri", "Tetangga", "Silang", "Bartas"], 
        "correct" : "Silang"},

        {"question" : "Perkembangan vegetatif terdiri menjadi dua macam, yaitu ....", 
        "answer" : ["Buatan dan fisika", "Alami dan buatan", "Biologi dan kimia ", "Alami dan biologi"], 
        "correct" : "Alami dan buatan"},

        {"question" : "Hewan berikut ini yang dapat membantu penyerbukan pada tumbuhan adalah ....", 
        "answer" : ["Jangkrik", "Lebah", "Gajah", "Ayam"], 
        "correct" : "Lebah"},

        {"question" : "Ovarium pada tubuh wanita melepaskan sel telur dengan jangka waktu ....", 
        "answer" : ["Setahun sekali", "Sebulan sekali", "Seminggu sekali", "Sehari sekali"], 
        "correct" : "Sebulan sekali"},

        {"question" : "Batang yang akan dicangkok dipilih cabang yang ....", 
        "answer" : ["Besar", "Bengkok", "Kecil", "Lurus"], 
        "correct" : "Lurus"},

        #20-27
        {"question" : "Perkembangbiakan tumbuhan dengan cara menimbun bagian cabang yang tumbuh memanjang dalam permukaan tanah dinamakan ....", 
        "answer" : ["Merunduk", "Okulasi", "Mengenten", "Stek"], 
        "correct" : "Merunduk"},

        {"question" : "Perkembangbiakan vegatatif buatan yang dilakukan dengan menanam bagian tertentu dari tumbuhan tanpa menunggu tumbuhnya akar disebut ....", 
        "answer" : ["Geragih", "Setek", "Mencangkok", "Okulasi"], 
        "correct" : "Setek"},

        {"question" : "Berikut adalah tumbuhan yang berkembang biak secara tunas ....", 
        "answer" : ["Pisang dan mangga", "Bambu dan mahoni", "Pisang dan padi", "Pisang dan bambu"], 
        "correct" : "Pisang dan bambu"},

        {"question" : "Jamur, tumbuhan paku dan lumut adalah contoh tumbuhan yang tidak berbiji. Tumbuhan tersebut berkembang biak dengan cara ....", 
        "answer" : ["Spora", "Stek", "Okulasi", "Membelah diri"], 
        "correct" : "Spora"},

        {"question" : "Contoh tumbuhan yang berkembang biak dengan cara umbi lapis adalah ....", 
        "answer" : ["Bawang merah, kentang, dan bawang putih", "Jambu, mangga, dan rambutan", "Tebu, bambu, dan pisang", "Bawang merah, bawang putih, dan bawang bombay"], 
        "correct" : "Bawang merah, bawang putih, dan bawang bombay"},

        {"question" : "Di bawah ini yang merupakan ciri bunga yang penyerbukannya dibantu oleh hewan adalah ....", 
        "answer" : ["Kepala putik agak tersembunyi", "Mahkota tidak berwarna mencolok", "Serbuk sari kering", "Mahkota bunga kecil"], 
        "correct" : "Kepala putik agak tersembunyi"},

        {"question" : "Setelah penyerbukan maka akan terjadi proses pembuahan (fertilisasi) yang terjadi di ....", 
        "answer" : ["Mahkota bunga", "Bakal biji", "Dasar bunga", "Kelopak"], 
        "correct" : "Bakal biji"},
        
    ]
