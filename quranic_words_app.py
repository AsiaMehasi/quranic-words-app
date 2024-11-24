import streamlit as st
import pandas as pd

quranic_words = [
 {"Word (Arabic)": "و", "Transliteration": "Wa", "Meaning": "And", "Example": "وَٱلۡعَصۡرِ (By Time)"},
 {"Word (Arabic)": "في" , "Transliteration": "Fi", "Meaning": "In, Inside", "Example": "فِي ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِ (In the heavens and the earth)"},
 {"Word (Arabic)": "من" , "Transliteration": "Min", "Meaning": "From, Of", "Example": "مِنَ ٱلۡجِنَّةِ وَٱلنَّاسِ (From among the jinn and mankind)"},
 {"Word (Arabic)": "على ", "Transliteration" : "'Ala", "Meaning": "On, Upon", "Example": "وَعَلَىٰ ٱللَّهِ فَلۡيَتَوَكَّلِ ٱلۡمُؤۡمِنُونَ (And upon Allah let the believers rely)"},
 {"Word (Arabic)": "إلى ", "Transliteration" : "Ila", "Meaning": "To", "Example": "إِلَىٰ رَبِّهِمْ يَحْشُرُونَ (To their Lord, they will be gathered)"},
 {"Word (Arabic)": "عن" , "Transliteration": "An", "Meaning": "About, Concerning", "Example": "قُلۡ سَمِيعٌۭ بِمَا فِى ٱلۡقُلُوبِ (Say, He is the All-Hearing of what is in the hearts)"},
 {"Word (Arabic)": "رب" , "Transliteration": "Rabb", "Meaning": "Lord", "Example": "رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِ (The Lord of the heavens and the earth)"},
 {"Word (Arabic)": "سَلاَم", "Transliteration": "Salam", "Meaning": "Peace", "Example": "فَسَلَّمُوٓا۟ عَلَيْهِمْ بِسَلاَمٍۢ (Greet them with peace)"},
 {"Word (Arabic)": "توكل", "Transliteration": "Tawakkul", "Meaning": "Trust, Reliance", "Example": "وَعَلَىٰ رَبِّهِمۡ يَتَوَكَّلُونَ (And upon their Lord they rely)"},
 {"Word (Arabic)": "غفر ", "Transliteration" : "Ghufran", "Meaning": "Forgiveness", "Example": "فَٱغْفِرْ لِمَن فَسَقَ (So forgive those who transgress)"},
 {"Word (Arabic)": "قمر ", "Transliteration" : "Qamar", "Meaning": "Moon", "Example": "وَٱلْقَمَرِ إِذَا تَلَاهَا (And the moon when it follows it)"},
 {"Word (Arabic)": "نجوم", "Transliteration": "Nujum", "Meaning": "Stars", "Example": "وَٱلنَّجْمِ وَٱلشَّجَرِ (By the stars and the trees)"},
 {"Word (Arabic)": "سماء", "Transliteration": "Sama'", "Meaning": "Sky", "Example": "إِنَّ فِى سَمَٰوَٰتِهِۦ (Indeed in the heavens)"},
 {"Word (Arabic)": "أرض ", "Transliteration" : "Ard", "Meaning": "Earth", "Example": "وَفِى ٱلۡأَرۡضِ (And in the earth)"},
 {"Word (Arabic)": "جند ", "Transliteration" : "Jund", "Meaning": "Army", "Example": "فَجَعَلْنَا جُندًۭا مِنْهُ (And we made from it an army)"},
 {"Word (Arabic)": "إصبع", "Transliteration": "Isba'", "Meaning": "Finger", "Example": "وَفَطَرْنَا ٱلۡإِصۡبَعَ (And we formed the fingers)"},
 {"Word (Arabic)": "كف" , "Transliteration": "Kaff", "Meaning": "Palm of the hand", "Example": "وَفَٰكَفَّهُۥ (And He closed his hand)"},
 {"Word (Arabic)": "أذن ", "Transliteration" : "Udhun", "Meaning": "Ear", "Example": "وَمَآ أَذَٰنَ (And their ears did not listen)"},
 {"Word (Arabic)": "عين ", "Transliteration" : "Ayn", "Meaning": "Eye", "Example": "وَفَجَّرْنَا عُيُونًا (And We caused springs to gush forth)"},
 {"Word (Arabic)": "لسان", "Transliteration": "Lisan", "Meaning": "Tongue", "Example": "وَفَصَّلْنَا لَهُۥ الْمَسَٰءَ (And We have detailed for him the speech)"},
 {"Word (Arabic)": "يد" , "Transliteration": "Yad", "Meaning": "Hand", "Example": "وَجَعَلْنَا يَدَٰهُ قَبْضًا (And We made his hand close)"},
 {"Word (Arabic)": "نساء", "Transliteration": "Nisa", "Meaning": "Women", "Example": "وَٱلنِّسَآءَ (And the women)"},
 {"Word (Arabic)": "والدة", "Transliteration": "Walidah", "Meaning": "Mother", "Example": "فِيٓ بُيُوتِهِۦ (In their homes)"},
 {"Word (Arabic)": "منزل", "Transliteration": "Manzil", "Meaning": "Abode, Residence", "Example": "وَفِى سَٰفَتِهِۦ (And in the safe abode)"},
 {"Word (Arabic)": "باب ", "Transliteration" : "Bab", "Meaning": "Door", "Example": "إِنَّ ٱلۡبَابَ (Indeed, the door)"},
 {"Word (Arabic)": "قبة ", "Transliteration" : "Qubba", "Meaning": "Dome", "Example": "تَحْتَ قُبَّتِهِۦ (Under his dome)"},
 {"Word (Arabic)": "سقف ", "Transliteration" : "Saqf", "Meaning": "Roof", "Example": "فِى سَٰمِهِۦ (In his roof)"},
 {"Word (Arabic)": "شجرة", "Transliteration": "Shajarah", "Meaning": "Tree", "Example": "وَٱلۡشَجَرَ (And the tree)"},
 {"Word (Arabic)": "ريح ", "Transliteration" : "Rih", "Meaning": "Wind", "Example": "وَفَجَّرْنَا فِيهَا (And We caused in it the wind to blow)"},
 {"Word (Arabic)": "صوت ", "Transliteration" : "Sawt", "Meaning": "Voice, Sound", "Example": "فَٱسْمَعُوا۟ لَهُۥ (So listen to him)"},
 {"Word (Arabic)": "محنة", "Transliteration": "Mihnah", "Meaning": "Trial", "Example": "فَٱصْبِرُوا۟ عَلَىٰ مَا يَقُولُونَ (So be patient with what they say)"},
 {"Word (Arabic)": "رسول", "Transliteration": "Rasul", "Meaning": "Messenger", "Example": "وَٱلۡرَّسُولُ فِى أَيَّامٍۢ (And the Messenger is in the days)"},
 {"Word (Arabic)": "أمل ", "Transliteration" : "Amal", "Meaning": "Hope, Expectation", "Example": "وَأَمَّلُوا۟ فَجَنَّٰتِهِۦ (And they hoped for his gardens)"},
 {"Word (Arabic)": "رجاء", "Transliteration": "Raja'", "Meaning": "Hope", "Example": "إِنَّ رَجَٰءَكَ لِرَبِّكَ (Indeed, your hope is for your Lord)"},
 {"Word (Arabic)": "سوء ", "Transliteration" : "Su'", "Meaning": "Evil, Harm", "Example": "إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ (Indeed, Allah is Forgiving and Merciful)"},
 {"Word (Arabic)": "وقت ", "Transliteration" : "Waqt", "Meaning": "Time", "Example": "إِنَّ وَقْتَكُمْ فِى (Indeed, your time in)"},
 {"Word (Arabic)": "صوم ", "Transliteration" : "Sawm", "Meaning": "Fasting", "Example": "فَصُمْتُ وَرَبُّكُمْ أَحْسَنُ (So I fasted and your Lord is the best)"},
 {"Word (Arabic)": "قادر", "Transliteration": "Qadir", "Meaning": "Capable, Powerful", "Example": "إِنَّنِيۤۦ عَلَىٰ كُلِّ شَىۡءٍۢ قَدِيرٌۭ (Indeed, I am capable of all things)"},
 {"Word (Arabic)": "كفر ", "Transliteration" : "Kufr", "Meaning": "Disbelief", "Example": "وَمَآ أُتۡلِفُ كُفۡرَكُمْ (And do not destroy your disbelief)"},
 {"Word (Arabic)": "طهور", "Transliteration": "Tuhur", "Meaning": "Purity", "Example": "إِنَّمَآ أَنَاۤۡ طَهُورٌۭ (Indeed, I am pure)"},
 {"Word (Arabic)": "ذكر ", "Transliteration" : "Dhikr", "Meaning": "Remembrance", "Example": "إِنَّ اللَّهَ يَذۡكُرُهُۥۤ (Indeed, Allah remembers him)"},
 {"Word (Arabic)": "حق" , "Transliteration": "Haqq", "Meaning": "Truth, Right", "Example": "إِنَّۢ هَٰذَا لَهُوَ الْحَقُّ (Indeed, this is the truth)"},
 {"Word (Arabic)": "باطل", "Transliteration": "Batil", "Meaning": "Falsehood", "Example": "إِنَّمَآ الْبَاطِلُ يُذْهِبُهُۥۤ (Indeed, falsehood is removed)"},
 {"Word (Arabic)": "حقيقة", "Transliteration": "Haqiqah", "Meaning": "Reality, Truth", "Example": "إِنَّ حَقَّ ٱلۡمَرْءِ فِي (Indeed, the truth of a person in)"},
 {"Word (Arabic)": "شرف ", "Transliteration" : "Sharaf", "Meaning": "Honor, Dignity", "Example": "إِنَّ الشَّرَفَ لِعِبَادِهِۦ (Indeed, honor is for His servants)"},
 {"Word (Arabic)": "عبود", "Transliteration": "Abd", "Meaning": "Servant, Slave", "Example": "إِنَّنيۤۦ عَبْدٌۭ لِلَّهِ (Indeed, I am a servant of Allah)"},
 {"Word (Arabic)": "نداء", "Transliteration": "Nida", "Meaning": "Call, Cry", "Example": "وَإِذَا نَادَىٰ رَبُّهُۥۤ (And when his Lord called him)"},
 {"Word (Arabic)": "صادق", "Transliteration": "Sadiq", "Meaning": "Truthful", "Example": "إِنَّٱللَّهَ مَعَ ٱلصَّٰدِقِينَ (Indeed, Allah is with the truthful)"},
 {"Word (Arabic)": "مبارك", "Transliteration": "Mubarak", "Meaning": "Blessed", "Example": "وَجَعَلۡنَٰهُۥ مُبَٰرَكٖا (And We made him blessed)"},
 {"Word (Arabic)": "طاهر", "Transliteration": "Taher", "Meaning": "Pure, Clean", "Example": "فَٱلطَّٰهِرُ فَٱطْهَرْهُۥ (So purify him, purify him)"},
 {"Word (Arabic)": "مصير", "Transliteration": "Maseer", "Meaning": "Destination, Fate", "Example": "إِنَّ ٱلۡمَصِيرَ (Indeed, the destination)"},
 {"Word (Arabic)": "عالم", "Transliteration": "Alim", "Meaning": "Knowledgeable, Scholar", "Example": "إِنَّ ٱللَّهَ عَلِيمٌۭ حَكِيمٌۭ (Indeed, Allah is All-Knowing, All-Wise)"},
 {"Word (Arabic)": "قدوس", "Transliteration": "Quddus", "Meaning": "The Holy", "Example": "سُبْحَٰنَ رَبِّكَ رَبِّ ٱلْعِزَّةِ عَمَّا يَصِفُونَ (Glory be to Your Lord, the Lord of Honor, above what they describe)"},
 {"Word (Arabic)": "مستقيم", "Transliteration": "Mustaqim", "Meaning": "Straight, Upright", "Example": "ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ (Guide us to the straight path)"},
 {"Word (Arabic)": "جليل", "Transliteration": "Jalil", "Meaning": "Majestic", "Example": "فَٱلۡجَلِيلُ أَصْلِهِۦ (The Majestic origin)"},
 {"Word (Arabic)": "فرح ", "Transliteration" : "Farah", "Meaning": "Happiness, Joy", "Example": "وَفَرِحَ بِنِعْمَتِهِۦ (And happy with His grace)"},
 {"Word (Arabic)": "رؤية", "Transliteration": "Ru’yah", "Meaning": "Vision, Sight", "Example": "رَءَآهُۥ فِى رُؤْيَآتِهِۦ (He saw it in his vision)"},
 {"Word (Arabic)": "ملك ", "Transliteration" : "Mulk", "Meaning": "Kingdom, Dominion", "Example": "تَبَٰرَكَ الَّذِى بِيَدِهِۦ ٱلۡمُلْكُ (Blessed is the One in whose hand is the dominion)"},
 {"Word (Arabic)": "طريق", "Transliteration": "Tariq", "Meaning": "Path, Way", "Example": "إِنَّ ٱللَّهَ يَهْدِىٓ بِهِۦٰٓ (Indeed, Allah guides by it)"},
 {"Word (Arabic)": "توبة", "Transliteration": "Tawbah", "Meaning": "Repentance", "Example": "وَٱلۡمُحْسِنِينَ فَٱلۡمُجْتَٰهِدِينَ (And those who do good, striving in repentance)"},
 {"Word (Arabic)": "ظلم ", "Transliteration" : "Zulm", "Meaning": "Injustice", "Example": "وَمَا رَبُّكَ بِظَلَّٰمٍۢ لِّلۡعَبِيدِ (And your Lord is not unjust to the servants)"},
 {"Word (Arabic)": "فرد ", "Transliteration" : "Fard", "Meaning": "Obligatory, Singular", "Example": "إِنَّۢ ٱللَّهَ جَعَلَكُمۡ فَرَائِضَ (Indeed, Allah has made for you obligations)"},
 {"Word (Arabic)": "عصمة", "Transliteration": "Ismah", "Meaning": "Infallibility, Protection", "Example": "إِنَّهُۥۤ لَمَٰرِهُۥ فِى عِصْمَتِهِۦ (Indeed, he was in protection)"},
 {"Word (Arabic)": "مجيد", "Transliteration": "Majid", "Meaning": "Glorious, Honorable", "Example": "إِنَّۢ رَبَّكُمۡ لَذُو مَجِيدٍۢ (Indeed, your Lord is full of glory)"},
 {"Word (Arabic)": "قوي ", "Transliteration" : "Qawi", "Meaning": "Strong", "Example": "إِنَّ ٱللَّهَ قَوِيٌّۭ عَزِيزٌۭ (Indeed, Allah is Strong, Almighty)"},
 {"Word (Arabic)": "دعا ", "Transliteration" : "Da’a", "Meaning": "To call, invoke", "Example": "دَعَوۡتُ رَبِّى لِيُحْشِرْنِى فِى جَنَّتِهِۦ (I called my Lord to gather me in His garden)"},
 {"Word (Arabic)": "خيرات", "Transliteration": "Khairat", "Meaning": "Good deeds, Charity", "Example": "إِنَّ ٱللَّهَ بِغَفْرٍۢ مِنْهُ وَرَحْمَةٍۢ (Indeed, Allah is forgiving and merciful)"},
 {"Word (Arabic)": "عبد ", "Transliteration" : "Abd", "Meaning": "Servant, Worshipper", "Example": "إِنَّ ٱللَّهَ يُحِبُّ ٱلۡمُتَّقِينَ (Indeed, Allah loves those who are righteous)"},
 {"Word (Arabic)": "سميع", "Transliteration": "Samir", "Meaning": "All-Hearing", "Example": "إِنَّ ٱللَّهَ سَمِيعٌۭ بِمَا يَفْعَلُونَ (Indeed, Allah is All-Hearing of what they do)"},
 {"Word (Arabic)": "عظيم", "Transliteration": "Azim", "Meaning": "Great, Mighty", "Example": "إِنَّۢ رَبَّكُمْ لَذُو عَزِيزٍۢ (Indeed, your Lord is mighty)"},
 {"Word (Arabic)": "شفاء", "Transliteration": "Shifa", "Meaning": "Healing, Cure", "Example": "وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ (And when I am ill, it is He who heals me)"},
 {"Word (Arabic)": "عافية", "Transliteration": "Afiya", "Meaning": "Health, Well-being", "Example": "اللّهُمَّ بَارِكْ لِي فِي عَافِيَتِى (O Allah, bless me in my well-being)"},
 {"Word (Arabic)": "عدالة", "Transliteration": "Adalah", "Meaning": "Justice, Fairness", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُم بِالۡعَدْلِ (Indeed, Allah commands you to act justly)"},
 {"Word (Arabic)": "آية ", "Transliteration" : "Ayah", "Meaning": "Sign, Verse", "Example": "وَجَعَلْنَا فِيهَاۤ آيَٰتٍۢ وَفَجَّرْنَا (And We made in it signs and made it flow)"},
 {"Word (Arabic)": "خالق", "Transliteration": "Khalik", "Meaning": "Creator", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلۡخَٰلِقُ (Indeed, Allah is the Creator)"},
 {"Word (Arabic)": "تقوى", "Transliteration": "Taqwa", "Meaning": "Piety, God-fearing", "Example": "وَٱتَّقُواْ ٱللَّهَ لَعَلَّكُمْ تُرْحَمُونَ (And fear Allah so that you may receive mercy)"},
 {"Word (Arabic)": "سلطان", "Transliteration": "Sultan", "Meaning": "Authority, Power", "Example": "إِنَّ ٱللَّهَ لَا يَظْلِمُ ٱحَدًۭا فِى سُلۡطَٰنِهِۦ (Indeed, Allah does not wrong anyone in His dominion)"},
 {"Word (Arabic)": "حمد ", "Transliteration" : "Hamd", "Meaning": "Praise", "Example": "ٱلۡحَمْدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ (Praise be to Allah, Lord of the worlds)"},
 {"Word (Arabic)": "قريب", "Transliteration": "Qareeb", "Meaning": "Near, Close", "Example": "إِنَّۢ رَبَّكُمْ لَقَرِيبٌۭ (Indeed, your Lord is near)"},
 {"Word (Arabic)": "جميل", "Transliteration": "Jameel", "Meaning": "Beautiful", "Example": "إِنَّۢ ٱللَّهَ جَمِيلٌۭ يُحِبُّ ٱلۡجَمَٰلَ (Indeed, Allah is Beautiful and loves beauty)"},
 {"Word (Arabic)": "شمس ", "Transliteration" : "Shams", "Meaning": "Sun", "Example": "وَجَعَلْنَا ٱلشَّمْسَ سِرَاجًا وَهَّاجًۭا (And We made the sun a shining lamp)"},
 {"Word (Arabic)": "عزيز", "Transliteration": "Aziz", "Meaning": "Mighty, Strong", "Example": "إِنَّٱللَّهَ عَزِيزٌۭ حَكِيمٌۭ (Indeed, Allah is Almighty, Wise)"},
 {"Word (Arabic)": "آيات", "Transliteration": "Ayat", "Meaning": "Signs, Verses", "Example": "إِنَّۢ فِى ذَٰلِكَ لَآيَٰتٍۢ لِّلۡمُؤْمِنِينَ (Indeed, in that are signs for the believers)"},
 {"Word (Arabic)": "خلق ", "Transliteration" : "Khalq", "Meaning": "Creation", "Example": "إِنَّ اللَّهَ خَلَقَ السَّمَٰوَٰتِ وَالْأَرْضَ فِي سِتَّةِ أَيَّامٍ (Indeed, Allah created the heavens and the earth in six days)"},
 {"Word (Arabic)": "سمع ", "Transliteration" : "Sama'a", "Meaning": "Hearing", "Example": "إِنَّ اللَّهَ سَمِيعٌ عَلِيمٌ (Indeed, Allah is Hearing and Knowing)"},
 {"Word (Arabic)": "بصر ", "Transliteration" : "Basar", "Meaning": "Sight", "Example": "إِنَّ اللَّهَ بَصِيرٌ بِمَا تَعْمَلُونَ (Indeed, Allah is All-Seeing of what you do)"},
 {"Word (Arabic)": "عبادة", "Transliteration": "Ibadah", "Meaning": "Worship", "Example": "وَمَآ خَلَقْتُ الْجِنَّ وَالإِنسَ إِلَّا لِيَعْبُدُونِ (And I did not create the jinn and mankind except to worship Me)"},
 {"Word (Arabic)": "فقر ", "Transliteration" : "Faqr", "Meaning": "Poverty", "Example": "إِنَّمَا ٱلۡمُؤْمِنُونَ إِخْوَةٌۢ فَأَصْلِحُوا۟ بَيْنَ أَخَوَيْكُمْ (Indeed, the believers are but brothers)"},
 {"Word (Arabic)": "غني ", "Transliteration" : "Ghani", "Meaning": "Rich, Self-sufficient", "Example": "إِنَّ اللَّهَ غَنِيٌّۭ حَمِيدٌ (Indeed, Allah is Self-Sufficient, Praiseworthy)"},
 {"Word (Arabic)": "حج" , "Transliteration": "Hajj", "Meaning": "Pilgrimage", "Example": "وَأَذِّنْ فِي النَّاسِ بِالْحَجِّ يَأْتُوكَ رِجَالًا (And proclaim to the people the Hajj)"},
 {"Word (Arabic)": "رزق ", "Transliteration" : "Rizq", "Meaning": "Provision, Sustenance", "Example": "وَمَآ أَتَاكُمْ مِّن رَّحْمَةٍۢ فَمِنْهُۥ (And whatever mercy has come to you is from Him)"},
 {"Word (Arabic)": "حسن ", "Transliteration" : "Husn", "Meaning": "Goodness, Excellence", "Example": "وَإِنَّكَ لَعَلَىٰ خُلُقٍ عَظِيمٍ (And indeed, you are of a great moral character)"},
 {"Word (Arabic)": "بشرى", "Transliteration": "Bushra", "Meaning": "Good Tidings", "Example": "فَبَشِّرْهُم بِجَنَّةٍ تَجْرِي مِن تَحْتِهَا (So give them glad tidings of a garden beneath which rivers flow)"},
 {"Word (Arabic)": "دعوة", "Transliteration": "Dawah", "Meaning": "Call, Invitation", "Example": "وَادْعُوۡا۟ إِلَىٰ رَبِّكِ (And call to your Lord)"},
 {"Word (Arabic)": "نعيم", "Transliteration": "Na’im", "Meaning": "Bliss, Comfort", "Example": "إِنَّ أَهْلَ ٱلْجَنَّةِ فِى نَعِيمٍۢ (Indeed, the people of Paradise are in bliss)"},
 {"Word (Arabic)": "لطف ", "Transliteration" : "Lutf", "Meaning": "Kindness, Gentleness", "Example": "فَٱلۡتَفَتۡتُ فِيهِمۡ لُطْفًۭا (And I became gentle among them)"},
 {"Word (Arabic)": "عفو ", "Transliteration" : "Afw", "Meaning": "Forgiveness", "Example": "إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌ (Indeed, Allah is Forgiving and Merciful)"},
 {"Word (Arabic)": "هداية", "Transliteration": "Hidayah", "Meaning": "Guidance", "Example": "إِنَّ عَلَيْنَا لِلْهُدَىٰ (Indeed, upon Us is guidance)"},
 {"Word (Arabic)": "أمة ", "Transliteration" : "Ummah", "Meaning": "Nation, Community", "Example": "إِنَّ هَٰذِهِۦٓ أُمَّتُكُمْ أُمَّةًۭ وَٰحِدَةًۭ (Indeed, this is your nation, one nation)"},
 {"Word (Arabic)": "صديق", "Transliteration": "Siddiq", "Meaning": "Truthful, Companion", "Example": "إِنَّ ٱللَّهَ مَعَ ٱلۡصَّٰدِقِينَ (Indeed, Allah is with the truthful)"},
 {"Word (Arabic)": "موت ", "Transliteration" : "Mawt", "Meaning": "Death", "Example": "وَلَا تَقُولُوا۟ لِمَن يُقْتَلُ فِى سَبِيلِ ٱللَّهِ أَمْوَٰتٌۭ (And do not say of those who are killed in the way of Allah that they are dead)"},
 {"Word (Arabic)": "نصر ", "Transliteration" : "Nasr", "Meaning": "Victory, Help", "Example": "إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلۡفَتْحُ (When the victory of Allah has come and the conquest)"},
 {"Word (Arabic)": "علمي", "Transliteration": "Ilmi", "Meaning": "My Knowledge", "Example": "قَالَ رَبُّكَمْ يَعْلَمُ مَا فِى السَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ (Your Lord knows what is in the heavens and what is on the earth)"},
 {"Word (Arabic)": "نوايا", "Transliteration": "Nawaya", "Meaning": "Intention", "Example": "إِنَّمَآ ٱلْأَعْمَٰلُ بِالنِّيَّاتِ (Indeed, actions are by intentions)"},
 {"Word (Arabic)": "حب" , "Transliteration": "Hubb", "Meaning": "Love", "Example": "وَٱلَّذِينَ ءَامَنُوا۟ أَشَدُّ حُبًّۭا لِّي (And those who believe are stronger in love for Him)"},
 {"Word (Arabic)": "عزة ", "Transliteration" : "Izzah", "Meaning": "Honor, Glory", "Example": "وَإِنَّ ٱللَّهَ سَمِيعٌۭ عَلِيمٌ (Indeed, Allah is All-Hearing, All-Knowing)"},
 {"Word (Arabic)": "حياة", "Transliteration": "Hayah", "Meaning": "Life", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلۡحَىُّۖ (Indeed, Allah is the Ever-Living)"},
 {"Word (Arabic)": "نار ", "Transliteration" : "Nar", "Meaning": "Fire", "Example": "إِنَّ جَهَنَّمَ لَتُحْشَرُ بِهَا الْكَافِرُونَ (Indeed, Hell is a fire that will burn them)"},
 {"Word (Arabic)": "رحيم", "Transliteration": "Rahim", "Meaning": "Merciful", "Example": "إِنَّ اللَّهَ رَحِيمٌۭ بِالۡعِبَادِ (Indeed, Allah is Merciful to His servants)"},
 {"Word (Arabic)": "غفور", "Transliteration": "Ghafur", "Meaning": "Forgiving", "Example": "إِنَّ رَبَّكَ غَفُورٌۭ رَّحِيمٌ (Indeed, your Lord is Forgiving and Merciful)"},
 {"Word (Arabic)": "قوم ", "Transliteration" : "Qaum", "Meaning": "People, Nation", "Example": "وَمَآ أَرْسَلْنَٰكَ إِلَّا كَٰفَّةًۭ لِّلنَّاسِ (And We have not sent you except to all mankind)"},
 {"Word (Arabic)": "دنيا", "Transliteration": "Dunya", "Meaning": "Worldly life", "Example": "تُحِبُّونَ ٱلۡحَيَوٰةَ ٱلدُّنْيَا (You love the life of this world)"},
 {"Word (Arabic)": "آخرة", "Transliteration": "Akhira", "Meaning": "Hereafter", "Example": "وَٱلۡبَٰتِلَٰتِ (And the Hereafter is better and everlasting)"},
 {"Word (Arabic)": "كتاب", "Transliteration": "Kitab", "Meaning": "Book", "Example": "إِنَّا أَنزَلْنَا عَلَيْكَ الْكِتَٰبَ بِالْحَقِّ (Indeed, We have sent down to you the Book in truth)"},
 {"Word (Arabic)": "كافر", "Transliteration": "Kafir", "Meaning": "Disbeliever", "Example": "إِنَّ الَّذِينَ كَفَرُوا۟ وَجَحَدُوا۟ بِالۡعَادَٰتِ (Indeed, those who disbelieve and reject the Signs)"},
 {"Word (Arabic)": "فعل ", "Transliteration" : "Fi’l", "Meaning": "Action", "Example": "وَفَعَلُوا۟ مَا فَعَلُوا۟ (And they did what they did)"},
 {"Word (Arabic)": "مغنم", "Transliteration": "Maghnam", "Meaning": "Gain, Spoil", "Example": "وَفَاءًۭ مِّنَ ٱللَّهِ وَرَحْمَةًۭ (A gain from Allah and a mercy)"},
 {"Word (Arabic)": "مفتاح", "Transliteration": "Miftah", "Meaning": "Key", "Example": "وَفَجَّرْنَا ٱلۡمَعَٰنِ فَجَّرْنَا فَجًّۭا (And We caused the fountains to gush)"},
 {"Word (Arabic)": "أمر ", "Transliteration" : "Amr", "Meaning": "Command, Matter", "Example": "إِنَّمَآ أَمْرُهُۥٓ إِذَآ أَرَادَ (Indeed, His command is when He intends)"},
 {"Word (Arabic)": "مقام", "Transliteration": "Maqam", "Meaning": "Station, Position", "Example": "وَإِنَّهُۥ لَفِى مَقَامٍۢ كَرِيمٍۢ (And indeed, he is in a noble position)"},
 {"Word (Arabic)": "بر" , "Transliteration": "Birr", "Meaning": "Righteousness", "Example": "وَقُولُوا۟ لِلنَّاسِ حُسْنًۭا (And speak to people good)"},
 {"Word (Arabic)": "فكر ", "Transliteration" : "Fikr", "Meaning": "Thought, Reflection", "Example": "وَفَكَرُوا۟ فِىٓ أَمْرِهِۦۖ (And they reflected on their matter)"},
 {"Word (Arabic)": "هدية", "Transliteration": "Hadiyah", "Meaning": "Gift, Offering", "Example": "وَمَآ أَتَىٰكُم مِّنْ هَدِيَّةٍۢ (And whatever gift has come to you)"},
 {"Word (Arabic)": "مائدة", "Transliteration": "Ma’idah", "Meaning": "Table, Feast", "Example": "إِذْ قَالَ الْحَوَارِيُّونَ يَا عِيسَىٰ (When the disciples said, 'O Jesus')"},
 {"Word (Arabic)": "ضيافة", "Transliteration": "Diyafah", "Meaning": "Hospitality", "Example": "فَذُوقُوا۟ بِمَا كُنتُمْ تَكْسِبُونَ (Taste the punishment for what you used to earn)"},
 {"Word (Arabic)": "محراب", "Transliteration": "Mihrab", "Meaning": "Sanctuary, Niche", "Example": "وَدَخَلَ الْمِحْرَابَ فَصَلَّىٰ (And he entered the sanctuary and prayed)"},
 {"Word (Arabic)": "سعي ", "Transliteration" : "Sa’y", "Meaning": "Effort", "Example": "إِنَّ سَعْيَكُمْ لَشَتَّىٰ (Indeed, your efforts are diverse)"},
 {"Word (Arabic)": "إيمان", "Transliteration": "Iman", "Meaning": "Faith, Belief", "Example": "إِنَّمَآ أَمَٰنَكُمْ إِذَآ آمَنُوا۟ (Indeed, the true believers are those who believe in Allah)"},
 {"Word (Arabic)": "حكمة", "Transliteration": "Hikmah", "Meaning": "Wisdom", "Example": "يُؤْتِى ٱلْحِكْمَةَ مَن يَشَآءُ (He gives wisdom to whom He wills)"},
 {"Word (Arabic)": "غنى ", "Transliteration": "Ghina", "Meaning": "Wealth, Self-sufficiency", "Example": "إِنَّ ٱللَّهَ غَنيٌّۭ حَمِيدٌ (Indeed, Allah is Free of need, Worthy of praise)"},
 {"Word (Arabic)": "صبر ", "Transliteration": "Sabr", "Meaning": "Patience", "Example": "وَصَابِرِينَ وَصَابِرَٰتٍۢ (And the patient men and the patient women)"},
 {"Word (Arabic)": "رغبة", "Transliteration": "Raghbah", "Meaning": "Desire, Wish", "Example": "وَإِنَّمَآ أَمْرُهُۥٓ إِذَآ أَرَادَ (And indeed, His command is when He intends)"},
 {"Word (Arabic)": "ماء ", "Transliteration" : "Ma’a", "Meaning": "Water", "Example": "وَجَعَلْنَا مِنَ ٱلۡمَاءِ كُلَّ شَىْءٍۢ حَىٍّ (And We made from water every living thing)"},
 {"Word (Arabic)": "نعم ", "Transliteration": "Na’am", "Meaning": "Blessing, Favor", "Example": "وَإِن تَعُدُّوا۟ نِعْمَتَ ٱللَّهِ لَا تُحۡصُوهَا (And if you count the favors of Allah, you will not be able to number them)"},
 {"Word (Arabic)": "طاعة", "Transliteration": "Ta’ah", "Meaning": "Obedience", "Example": "وَطَاعَتُهُۥ فِى دِينِهِۦۚ (And His obedience in His religion)"},
 {"Word (Arabic)": "كلمة", "Transliteration": "Kalima", "Meaning": "Word, Statement", "Example": "قَالَتِ ٱمْرَأَتُ فِرْعَوْنَ (The wife of Pharaoh said)"},
 {"Word (Arabic)": "دين ", "Transliteration" : "Din", "Meaning": "Religion, Way of life", "Example": "إِنَّ ٱلدِّينَ عِندَ ٱللَّهِ ٱلۡإِسْلَٰمُ (Indeed, the religion in the sight of Allah is Islam)"},
 {"Word (Arabic)": "سر" , "Transliteration": "Sirr", "Meaning": "Secret", "Example": "قُلْ لِّذِينَ كَفَرُوا۟ إِن كَانَتْ فِى قُلُوبِهِۦٓمْ (Say to those who disbelieve, if they believe in what is hidden in their hearts)"},
 {"Word (Arabic)": "مؤمنون", "Transliteration": "Mu’minun", "Meaning": "Believers", "Example": "إِنَّ ٱلۡمُؤْمِنِينَ وَٱلۡمُؤْمِنَٰتِ (Indeed, the believing men and believing women)"},
 {"Word (Arabic)": "حلال", "Transliteration": "Halal", "Meaning": "Permissible", "Example": "وَأَحَلَّ اللَّهُ ٱلۡبَيِّ (And Allah has made lawful the sale)"},
 {"Word (Arabic)": "حرام", "Transliteration": "Haram", "Meaning": "Forbidden", "Example": "وَٱلۡخُمُرَ وَٱلْمَيْسِرَ حَرَّمَۚ (And intoxicants and gambling are forbidden)"},
 {"Word (Arabic)": "صلاة", "Transliteration": "Salah", "Meaning": "Prayer", "Example": "إِنَّمَآ أُمِرُوا۟ أَنْ يُصَلُّوا۟ (Indeed, they were commanded to pray)"},
 {"Word (Arabic)": "زكاة", "Transliteration": "Zakah", "Meaning": "Almsgiving", "Example": "وَأَقِيمُوا۟ ٱلصَّلَاةَ وَآتُوا۟ الزَّكَاةَ (And establish prayer and give zakah)"},
 {"Word (Arabic)": "الحق", "Transliteration": "Al-Haq", "Meaning": "The Truth", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلْحَقُّۚ (Indeed, Allah is the Truth)"},
 {"Word (Arabic)": "قدرة", "Transliteration": "Qudrah", "Meaning": "Power", "Example": "وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ (And Allah is capable of all things)"},
 {"Word (Arabic)": "رحمة", "Transliteration": "Rahmah", "Meaning": "Mercy", "Example": "وَرَحْمَتُهُۥ وَرَحِيمٌۭ (His mercy is vast and all-encompassing)"},
 {"Word (Arabic)": "عذاب", "Transliteration": "Adhab", "Meaning": "Punishment", "Example": "فَذُوقُوا۟ بِمَا كُنتُمْ تَكْسِبُونَ (So taste the punishment for what you earned)"},
 {"Word (Arabic)": "إجابة", "Transliteration": "Ijabah", "Meaning": "Response, Answer", "Example": "وَإِذَا سَأَلَكَ عِبَادِى عَنِّىۚ (And when My servants ask you concerning Me)"},
 {"Word (Arabic)": "رسالة", "Transliteration": "Risalah", "Meaning": "Message", "Example": "إِنَّمَآ أُو۟حِىٓ إِلَىٰٓ (Indeed, I am sent only as a messenger)"},
 {"Word (Arabic)": "فتنة", "Transliteration": "Fitnah", "Meaning": "Trial, Temptation", "Example": "وَٱلۡفِتْنَةُ أَشَدُّ مِنَ ٱلۡقَتْلِ (And trial is worse than killing)"},
 {"Word (Arabic)": "عقل ", "Transliteration" : "Aql", "Meaning": "Mind, Intellect", "Example": "إِنَّ فِى ذَٰلِكَ لَآيَٰتٍ لِّي أُو۟لِى ٱلْأَلْبَابِ (Indeed, in that are signs for those of understanding)"},
 {"Word (Arabic)": "أمانة", "Transliteration": "Amanah", "Meaning": "Trust, Deposit", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُمْ أَنْ تُؤَدُّوا۟ ٱلْأَمَٰنَٰتِ (Indeed, Allah commands you to return trusts)"},
 {"Word (Arabic)": "بركة", "Transliteration": "Barakah", "Meaning": "Blessing, Increase", "Example": "فَٱلَّذِينَ يَحْتَسُونَ ٱلْمَاءَ لَهُمْ فِيهِ بَرَكَهٌۭ (Those who drink the water will find blessings in it)"},
 {"Word (Arabic)": "هدى ", "Transliteration" : "Hudah", "Meaning": "Guidance", "Example": "وَإِنَّكَ لَتَهْدِىٓ إِلَىٰ صِرَٰطٍ مُسْتَقِيمٍ (And indeed, you guide to a straight path)"},
 {"Word (Arabic)": "شهادة", "Transliteration": "Shahadah", "Meaning": "Testimony, Witness", "Example": "شَهِدَ اللَّهُ أَنَّهُۥ لَآ إِلٰهَ إِلَّا هُوَ (Allah bears witness that there is no god but Him)"},
 {"Word (Arabic)": "خوف ", "Transliteration" : "Khauf", "Meaning": "Fear", "Example": "وَقُلْ رَبِّ أَعُوذُ بِكَ مِنْ خَوْفٍۢ (And say, 'My Lord, I seek refuge in You from fear')"},
 {"Word (Arabic)": "كفار", "Transliteration": "Kuffar", "Meaning": "Disbelievers", "Example": "إِنَّ ٱلۡمُكَذِّبِينَ بِالۡمِلَّةِ ٱلۡكُفَّارِ (Indeed, the disbelievers are the ones who deny the truth)"},
 {"Word (Arabic)": "سلامة", "Transliteration": "Salamah", "Meaning": "Safety, Health", "Example": "فَسَلِّمُوا۟ عَلَيْهِمْ بِسَلاَمٍۢ (Then greet them with a greeting of peace)"},
 {"Word (Arabic)": "عدل ", "Transliteration": "Adl", "Meaning": "Justice, Fairness", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُمْ بِالْعَدْلِ وَالْإِحْسَٰنِ (Indeed, Allah commands justice and the doing of good)"},
 {"Word (Arabic)": "نور ", "Transliteration" : "Nur", "Meaning": "Light", "Example": "ٱللَّهُ وَلِيُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَىٰ النُّورِ (Allah is the protector of those who believe, He brings them out of darkness into the light)"},
 {"Word (Arabic)": "غضب ", "Transliteration" : "Ghadab", "Meaning": "Anger", "Example": "وَٱللَّهُ غَضِبَ عَلَيْهِمْ (And Allah became angry with them)"},
 {"Word (Arabic)": "قلب ", "Transliteration" : "Qalb", "Meaning": "Heart", "Example": "فِي قُلُوبِهِمْ مَرَضٌۭ (In their hearts is a disease)"},
 {"Word (Arabic)": "جنة ", "Transliteration" : "Jannah", "Meaning": "Paradise, Garden", "Example": "إِنَّ ٱلۡمُتَّقِينَ فِى جَنَّٰتٍ وَنَعِيمٍۢ (Indeed, the righteous will be in gardens and delight)"},
 {"Word (Arabic)": "كريم", "Transliteration": "Karim", "Meaning": "Generous, Noble", "Example": "إِنَّ رَبَّكُمْ لَذُو فَضْلٍۢ عَلَىٰ (Indeed, your Lord is full of bounty)"},
 {"Word (Arabic)": "عدو ", "Transliteration" : "Aduww", "Meaning": "Enemy", "Example": "إِنَّ عَدُوَّكُمُ الشَّيْطَٰنُ (Indeed, your enemy is the devil)"},
 {"Word (Arabic)": "صمت ", "Transliteration" : "Samt", "Meaning": "Silence", "Example": "وَمَنۢ صَمَتَ نَجَا (Whoever remains silent is safe)"},
 {"Word (Arabic)": "شكر ًا", "Transliteration": "Shukran", "Meaning": "Thank you", "Example": "قُلْ شُكْرًا لِّلَّهِ (Say, 'Thank you to Allah')"},
 {"Word (Arabic)": "قوة ", "Transliteration" : "Quwwah", "Meaning": "Strength", "Example": "وَأَعِزَّنِى بِقُوَّتِهِۦ (And grant me strength through Your power)"},
 {"Word (Arabic)": "صراع", "Transliteration": "Sira’a", "Meaning": "Struggle", "Example": "وَمَآ كُنتُمُ فِى ٱلۡصِّرَاعِ (And you were not in the struggle)"},
 {"Word (Arabic)": "سورة", "Transliteration": "Surah", "Meaning": "Chapter, Surah", "Example": "وَقُرْءَٰنًا فَرَقْنَٰهُ لِيَتْلُوهُ عَلَىٰكُ (And a Qur’an that We have divided for you to recite)"},
 {"Word (Arabic)": "قضاء", "Transliteration": "Qada’a", "Meaning": "Decree", "Example": "قَدْ قَضَتْ قَضَاءًۭ وَإِنَّ اللَّٰهِ قَٰضٍۢ (He decreed it as a judgment, and indeed, Allah is the best of judges)"},
 {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "فَٱغْفِرْ لِىٰ إِنَّكَ أَنتَ ٱلْغَفُورُ (So forgive me, indeed, You are the Forgiving)"},
{"Word (Arabic)": "رحمن", "Transliteration": "Rahman", "Meaning": "Most Merciful", "Example": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ (In the name of Allah, the Most Merciful, the Most Compassionate)"
    },
    {
        "Word (Arabic)": "قدير",
        "Transliteration": "Qadeer",
        "Meaning": "All-Powerful",
        "Example": "إِنَّ اللَّهَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ (Indeed, Allah is All-Powerful over everything)"
    },
    {
        "Word (Arabic)": "عليم",
        "Transliteration": "Aleem",
        "Meaning": "All-Knowing",
        "Example": "إِنَّ اللَّهَ كَانَ عَلِيمًا حَكِيمًا (Indeed, Allah is All-Knowing, All-Wise)"
    },
    {
        "Word (Arabic)": "توحيد",
        "Transliteration": "Tawheed",
        "Meaning": "Oneness (of Allah)",
        "Example": "وَإِلَٰهُكُمْ إِلَٰهٌ وَٰحِدٌ (And your God is One God)"
    },
    {
        "Word (Arabic)": "شرك",
        "Transliteration": "Shirk",
        "Meaning": "Associating partners with Allah",
        "Example": "إِنَّ اللَّهَ لَا يَغْفِرُ أَنْ يُشْرَكَ بِهِ (Indeed, Allah does not forgive associating others with Him)"
    },
    {
        "Word (Arabic)": "صيام",
        "Transliteration": "Siyam",
        "Meaning": "Fasting",
        "Example": "يَا أَيُّهَا الَّذِينَ آمَنُوا كُتِبَ عَلَيْكُمُ الصِّيَامُ (O you who believe, fasting is prescribed for you)"
    },
    {
        "Word (Arabic)": "صدق",
        "Transliteration": "Sadaq",
        "Meaning": "Truthfulness",
        "Example": "وَكُونُوا مَعَ الصَّادِقِينَ (And be with the truthful)"
    },
    {
        "Word (Arabic)": "إحسان",
        "Transliteration": "Ihsan",
        "Meaning": "Excellence",
        "Example": "إِنَّ اللَّهَ يُحِبُّ الْمُحْسِنِينَ (Indeed, Allah loves those who strive for excellence)"
    },
    {
        "Word (Arabic)": "رسول",
        "Transliteration": "Rasool",
        "Meaning": "Messenger",
        "Example": "وَإِذْ بَعَثَ اللَّهُ نَبِيًّا رَسُولًا (And when Allah sends forth a prophet as a messenger)"
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
    st.write(f"**Example**: {row['Example']}")
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
        Made by Asia Mehasi
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
