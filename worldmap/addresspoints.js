// index 1 is the status of the language: 0 = well, 1 = medium, 2 = under
var addressPoints = [
    ["Chinese",0,"The adventures of Huckleberry Finn","undefined",1979,"Shanghai Foreign Language Publishing House","Shanghai, China",353,31.275595,121.4798653],
    ["Chinese",0,"哈克貝利. 費恩歷險記 (Hakebeili Fei\'en li xian ji)","張友松 (Zhang Yousong), 張振先譯 (Zhang Zhenxian yi)",1956,"China Youth Press","Beijing, China",349,39.9385466,116.1172715],
    ["French",0,"Les aventures de Tom Sawyer, Les aventures de Huck Finn, Le prince et le pauvre","P. F. Caillé, Yolande et René Surleau, Jean Muray",1964,"Hachette","Paris, France",223,48.8222048,2.2947085],
    ["French",0,"Les aventures de Huck Finn : l\'ami de Tom Sawyer","William L. Hughes, Illustrator: Achille Sirouy",1886,"Bibliotheque nouvelle de la jeunesse","Paris, France",276,48.8520155,2.3450284],
    ["French",0,"Les aventures de Huck Finn / Mark Twain","Yolande et René Surleau, Illustrator: Daniel Billon",1977,"Hachette","Paris, France",254,48.8222048,2.2947085],
    ["French",0,"Les aventures d\'Huckleberry Finn","Suzanne Nétillard, Illustrator: Nathaële Vogel",1982,"Éditions Gallimard","Paris, France",380,48.856993,2.3264833],
    ["German",0,"Die streiche Tom Sawyers und Huckleberry Finns","Carl Hartz","after 1880?","Gemeinschaft","Berlin, Germany",367,52.5065133,13.1445526],
    ["German",0,"Huckleberry Finns Fahrten und Abenteuer","Julie Mathieu, Gerhard Jaeckel, Illustrator: Alex",1938,"Deutschen Verlag","Berlin, Germany",269,52.5246107,13.4026677],
    ["German",0,"Huckleberry Finns Fahrten und Abenteuer","Ulrich Steindorff",1921,"Ulrich Steindorff","Berlin, Germany",473,52.5246107,13.4026677],
    ["German",0,"Tom Sawyers Abenteuer ; Huckleberry Finns Abenteuer","undefined",1981,"Deutscher Taschenbuch Verlag (dtv Verlagsgesellschaft)","Munich, Germany",613,48.1254311,11.5553409],
    ["German",0,"Abenteuer und Fahrten des Huckleberry Finn","Henny Koch",1890,"Robert Lutz","Stuttgart, Germany",321,48.7791242,9.0371318],
    ["German",0,"Huckleberry Finns abenteuer und fahrten","Henny Koch","19--?","undefined","Leipzig, Germany",333,51.341699,12.2535519],
    ["Italian",0,"Le avventure di Huckleberry Finn","Pietro Citati, Gabriele Musumarra",1982,"Biblioteca Universale Rizzoli (BUR)","Milan, Italy",364,45.5055421,9.2343733],
    ["Japanese",0,"The adventures of Huckleberry Finn","Eizō Ōhashi",1967,"undefined","Tōkyō, Japan",538,35.6681625,139.6007824],
    ["Japanese",0,"トム・ソ－ヤ－ と ハックルベリ－・フィン : マ－ク・トウェイン の ミシシッピ河 (Tomu Sōyā to Hakkuruberī Fin : Māku Towein no Mishishippigawa)","今村 楯夫 (Imamura Tateo), 川村 湊 (Gotō Kazuhiko), 和田 悟 (Wada Satoru)",1996,"Kyuryudo Graphics","Tōkyō, Japan",119,35.6826453,139.735866],
    ["Japanese",0,"ハックルベリイ・フィンの冒険 (Hakkuruberii Fin no bōken)","村岡花子訳 (Muraoka Hanako yaku)","昭和 34 (Showa 47) / 1972","新潮社 (Shinchosha Publishing Co)","Tōkyō, Japan",415,35.7029727,139.7308449],
    ["Japanese",0,"ハックルベリイ・フィンの冒険 (Hakkuruberii Fin no bōken)","野崎孝訳 (Nozaki Takashi yaku)","昭和 46 (Showa 46) / 1971","講談社 (Kōdansha)","Tōkyō, Japan",552,35.7177365,139.7256228],
    ["Korean",0,"Hok\'ulperi p\'in-ui mohom","Kwak, Kyong-su",1990,"Kumsong Youth Publishing House (Kumsong ch\'ulp\'ansa)","Seoul, South Korea",534,37.5665,126.978],
    ["Russian",0,"The adventures of Tom Sawyer; The adventures of Huckleberry Finn","Mariia Nesterovna Bobrova",1960,"Foreign Language Publishing House","Moscow, Russia (USSR until 1991)",588,55.735979,37.5879314],
    ["Russian",0,"Prikli︠u︡chenii︠a︡ Toma Soĭera : povestʼ; Prikli︠u︡chenii︠a︡ Geklʼberri Finna : roman.","undefined",1985,"Detskai︠a︡ literatura","Moscow, Russia (USSR until 1991)",462,55.580748,36.825123],
    ["Russian",0,"Prikli︠u︡chenii︠a︡ Toma Soĭera ; Prikli︠u︡chenii︠a︡ Geklʹberri Finna : povesti","N. Daruzes",1984,"Zhalyn","Almaty, Kazakhstan",381,43.2173601,76.6639798],
    ["Russian",0,"Prikli︠u︡chenii︠a︡ Toma Soĭera ; Prikli︠u︡chenii︠a︡ Geklʹberri Finna","undefined",1984,"Ėnergoatomizdat","Moscow, Russia (USSR until 1991)",510,55.7616131,37.6211646],
    ["Russian",0,"Prikli︠u︡chenii︠a︡ Toma Soĭera ; Prikli︠u︡chenii︠a︡ Geklʹberri Finna ; Print︠s︡ i nishchiĭ : povesti ","G. Mazurina",1981,"Detskai︠a︡ literatura","Moscow, Russia (USSR until 1991)",669,55.580748,36.825123],
    ["Russian",0,"Prikli︠u︡chenii︠a︡ Toma Soĭera ; Prikli︠u︡chenii︠a︡ Geklʹberri Finna ; Print︠s︡ i nishchiĭ","undefined",1978,"Detskai︠a︡ literatura","Moscow, Russia (USSR until 1991)",669,55.580748,36.825123],
    ["Russian",0,"Prikli︠u︡chenii︠a︡ Toma Soĭera ; Prikli︠u︡chenii︠a︡ Geklʹberri Finna ; Print︠s︡ i nishchiĭ : povesti ","G. Mazurina",1982,"Detskai︠a︡ literatura","Moscow, Russia (USSR until 1991)",669,55.580748,36.825123],
    ["Spanish",0,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Swedish",0,"Huckleberry Finns äventyr","Sven Barthel, Illustrator: Bertil Bull Hedlund, Cover: Nils Stödberg",1984,"Bonniers Junior Förlag","Stockholm, Sweden",333,59.3386281,18.0598751],
    ["Swedish",0,"Tom Sawyers och Huckleberry Finns äfventyr","Petrus Hedberg",1898,"W. Siléns","Stockholm, Sweden",982,59.3260668,17.841971],
    ["Arabic",1,"Mughāmrāt Hilkbirīfīn","Al-Siwīfī, Mukhtār",1986,"Al-Hayʻah al-Miṣrīyah al-Āmmah lil-Kitāb","Al-Qāhirah (Cairo), Egypt",363,30.0444,31.2357],
    ["Bulgarian",1,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Czech",1,"Dobrodružství Frantíka Finna : kamaráda Toma Sawyera / Mark Twain","Karel Kolman",1900,"J. Otty","Prague (Praze), Czech Republic",231,50.0595854,14.3255407],
    ["Croatian",1,"Doživljaji Haklberi Fina : drugara Toma Sojera : događa se u dolini Misisipe oko polovine XIX veka","Jelisaveta Marković",1952,"Preduzeđe Novo Pokolenje","Belgrade (Београд), Serbia",428,44.8070042,20.381265],
    ["Danish",1,"Huckleberry Finn / Mark Twain","Ole Storm",1983,"Gyldendal","Copenhagen, Denmark","undefined",55.6811075,12.5761768],
    ["Dutch",1,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Estonian",1,"Huckleberry Finni seiklused","Bergmann, A.; Sillaots, M.",1989,"Eesti Raamat","Tallinn, Estonia",512,59.4129419,24.673865],
    ["Finnish",1,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Greek",1,"Hoi peripeteies tou Chaklbery Phin","Nikos Lampropoulos",1977,"Ekdoseis Odysseas","Athens, Greece",318,37.990832,23.7033198],
    ["Hebrew",1,"Harpatqeotaw shel Huckleberry Finn","Farkash, Yaniv",2005,"Aryeh Nir Publishing House","Tel Aviv, Israel",431,32.089653,34.882277],
    ["Hungarian",1,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Icelandic",1,"Stikilberja-Finnur","Bjarnason, Kristmundur; Kristjánsson, Árni",1986,"Reykjavík: Ab","Reykjavík, Iceland",244,64.146521,-21.942368],
    ["Icelandic",1,"Stikilsberja Finnur","Jónsson, Daníel Freyr; Redondo, Francisco",1995,"Reykjavík: Graena gáttin","Reykjavík, Iceland",62,64.137011,-21.955134],
    ["Latvian",1,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Lithuanian",1,"Heklberio Fino nuotykiai","Churginaitė, Valentina",1984,"Vaga","Vilnius, Lithuania (USSR until 1991)",519,54.6892947,25.2660656],
    ["Norwegian",1,"Huckleberry Finn","Hopp, Zinken",2006,"Fono forl","Oslo, Norway","undefined",59.9147789,10.7501571],
    ["Norwegian",1,"Huckleberry Finn","Olav Angell, Illustrator: Erik Palmquist",1985,"Bokklubben","Oslo, Norway",372,59.9458416,10.7755087],
    ["Norwegian",1,"Huckleberry Finn","undefined",1982,"Atlantic Vorlag","Oslo, Norway",47,59.9458416,10.7755087],
    ["Polish",1,"Przygody Hucka","Tarnowska, Krystyna",1988,"Iskry","Warsaw (Warszawa), Poland (USSR until 1989)",317,52.250551,20.8704507],
    ["Portuguese",1,"As aventuras de Huckleberry Finn","Daniel Augusto Gonçalves",1980,"Livraria Civilização","Porto, Portugal",410, 41.1465414,-8.6204142],
    ["Portuguese",1,"As aventuras de Huckleberry Finn : (companheiro de Tom Sawyer) ","undefined",1961,"Clube do Livro","São Paulo, Brazil","undefined",-23.4609589,-47.2139599],
    ["Romanian",1,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Serbian",1,"Doživljaji Haklberi Fina","Držić, Leo; Miličević, Nika",2005,"Mediasat","Madrid, Spain",505,40.4362907,-3.6765904],
    ["Slovak",1,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Slovenian",1,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Turkish",1,"Huck Finn\'in başından geçenler","undefined",1984,"Kurtuluş Ofset Basımevi","Ankara, Turkey","undefined",39.9032923,32.6226823],
    ["Ukrainian",1,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Afrikans",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Albanian",2,"Aventurat e Hekelber Finit","Zheji, Gjergj",2006,"Argeta LMG","Tiranë, Albania","undefined",41.32749,19.818613],
    ["Albanian",2,"Aventurat e Hakëlberi Finit","Koka, Dritan",2008,"Dritan","Tiranë, Albania",243,41.320261,19.81293],
    ["Assamese",2,"Aghari Lara","Baruwa, Tarun Chandra",2002,"Saraighat Prakashan","Guwahati, India",158,26.2124664,91.6839302],
    ["Bengali",2,"The Adventures of Huckleberry Finn","Jamil, Rowshan",1986,"Sheba Prokashoni","Dhaka, Bangladesh",190,23.7806207,90.3492859],
    ["Bengali",2,"Huckleberry finner dussahasik ovijan","Momen, Nurul",1986,"Bangla Academy","Dhaka, Bangladesh","undefined",23.7300117,90.3945764],
    ["Bengali",2,"Dya ayadbhenchars ab Hakleberi Phin","Raha, Sudhindranath",1985,"Deb Sahitya Kutir","Calcutta, India","undefined",22.5792039,88.3665253],
    ["Burmese",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Catalan",2,"Les aventures d\'en Huckleberry Finn","Fontcuberta i Gel, Joan",1981,"Edicions de la Magrana","Barcelona, Spain","undefined",41.3947687,2.0785567],
    ["Chuvash",2,"Gekl\'berri Finn temtepĕr kursa şüreni","Sokolova, Askliada",1985,"Čuvašskoe knižnoe izdatel\'stvo","Čeboksary, Russia (USSR until 1991)",327,56.1041403,47.1193363],
    ["Farsi",2,"Sargozasht-e Hakelberi Fin","Daryā Bandari, Najaf",1987,"Khārazmi","Tehrān, Islamic Republic of Iran",379,35.7539787,51.3891088],
    ["Farsi",2,"Hākelberry Fīn","Alvī, Mehdī",1999,"Koshsh","Tehrān, Islamic Republic of Iran",143,35.6964879,51.0689516],
    ["Georgian",2,"Priključenija Gekl\'berri Finna","undefined",1983,"Nakaduli","Tbilisi, Georgia (USSR until 1991)",276,41.6653051,44.8940595],
    ["Hindi",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Indonesian",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Kazakh",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Kirghiz",2,"Gekl\'berri Findin žoruktary","Isaev, Kurmanbek",1987,"Frunze: Mektep","Bishkek, Kyrgyzstan (USSR until 1991)",267,42.8767892,74.4514355],
    ["Macedonian",2,"Haklberi Fin","Crvenkovski, Dušan",1979,"Skopje: Kultura","Skopje, North Macedonia (Yugoslavia until 2002)",284,41.995594,21.4288916],
    ["Macedonian",2,"Fin","Crvenkovski, Dušan",1987,"Skopje: Kultura","Skopje, North Macedonia (Yugoslavia until 2002)",296,41.995594,21.4288913],
    ["Macedonian",2,"Haklberi Fin","Popov, Vladimir",2004,"Skopje: Feniks","Skopje, North Macedonia",286,41.9926971,21.4265236],
    ["Malay",2,"Pengembaraan Huckleberry Finn","undefined",1983,"Whereever Distributors","Kuala Lumpur, Malaysia",143,3.1385036,101.6169494],
    ["Malayalam",2,"Hakklbari Phin","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Marathi",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Oriya",2,"Sahari yubaka","Acharya, Rajendraprasad","undefined","Jagannath Rath","Cuttack, India",69,20.4630933,85.7977059],
    ["Oriya",2,"Hucklberry Finnra duhsahasika Kāhāni","Mahapatra, Chintamani",1992,"Vidyapuri","Cuttack, India","undefined",20.3301911,85.7884362],
    ["Sinhalese",2,"Huckleberryge hapankam","Anagiratne, Chandra",1998,"Dayawansa Jayakody and Company","Colombo, Sri Lanka",333,6.9252263,79.8646707],
    ["Tamil",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Tatar",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Telugu",2,"Hakalberi phin","Nanduri Ramamohanaravu",1978,"Navodaya Publishers","Vijayavada, India",228,16.5101531,80.5748443],
    ["Thai",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Uzbech",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Basque",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Vietnamese",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Yiddish",2,"undefined","undefined","undefined","undefined","undefined","undefined",0,0],
    ["Moldovan",2,"Aventurile lui Huckleberry Finn","Solomon, Petre",2008,"Prut Internaţional","Chişinău, Republic of Moldova",332,46.9997836,28.7180949],
    ["Armenian",2,"Hek\'lberi Finni arkaçnerë","undefined",1979,"Erevan: Sovetakan groh","Yerevan, Armenia",549,40.105564,44.0474115],
    ["Turkmen",2,"Tom Sojeriń ve Gekl\'berri Finniń bašdan gečirenleri","Berdiev, Danatar",1989,"Ašhabad: Magaryf","Ašhabad, Turkmenistan (USSR until 1991)",443,37.9628753,57.970105],
    ["Persian",0,"Hakelberifin","Ebrahim Golestan","1328 / 1949","undefined","undefined","undefined",0,0],
    ["Persian",0,"Bardeh-ye Farari (Sargozasht-e Hak Fin)","Javad Mohyi","1334 / 1955","Bongah-e Matbu’ati-ye Gutenberg","Tehrān","undefined",35.7180629,51.8249706],
    ["Persian",0,"Majara-haye Hakelberifin","Hushang Pirnazar","1339 / 1960","Feranklin","Tehrān","undefined",35.6967329,51.2097333],
    ["Persian",0,"Sargozasht-e Hakelberifin","Najaf Daryabandari","1366 / 1987","Kharazmi","Tehrān",434,35.7007556,51.3935473],
    ["Persian",0,"Hakelberifin","Ebrahim Golestan","1393 / 2014","Kalagh","Tehrān",368,35.7026012,51.4200776],
    ["Persian",0,"Majarajuyi-haye Hakelberifin","Hasan Majidi","1394 / 2015","Sokhangostar","Tehrān",242,35.7052604,51.3477373],
    ["Persian",0,"Majarajuyi-haye Shegeftangiz-e Tam Sayer va Hakelberifin","Allahverdi Azari Najafabad, Illustrator: Nikpey","1382 / 2003","Aftab Mahtab","Tehrān",12,35.8059743,51.4289871],
    ["Persian",0,"Majara-haye Hakelberifin","Roya Gilani","1372 / 1993","Arghavan","Tehrān",136,35.7871072,51.3773519],
    ["Persian",0,"Majara-haye Hakelberifin","Akram shekarzadeh","1398 / 2019","Asmangun","Tehrān",72,35.4885313,50.6462407],
    ["Persian",0,"Majara-haye Hakelberifin","Akram shekarzadeh","1395 / 2016","Negah-e Ashena","Tehrān",88,35.4885313,50.6462407],
    ["Persian",0,"Majara-haye Hakelberifin","Shokufeh Akhavan","1372 / 1993","Nahal-e Navidan","Tehrān",240,35.4885313,50.6462407],
    ["Persian",0,"Majara-haye Hakelberifin","Shokufeh Akhavan","1391 / 2012","Nahal-e Navidan","Tehrān",176,35.4885313,50.6462407],
    ["Persian",0,"Majara-haye Hakelberifin","Elham al-Sadat Yasini","1398 / 2019","Ketabestan-e Ma‘refat","Tehrān",68,34.6392401,50.8747941],
    ["Persian",0,"Majara-haye Hakelberifin","Elham Keshavarzi Khuzani","1398 / 2019","Dadju","Tehrān",96,35.7984573,51.447306],
    ["Persian",0,"Majara-haye Hakelberifin","Maryam Tayyebi","1396 / 2017","Atun-e Ketab","Tehrān",512,35.4885313,50.6462407],
    ["Persian",0,"Majara-haye Hakelberifin","Sudabeh Zarkaf","1365 / 1986","Dadju","Tehrān",256,35.7984573,51.447306],
    ["Persian",0,"Hakelberifin","Parviz Najm al-dini","1369 / 1990","Tusan","Tehrān",140,35.7867294,51.3465689],
    ["Persian",0,"Majara-haye Hakelberifin","Shahram Puranfar","1362 / 1983","Zarrin","Tehrān",394,35.7633307,51.4440336],
    ["Persian",0,"Majara-haye Hakelberifin","Shahram Puranfar","1370 / 1991","Mahtab","Tehrān",394,35.7703604,51.477204],
    ["Persian",0,"Majara-haye Hakelberifin","Shahram Puranfar","1364 / 1985","Arastu","Tehrān",398,35.6885505,50.8725357],
    ["Persian",0,"Majara-haye Hakelberifin","Mohammad Hemmatkhah","1391 / 2012","Asr-e Andisheh","Tehrān",60,32.3295313,50.850859],
    ["Persian",0,"Hakelberifin","Mohsen Soleymani","1388 / 2009","Ofoq","Tehrān",538,35.7301812,51.5837023],
    ["Persian",0,"Majara-haye Hakelberifin: Matn-e Kutahshodeh","Mohsen Soleymani","1386 / 2007","Ofoq","Tehrān",288,35.7301812,51.5837023],
    ["Persian",0,"Hakelberifin","Mohammad Qasa’","1397 / 2018","Shahr-e Qalam","Tehrān",116,36.5186314,52.4888402],
    ["Persian",0,"Hakelberifin","Fatemeh Nazarahari","1397 / 2018","Guhar-e Andisheh","Tehrān",698,35.7113508,50.9820014],
    ["Persian",0,"Hakelberifin","Mojtaba Nikseresht","1397 / 2018","Daryush","Tehrān",218,35.6650778,51.3966983],
    ["Persian",0,"Hakelberifin","Mehdi Alavi","1392 / 2013","Dabir","Tehrān",128,35.7666602,51.4147204],
    ["Persian",0,"Hakelberifin","Ma’sumeh Mosavi, Illustrator: Maliheh Ahmad","1396 / 2017","Ava-ye Biseda","Tehrān",56,35.4885313,50.6462407],
    ["Persian",0,"Hakelberifin","Ma’sumeh Mosavi","1397 / 2018","Yaqut","Tehrān",56,35.7607128,51.4501204],
    ["Persian",0,"Hakelberifin","Shima Mohammadi","1396 / 2017","Panguan","Tehrān",184,35.6321993,51.3814473],
    ["Persian",0,"Hakelberifin","Khosrow Shayesteh","1364 / 1985","Sepideh","Tehrān",176,35.6865217,51.3545774],
    ["Persian",0,"Hakelberifin","Khosrow Shayesteh, Rewriter: Majid Seyf","1382 / 2003","Sepideh","Tehrān",12,35.6865217,51.3545774],
    ["Persian",0,"Hakelberifin","Ma’sumeh Mohammadi","1397 / 2018","Yushita","Tehrān",56,35.4885313,50.6462407],
    ["Persian",0,"Hakelberifin","Nafiseh Darbeheshti","1376 / 1997","Nashr-e Peyman","Tehrān",160,35.4885313,50.6462407],
    ["Persian",0,"Hakelberifin","Daryush Shahin, Susan Ardakani","1396 / 2017","Nezareh","Tehrān",410,35.4885313,50.6462407],
    ["Persian",0,"Hakelberifin","Ma’sumeh Mosavi","1397 / 2018","Yaqut","Tehrān",56,35.7607128,51.4501204],
    ["Persian",0,"Hakelberifin","Alireza Khosravi","1398 / 2019","Fanus-e Danesh-e Tarvij-e Ketabkhani","Tehrān",288,35.7200703,51.4029742],
    ["Persian",0,"Hakelberifin","Narges Bahrami","1396 / 2017","Guyesh Now","Tehrān",48,35.7908428,51.4174436]
];