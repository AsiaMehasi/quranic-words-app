import streamlit as st
import pandas as pd

quranic_words = [
 {"Word (Arabic)": "و", "Transliteration": "Wa", "Meaning": "And", "Example": "وَٱللَّهُ غَفُورٌ رَّحِيمٌ", "Translation": "And Allah is Forgiving and Merciful"},
 {"Word (Arabic)": "في" , "Transliteration": "Fi", "Meaning": "In, Inside", "Example": "فِي ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِ", "Translation": "In the heavens and the earth"},
 {"Word (Arabic)": "من" , "Transliteration": "Min", "Meaning": "From, Of", "Example": "مِنَ ٱلۡجِنَّةِ وَٱلنَّاسِ", "Translation": "From among the jinn and mankind"},
 {"Word (Arabic)": "على ", "Transliteration" : "'Ala", "Meaning": "On, Upon", "Example": "وَعَلَىٰ ٱللَّهِ فَلۡيَتَوَكَّلِ ٱلۡمُؤۡمِنُونَ", "Translation": "And upon Allah let the believers rely"},
 {"Word (Arabic)": "إلى ", "Transliteration" : "Ila", "Meaning": "To", "Example": "إِلَىٰ رَبِّهِمْ يَحْشُرُونَ", "Translation": "To their Lord, they will be gathered"},
 {"Word (Arabic)": "عن" , "Transliteration": "An", "Meaning": "About, Concerning, From", "Example": "عَن سَبِيلِ ٱللَّهِ", "Translation": "From the path of Allah"},
 {"Word (Arabic)": "رب" , "Transliteration": "Rabb", "Meaning": "Lord", "Example": "رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِ", "Translation": "The Lord of the heavens and the earth"},
 {"Word (Arabic)": "سَلاَم", "Transliteration": "Salam", "Meaning": "Peace", "Example": "فَسَلَّمُوٓا۟ عَلَيْهِمْ بِسَلاَمٍۢ", "Translation": "Greet them with peace"},
 {"Word (Arabic)": "توكل", "Transliteration": "Tawakkul", "Meaning": "Trust, Reliance", "Example": "وَعَلَىٰ رَبِّهِمۡ يَتَوَكَّلُونَ", "Translation": "And upon their Lord they rely"},
 {"Word (Arabic)": "غفر ", "Transliteration" : "Ghufran", "Meaning": "Forgiveness", "Example": "رَبَّنَا ٱغْفِرْ لَنَا ذُنُوبَنَا", "Translation": "Our Lord, forgive us our sins"},
 {"Word (Arabic)": "قمر ", "Transliteration" : "Qamar", "Meaning": "Moon", "Example": "وَٱلْقَمَرِ إِذَا تَلَاهَا", "Translation": "And the moon when it follows it"},
 {"Word (Arabic)": "نجوم", "Transliteration": "Nujum", "Meaning": "Stars", "Example": "وَٱلنَّجْمِ وَٱلشَّجَرِ", "Translation": "By the stars and the trees"},
 {"Word (Arabic)": "سماء", "Transliteration": "Sama'", "Meaning": "Sky", "Example": "إِنَّ فِى سَمَٰوَٰتِهِۦ", "Translation": "Indeed in the heavens"},
 {"Word (Arabic)": "أرض ", "Transliteration" : "Ard", "Meaning": "Earth", "Example": " وَفِي ٱلۡأَرۡضِ ءَايَٰتٌ لِّلۡمُوقِنِينَ", "Translation": "And on the earth are signs for the certain in faith - Surah Al-Jathiya 45:3 "},
 {"Word (Arabic)": "جند ", "Transliteration" : "Jund", "Meaning": "Army", "Example": "وَكَانَ جُندُهُمَا هُنَالِكَ مَغۡلُوبِ", "Translation": "And their army was defeated there"},
 {"Word (Arabic)": "إصبع", "Transliteration": "Isba'", "Meaning": "Finger", "Example": "وَفَطَرْنَا ٱلۡإِصۡبَعَ", "Translation": "And we formed the fingers"},
 {"Word (Arabic)": "أذن ", "Transliteration" : "Udhun", "Meaning": "Ear", "Example": "لَهُمۡ ءَاذَانٌۭ لَّا يَسۡمَعُونَ بِهَا", "Translation": "They have ears with which they do not hear - Surah Al-A'raf, 7:179"},
 {"Word (Arabic)": "عين ", "Transliteration" : "Ayn", "Meaning": "Eye", "Example": "وَاصْنَعِ ٱلۡفُلۡكَ بِأَعۡيُنِنَا وَوَحۡيِنَا", "Translation": "And construct the ship under Our eyes and Our inspiration - Surah Hud, 11:37"},
 {"Word (Arabic)": "لسان", "Transliteration": "Lisan", "Meaning": "Tongue", "Example": "وَمَآ أَرۡسَلۡنَا مِن رَّسُولٍ إِلَّا بِلِسَانِ قَوۡمِهِۦ", "Translation": "And We did not send any messenger except [speaking] in the tongue of his people - Surah Ibrahim, 14:4"},
 {"Word (Arabic)": "يد" , "Transliteration": "Yad", "Meaning": "Hand", "Example": "وَجَعَلْنَا يَدَٰهُ قَبْضًا", "Translation": "And We made his hand close"},
 {"Word (Arabic)": "نساء", "Transliteration": "Nisa", "Meaning": "Women", "Example": "وَعَاشِرُوهُنَّ بِٱلۡمَعۡرُوفِۚ", "Translation": "And live with them in kindness - Surah An-Nisa, 4:19"},
 {"Word (Arabic)": "والدة", "Transliteration": "Walidah", "Meaning": "Mother", "Example": "وَوَصَّيْنَا ٱلۡإِنسَـٰنَ بِوَٰلِدَيۡهِ", "Translation": "And We have enjoined upon man [care] for his parents - Surah Luqman, 31:14"},
 {"Word (Arabic)": "منزل", "Transliteration": "Manzil", "Meaning": "Abode, Residence", "Example": "وَأَنزَلَ ٱلۡقُرۡءَانَ", "Translation": "And He sent down the Quran - Surah Al-Isra, 17:9"},
 {"Word (Arabic)": "باب ", "Transliteration" : "Bab", "Meaning": "Door", "Example": "وَقَالَ ٱدۡخُلُوا۟ ٱلۡبَابَ سُجَّدًۭا", "Translation": "And He said, 'Enter the door in prostration' - Surah Al-Baqarah, 2:58"},
 {"Word (Arabic)": "قبة ", "Transliteration" : "Qubba", "Meaning": "Dome", "Example": "تَحْتَ قُبَّتِهِۦ", "Translation": "Under his dome"},
 {"Word (Arabic)": "سقف ", "Transliteration" : "Saqf", "Meaning": "Roof", "Example": "وَجَعَلۡنَا ٱلسَّمَآءَ سَقۡفًۭا مَّحۡفُوظًۭا", "Translation": "And We made the sky a protected ceiling - Surah Al-Anbiya, 21:32"},
 {"Word (Arabic)": "شجرة", "Transliteration": "Shajarah", "Meaning": "Tree", "Example": "وَشَجَرَةً۬ تَخۡرُجُ مِن طُورِ سَيۡنَآءَ", "Translation": "And a tree that grows out of Mount Sinai - Surah Al-Mu’minun, 23:20"},
 {"Word (Arabic)": "ريح ", "Transliteration" : "Rih", "Meaning": "Wind", "Example": "وَفِى عَادٍ إِذۡ أَرۡسَلۡنَا عَلَيۡهِمُ ٱلرِّيحَ ٱلۡعَقِيمَ", "Translation": "And in [the case of] 'Aad, when We sent against them the barren wind - Surah Adh-Dhariyat, 51:41"},
 {"Word (Arabic)": "صوت ", "Transliteration" : "Sawt", "Meaning": "Voice, Sound", "Example": "إِنَّ أَنكَرَ ٱلۡأَصۡوَٲتِ لَصَوۡتُ ٱلۡحَمِيرِ", "Translation": "Indeed, the most disagreeable of sounds is the voice of donkeys - Surah Luqman, 31:19"},
 {"Word (Arabic)": "رسول", "Transliteration": "Rasul", "Meaning": "Messenger", "Example": "وَمَا مُحَمَّدٌ إِلَّا رَسُولٌۭ", "Translation": "And Muhammad is not but a messenger - Surah Aal-E-Imran, 3:144"},
 {"Word (Arabic)": "أمل ", "Transliteration" : "Amal", "Meaning": "Hope, Expectation", "Example": "وَأَمَّلُوا۟ فَجَنَّٰتِهِۦ", "Translation": "And they hoped for his gardens"},
 {"Word (Arabic)": "رجاء", "Transliteration": "Raja'", "Meaning": "Hope", "Example": "مَّن كَانَ يَرۡجُواْ لِقَآءَ ٱللَّهِ", "Translation": "Whoever hopes for the meeting with Allah - Surah Al-Ankabut, 29:5"},
 {"Word (Arabic)": "سوء ", "Transliteration" : "Su'", "Meaning": "Evil, Harm", "Example": "وَيَخَافُونَ سُوٓءَ ٱلۡحِسَابِ", "Translation": "And they fear the evil of [His] account - Surah Ar-Ra'd, 13:21"},
 {"Word (Arabic)": "وقت ", "Transliteration" : "Waqt", "Meaning": "Time", "Example": "إِنَّ ٱلصَّلَوٰةَ كَانَتۡ عَلَى ٱلۡمُؤۡمِنِينَ كِتَٰبًۭا مَّوۡقُوتًۭا", "Translation": "Indeed, prayer has been decreed upon the believers a decree of specified times - Surah An-Nisa, 4:103"},
 {"Word (Arabic)": "صوم ", "Transliteration" : "Sawm", "Meaning": "Fasting", "Example": "كُتِبَ عَلَيۡكُمُ ٱلصِّيَامُ", "Translation": "Fasting has been decreed upon you - Surah Al-Baqarah, 2:183"},
 {"Word (Arabic)": "قادر", "Transliteration": "Qadir", "Meaning": "Capable, Powerful", "Example": "إِنَّنِيۤۦ عَلَىٰ كُلِّ شَىۡءٍۢ قَدِيرٌۭ", "Translation": "Indeed, I am capable of all things"},
 {"Word (Arabic)": "كفر ", "Transliteration" : "Kufr", "Meaning": "Disbelief", "Example": "إِنَّ ٱلَّذِينَ كَفَرُواْ", "Translation": "Indeed, those who disbelieve - Surah Al-Baqarah, 2:6"},
 {"Word (Arabic)": "طهور", "Transliteration": "Tuhur", "Meaning": "Purity", "Example": "وَثِيَابَكَ فَطَهِّرۡ", "Translation": "And purify your garments - Surah Al-Muddathir, 74:4"},
 {"Word (Arabic)": "ذكر ", "Transliteration" : "Dhikr", "Meaning": "Remembrance", "Example": "إِنَّ اللَّهَ يَذۡكُرُهُۥۤ", "Translation": "Indeed, Allah remembers him"},
 {"Word (Arabic)": "حق" , "Transliteration": "Haqq", "Meaning": "Truth, Right", "Example": "إِنَّۢ هَٰذَا لَهُوَ الْحَقُّ", "Translation": "Indeed, this is the truth"},
 {"Word (Arabic)": "باطل", "Transliteration": "Batil", "Meaning": "Falsehood", "Example": "إِنَّمَآ الْبَاطِلُ يُذْهِبُهُۥۤ", "Translation": "Indeed, falsehood is removed"},
 {"Word (Arabic)": "حقيقة", "Transliteration": "Haqiqah", "Meaning": "Reality, Truth", "Example": "بَلْ كَانَتۡ مَعَٰهِمْ حَقِيقَةًۭ فَأَكَلُوا۟", "Translation": "But the reality was with them, and they ate - Surah Al-Jathiya, 45:13"},
 {"Word (Arabic)": "شرف ", "Transliteration" : "Sharaf", "Meaning": "Honor, Dignity", "Example": "إِنَّ الشَّرَفَ لِعِبَادِهِۦ", "Translation": "Indeed, honor is for His servants"},
 {"Word (Arabic)": "عبود", "Transliteration": "Abd", "Meaning": "Servant, Slave", "Example": "إِنَّنيۤۦ عَبْدٌۭ لِلَّهِ", "Translation": "Indeed, I am a servant of Allah"},
 {"Word (Arabic)": "نداء", "Transliteration": "Nida", "Meaning": "Call, Cry", "Example": "وَإِذَا نَادَىٰ رَبُّهُۥۤ", "Translation": "And when his Lord called him"},
 {"Word (Arabic)": "صادق", "Transliteration": "Sadiq", "Meaning": "Truthful", "Example": "إِنَّٱللَّهَ مَعَ ٱلصَّٰدِقِينَ", "Translation": "Indeed, Allah is with the truthful"},
 {"Word (Arabic)": "مبارك", "Transliteration": "Mubarak", "Meaning": "Blessed", "Example": "وَجَعَلۡنَٰهُۥ مُبَٰرَكٖا", "Translation": "And We made him blessed"},
 {"Word (Arabic)": "طاهر", "Transliteration": "Taher", "Meaning": "Pure, Clean", "Example": "وَيُحِبُّ ٱلۡمُطَّهِّرِينَۥ", "Translation": "And He loves those who purify themselves"},
 {"Word (Arabic)": "مصير", "Transliteration": "Maseer", "Meaning": "Destination, Fate", "Example": "إِنَّ إِلَىٰ رَبِّكَ ٱلۡمَصِيرَ", "Translation": "Indeed, to your Lord is the final destination - Surah Al-Qiyamah, 75:30"},
 {"Word (Arabic)": "عالم", "Transliteration": "Alim", "Meaning": "Knowledgeable, Scholar", "Example": "إِنَّ ٱللَّهَ عَلِيمٌۭ حَكِيمٌۭ", "Translation": "Indeed, Allah is All-Knowing, All-Wise"},
 {"Word (Arabic)": "قدوس", "Transliteration": "Quddus", "Meaning": "The Holy", "Example": " ٱلۡمَلِكُ ٱلۡقُدُّوسُ ٱلسَّلَٰمُ", "Translation": "The King, the Holy, the Peace"},
 {"Word (Arabic)": "مستقيم", "Transliteration": "Mustaqim", "Meaning": "Straight, Upright", "Example": "ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ", "Translation": "Guide us to the straight path"},
 {"Word (Arabic)": "جليل", "Transliteration": "Jalil", "Meaning": "Majestic", "Example": "ذُو ٱلۡجَلَٰلِ وَٱلۡإِكۡرَامِ", "Translation": "Possessor of Majesty and Honor"},
 {"Word (Arabic)": "فرح ", "Transliteration" : "Farah", "Meaning": "Happiness, Joy", "Example": "وَفَرِحَ بِنِعْمَتِهِۦ", "Translation": "And happy with His grace"},
 {"Word (Arabic)": "رؤية", "Transliteration": "Ru’yah", "Meaning": "Vision, Sight", "Example": "رَءَآهُۥ فِى رُؤْيَآتِهِۦ", "Translation": "He saw it in his vision"},
 {"Word (Arabic)": "ملك ", "Transliteration" : "Mulk", "Meaning": "Kingdom, Dominion", "Example": "تَبَٰرَكَ الَّذِى بِيَدِهِۦ ٱلۡمُلْكُ", "Translation": "Blessed is the One in whose hand is the dominion"},
 {"Word (Arabic)": "طريق", "Transliteration": "Tariq", "Meaning": "Path, Way", "Example": "وَأَنَّ هَٰذَا صِرَٰطِي مُسۡتَقِيمٗا", "Translation": "And that this is My straight path"},
 {"Word (Arabic)": "توبة", "Transliteration": "Tawbah", "Meaning": "Repentance", "Example": "وَهُوَ ٱلَّذِي يَقۡبَلُ ٱلتَّوۡبَةَ عَنۡ عِبَادِهِۦ", "Translation": "And He is the One who accepts repentance from His servants"},
 {"Word (Arabic)": "ظلم ", "Transliteration" : "Zulm", "Meaning": "Injustice", "Example": "وَمَا رَبُّكَ بِظَلَّٰمٍۢ لِّلۡعَبِيدِ", "Translation": "And your Lord is not unjust to the servants"},
 {"Word (Arabic)": "فرد ", "Transliteration" : "Fard", "Meaning": "Obligatory, Singular", "Example": "إِنَّۢ ٱللَّهَ جَعَلَكُمۡ فَرَائِضَ", "Translation": "Indeed, Allah has made for you obligations"},
 {"Word (Arabic)": "عصمة", "Transliteration": "Ismah", "Meaning": "Infallibility, Protection", "Example": "إِنَّهُۥۤ لَمَٰرِهُۥ فِى عِصْمَتِهِۦ", "Translation": "Indeed, he was in protection"},
 {"Word (Arabic)": "مجيد", "Transliteration": "Majid", "Meaning": "Glorious, Honorable", "Example": "إِنَّۢ رَبَّكُمۡ لَذُو مَجِيدٍۢ", "Translation": "Indeed, your Lord is full of glory"},
 {"Word (Arabic)": "قوي ", "Transliteration" : "Qawi", "Meaning": "Strong", "Example": "إِنَّ ٱللَّهَ قَوِيٌّۭ عَزِيزٌۭ", "Translation": "Indeed, Allah is Strong, Almighty"},
 {"Word (Arabic)": "دعا ", "Transliteration" : "Da’a", "Meaning": "To call, invoke", "Example": "دَعَوۡتُ رَبِّى لِيُحْشِرْنِى فِى جَنَّتِهِۦ", "Translation": "I called my Lord to gather me in His garden"},
 {"Word (Arabic)": "خيرات", "Transliteration": "Khairat", "Meaning": "Good deeds, Charity", "Example": "إِنَّ ٱللَّهَ بِغَفْرٍۢ مِنْهُ وَرَحْمَةٍۢ", "Translation": "Indeed, Allah is forgiving and merciful"},
 {"Word (Arabic)": "عبد ", "Transliteration" : "Abd", "Meaning": "Servant, Worshipper", "Example": "وَمَا خَلَقۡتُ ٱلۡجِنَّ وَٱلۡإِنسَ إِلَّا لِيَعۡبُدُونِ", "Translation": "And I did not create jinn and mankind except to worship Me"},
 {"Word (Arabic)": "سميع", "Transliteration": "Sami", "Meaning": "All-Hearing", "Example": "إِنَّ ٱللَّهَ سَمِيعٌۭ بِمَا يَفْعَلُونَ", "Translation": "Indeed, Allah is All-Hearing of what they do"},
 {"Word (Arabic)": "عظيم", "Transliteration": "Azim", "Meaning": "Great, Mighty", "Example": "إِنَّۢ رَبَّكُمْ لَذُو عَزِيزٍۢ", "Translation": "Indeed, your Lord is mighty"},
 {"Word (Arabic)": "شفاء", "Transliteration": "Shifa", "Meaning": "Healing, Cure", "Example": "وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ", "Translation": "And when I am ill, it is He who heals me"},
 {"Word (Arabic)": "عافية", "Transliteration": "Afiya", "Meaning": "Health, Well-being", "Example": "اللّهُمَّ بَارِكْ لِي فِي عَافِيَتِى", "Translation": "O Allah, bless me in my well-being"},
 {"Word (Arabic)": "عدالة", "Transliteration": "Adalah", "Meaning": "Justice, Fairness", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُم بِالۡعَدْلِ", "Translation": "Indeed, Allah commands you to act justly"},
 {"Word (Arabic)": "آية ", "Transliteration" : "Ayah", "Meaning": "Sign, Verse", "Example": "وَجَعَلْنَا فِيهَاۤ آيَٰتٍۢ وَفَجَّرْنَا", "Translation": "And We made in it signs and made it flow"},
 {"Word (Arabic)": "خالق", "Transliteration": "Khalik", "Meaning": "Creator", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلۡخَٰلِقُ", "Translation": "Indeed, Allah is the Creator"},
 {"Word (Arabic)": "تقوى", "Transliteration": "Taqwa", "Meaning": "Piety, God-fearing", "Example": "وَٱتَّقُواْ ٱللَّهَ لَعَلَّكُمْ تُرْحَمُونَ", "Translation": "And fear Allah so that you may receive mercy"},
 {"Word (Arabic)": "سلطان", "Transliteration": "Sultan", "Meaning": "Authority, Power", "Example": "إِنَّ ٱللَّهَ لَا يَظْلِمُ ٱحَدًۭا فِى سُلۡطَٰنِهِۦ", "Translation": "Indeed, Allah does not wrong anyone in His dominion"},
 {"Word (Arabic)": "حمد ", "Transliteration" : "Hamd", "Meaning": "Praise", "Example": "ٱلۡحَمْدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ", "Translation": "Praise be to Allah, Lord of the worlds"},
 {"Word (Arabic)": "قريب", "Transliteration": "Qareeb", "Meaning": "Near, Close", "Example": "إِنَّۢ رَبَّكُمْ لَقَرِيبٌۭ", "Translation": "Indeed, your Lord is near"},
 {"Word (Arabic)": "جميل", "Transliteration": "Jameel", "Meaning": "Beautiful", "Example": "إِنَّۢ ٱللَّهَ جَمِيلٌۭ يُحِبُّ ٱلۡجَمَٰلَ", "Translation": "Indeed, Allah is Beautiful and loves beauty"},
 {"Word (Arabic)": "شمس ", "Transliteration" : "Shams", "Meaning": "Sun", "Example": "وَجَعَلْنَا ٱلشَّمْسَ سِرَاجًا وَهَّاجًۭا", "Translation": "And We made the sun a shining lamp"},
 {"Word (Arabic)": "عزيز", "Transliteration": "Aziz", "Meaning": "Mighty, Strong", "Example": "إِنَّٱللَّهَ عَزِيزٌۭ حَكِيمٌۭ", "Translation": "Indeed, Allah is Almighty, Wise"},
 {"Word (Arabic)": "آيات", "Transliteration": "Ayat", "Meaning": "Signs, Verses", "Example": "إِنَّۢ فِى ذَٰلِكَ لَآيَٰتٍۢ لِّلۡمُؤْمِنِينَ", "Translation": "Indeed, in that are signs for the believers"},
 {"Word (Arabic)": "خلق ", "Transliteration" : "Khalq", "Meaning": "Creation", "Example": "إِنَّ اللَّهَ خَلَقَ السَّمَٰوَٰتِ وَالْأَرْضَ فِي سِتَّةِ أَيَّامٍ", "Translation": "Indeed, Allah created the heavens and the earth in six days"},
 {"Word (Arabic)": "سمع ", "Transliteration" : "Sama'a", "Meaning": "Hearing", "Example": "إِنَّ اللَّهَ سَمِيعٌ عَلِيمٌ", "Translation": "Indeed, Allah is Hearing and Knowing"},
 {"Word (Arabic)": "بصر ", "Transliteration" : "Basar", "Meaning": "Sight", "Example": "إِنَّ اللَّهَ بَصِيرٌ بِمَا تَعْمَلُونَ", "Translation": "Indeed, Allah is All-Seeing of what you do"},
 {"Word (Arabic)": "عبادة", "Transliteration": "Ibadah", "Meaning": "Worship", "Example": "وَمَآ خَلَقْتُ الْجِنَّ وَالإِنسَ إِلَّا لِيَعْبُدُونِ", "Translation": "And I did not create the jinn and mankind except to worship Me"},
 {"Word (Arabic)": "فقر ", "Transliteration" : "Faqr", "Meaning": "Poverty", "Example": "إِنَّمَا الصَّدَقَٰتُ لِلۡفُقَرَاءِ وَٱلۡمَسَٰكِينِ", "Translation": "Indeed, the alms are for the poor and the needy - Surah At-Tawbah, 9:60"},
 {"Word (Arabic)": "غني ", "Transliteration" : "Ghani", "Meaning": "Rich, Self-sufficient", "Example": "إِنَّ اللَّهَ غَنِيٌّۭ حَمِيدٌ", "Translation": "Indeed, Allah is Self-Sufficient, Praiseworthy"},
 {"Word (Arabic)": "حج" , "Transliteration": "Hajj", "Meaning": "Pilgrimage", "Example": "وَأَذِّنْ فِي النَّاسِ بِالْحَجِّ يَأْتُوكَ رِجَالًا", "Translation": "And proclaim to the people the Hajj"},
 {"Word (Arabic)": "رزق ", "Transliteration" : "Rizq", "Meaning": "Provision, Sustenance", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلرَّزَّاقُ ذُو ٱلۡقُوَّةِ ٱلۡمَتِينُ", "Translation": "Indeed, Allah is the Provider, the firm possessor of strength"},
 {"Word (Arabic)": "حسن ", "Transliteration" : "Husn", "Meaning": "Goodness, Excellence", "Example": "إِنَّمَآ يُؤْمِنُونَ بِالْحَسَنَاتِ وَالْمَعْرُوفِ", "Translation": "Indeed, they only believe in goodness and what is right - Surah Al-Baqarah, 2:177"},
 {"Word (Arabic)": "بشرى", "Transliteration": "Bushra", "Meaning": "Good Tidings", "Example": "فَبَشِّرْهُم بِجَنَّةٍ تَجْرِي مِن تَحْتِهَا", "Translation": "So give them glad tidings of a garden beneath which rivers flow"},
 {"Word (Arabic)": "دعوة", "Transliteration": "Dawah", "Meaning": "Call, Invitation", "Example": "وَادْعُوۡا۟ إِلَىٰ رَبِّكِ", "Translation": "And call to your Lord"},
 {"Word (Arabic)": "نعيم", "Transliteration": "Na’im", "Meaning": "Bliss, Comfort", "Example": "إِنَّ أَهْلَ ٱلْجَنَّةِ فِى نَعِيمٍۢ", "Translation": "Indeed, the people of Paradise are in bliss"},
 {"Word (Arabic)": "لطف ", "Transliteration" : "Lutf", "Meaning": "Kindness, Gentleness", "Example": "وَكَانَ اللَّٰهُ لَطِيفًۭا بِعِبَادِهِۦ", "Translation": "And Allah is gentle with His servants - Surah Ash-Shura, 42:19"},
 {"Word (Arabic)": "عفو ", "Transliteration" : "Afw", "Meaning": "Forgiveness", "Example": "إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌ", "Translation": "Indeed, Allah is Forgiving and Merciful"},
 {"Word (Arabic)": "هداية", "Transliteration": "Hidayah", "Meaning": "Guidance", "Example": "إِنَّ عَلَيْنَا لِلْهُدَىٰ", "Translation": "Indeed, upon Us is guidance"},
 {"Word (Arabic)": "أمة ", "Transliteration" : "Ummah", "Meaning": "Nation, Community", "Example": "إِنَّ هَٰذِهِۦٓ أُمَّتُكُمْ أُمَّةًۭ وَٰحِدَةًۭ", "Translation": "Indeed, this is your nation, one nation"},
 {"Word (Arabic)": "صديق", "Transliteration": "Siddiq", "Meaning": "Truthful, Companion", "Example": "إِنَّ ٱللَّهَ مَعَ ٱلۡصَّٰدِقِينَ", "Translation": "Indeed, Allah is with the truthful"},
 {"Word (Arabic)": "موت ", "Transliteration" : "Mawt", "Meaning": "Death", "Example": "وَلَا تَقُولُوا۟ لِمَن يُقْتَلُ فِى سَبِيلِ ٱللَّهِ أَمْوَٰتٌۭ", "Translation": "And do not say of those who are killed in the way of Allah that they are dead"},
 {"Word (Arabic)": "نصر ", "Transliteration" : "Nasr", "Meaning": "Victory, Help", "Example": "إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلۡفَتْحُ", "Translation": "When the victory of Allah has come and the conquest"},
 {"Word (Arabic)": "علمي", "Transliteration": "Ilmi", "Meaning": "My Knowledge", "Example": "قَالَ رَبُّكَمْ يَعْلَمُ مَا فِى السَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ", "Translation": "Your Lord knows what is in the heavens and what is on the earth"},
 {"Word (Arabic)": "نوايا", "Transliteration": "Nawaya", "Meaning": "Intention", "Example": "إِنَّمَآ ٱلْأَعْمَٰلُ بِالنِّيَّاتِ", "Translation": "Indeed, actions are by intentions"},
 {"Word (Arabic)": "حب" , "Transliteration": "Hubb", "Meaning": "Love", "Example": "وَٱلَّذِينَ ءَامَنُوا۟ أَشَدُّ حُبًّۭا لِّي", "Translation": "And those who believe are stronger in love for Him"},
 {"Word (Arabic)": "عزة ", "Transliteration" : "Izzah", "Meaning": "Honor, Glory", "Example": "وَلِلَّهِ ٱلۡعِزَّةُ جَمِيعًا", "Translation": "And to Allah belongs all honor"},
 {"Word (Arabic)": "حياة", "Transliteration": "Hayah", "Meaning": "Life", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلۡحَىُّۖ", "Translation": "Indeed, Allah is the Ever-Living"},
 {"Word (Arabic)": "نار ", "Transliteration" : "Nar", "Meaning": "Fire", "Example": "إِنَّ جَهَنَّمَ لَتُحْشَرُ بِهَا الْكَافِرُونَ", "Translation": "Indeed, Hell is a fire that will burn them"},
 {"Word (Arabic)": "رحيم", "Transliteration": "Rahim", "Meaning": "Merciful", "Example": "إِنَّ اللَّهَ رَحِيمٌۭ بِالۡعِبَادِ", "Translation": "Indeed, Allah is Merciful to His servants"},
 {"Word (Arabic)": "غفور", "Transliteration": "Ghafur", "Meaning": "Forgiving", "Example": "إِنَّ رَبَّكَ غَفُورٌۭ رَّحِيمٌ", "Translation": "Indeed, your Lord is Forgiving and Merciful"},
 {"Word (Arabic)": "قوم ", "Transliteration" : "Qaum", "Meaning": "People, Nation", "Example": "وَمَآ أَرْسَلْنَٰكَ إِلَّا كَٰفَّةًۭ لِّلنَّاسِ", "Translation": "And We have not sent you except to all mankind"},
 {"Word (Arabic)": "دنيا", "Transliteration": "Dunya", "Meaning": "Worldly life", "Example": "تُحِبُّونَ ٱلۡحَيَوٰةَ ٱلدُّنْيَا", "Translation": "You love the life of this world"},
 {"Word (Arabic)": "آخرة", "Transliteration": "Akhira", "Meaning": "Hereafter", "Example": "وَٱلۡبَٰتِلَٰتِ", "Translation": "And the Hereafter is better and everlasting"},
 {"Word (Arabic)": "كتاب", "Transliteration": "Kitab", "Meaning": "Book", "Example": "إِنَّا أَنزَلْنَا عَلَيْكَ الْكِتَٰبَ بِالْحَقِّ", "Translation": "Indeed, We have sent down to you the Book in truth"},
 {"Word (Arabic)": "كافر", "Transliteration": "Kafir", "Meaning": "Disbeliever", "Example": "إِنَّ الَّذِينَ كَفَرُوا۟ وَجَحَدُوا۟ بِالۡعَادَٰتِ", "Translation": "Indeed, those who disbelieve and reject the Signs"},
 {"Word (Arabic)": "فعل ", "Transliteration" : "Fi’l", "Meaning": "Action", "Example": "وَفَعَلُوا۟ مَا فَعَلُوا۟", "Translation": "And they did what they did"},
 {"Word (Arabic)": "مغنم", "Transliteration": "Maghnam", "Meaning": "Gain, Spoil", "Example": "وَفَاءًۭ مِّنَ ٱللَّهِ وَرَحْمَةًۭ", "Translation": "A gain from Allah and a mercy"},
 {"Word (Arabic)": "مفتاح", "Transliteration": "Miftah", "Meaning": "Key", "Example": "وَعِندَهُۥ مَفَاتِحُ ٱلۡغَيۡبِ", "Translation": "And with Him are the keys of the unseen"},
 {"Word (Arabic)": "أمر ", "Transliteration" : "Amr", "Meaning": "Command, Matter", "Example": "إِنَّمَآ أَمْرُهُۥٓ إِذَآ أَرَادَ", "Translation": "Indeed, His command is when He intends"},
 {"Word (Arabic)": "مقام", "Transliteration": "Maqam", "Meaning": "Station, Position", "Example": "وَإِنَّهُۥ لَفِى مَقَامٍۢ كَرِيمٍۢ", "Translation": "And indeed, he is in a noble position"},
 {"Word (Arabic)": "بر" , "Transliteration": "Birr", "Meaning": "Righteousness", "Example": "وَبِرًّا بِوَالِدَيْهِا", "Translation": "And [I am] dutiful to my parents - Surah Maryam, 19:14"},
 {"Word (Arabic)": "فكر ", "Transliteration" : "Fikr", "Meaning": "Thought, Reflection", "Example": "وَفَكَرُوا۟ فِىٓ أَمْرِهِۦۖ", "Translation": "And they reflected on their matter"},
 {"Word (Arabic)": "هدية", "Transliteration": "Hadiyah", "Meaning": "Gift, Offering", "Example": "وَمَآ أَتَىٰكُم مِّنْ هَدِيَّةٍۢ", "Translation": "And whatever gift has come to you"},
 {"Word (Arabic)": "مائدة", "Transliteration": "Ma’idah", "Meaning": "Table, Feast", "Example": "ٱللَّهُمَّ ٱنْزِلۡ عَلَيۡنَا مَآئِدَةًۭ مِّنَ ٱلسَّمَآءِ", "Translation": "O Allah, send down to us a table spread with food from the heavens"},
 {"Word (Arabic)": "ضيافة", "Transliteration": "Diyafah", "Meaning": "Hospitality", "Example": "هَلْ أَتَىٰكَ حَدِيثُ ضَيْفِ إِبْرَٰهِيمَ", "Translation": "Has the story reached you of the guests of Abraham?"},
 {"Word (Arabic)": "محراب", "Transliteration": "Mihrab", "Meaning": "Sanctuary, Niche", "Example": "وَدَخَلَ الْمِحْرَابَ فَصَلَّىٰ", "Translation": "And he entered the sanctuary and prayed"},
 {"Word (Arabic)": "سعي ", "Transliteration" : "Sa’y", "Meaning": "Effort", "Example": "إِنَّ سَعْيَكُمْ لَشَتَّىٰ", "Translation": "Indeed, your efforts are diverse"},
 {"Word (Arabic)": "إيمان", "Transliteration": "Iman", "Meaning": "Faith, Belief", "Example": "إِنَّمَآ أَمَٰنَكُمْ إِذَآ آمَنُوا۟", "Translation": "Indeed, the true believers are those who believe in Allah"},
 {"Word (Arabic)": "حكمة", "Transliteration": "Hikmah", "Meaning": "Wisdom", "Example": "يُؤْتِى ٱلْحِكْمَةَ مَن يَشَآءُ", "Translation": "He gives wisdom to whom He wills"},
 {"Word (Arabic)": "غنى ", "Transliteration": "Ghina", "Meaning": "Wealth, Self-sufficiency", "Example": "إِنَّ ٱللَّهَ غَنيٌّۭ حَمِيدٌ", "Translation": "Indeed, Allah is Free of need, Worthy of praise"},
 {"Word (Arabic)": "صبر ", "Transliteration": "Sabr", "Meaning": "Patience", "Example": "وَصَابِرِينَ وَصَابِرَٰتٍۢ", "Translation": "And the patient men and the patient women"},
 {"Word (Arabic)": "رغبة", "Transliteration": "Raghbah", "Meaning": "Desire, Wish", "Example": "وَفَجَّرْنَا ٱلۡأَرۡضَ عُيُونًۭا فَٱلۡتَقَى ٱلۡمَآءُ عَلَىٰٓ أَمۡرٍۢ قَدَرٍۢ", "Translation": "And We caused the earth to gush forth with springs, so the waters met for a matter already predestined"},
 {"Word (Arabic)": "ماء ", "Transliteration" : "Ma’a", "Meaning": "Water", "Example": "وَجَعَلْنَا مِنَ ٱلۡمَاءِ كُلَّ شَىْءٍۢ حَىٍّ", "Translation": "And We made from water every living thing"},
 {"Word (Arabic)": "نعم ", "Transliteration": "Na’am", "Meaning": "Blessing, Favor", "Example": "وَإِن تَعُدُّوا۟ نِعْمَتَ ٱللَّهِ لَا تُحۡصُوهَا", "Translation": "And if you count the favors of Allah, you will not be able to number them"},
 {"Word (Arabic)": "طاعة", "Transliteration": "Ta’ah", "Meaning": "Obedience", "Example": "وَطَاعَتُهُۥ فِى دِينِهِۦۚ", "Translation": "And His obedience in His religion"},
 {"Word (Arabic)": "كلمة", "Transliteration": "Kalima", "Meaning": "Word, Statement", "Example": "وَقُلۡنَا لَهُۥٓ كَلِمَةًۭۚ", "Translation": "And We gave him a word of truth and a word of life - Surah Al-An'am, 6:92"},
 {"Word (Arabic)": "دين ", "Transliteration" : "Din", "Meaning": "Religion, Way of life", "Example": "إِنَّ ٱلدِّينَ عِندَ ٱللَّهِ ٱلۡإِسْلَٰمُ", "Translation": "Indeed, the religion in the sight of Allah is Islam"},
 {"Word (Arabic)": "سر" , "Transliteration": "Sirr", "Meaning": "Secret", "Example": "قُلْ لِّذِينَ كَفَرُوا۟ إِن كَانَتْ فِى قُلُوبِهِۦٓمْ", "Translation": "Say to those who disbelieve, if they believe in what is hidden in their hearts"},
 {"Word (Arabic)": "مؤمنون", "Transliteration": "Mu’minun", "Meaning": "Believers", "Example": "إِنَّ ٱلۡمُؤْمِنِينَ وَٱلۡمُؤْمِنَٰتِ", "Translation": "Indeed, the believing men and believing women"},
 {"Word (Arabic)": "حلال", "Transliteration": "Halal", "Meaning": "Permissible", "Example": "وَأَحَلَّ اللَّهُ ٱلۡبَيِّ", "Translation": "And Allah has made lawful the sale"},
 {"Word (Arabic)": "حرام", "Transliteration": "Haram", "Meaning": "Forbidden", "Example": "وَٱلۡخُمُرَ وَٱلْمَيْسِرَ حَرَّمَۚ", "Translation": "And intoxicants and gambling are forbidden"},
 {"Word (Arabic)": "صلاة", "Transliteration": "Salah", "Meaning": "Prayer", "Example": "إِنَّمَآ أُمِرُوا۟ أَنْ يُصَلُّوا۟", "Translation": "Indeed, they were commanded to pray"},
 {"Word (Arabic)": "زكاة", "Transliteration": "Zakah", "Meaning": "Almsgiving", "Example": "وَأَقِيمُوا۟ ٱلصَّلَاةَ وَآتُوا۟ الزَّكَاةَ", "Translation": "And establish prayer and give zakah"},
 {"Word (Arabic)": "الحق", "Transliteration": "Al-Haq", "Meaning": "The Truth", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلْحَقُّۚ", "Translation": "Indeed, Allah is the Truth"},
 {"Word (Arabic)": "قدرة", "Transliteration": "Qudrah", "Meaning": "Power", "Example": "وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ", "Translation": "And Allah is capable of all things"},
 {"Word (Arabic)": "رحمة", "Transliteration": "Rahmah", "Meaning": "Mercy", "Example": "وَرَحْمَتُهُۥ وَرَحِيمٌۭ", "Translation": "His mercy is vast and all-encompassing"},
 {"Word (Arabic)": "عذاب", "Transliteration": "Adhab", "Meaning": "Punishment", "Example": "فَذُوقُوا۟ بِمَا كُنتُمْ تَكْسِبُونَ", "Translation": "So taste the punishment for what you earned"},
 {"Word (Arabic)": "إجابة", "Transliteration": "Ijabah", "Meaning": "Response, Answer", "Example": "فَٱسۡتَجَابَ لَهُمۡ رَبُّهُمۡ", "Translation": "So their Lord responded to them"},
 {"Word (Arabic)": "رسالة", "Transliteration": "Risalah", "Meaning": "Message", "Example": "يُحِبُّونَ أَنْ يَحْمِلُوا۟ كُلَّ جُرْمِهِمْ فِىٰ يَوْمِ ٱلۡقِيَـٰمَةِۚ وَمِنْ أَجْلِهِۦٰٓ كُتِبَ عَلَيْهِمْ أَنَّهُۥۤ أَحْسَنَ رَسَـٰلَتِهِۦٓ", "Translation": "They love to carry their sin on the Day of Judgment, and for that reason, it was written for them that they would bear their message - Surah Al-Ma’idah, 5:67"},
 {"Word (Arabic)": "فتنة", "Transliteration": "Fitnah", "Meaning": "Trial, Temptation", "Example": "وَٱلۡفِتْنَةُ أَشَدُّ مِنَ ٱلۡقَتْلِ", "Translation": "And trial is worse than killing"},
 {"Word (Arabic)": "عقل ", "Transliteration" : "Aql", "Meaning": "Mind, Intellect", "Example": "إِنَّ فِى ذَٰلِكَ لَآيَٰتٍ لِّي أُو۟لِى ٱلْأَلْبَابِ", "Translation": "Indeed, in that are signs for those of understanding"},
 {"Word (Arabic)": "أمانة", "Transliteration": "Amanah", "Meaning": "Trust, Deposit", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُمْ أَنْ تُؤَدُّوا۟ ٱلْأَمَٰنَٰتِ", "Translation": "Indeed, Allah commands you to return trusts"},
 {"Word (Arabic)": "بركة", "Transliteration": "Barakah", "Meaning": "Blessing, Increase", "Example": "فَٱلَّذِينَ يَحْتَسُونَ ٱلْمَاءَ لَهُمْ فِيهِ بَرَكَهٌۭ", "Translation": "Those who drink the water will find blessings in it"},
 {"Word (Arabic)": "هدى ", "Transliteration" : "Hudah", "Meaning": "Guidance", "Example": "وَإِنَّكَ لَتَهْدِىٓ إِلَىٰ صِرَٰطٍ مُسْتَقِيمٍ", "Translation": "And indeed, you guide to a straight path"},
 {"Word (Arabic)": "شهادة", "Transliteration": "Shahadah", "Meaning": "Testimony, Witness", "Example": "شَهِدَ اللَّهُ أَنَّهُۥ لَآ إِلٰهَ إِلَّا هُوَ", "Translation": "Allah bears witness that there is no god but Him"},
 {"Word (Arabic)": "خوف ", "Transliteration" : "Khauf", "Meaning": "Fear", "Example": "وَقُلْ رَبِّ أَعُوذُ بِكَ مِنْ خَوْفٍۢ", "Translation": "And say, 'My Lord, I seek refuge in You from fear'"},
 {"Word (Arabic)": "كفار", "Transliteration": "Kuffar", "Meaning": "Disbelievers", "Example": "إِنَّ ٱلۡمُكَذِّبِينَ بِالۡمِلَّةِ ٱلۡكُفَّارِ", "Translation": "Indeed, the disbelievers are the ones who deny the truth"},
 {"Word (Arabic)": "سلامة", "Transliteration": "Salamah", "Meaning": "Safety, Health", "Example": "فَسَلِّمُوا۟ عَلَيْهِمْ بِسَلاَمٍۢ", "Translation": "Then greet them with a greeting of peace"},
 {"Word (Arabic)": "عدل ", "Transliteration": "Adl", "Meaning": "Justice, Fairness", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُمْ بِالْعَدْلِ وَالْإِحْسَٰنِ", "Translation": "Indeed, Allah commands justice and the doing of good"},
 {"Word (Arabic)": "نور ", "Transliteration" : "Nur", "Meaning": "Light", "Example": "ٱللَّهُ وَلِيُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَىٰ النُّورِ", "Translation": "Allah is the protector of those who believe, He brings them out of darkness into the light"},
 {"Word (Arabic)": "غضب ", "Transliteration" : "Ghadab", "Meaning": "Anger", "Example": "وَٱللَّهُ غَضِبَ عَلَيْهِمْ", "Translation": "And Allah became angry with them"},
 {"Word (Arabic)": "قلب ", "Transliteration" : "Qalb", "Meaning": "Heart", "Example": "فِي قُلُوبِهِمْ مَرَضٌۭ", "Translation": "In their hearts is a disease"},
 {"Word (Arabic)": "جنة ", "Transliteration" : "Jannah", "Meaning": "Paradise, Garden", "Example": "إِنَّ ٱلۡمُتَّقِينَ فِى جَنَّٰتٍ وَنَعِيمٍۢ", "Translation": "Indeed, the righteous will be in gardens and delight"},
 {"Word (Arabic)": "كريم", "Transliteration": "Karim", "Meaning": "Generous, Noble", "Example": "إِنَّ رَبَّكُمْ لَذُو فَضْلٍۢ عَلَىٰ", "Translation": "Indeed, your Lord is full of bounty"},
 {"Word (Arabic)": "عدو ", "Transliteration" : "Aduww", "Meaning": "Enemy", "Example": "إِنَّ عَدُوَّكُمُ الشَّيْطَٰنُ", "Translation": "Indeed, your enemy is the devil"},
 {"Word (Arabic)": "صمت ", "Transliteration" : "Samt", "Meaning": "Silence", "Example": "وَمَنۢ صَمَتَ نَجَا", "Translation": "Whoever remains silent is safe"},
 {"Word (Arabic)": "شكر ًا", "Transliteration": "Shukran", "Meaning": "Thank you", "Example": "قُلْ شُكْرًا لِّلَّهِ", "Translation": "Say, 'Thank you to Allah'"},
 {"Word (Arabic)": "قوة ", "Transliteration" : "Quwwah", "Meaning": "Strength", "Example": "وَأَعِزَّنِى بِقُوَّتِهِۦ", "Translation": "And grant me strength through Your power"},
 {"Word (Arabic)": "صراع", "Transliteration": "Sira’a", "Meaning": "Struggle", "Example": "وَمَآ كُنتُمُ فِى ٱلۡصِّرَاعِ", "Translation": "And you were not in the struggle"},
 {"Word (Arabic)": "سورة", "Transliteration": "Surah", "Meaning": "Chapter, Surah"},
 {"Word (Arabic)": "قضاء", "Transliteration": "Qada’a", "Meaning": "Decree", "Example": "قَدْ قَضَتْ قَضَاءًۭ وَإِنَّ اللَّٰهِ قَٰضٍۢ", "Translation": "He decreed it as a judgment, and indeed, Allah is the best of judges"},
 {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "فَٱغْفِرْ لِىٰ إِنَّكَ أَنتَ ٱلْغَفُورُ", "Translation": "So forgive me, indeed, You are the Forgiving"},
{"Word (Arabic)": "رحمن", "Transliteration": "Rahman", "Meaning": "Most Merciful", "Example": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ", "Translation": "In the name of Allah, the Most Merciful, the Most Compassionate)"
    },
  {"Word (Arabic)": "محنة", "Transliteration": "Mihnah", "Meaning": "Trial", "Example": "وَلَنَبْلُوَنَّكُمْ بِشَيْءٍۢ مِّنَ ٱلْخَوْفِ وَٱلْجُوعِ وَنَقْصٍۢ مِّنَ ٱلْأَمْوَٰلِ وَٱلْأَنفُسِ وَٱلثَّمَرَٰتِ ۚ وَبَشِّرِ ٱلصَّٰبِرِينَ", "Translation": "And We will surely test you with something of fear and hunger and a loss of wealth and lives and fruits. But give good tidings to the patient - Surah Al-Baqarah, 2:155"},
    {
        "Word (Arabic)": "قدير",
        "Transliteration": "Qadeer",
        "Meaning": "All-Powerful",
        "Example": "إِنَّ اللَّهَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ", "Translation": "Indeed, Allah is All-Powerful over everything"
    },
    {
        "Word (Arabic)": "عليم",
        "Transliteration": "Aleem",
        "Meaning": "All-Knowing",
        "Example": "إِنَّ اللَّهَ كَانَ عَلِيمًا حَكِيمًا", "Translation": "Indeed, Allah is All-Knowing, All-Wise"
    },
    {
        "Word (Arabic)": "توحيد",
        "Transliteration": "Tawheed",
        "Meaning": "Oneness (of Allah)",
        "Example": "إِنَّمَآ إِلَٰهُكُمْ إِلَٰهٌ وَٰحِدٌۢ لَّآ إِلَٰهَ إِلَّا هُوَ الرَّحْمَٰنُ الرَّحِيمُ", "Translation": "Your God is but one God; there is no deity except Him, the Most Gracious, the Most Merciful - Surah Al-Baqarah, 2:163"
    },
    {
        "Word (Arabic)": "شرك",
        "Transliteration": "Shirk",
        "Meaning": "Associating partners with Allah",
        "Example": "إِنَّ ٱللَّهَ لَا يَغْفِرُ أَن يُشْرَكَ بِهِۦ وَيَغْفِرُ مَا دُونَ ذَٰلِكَ لِمَن يَشَآءُ ۚ وَمَن يُشْرِكْ بِٱللَّهِ فَقَدْ ضَلَّ ضَلَٰلًۭا بَعِيدًۭا", "Translation": "Indeed, Allah does not forgive associating partners with Him, but He forgives what is less than that for whom He wills. And whoever associates partners with Allah has certainly gone far astray - Surah An-Nisa, 4:116"
    },
    {
        "Word (Arabic)": "صيام",
        "Transliteration": "Siyam",
        "Meaning": "Fasting",
        "Example": "يَا أَيُّهَا الَّذِينَ آمَنُوا كُتِبَ عَلَيْكُمُ الصِّيَامُ", "Translation": "O you who believe, fasting is prescribed for you"
    },
    {
        "Word (Arabic)": "صدق",
        "Transliteration": "Sadaq",
        "Meaning": "Truthfulness",
        "Example": "وَكُونُوا مَعَ الصَّادِقِينَ", "Translation": "And be with the truthful"
    },
    {
        "Word (Arabic)": "إحسان",
        "Transliteration": "Ihsan",
        "Meaning": "Excellence",
        "Example": "إِنَّ اللَّهَ يُحِبُّ الْمُحْسِنِينَ", "Translation": "Indeed, Allah loves those who strive for excellence"
    },
    {
        "Word (Arabic)": "رسول",
        "Transliteration": "Rasool",
        "Meaning": "Messenger",
        "Example": "وَإِذْ بَعَثَ اللَّهُ نَبِيًّا رَسُولًا", "Translation": "And when Allah sends forth a prophet as a messenger"
    }
]


# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(quranic_words)

# Search bar to filter words
search_query = st.text_input("Search for a Quranic word (Arabic or Meaning):", "")

# Filter words based on the search query
if search_query:
    df_filtered = df[
        df['Word (Arabic)'].str.contains(search_query, case=False) |
        df['Meaning'].str.contains(search_query, case=False)
    ].drop_duplicates()
else:
    df_filtered = df

# Display the title "Quranic Words" at the top
st.markdown("""
    <h1 style='text-align: center; color: #2C6E49; font-family: "Georgia", serif; font-size: 40px; margin-top: 50px;'>Quranic Words</h1>
    <h3 style='text-align: center; color: #2C6E49; font-family: "Georgia", sans-serif; font-size: 22px;'>- Commonly used words in the Quran -</h3>
""", unsafe_allow_html=True)

# Display the words for the current page with continuous numbering
for idx, (index, row) in enumerate(df_filtered.iterrows(), 1):
    # Arabic word in green color with a number in front
    st.markdown(f"<h2 style='color: #2C6E49;'>{idx}. {row['Word (Arabic)']}</h2>", unsafe_allow_html=True)
    st.write(f"**Transliteration**: {row['Transliteration']}")
    st.write(f"**Meaning**: {row['Meaning']}")
# arabic example bigger
    st.markdown(f"**Example**: <h4 style='font-size: 24px; color: #000; text-align: left;'>{row['Example']}</h4>", unsafe_allow_html=True)     
 #  st.write(f"**Example**: {row['Example']}")
    st.write(f"**Translation**: {row['Translation']}")
    st.write("---")

# Display 'Home' button only after a search query is entered
if search_query:
    st.markdown(f"""
        <div style="position: absolute; top: 70px; right: 20px;">
            <form action="/" method="get">
                <button type="submit" style="
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 12px;
                    padding: 10px 20px;
                    font-size: 16px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    cursor: pointer;">
                    Home
                </button>
            </form>
        </div>
    """, unsafe_allow_html=True)

# Display attribution at the bottom of the page
st.markdown("""
    <div style="position: fixed; bottom: 10px; left: 10px; font-size: 12px; color: #888888; font-family: 'Helvetica', sans-serif;">
        Made by Asia Mehasi <br> If you find any mistakes email me on amehasi@gmail.com.
    </div>
""", unsafe_allow_html=True)

# Custom CSS for improved styling
st.markdown(""" 
    <style>
    body {
        background-color: #F4F6F2;
        font-family: 'Helvetica', sans-serif;
    }

    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #45a049;
    }

    .stTextInput>div>input {
        font-size: 18px;
        padding: 10px;
        border-radius: 12px;
        border: 1px solid #ddd;
        width: 50%;
        line-height: 1.5em;
        margin: 0 auto;
    }

    .stMarkdown h1 {
        color: #2C6E49;
        font-family: 'Georgia', serif;
    }

    .stMarkdown h3 {
        color: #4C9D5A;
        font-family: 'Helvetica', sans-serif;
    }

    .stMarkdown ul {
        list-style: none;
        padding: 0;
    }

    .stMarkdown li {
        margin-bottom: 10px;
        font-size: 18px;
    }

    .stTextInput div {
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)
