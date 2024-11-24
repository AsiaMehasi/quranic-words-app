import streamlit as st
import pandas as pd

quranic_words = [
       {"Word (Arabic)": "و", "Transliteration": "Wa", "Meaning": "And", "Example": "وَٱلۡعَصۡرِ (By Time)"},
    {"Word (Arabic)": "في", "Transliteration": "Fi", "Meaning": "In, Inside", "Example": "فِي ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِ (In the heavens and the earth)"},
    {"Word (Arabic)": "من", "Transliteration": "Min", "Meaning": "From, Of", "Example": "مِنَ ٱلۡجِنَّةِ وَٱلنَّاسِ (From among the jinn and mankind)"},
    {"Word (Arabic)": "على", "Transliteration": "'Ala", "Meaning": "On, Upon", "Example": "وَعَلَىٰ ٱللَّهِ فَلۡيَتَوَكَّلِ ٱلۡمُؤۡمِنُونَ (And upon Allah let the believers rely)"},
    {"Word (Arabic)": "إلى", "Transliteration": "Ila", "Meaning": "To", "Example": "إِلَىٰ رَبِّهِمْ يَحْشُرُونَ (To their Lord, they will be gathered)"},
    {"Word (Arabic)": "عن", "Transliteration": "An", "Meaning": "About, Concerning", "Example": "قُلۡ سَمِيعٌۭ بِمَا فِى ٱلۡقُلُوبِ (Say, He is the All-Hearing of what is in the hearts)"},
    {"Word (Arabic)": "رب", "Transliteration": "Rabb", "Meaning": "Lord", "Example": "رَّبُّ ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِ (The Lord of the heavens and the earth)"},
    {"Word (Arabic)": "كتاب", "Transliteration": "Kitab", "Meaning": "Book", "Example": "إِنَّ هَٰذَا لَفِى ٱلۡقُرۡآنِ (This is in the Quran)"},
    {"Word (Arabic)": "آية", "Transliteration": "Ayah", "Meaning": "Verse, Sign", "Example": "فَإِذَا جَآءَتِ ٱلصَّٰحَةُ (When the sign of the Hour comes)"},
    {"Word (Arabic)": "نور", "Transliteration": "Nur", "Meaning": "Light", "Example": "اللَّهُ نُورُ ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِ (Allah is the Light of the heavens and the earth)"},
    {"Word (Arabic)": "سَلاَم", "Transliteration": "Salam", "Meaning": "Peace", "Example": "فَسَلَّمُوٓا۟ عَلَيْهِمْ بِسَلاَمٍۢ (Greet them with peace)"},
    {"Word (Arabic)": "سلامة", "Transliteration": "Salamah", "Meaning": "Safety, Health", "Example": "سَلامَةًۭ فِى أَمَٰنٍۢ (Safety and security in peace)"},
    {"Word (Arabic)": "حب", "Transliteration": "Hubb", "Meaning": "Love", "Example": "وَٱلَّذِينَ ءَامَنُوا۟ أَشَدُّ حُبًّۭا لِّلَّهِ (But those who believe are stronger in love for Allah)"},
    {"Word (Arabic)": "إيمان", "Transliteration": "Iman", "Meaning": "Faith", "Example": "قَالَتْ رَٰبِطُ ٱلۡقُلبِ إِيمَٰنًا (The heart is bound with faith)"},
    {"Word (Arabic)": "رحمة", "Transliteration": "Rahmah", "Meaning": "Mercy", "Example": "وَرَحْمَتُهُۥ وَسِعَتْ كُلَّ شَىۡءٍۢ (His mercy encompasses all things)"},
    {"Word (Arabic)": "جنة", "Transliteration": "Jannah", "Meaning": "Paradise", "Example": "إِنَّ ٱلۡمُتَّقِينَ فِى جَنَّٰتٍۢ وَنَعِيمٍۢ (Indeed the righteous will be in gardens and bliss)"},
    {"Word (Arabic)": "سورة", "Transliteration": "Surah", "Meaning": "Chapter", "Example": "سورة الفاتحة (Surah Al-Fatiha)"},
    {"Word (Arabic)": "دعوة", "Transliteration": "Da'wah", "Meaning": "Call, Invitation", "Example": "وَدَعَوْهُمۡ إِلَىٰ سَبِيلِ رَبِّهِمْ (And invite them to the way of their Lord)"},
    {"Word (Arabic)": "حكمة", "Transliteration": "Hikmah", "Meaning": "Wisdom", "Example": "إِنَّآ أَتَيْنَٰكَ بِحِكْمَةٍۢ (We have given you wisdom)"},
    {"Word (Arabic)": "شكر", "Transliteration": "Shukr", "Meaning": "Gratitude", "Example": "إِذَا شَكَرْتُمْ لَأَزِيدَنَّكُمْ (If you are grateful, I will surely increase your favor)"},
    {"Word (Arabic)": "ذكر", "Transliteration": "Dhikr", "Meaning": "Remembrance", "Example": "وَٱذْكُرُوا۟ رَبَّكُمْ (And remember your Lord)"},
    {"Word (Arabic)": "حق", "Transliteration": "Haq", "Meaning": "Truth", "Example": "إِنَّ هَٰذَا لَهُوَ الْحَقُّ (Indeed, this is the truth)"},
    {"Word (Arabic)": "صلاة", "Transliteration": "Salah", "Meaning": "Prayer", "Example": "وَقُومُوا۟ لِلَّهِ قَٰنِتِينَ (And stand before Allah in devotion)"},
    {"Word (Arabic)": "صبر", "Transliteration": "Sabr", "Meaning": "Patience", "Example": "وَٱصْبِرْ وَمَا صَبَرُكَ إِلَّا بِٱللَّهِ (And be patient, and your patience is only with Allah)"},
    {"Word (Arabic)": "توكل", "Transliteration": "Tawakkul", "Meaning": "Trust, Reliance", "Example": "وَعَلَىٰ رَبِّهِمۡ يَتَوَكَّلُونَ (And upon their Lord they rely)"},
    {"Word (Arabic)": "خوف", "Transliteration": "Khauf", "Meaning": "Fear", "Example": "وَٱذْكُرْ رَبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ (And remember your Lord within yourself in humility and fear)"},
    {"Word (Arabic)": "سلامة", "Transliteration": "Salama", "Meaning": "Safety", "Example": "وَسَٰلِمٌۭ (And they will be safe)"},
    {"Word (Arabic)": "هدى", "Transliteration": "Huda", "Meaning": "Guidance", "Example": "إِنَّ هَٰذَا لَهُوَ ٱلۡهُدَىٰ (Indeed, this is the guidance)"},
    {"Word (Arabic)": "إجابة", "Transliteration": "Ijabah", "Meaning": "Response", "Example": "وَٱجِيبُوا۟ لِرَبِّكُمْ (And respond to your Lord)"},
    {"Word (Arabic)": "غفر", "Transliteration": "Ghufran", "Meaning": "Forgiveness", "Example": "فَٱغْفِرْ لِمَن فَسَقَ (So forgive those who transgress)"},
    {"Word (Arabic)": "كفر", "Transliteration": "Kufr", "Meaning": "Disbelief", "Example": "وَمَن يَكْفُرْ فَإِنَّ ٱللَّهَ غَنِيٌّۭ (And whoever disbelieves, indeed Allah is Self-Sufficient)"},
    {"Word (Arabic)": "شمس", "Transliteration": "Shams", "Meaning": "Sun", "Example": "وَٱلشَّمْسِ وَضُحَٰهَا (By the sun and its brightness)"},
    {"Word (Arabic)": "قمر", "Transliteration": "Qamar", "Meaning": "Moon", "Example": "وَٱلْقَمَرِ إِذَا تَلَاهَا (And the moon when it follows it)"},
    {"Word (Arabic)": "نجوم", "Transliteration": "Nujum", "Meaning": "Stars", "Example": "وَٱلنَّجْمِ وَٱلشَّجَرِ (By the stars and the trees)"},
    {"Word (Arabic)": "سماء", "Transliteration": "Sama'", "Meaning": "Sky", "Example": "إِنَّ فِى سَمَٰوَٰتِهِۦ (Indeed in the heavens)"},
    {"Word (Arabic)": "أرض", "Transliteration": "Ard", "Meaning": "Earth", "Example": "وَفِى ٱلۡأَرۡضِ (And in the earth)"},
    {"Word (Arabic)": "دنيا", "Transliteration": "Dunya", "Meaning": "World, Life", "Example": "إِنَّمَا حَيَاةُ ٱلدُّنْيَا (Indeed the life of this world)"},
    {"Word (Arabic)": "آخرة", "Transliteration": "Akhirah", "Meaning": "Hereafter", "Example": "وَمَا لَكُمۡ فِى ٱلۡٓآخِرَةِ (And what is for you in the Hereafter)"},
    {"Word (Arabic)": "ظلم", "Transliteration": "Zulm", "Meaning": "Injustice", "Example": "إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلۡظَّٰلِمِينَ (Indeed, Allah does not like the wrongdoers)"},
    {"Word (Arabic)": "عدو", "Transliteration": "Aduww", "Meaning": "Enemy", "Example": "إِنَّ ٱلۡعَدُوَّ لَكُمۡ (Indeed, the enemy is to you)"},
    {"Word (Arabic)": "جند", "Transliteration": "Jund", "Meaning": "Army", "Example": "فَجَعَلْنَا جُندًۭا مِنْهُ (And we made from it an army)"},
    {"Word (Arabic)": "إصبع", "Transliteration": "Isba'", "Meaning": "Finger", "Example": "وَفَطَرْنَا ٱلۡإِصۡبَعَ (And we formed the fingers)"},
    {"Word (Arabic)": "كف", "Transliteration": "Kaff", "Meaning": "Palm of the hand", "Example": "وَفَٰكَفَّهُۥ (And He closed his hand)"},
    {"Word (Arabic)": "عقل", "Transliteration": "Aql", "Meaning": "Mind, Intellect", "Example": "لَعَلَّكُمۡ تَعۡقِلُونَ (That you may understand)"},
    {"Word (Arabic)": "أذن", "Transliteration": "Udhun", "Meaning": "Ear", "Example": "وَمَآ أَذَٰنَ (And their ears did not listen)"},
    {"Word (Arabic)": "عين", "Transliteration": "Ayn", "Meaning": "Eye", "Example": "وَفَجَّرْنَا عُيُونًا (And We caused springs to gush forth)"},
    {"Word (Arabic)": "قلب", "Transliteration": "Qalb", "Meaning": "Heart", "Example": "وَٱلۡقُلُوبُ يَوْمَئِذٍۢ (And the hearts will be on that Day)"},
    {"Word (Arabic)": "لسان", "Transliteration": "Lisan", "Meaning": "Tongue", "Example": "وَفَصَّلْنَا لَهُۥ الْمَسَٰءَ (And We have detailed for him the speech)"},
    {"Word (Arabic)": "يد", "Transliteration": "Yad", "Meaning": "Hand", "Example": "وَجَعَلْنَا يَدَٰهُ قَبْضًا (And We made his hand close)"},
    {"Word (Arabic)": "رجال", "Transliteration": "Rijal", "Meaning": "Men", "Example": "فِى أَيُّهَا لَٰهِ قَوْمٌۭ (Men of their kind)"},
    {"Word (Arabic)": "نساء", "Transliteration": "Nisa", "Meaning": "Women", "Example": "وَٱلنِّسَآءَ (And the women)"},
    {"Word (Arabic)": "والد", "Transliteration": "Walid", "Meaning": "Father", "Example": "وَٱلۡوَٰلِدَٰتِ (And the mothers)"},
    {"Word (Arabic)": "والدة", "Transliteration": "Walidah", "Meaning": "Mother", "Example": "فِيٓ بُيُوتِهِۦ (In their homes)"},
    {"Word (Arabic)": "منزل", "Transliteration": "Manzil", "Meaning": "Abode, Residence", "Example": "وَفِى سَٰفَتِهِۦ (And in the safe abode)"},
    {"Word (Arabic)": "باب", "Transliteration": "Bab", "Meaning": "Door", "Example": "إِنَّ ٱلۡبَابَ (Indeed, the door)"},
    {"Word (Arabic)": "قبة", "Transliteration": "Qubba", "Meaning": "Dome", "Example": "تَحْتَ قُبَّتِهِۦ (Under his dome)"},
    {"Word (Arabic)": "سقف", "Transliteration": "Saqf", "Meaning": "Roof", "Example": "فِى سَٰمِهِۦ (In his roof)"},
    {"Word (Arabic)": "شجرة", "Transliteration": "Shajarah", "Meaning": "Tree", "Example": "وَٱلۡشَجَرَ (And the tree)"},
    {"Word (Arabic)": "ماء", "Transliteration": "Ma'", "Meaning": "Water", "Example": "وَجَعَلْنَا مِنَ ٱلۡمَاءِ كُلَّ شَىۡءٍۢ حَيٍّۢ (And We made from water every living thing)"},
    {"Word (Arabic)": "نار", "Transliteration": "Nar", "Meaning": "Fire", "Example": "وَٱلۡنَّارِ (And the fire)"},
    {"Word (Arabic)": "ريح", "Transliteration": "Rih", "Meaning": "Wind", "Example": "وَفَجَّرْنَا فِيهَا (And We caused in it the wind to blow)"},
    {"Word (Arabic)": "قوة", "Transliteration": "Quwah", "Meaning": "Strength", "Example": "وَفِى قُوَّتِهِۦ (And in his strength)"},
    {"Word (Arabic)": "صوت", "Transliteration": "Sawt", "Meaning": "Voice, Sound", "Example": "فَٱسْمَعُوا۟ لَهُۥ (So listen to him)"},
    {"Word (Arabic)": "علم", "Transliteration": "Ilm", "Meaning": "Knowledge", "Example": "إِنَّ ٱللَّهَ عَلِيمٌۭ (Indeed, Allah is All-Knowing)"},
    {"Word (Arabic)": "عقل", "Transliteration": "Aql", "Meaning": "Mind, Understanding", "Example": "فَفَهِمْنَٰهَا سُلَيْمَٰنَ (And We gave it understanding to Solomon)"},
    {"Word (Arabic)": "حكمة", "Transliteration": "Hikmah", "Meaning": "Wisdom", "Example": "وَإِنَّ هَٰذَا لَفِى ٱلۡحِكْمَةِ (And indeed, this is in wisdom)"},
    {"Word (Arabic)": "صبر", "Transliteration": "Sabr", "Meaning": "Patience", "Example": "وَصَابِرُوا۟ وَرَابِطُوا۟ (And be patient and endure)"},
    {"Word (Arabic)": "نعمة", "Transliteration": "Ni'mah", "Meaning": "Blessing", "Example": "وَإِنَّكَ لَذُو فَضْلٍ عَلَىٰ عَظِيمٍ (And indeed, you are of great favor)"},
    {"Word (Arabic)": "محنة", "Transliteration": "Mihnah", "Meaning": "Trial", "Example": "فَٱصْبِرُوا۟ عَلَىٰ مَا يَقُولُونَ (So be patient with what they say)"},
    {"Word (Arabic)": "عذاب", "Transliteration": "Adhab", "Meaning": "Punishment", "Example": "وَإِنَّۢ عَذَابِى لَشَدِيدٌۭ (And indeed, My punishment is severe)"},
    {"Word (Arabic)": "شكر", "Transliteration": "Shukr", "Meaning": "Gratitude", "Example": "إِنَّ شُكْرِي لِي (Indeed, My gratitude is for Me)"},
    {"Word (Arabic)": "توبة", "Transliteration": "Tawbah", "Meaning": "Repentance", "Example": "إِنَّ اللَّهَ يَتُوبُ عَلَىٰ مَن يَشَاءُ (Indeed, Allah accepts the repentance of whom He wills)"},
    {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "فَٱغْفِرْ لِمَن فَسَقَ (So forgive those who transgress)"},
    {"Word (Arabic)": "جنة", "Transliteration": "Jannah", "Meaning": "Paradise", "Example": "إِنَّ الَّذِينَ آمَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فَسَادِدُهُمْ إِلَىٰ جَنَّةِ (Indeed those who have believed and done righteous deeds will be guided to Paradise)"},
    {"Word (Arabic)": "نار", "Transliteration": "Nar", "Meaning": "Fire", "Example": "إِنَّنَا أَعَذَّبْنَا۟ أَهْلَ النَّارِ (Indeed, We have punished the people of the Fire)"},
    {"Word (Arabic)": "دعوة", "Transliteration": "Da'wah", "Meaning": "Call, Invitation", "Example": "ادْعُوۡا۟ إِلَىٰ سَبِيلِ رَبِّكَ (Call to the way of your Lord)"},
    {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfira", "Meaning": "Pardon, Forgiveness", "Example": "فَٱغْفِرْ لَنَآۚ إِنَّكَ أَنتَ ٱلۡغَفُورُ ٱلرَّحِيمُ (So forgive us; indeed, You are the Forgiving, the Merciful)"},
    {"Word (Arabic)": "كتاب", "Transliteration": "Kitab", "Meaning": "Book", "Example": "إِنَّمَا يُؤْمِنُونَ بِمَا أُنْزِلَ إِلَيْهِمْ وَٱلۡكِتَٰبُ وَٱلۡمُؤْمِنُونَ (They believe in what has been revealed to them, and the Book, and the believers)"},
    {"Word (Arabic)": "قلب", "Transliteration": "Qalb", "Meaning": "Heart", "Example": "فَٱلَّذِينَ فِي قُلُوبِهِۦ مَرَضٌۭ (So those in whose hearts is disease)"},
    {"Word (Arabic)": "رسول", "Transliteration": "Rasul", "Meaning": "Messenger", "Example": "وَٱلۡرَّسُولُ فِى أَيَّامٍۢ (And the Messenger is in the days)"},
    {"Word (Arabic)": "إيمان", "Transliteration": "Iman", "Meaning": "Faith", "Example": "وَأَمَرَ أُمَّتِهِۦ بِإِيمَٰنٍۢ (And He ordered his people to believe)"},
    {"Word (Arabic)": "أمل", "Transliteration": "Amal", "Meaning": "Hope, Expectation", "Example": "وَأَمَّلُوا۟ فَجَنَّٰتِهِۦ (And they hoped for his gardens)"},
    {"Word (Arabic)": "عبادة", "Transliteration": "Ibadah", "Meaning": "Worship", "Example": "فَٱعْبُدُوا۟ رَبَّكُمْ (Worship your Lord)"},
    {"Word (Arabic)": "شهادة", "Transliteration": "Shahadah", "Meaning": "Testimony, Witnessing", "Example": "وَأَشْهِدُوا۟ أَنْ لَآ إِلَٰهَ إِلَّآ اللَّهُ (And testify that there is no god but Allah)"},
    {"Word (Arabic)": "عدالة", "Transliteration": "Adalah", "Meaning": "Justice", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُم بِالۡعَدْلِ (Indeed, Allah commands justice)"},
    {"Word (Arabic)": "صلاة", "Transliteration": "Salah", "Meaning": "Prayer", "Example": "إِنَّ ٱلۡصَّلَٰةَ (Indeed, the prayer)"},
    {"Word (Arabic)": "خوف", "Transliteration": "Khauf", "Meaning": "Fear", "Example": "إِنَّمَا يُخَوِّفُونَكُمۡ (They are only trying to frighten you)"},
    {"Word (Arabic)": "رجاء", "Transliteration": "Raja'", "Meaning": "Hope", "Example": "إِنَّ رَجَٰءَكَ لِرَبِّكَ (Indeed, your hope is for your Lord)"},
    {"Word (Arabic)": "غضب", "Transliteration": "Ghadab", "Meaning": "Anger", "Example": "فَفَارِّينَ مِنَ ٱلۡغَضَبِ (They were fleeing from the anger)"},
    {"Word (Arabic)": "سوء", "Transliteration": "Su'", "Meaning": "Evil, Harm", "Example": "إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ (Indeed, Allah is Forgiving and Merciful)"},
    {"Word (Arabic)": "موت", "Transliteration": "Mawt", "Meaning": "Death", "Example": "إِنَّ ٱلْمَوْتَ (Indeed, death)"},
    {"Word (Arabic)": "حياة", "Transliteration": "Hayah", "Meaning": "Life", "Example": "إِنَّ ٱلۡحَيَٰةَ (Indeed, life)"},
    {"Word (Arabic)": "وقت", "Transliteration": "Waqt", "Meaning": "Time", "Example": "إِنَّ وَقْتَكُمْ فِى (Indeed, your time in)"},
    {"Word (Arabic)": "علماء", "Transliteration": "Ulama", "Meaning": "Scholars", "Example": "وَقَالَ ٱلۡعُلَمَآءُ (And the scholars said)"},
    {"Word (Arabic)": "عدو", "Transliteration": "Aduww", "Meaning": "Enemy", "Example": "إِنَّ ٱلۡعَدُوَّ (Indeed, the enemy)"},
    {"Word (Arabic)": "أمة", "Transliteration": "Ummah", "Meaning": "Nation, Community", "Example": "إِنَّ أُمَّتِهِۦۤ (Indeed, his nation)"},
    {"Word (Arabic)": "نصر", "Transliteration": "Nasr", "Meaning": "Victory", "Example": "إِنَّۭ نَصْرَنا (Indeed, Our victory)"},
    {"Word (Arabic)": "حلال", "Transliteration": "Halal", "Meaning": "Permissible", "Example": "إِنَّ مَا أَحَلَّ اللَّهُ (Indeed, what Allah has made permissible)"},
    {"Word (Arabic)": "حرام", "Transliteration": "Haram", "Meaning": "Forbidden", "Example": "إِنَّ مَا حَرَّمَ اللَّهُ (Indeed, what Allah has forbidden)"},
    {"Word (Arabic)": "صوم", "Transliteration": "Sawm", "Meaning": "Fasting", "Example": "فَصُمْتُ وَرَبُّكُمْ أَحْسَنُ (So I fasted and your Lord is the best)"},
    {"Word (Arabic)": "نور", "Transliteration": "Nur", "Meaning": "Light", "Example": "ٱللَّهُ نُورُ ٱلسَّمَٰوَٰتِ وَٱلۡأَرْضِ (Allah is the Light of the heavens and the earth)"},
    {"Word (Arabic)": "قادر", "Transliteration": "Qadir", "Meaning": "Capable, Powerful", "Example": "إِنَّنِيۤۦ عَلَىٰ كُلِّ شَىۡءٍۢ قَدِيرٌۭ (Indeed, I am capable of all things)"},
    {"Word (Arabic)": "عزيز", "Transliteration": "Aziz", "Meaning": "Almighty, Invincible", "Example": "إِنَّ اللَّٰهَ عَزِيزٌۭ حَكِيمٌۭ (Indeed, Allah is Exalted in Might, Wise)"},
    {"Word (Arabic)": "رحمة", "Transliteration": "Rahmah", "Meaning": "Mercy", "Example": "وَرَحْمَتِى وَسِعَتْ كُلَّ شَىۡءٍۢ (And My mercy encompasses all things)"},
    {"Word (Arabic)": "سلام", "Transliteration": "Salam", "Meaning": "Peace", "Example": "سَلاَمٌۭ قَوۡلٖا مِّن رَّبٍّ رَّحِيمٍۢ (Peace, a word from a Merciful Lord)"},
    {"Word (Arabic)": "حسن", "Transliteration": "Husn", "Meaning": "Goodness, Excellence", "Example": "إِنَّآ أَحْسَنَآ أَحْسَنَ ٱلۡمَقَالِ (Indeed, we have given the best of speech)"},
    {"Word (Arabic)": "كريم", "Transliteration": "Karim", "Meaning": "Generous, Noble", "Example": "إِنَّ اللَّٰهَ كَرِيمٌۭ حَلِيمٌۭ (Indeed, Allah is Generous and Forbearing)"},
    {"Word (Arabic)": "مؤمن", "Transliteration": "Mu’min", "Meaning": "Believer", "Example": "إِنَّمَآ ٱلۡمُؤْمِنُونَ (Indeed, the believers are)"},
    {"Word (Arabic)": "كفر", "Transliteration": "Kufr", "Meaning": "Disbelief", "Example": "وَمَآ أُتۡلِفُ كُفۡرَكُمْ (And do not destroy your disbelief)"},
    {"Word (Arabic)": "طهور", "Transliteration": "Tuhur", "Meaning": "Purity", "Example": "إِنَّمَآ أَنَاۤۡ طَهُورٌۭ (Indeed, I am pure)"},
    {"Word (Arabic)": "ذكر", "Transliteration": "Dhikr", "Meaning": "Remembrance", "Example": "إِنَّ اللَّهَ يَذۡكُرُهُۥۤ (Indeed, Allah remembers him)"},
    {"Word (Arabic)": "حق", "Transliteration": "Haqq", "Meaning": "Truth, Right", "Example": "إِنَّۢ هَٰذَا لَهُوَ الْحَقُّ (Indeed, this is the truth)"},
    {"Word (Arabic)": "باطل", "Transliteration": "Batil", "Meaning": "Falsehood", "Example": "إِنَّمَآ الْبَاطِلُ يُذْهِبُهُۥۤ (Indeed, falsehood is removed)"},
    {"Word (Arabic)": "خير", "Transliteration": "Khair", "Meaning": "Good, Benefit", "Example": "فَٱصْبِرْ إِنَّ الْخَيْرَ لَفِي (So be patient, indeed, the good is in)"},
    {"Word (Arabic)": "أمانة", "Transliteration": "Amanah", "Meaning": "Trust, Responsibility", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُمۡ أَن تُؤَدُّوا۟ ٱلْأَمَٰنَٰتِ (Indeed, Allah commands you to deliver trusts)"},
    {"Word (Arabic)": "حقيقة", "Transliteration": "Haqiqah", "Meaning": "Reality, Truth", "Example": "إِنَّ حَقَّ ٱلۡمَرْءِ فِي (Indeed, the truth of a person in)"},
    {"Word (Arabic)": "شرف", "Transliteration": "Sharaf", "Meaning": "Honor, Dignity", "Example": "إِنَّ الشَّرَفَ لِعِبَادِهِۦ (Indeed, honor is for His servants)"},
    {"Word (Arabic)": "غنى", "Transliteration": "Ghinā", "Meaning": "Wealth, Richness", "Example": "إِنَّ اللَّٰهَ غَنِيٌّۭ حَمِيدٌۭ (Indeed, Allah is Rich and Praiseworthy)"},
    {"Word (Arabic)": "عبود", "Transliteration": "Abd", "Meaning": "Servant, Slave", "Example": "إِنَّنيۤۦ عَبْدٌۭ لِلَّهِ (Indeed, I am a servant of Allah)"},
    {"Word (Arabic)": "سورة", "Transliteration": "Surah", "Meaning": "Chapter of the Quran", "Example": "قَدْ أَنزَلْنَا فِيهَا سُورَةًۭ (We have revealed a chapter in it)"},
    {"Word (Arabic)": "محراب", "Transliteration": "Mihrab", "Meaning": "Sanctuary, Niche", "Example": "فَفِى ٱلۡمِحْرَابِ (So in the niche)"},
    {"Word (Arabic)": "نداء", "Transliteration": "Nida", "Meaning": "Call, Cry", "Example": "وَإِذَا نَادَىٰ رَبُّهُۥۤ (And when his Lord called him)"},
    {"Word (Arabic)": "صادق", "Transliteration": "Sadiq", "Meaning": "Truthful", "Example": "إِنَّٱللَّهَ مَعَ ٱلصَّٰدِقِينَ (Indeed, Allah is with the truthful)"},
    {"Word (Arabic)": "سعي", "Transliteration": "Sa'i", "Meaning": "Effort, Striving", "Example": "وَفِى سَعْىٍۢ جَاءٌۭ (And in striving came)"},
    {"Word (Arabic)": "مبارك", "Transliteration": "Mubarak", "Meaning": "Blessed", "Example": "وَجَعَلۡنَٰهُۥ مُبَٰرَكٖا (And We made him blessed)"},
    {"Word (Arabic)": "طاهر", "Transliteration": "Taher", "Meaning": "Pure, Clean", "Example": "فَٱلطَّٰهِرُ فَٱطْهَرْهُۥ (So purify him, purify him)"},
    {"Word (Arabic)": "مصير", "Transliteration": "Maseer", "Meaning": "Destination, Fate", "Example": "إِنَّ ٱلۡمَصِيرَ (Indeed, the destination)"},
    {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "وَيُحْشَرُ فِيهَا مَنْ يَغْفِرُ لَهُۥ (And he will be gathered in it, whom Allah forgives)"},
    {"Word (Arabic)": "عالم", "Transliteration": "Alim", "Meaning": "Knowledgeable, Scholar", "Example": "إِنَّ ٱللَّهَ عَلِيمٌۭ حَكِيمٌۭ (Indeed, Allah is All-Knowing, All-Wise)"},
    {"Word (Arabic)": "قدوس", "Transliteration": "Quddus", "Meaning": "The Holy", "Example": "سُبْحَٰنَ رَبِّكَ رَبِّ ٱلْعِزَّةِ عَمَّا يَصِفُونَ (Glory be to Your Lord, the Lord of Honor, above what they describe)"},
    {"Word (Arabic)": "إيمان", "Transliteration": "Iman", "Meaning": "Faith, Belief", "Example": "فَٱمْرَأَتُهُۥۤ حَامِلَةٌۭ بِٱلۡإِيمَٰنِ (And his wife carried in faith)"},
    {"Word (Arabic)": "مستقيم", "Transliteration": "Mustaqim", "Meaning": "Straight, Upright", "Example": "ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ (Guide us to the straight path)"},
    {"Word (Arabic)": "جليل", "Transliteration": "Jalil", "Meaning": "Majestic", "Example": "فَٱلۡجَلِيلُ أَصْلِهِۦ (The Majestic origin)"},
    {"Word (Arabic)": "شكر", "Transliteration": "Shukr", "Meaning": "Gratitude", "Example": "وَشَٰكِرٌۭ لَّكَ إِنَّهُۥۤ أَكْبَرُ شُكْرٍۢ (And grateful to You, for it is greater than gratitude)"},
    {"Word (Arabic)": "فرح", "Transliteration": "Farah", "Meaning": "Happiness, Joy", "Example": "وَفَرِحَ بِنِعْمَتِهِۦ (And happy with His grace)"},
    {"Word (Arabic)": "رؤية", "Transliteration": "Ru’yah", "Meaning": "Vision, Sight", "Example": "رَءَآهُۥ فِى رُؤْيَآتِهِۦ (He saw it in his vision)"},
    {"Word (Arabic)": "عبادة", "Transliteration": "Ibadah", "Meaning": "Worship", "Example": "إِنَّۢ إِبَادَتِهِۦ وَرَاءَ إِيمَٰنِهِۦ (Indeed, his worship is behind his faith)"},
    {"Word (Arabic)": "قوة", "Transliteration": "Quwwah", "Meaning": "Strength, Power", "Example": "إِنَّ ٱللَّهَ قَوِيٌّۭ عَزِيزٌۭ (Indeed, Allah is Strong and Almighty)"},
    {"Word (Arabic)": "ملك", "Transliteration": "Mulk", "Meaning": "Kingdom, Dominion", "Example": "تَبَٰرَكَ الَّذِى بِيَدِهِۦ ٱلۡمُلْكُ (Blessed is the One in whose hand is the dominion)"},
    {"Word (Arabic)": "خالد", "Transliteration": "Khalid", "Meaning": "Eternal, Everlasting", "Example": "إِنَّۢ كُلَّ ٱلۡخَٰلِدِينَ فِيهَا (Indeed, all those who are eternal in it)"},
    {"Word (Arabic)": "صلاة", "Transliteration": "Salah", "Meaning": "Prayer", "Example": "وَأَقِيمُوا۟ ٱلصَّلَوٰةَ (And establish the prayer)"},
    {"Word (Arabic)": "كتاب", "Transliteration": "Kitab", "Meaning": "Book, Scripture", "Example": "إِنَّآ أَنزَلْنَآ إِلَيْكَ الْكِتَٰبَ (Indeed, We have sent down to you the Book)"},
    {"Word (Arabic)": "طريق", "Transliteration": "Tariq", "Meaning": "Path, Way", "Example": "إِنَّ ٱللَّهَ يَهْدِىٓ بِهِۦٰٓ (Indeed, Allah guides by it)"},
    {"Word (Arabic)": "أمة", "Transliteration": "Ummah", "Meaning": "Nation, Community", "Example": "إِنَّ ٱللَّهَ جَعَلَكُمۡ أُمَّةًۭ وَسَطًۭا (Indeed, Allah has made you a just community)"},
    {"Word (Arabic)": "أمان", "Transliteration": "Aman", "Meaning": "Security, Peace", "Example": "وَجَعَلْنَا لَكُمُ الأَمَٰنَ (And We made for you security)"},
    {"Word (Arabic)": "تقوى", "Transliteration": "Taqwa", "Meaning": "Piety, God-consciousness", "Example": "إِنَّ أَكْرَمَكُمْ عِندَ ٱللَّهِ أَتْقَىٰكُمْ (Indeed, the most honored of you with Allah is the most righteous among you)"},
    {"Word (Arabic)": "نصر", "Transliteration": "Nasr", "Meaning": "Victory, Help", "Example": "فَٱلۡجَٰمِعُ لَكُمْ فَإِنَّ اللّهَ نَصِيرٌۭ (And indeed, Allah is the Helper)"},
    {"Word (Arabic)": "توبة", "Transliteration": "Tawbah", "Meaning": "Repentance", "Example": "وَٱلۡمُحْسِنِينَ فَٱلۡمُجْتَٰهِدِينَ (And those who do good, striving in repentance)"},
    {"Word (Arabic)": "خوف", "Transliteration": "Khawf", "Meaning": "Fear", "Example": "إِنَّمَاۤ فِي ذَٰلِكَ خَوْفٌۭ (Indeed, in this there is fear)"},
    {"Word (Arabic)": "رحيم", "Transliteration": "Rahim", "Meaning": "Merciful", "Example": "إِنَّ ٱللَّهَ رَحِيمٌۭ بِٱلۡعَبِيدِ (Indeed, Allah is Merciful to His servants)"},
    {"Word (Arabic)": "صبر", "Transliteration": "Sabr", "Meaning": "Patience", "Example": "وَٱلصَّابِرِينَ فِى ٱلۡبَأْسَآءِ (And the patient ones in adversity)"},
    {"Word (Arabic)": "علم", "Transliteration": "Ilm", "Meaning": "Knowledge", "Example": "إِنَّۢ عَلَمَٓتِهِۦ لِيَزْدَادُ فِيهِ (Indeed, His signs increase in knowledge)"},
    {"Word (Arabic)": "جنة", "Transliteration": "Jannah", "Meaning": "Paradise, Garden", "Example": "إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلۡكَٰفِرِينَ (Indeed, Allah does not like the disbelievers)"},
    {"Word (Arabic)": "ظلم", "Transliteration": "Zulm", "Meaning": "Injustice", "Example": "وَمَا رَبُّكَ بِظَلَّٰمٍۢ لِّلۡعَبِيدِ (And your Lord is not unjust to the servants)"},
    {"Word (Arabic)": "فرد", "Transliteration": "Fard", "Meaning": "Obligatory, Singular", "Example": "إِنَّۢ ٱللَّهَ جَعَلَكُمۡ فَرَائِضَ (Indeed, Allah has made for you obligations)"},
    {"Word (Arabic)": "عصمة", "Transliteration": "Ismah", "Meaning": "Infallibility, Protection", "Example": "إِنَّهُۥۤ لَمَٰرِهُۥ فِى عِصْمَتِهِۦ (Indeed, he was in protection)"},
    {"Word (Arabic)": "غفور", "Transliteration": "Ghafur", "Meaning": "Forgiving", "Example": "إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ (Indeed, Allah is Most Forgiving, Most Merciful)"},
    {"Word (Arabic)": "حكمة", "Transliteration": "Hikmah", "Meaning": "Wisdom", "Example": "وَمَنۡ يُؤْتِ ٱلْحِكْمَةَ فَقَدْ أُوتِىَ خَيْرًۭا كَثِيرًۭا (And whoever is given wisdom has certainly been given much good)"},
    {"Word (Arabic)": "نور", "Transliteration": "Nur", "Meaning": "Light", "Example": "اللَّهُ نُورُ السَّمَٰوَٰتِ وَٱلۡأَرْضِ (Allah is the Light of the heavens and the earth)"},
    {"Word (Arabic)": "مجيد", "Transliteration": "Majid", "Meaning": "Glorious, Honorable", "Example": "إِنَّۢ رَبَّكُمۡ لَذُو مَجِيدٍۢ (Indeed, your Lord is full of glory)"},
    {"Word (Arabic)": "قوي", "Transliteration": "Qawi", "Meaning": "Strong", "Example": "إِنَّ ٱللَّهَ قَوِيٌّۭ عَزِيزٌۭ (Indeed, Allah is Strong, Almighty)"},
    {"Word (Arabic)": "غني", "Transliteration": "Ghani", "Meaning": "Self-sufficient, Rich", "Example": "إِنَّ ٱللَّهَ غَنِىٌّۭ حَمِيدٌۭ (Indeed, Allah is Self-sufficient, Praiseworthy)"},
    {"Word (Arabic)": "بر", "Transliteration": "Birr", "Meaning": "Goodness, Piety", "Example": "إِنَّ ٱللَّهَ يُحِبُّ ٱلۡمُحْسِنِينَ (Indeed, Allah loves the doers of good)"},
    {"Word (Arabic)": "دعا", "Transliteration": "Da’a", "Meaning": "To call, invoke", "Example": "دَعَوۡتُ رَبِّى لِيُحْشِرْنِى فِى جَنَّتِهِۦ (I called my Lord to gather me in His garden)"},
    {"Word (Arabic)": "خيرات", "Transliteration": "Khairat", "Meaning": "Good deeds, Charity", "Example": "إِنَّ ٱللَّهَ بِغَفْرٍۢ مِنْهُ وَرَحْمَةٍۢ (Indeed, Allah is forgiving and merciful)"},
    {"Word (Arabic)": "سلام", "Transliteration": "Salam", "Meaning": "Peace, Safety", "Example": "إِنَّۢ جَزَٰؤُهُمْ فِيهَا سَلاَمٌۭ (Indeed, their reward in it is peace)"},
    {"Word (Arabic)": "شكر", "Transliteration": "Shukr", "Meaning": "Gratitude", "Example": "فَشَٰكِرٌۭ لَّكَ إِنَّهُۥۤ أَكْبَرُ شُكْرٍۢ (And grateful to You, for it is greater than gratitude)"},
    {"Word (Arabic)": "عبد", "Transliteration": "Abd", "Meaning": "Servant, Worshipper", "Example": "إِنَّ ٱللَّهَ يُحِبُّ ٱلۡمُتَّقِينَ (Indeed, Allah loves those who are righteous)"},
    {"Word (Arabic)": "سميع", "Transliteration": "Samir", "Meaning": "All-Hearing", "Example": "إِنَّ ٱللَّهَ سَمِيعٌۭ بِمَا يَفْعَلُونَ (Indeed, Allah is All-Hearing of what they do)"},
    {"Word (Arabic)": "عظيم", "Transliteration": "Azim", "Meaning": "Great, Mighty", "Example": "إِنَّۢ رَبَّكُمْ لَذُو عَزِيزٍۢ (Indeed, your Lord is mighty)"},
    {"Word (Arabic)": "قلب", "Transliteration": "Qalb", "Meaning": "Heart, Mind", "Example": "إِنَّۢ ٱللَّهَ يَعْلَمُ مَا فِى قُلُوبِهِۦ (Indeed, Allah knows what is in the hearts)"},
    {"Word (Arabic)": "شفاء", "Transliteration": "Shifa", "Meaning": "Healing, Cure", "Example": "وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ (And when I am ill, it is He who heals me)"},
    {"Word (Arabic)": "عافية", "Transliteration": "Afiya", "Meaning": "Health, Well-being", "Example": "اللّهُمَّ بَارِكْ لِي فِي عَافِيَتِى (O Allah, bless me in my well-being)"},
    {"Word (Arabic)": "عدو", "Transliteration": "Aduw", "Meaning": "Enemy", "Example": "إِنَّۢ ٱللَّهَ يُحِبُّ ٱلۡمُتَّقِينَ (Indeed, Allah loves those who are righteous)"},
    {"Word (Arabic)": "عدالة", "Transliteration": "Adalah", "Meaning": "Justice, Fairness", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُم بِالۡعَدْلِ (Indeed, Allah commands you to act justly)"},
    {"Word (Arabic)": "طاعة", "Transliteration": "Taa’a", "Meaning": "Obedience, Compliance", "Example": "وَإِنَّمَاۤ مَا يُمْسِكُهُۥۤ لِطَاعَتِهِۦ (And whatever He withholds, it is by His command)"},
    {"Word (Arabic)": "أمانة", "Transliteration": "Amanah", "Meaning": "Trust, Responsibility", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُمْ بِأَمَٰنَٰتِكُمْ (Indeed, Allah commands you regarding trusts)"},
    {"Word (Arabic)": "خوف", "Transliteration": "Khawf", "Meaning": "Fear, Terror", "Example": "إِنَّۢ فَٱلۡمَخَٰٓفَةِ فِي قُلُوبِهِۦ (Indeed, the fear in their hearts)"},
    {"Word (Arabic)": "كريم", "Transliteration": "Karim", "Meaning": "Generous, Noble", "Example": "إِنَّ ٱللَّهَ كَرِيمٌۭ وَمَنَّ (Indeed, Allah is Generous and Gracious)"},
    {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "وَٱلۡمُغْفِرِينَ فِى ٱلۡقُرْءَانِ (And those who forgive in the Qur’an)"},
    {"Word (Arabic)": "عذاب", "Transliteration": "Adhab", "Meaning": "Punishment", "Example": "إِنَّۢ رَبَّكُمْ لَذُو عَذَابٍۢ شَدِيدٍۢ (Indeed, your Lord is the possessor of severe punishment)"},
    {"Word (Arabic)": "نور", "Transliteration": "Nur", "Meaning": "Light, Radiance", "Example": "ٱللَّهُ نُورُ السَّمَٰوَٰتِ وَٱلۡأَرْضِ (Allah is the Light of the heavens and the earth)"},
    {"Word (Arabic)": "رزق", "Transliteration": "Rizq", "Meaning": "Provision, Sustenance", "Example": "وَفَجَّرْنَا ٱلۡأَرۡضَ بِرُزْقِهِۦ (And We made the earth gush forth with its sustenance)"},
    {"Word (Arabic)": "آية", "Transliteration": "Ayah", "Meaning": "Sign, Verse", "Example": "وَجَعَلْنَا فِيهَاۤ آيَٰتٍۢ وَفَجَّرْنَا (And We made in it signs and made it flow)"},
    {"Word (Arabic)": "حياة", "Transliteration": "Hayat", "Meaning": "Life", "Example": "وَٱلۡحَيَوَٰةَ الدُّنۡيَآ (And the life of this world)"},
    {"Word (Arabic)": "خالق", "Transliteration": "Khalik", "Meaning": "Creator", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلۡخَٰلِقُ (Indeed, Allah is the Creator)"},
    {"Word (Arabic)": "بركة", "Transliteration": "Barakah", "Meaning": "Blessing", "Example": "يُحْشَرُ فِيهَا بِرَٰكَتٍۢ (It will be gathered in a blessed way)"},
    {"Word (Arabic)": "تقوى", "Transliteration": "Taqwa", "Meaning": "Piety, God-fearing", "Example": "وَٱتَّقُواْ ٱللَّهَ لَعَلَّكُمْ تُرْحَمُونَ (And fear Allah so that you may receive mercy)"},
    {"Word (Arabic)": "حكم", "Transliteration": "Hukm", "Meaning": "Judgment, Ruling", "Example": "إِنَّ ٱللَّهَ حَكِيمٌۭ عَلِيمٌۭ (Indeed, Allah is Wise, All-Knowing)"},
    {"Word (Arabic)": "سلطان", "Transliteration": "Sultan", "Meaning": "Authority, Power", "Example": "إِنَّ ٱللَّهَ لَا يَظْلِمُ ٱحَدًۭا فِى سُلۡطَٰنِهِۦ (Indeed, Allah does not wrong anyone in His dominion)"},
    {"Word (Arabic)": "حمد", "Transliteration": "Hamd", "Meaning": "Praise", "Example": "ٱلۡحَمْدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ (Praise be to Allah, Lord of the worlds)"},
    {"Word (Arabic)": "صلاة", "Transliteration": "Salat", "Meaning": "Prayer", "Example": "إِنَّٓاٰنِّيۡ أُحِبُّ صَلَاةًۭ لَّا تَعْلَمُونَ (Indeed, I love prayer that you do not know)"},
    {"Word (Arabic)": "عدو", "Transliteration": "Adu", "Meaning": "Enemy", "Example": "وَفِى قُلُوبِهِۦۤ عَدَاءٌۭ (And in their hearts is enmity)"},
    {"Word (Arabic)": "قريب", "Transliteration": "Qareeb", "Meaning": "Near, Close", "Example": "إِنَّۢ رَبَّكُمْ لَقَرِيبٌۭ (Indeed, your Lord is near)"},
    {"Word (Arabic)": "رحمن", "Transliteration": "Rahman", "Meaning": "The Beneficent", "Example": "ٱلرَّحْمَٰنِ عَلَى ٱلۡعَرۡشِ ٱسْتَوَىٰ (The Beneficent, who is above the Throne)"},
    {"Word (Arabic)": "جميل", "Transliteration": "Jameel", "Meaning": "Beautiful", "Example": "إِنَّۢ ٱللَّهَ جَمِيلٌۭ يُحِبُّ ٱلۡجَمَٰلَ (Indeed, Allah is Beautiful and loves beauty)"},
    {"Word (Arabic)": "شمس", "Transliteration": "Shams", "Meaning": "Sun", "Example": "وَجَعَلْنَا ٱلشَّمْسَ سِرَاجًا وَهَّاجًۭا (And We made the sun a shining lamp)"},
    {"Word (Arabic)": "مؤمن", "Transliteration": "Mu’min", "Meaning": "Believer", "Example": "إِنَّٱلۡمُؤْمِنِينَ وَٱلۡمُؤْمِنَٰتِ (Indeed, the believing men and believing women)"},
    {"Word (Arabic)": "عزيز", "Transliteration": "Aziz", "Meaning": "Mighty, Strong", "Example": "إِنَّٱللَّهَ عَزِيزٌۭ حَكِيمٌۭ (Indeed, Allah is Almighty, Wise)"},
    {"Word (Arabic)": "آيات", "Transliteration": "Ayat", "Meaning": "Signs, Verses", "Example": "إِنَّۢ فِى ذَٰلِكَ لَآيَٰتٍۢ لِّلۡمُؤْمِنِينَ (Indeed, in that are signs for the believers)"},
    {"Word (Arabic)": "خلق", "Transliteration": "Khalq", "Meaning": "Creation", "Example": "إِنَّ اللَّهَ خَلَقَ السَّمَٰوَٰتِ وَالْأَرْضَ فِي سِتَّةِ أَيَّامٍ (Indeed, Allah created the heavens and the earth in six days)"},
    {"Word (Arabic)": "سمع", "Transliteration": "Sama'a", "Meaning": "Hearing", "Example": "إِنَّ اللَّهَ سَمِيعٌ عَلِيمٌ (Indeed, Allah is Hearing and Knowing)"},
    {"Word (Arabic)": "بصر", "Transliteration": "Basar", "Meaning": "Sight", "Example": "إِنَّ اللَّهَ بَصِيرٌ بِمَا تَعْمَلُونَ (Indeed, Allah is All-Seeing of what you do)"},
    {"Word (Arabic)": "علم", "Transliteration": "Ilm", "Meaning": "Knowledge", "Example": "يُعَلِّمُكُمُ اللَّهُ وَاللَّهُ بِكُلِّ شَيْءٍ عَلِيمٌ (Allah teaches you, and Allah is Knowing of all things)"},
    {"Word (Arabic)": "كلمة", "Transliteration": "Kalima", "Meaning": "Word", "Example": "وَقَوْلُهُۥٓ حَقٌّ (And His word is truth)"},
    {"Word (Arabic)": "عبادة", "Transliteration": "Ibadah", "Meaning": "Worship", "Example": "وَمَآ خَلَقْتُ الْجِنَّ وَالإِنسَ إِلَّا لِيَعْبُدُونِ (And I did not create the jinn and mankind except to worship Me)"},
    {"Word (Arabic)": "نعمة", "Transliteration": "Ni’mah", "Meaning": "Blessing", "Example": "وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَعَمْنَا عَلَيْهِمْ (And do not be like those upon whom We have bestowed favor)"},
    {"Word (Arabic)": "فقر", "Transliteration": "Faqr", "Meaning": "Poverty", "Example": "إِنَّمَا ٱلۡمُؤْمِنُونَ إِخْوَةٌۢ فَأَصْلِحُوا۟ بَيْنَ أَخَوَيْكُمْ (Indeed, the believers are but brothers)"},
    {"Word (Arabic)": "غني", "Transliteration": "Ghani", "Meaning": "Rich, Self-sufficient", "Example": "إِنَّ اللَّهَ غَنِيٌّۭ حَمِيدٌ (Indeed, Allah is Self-Sufficient, Praiseworthy)"},
    {"Word (Arabic)": "شكر", "Transliteration": "Shukr", "Meaning": "Gratitude", "Example": "لَئِن شَكَرْتُمْ لَأَزِيدَنَّكُمْ (If you are grateful, I will surely increase your favor upon you)"},
    {"Word (Arabic)": "حج", "Transliteration": "Hajj", "Meaning": "Pilgrimage", "Example": "وَأَذِّنْ فِي النَّاسِ بِالْحَجِّ يَأْتُوكَ رِجَالًا (And proclaim to the people the Hajj)"},
    {"Word (Arabic)": "حرام", "Transliteration": "Haram", "Meaning": "Forbidden", "Example": "وَإِنَّهُۥ فَٱلۡمُحَرَّمَاتِ عَلَيۡكُم (And indeed, the prohibited are for you)"},
    {"Word (Arabic)": "حلال", "Transliteration": "Halal", "Meaning": "Permissible", "Example": "إِنَّمَا حِلَّتِ ٱلۡمَسَٰجِدُ لِلَّهِ (Indeed, the mosques are for Allah)"},
    {"Word (Arabic)": "رزق", "Transliteration": "Rizq", "Meaning": "Provision, Sustenance", "Example": "وَمَآ أَتَاكُمْ مِّن رَّحْمَةٍۢ فَمِنْهُۥ (And whatever mercy has come to you is from Him)"},
    {"Word (Arabic)": "حسن", "Transliteration": "Husn", "Meaning": "Goodness, Excellence", "Example": "وَإِنَّكَ لَعَلَىٰ خُلُقٍ عَظِيمٍ (And indeed, you are of a great moral character)"},
    {"Word (Arabic)": "بشرى", "Transliteration": "Bushra", "Meaning": "Good Tidings", "Example": "فَبَشِّرْهُم بِجَنَّةٍ تَجْرِي مِن تَحْتِهَا (So give them glad tidings of a garden beneath which rivers flow)"},
    {"Word (Arabic)": "دعوة", "Transliteration": "Dawah", "Meaning": "Call, Invitation", "Example": "وَادْعُوۡا۟ إِلَىٰ رَبِّكِ (And call to your Lord)"},
    {"Word (Arabic)": "نعيم", "Transliteration": "Na’im", "Meaning": "Bliss, Comfort", "Example": "إِنَّ أَهْلَ ٱلْجَنَّةِ فِى نَعِيمٍۢ (Indeed, the people of Paradise are in bliss)"},
    {"Word (Arabic)": "صبر", "Transliteration": "Sabr", "Meaning": "Patience", "Example": "وَبَشِّرِ ٱلصَّٰبِرِينَ (And give good tidings to the patient)"},
    {"Word (Arabic)": "عدل", "Transliteration": "Adl", "Meaning": "Justice", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُم بِالْعَدْلِ (Indeed, Allah commands justice)"},
    {"Word (Arabic)": "قوة", "Transliteration": "Quwah", "Meaning": "Strength, Power", "Example": "وَأَعِزَّنِي بِالْقُوَّةِ وَاللَّيْلِ (And strengthen me with strength)"},
    {"Word (Arabic)": "خوف", "Transliteration": "Khawf", "Meaning": "Fear", "Example": "إِنَّٱللَّهَ يُحِبُّ ٱلۡمُتَّقِينَ (Indeed, Allah loves the righteous)"},
    {"Word (Arabic)": "علماء", "Transliteration": "Ulama", "Meaning": "Scholars", "Example": "إِنَّ ٱلْعُلَمَٰٓءَ وَرَثَةُ ٱلْأَنْبِيَاءِ (Indeed, the scholars are the heirs of the Prophets)"},
    {"Word (Arabic)": "سلام", "Transliteration": "Salaam", "Meaning": "Peace, Safety", "Example": "وَإِذَا حُيِّيتُمْ بِتَحِيَّةٍۢ فَحَيُّوا۟ بِأَحْسَنَ مِنْهَا (And when you are greeted with a greeting, greet with something better)"},
    {"Word (Arabic)": "لطف", "Transliteration": "Lutf", "Meaning": "Kindness, Gentleness", "Example": "فَٱلۡتَفَتۡتُ فِيهِمۡ لُطْفًۭا (And I became gentle among them)"},
    {"Word (Arabic)": "عفو", "Transliteration": "Afw", "Meaning": "Forgiveness", "Example": "إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌ (Indeed, Allah is Forgiving and Merciful)"},
    {"Word (Arabic)": "هداية", "Transliteration": "Hidayah", "Meaning": "Guidance", "Example": "إِنَّ عَلَيْنَا لِلْهُدَىٰ (Indeed, upon Us is guidance)"},
    {"Word (Arabic)": "أمة", "Transliteration": "Ummah", "Meaning": "Nation, Community", "Example": "إِنَّ هَٰذِهِۦٓ أُمَّتُكُمْ أُمَّةًۭ وَٰحِدَةًۭ (Indeed, this is your nation, one nation)"},
    {"Word (Arabic)": "صديق", "Transliteration": "Siddiq", "Meaning": "Truthful, Companion", "Example": "إِنَّ ٱللَّهَ مَعَ ٱلۡصَّٰدِقِينَ (Indeed, Allah is with the truthful)"},
    {"Word (Arabic)": "موت", "Transliteration": "Mawt", "Meaning": "Death", "Example": "وَلَا تَقُولُوا۟ لِمَن يُقْتَلُ فِى سَبِيلِ ٱللَّهِ أَمْوَٰتٌۭ (And do not say of those who are killed in the way of Allah that they are dead)"},
    {"Word (Arabic)": "نصر", "Transliteration": "Nasr", "Meaning": "Victory, Help", "Example": "إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلۡفَتْحُ (When the victory of Allah has come and the conquest)"},
    {"Word (Arabic)": "علمي", "Transliteration": "Ilmi", "Meaning": "My Knowledge", "Example": "قَالَ رَبُّكَمْ يَعْلَمُ مَا فِى السَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ (Your Lord knows what is in the heavens and what is on the earth)"},
    {"Word (Arabic)": "نوايا", "Transliteration": "Nawaya", "Meaning": "Intention", "Example": "إِنَّمَآ ٱلْأَعْمَٰلُ بِالنِّيَّاتِ (Indeed, actions are by intentions)"},
    {"Word (Arabic)": "سورة", "Transliteration": "Surah", "Meaning": "Chapter", "Example": "وَفِى سُورَةٍۢ لَّاٰتِينَ (And in a surah that does not deny)"},
    {"Word (Arabic)": "هدى", "Transliteration": "Huda", "Meaning": "Guidance", "Example": "إِنَّكَ لَا تَحْتَسِبُ إِنَّ اللَّهَ هَادِيۡ (Indeed, Allah is the Guide)"},
    {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "وَٱلۡمُغۡفِرَٰتِ لَكُمْ فَٱلۡمُحِبُّ (And the forgiveness of your Lord)"},
    {"Word (Arabic)": "قلب", "Transliteration": "Qalb", "Meaning": "Heart", "Example": "إِنَّ قُلُوبَكُمْ فِى فِتْنَةٍۢ (Indeed, your hearts are in turmoil)"},
    {"Word (Arabic)": "حب", "Transliteration": "Hubb", "Meaning": "Love", "Example": "وَٱلَّذِينَ ءَامَنُوا۟ أَشَدُّ حُبًّۭا لِّي (And those who believe are stronger in love for Him)"},
    {"Word (Arabic)": "عزة", "Transliteration": "Izzah", "Meaning": "Honor, Glory", "Example": "وَإِنَّ ٱللَّهَ سَمِيعٌۭ عَلِيمٌ (Indeed, Allah is All-Hearing, All-Knowing)"},
    {"Word (Arabic)": "حياة", "Transliteration": "Hayah", "Meaning": "Life", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلۡحَىُّۖ (Indeed, Allah is the Ever-Living)"},
    {"Word (Arabic)": "جنة", "Transliteration": "Jannah", "Meaning": "Paradise", "Example": "إِنَّ الَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ فِي جَنَّٰتٍۢ لَّهُمْ (Indeed, those who believe and do righteous deeds will have gardens)"},
    {"Word (Arabic)": "نار", "Transliteration": "Nar", "Meaning": "Fire", "Example": "إِنَّ جَهَنَّمَ لَتُحْشَرُ بِهَا الْكَافِرُونَ (Indeed, Hell is a fire that will burn them)"},
    {"Word (Arabic)": "رحيم", "Transliteration": "Rahim", "Meaning": "Merciful", "Example": "إِنَّ اللَّهَ رَحِيمٌۭ بِالۡعِبَادِ (Indeed, Allah is Merciful to His servants)"},
    {"Word (Arabic)": "غفور", "Transliteration": "Ghafur", "Meaning": "Forgiving", "Example": "إِنَّ رَبَّكَ غَفُورٌۭ رَّحِيمٌ (Indeed, your Lord is Forgiving and Merciful)"},
    {"Word (Arabic)": "نور", "Transliteration": "Nur", "Meaning": "Light", "Example": "اللَّهُ نُورُ السَّمَٰوَٰتِ وَالْأَرْضِ (Allah is the Light of the heavens and the earth)"},
    {"Word (Arabic)": "قوم", "Transliteration": "Qaum", "Meaning": "People, Nation", "Example": "وَمَآ أَرْسَلْنَٰكَ إِلَّا كَٰفَّةًۭ لِّلنَّاسِ (And We have not sent you except to all mankind)"},
    {"Word (Arabic)": "دنيا", "Transliteration": "Dunya", "Meaning": "Worldly life", "Example": "تُحِبُّونَ ٱلۡحَيَوٰةَ ٱلدُّنْيَا (You love the life of this world)"},
    {"Word (Arabic)": "آخرة", "Transliteration": "Akhira", "Meaning": "Hereafter", "Example": "وَٱلۡبَٰتِلَٰتِ (And the Hereafter is better and everlasting)"},
    {"Word (Arabic)": "كتاب", "Transliteration": "Kitab", "Meaning": "Book", "Example": "إِنَّا أَنزَلْنَا عَلَيْكَ الْكِتَٰبَ بِالْحَقِّ (Indeed, We have sent down to you the Book in truth)"},
    {"Word (Arabic)": "مؤمن", "Transliteration": "Mu’min", "Meaning": "Believer", "Example": "إِنَّمَا ٱلۡمُؤْمِنُونَ إِخْوَةٌۭ (Indeed, the believers are brothers)"},
    {"Word (Arabic)": "كافر", "Transliteration": "Kafir", "Meaning": "Disbeliever", "Example": "إِنَّ الَّذِينَ كَفَرُوا۟ وَجَحَدُوا۟ بِالۡعَادَٰتِ (Indeed, those who disbelieve and reject the Signs)"},
    {"Word (Arabic)": "فعل", "Transliteration": "Fi’l", "Meaning": "Action", "Example": "وَفَعَلُوا۟ مَا فَعَلُوا۟ (And they did what they did)"},
    {"Word (Arabic)": "مغنم", "Transliteration": "Maghnam", "Meaning": "Gain, Spoil", "Example": "وَفَاءًۭ مِّنَ ٱللَّهِ وَرَحْمَةًۭ (A gain from Allah and a mercy)"},
    {"Word (Arabic)": "مفتاح", "Transliteration": "Miftah", "Meaning": "Key", "Example": "وَفَجَّرْنَا ٱلۡمَعَٰنِ فَجَّرْنَا فَجًّۭا (And We caused the fountains to gush)"},
    {"Word (Arabic)": "أمر", "Transliteration": "Amr", "Meaning": "Command, Matter", "Example": "إِنَّمَآ أَمْرُهُۥٓ إِذَآ أَرَادَ (Indeed, His command is when He intends)"},
    {"Word (Arabic)": "مقام", "Transliteration": "Maqam", "Meaning": "Station, Position", "Example": "وَإِنَّهُۥ لَفِى مَقَامٍۢ كَرِيمٍۢ (And indeed, he is in a noble position)"},
    {"Word (Arabic)": "بر", "Transliteration": "Birr", "Meaning": "Righteousness", "Example": "وَقُولُوا۟ لِلنَّاسِ حُسْنًۭا (And speak to people good)"},
    {"Word (Arabic)": "فكر", "Transliteration": "Fikr", "Meaning": "Thought, Reflection", "Example": "وَفَكَرُوا۟ فِىٓ أَمْرِهِۦۖ (And they reflected on their matter)"},
    {"Word (Arabic)": "هدية", "Transliteration": "Hadiyah", "Meaning": "Gift, Offering", "Example": "وَمَآ أَتَىٰكُم مِّنْ هَدِيَّةٍۢ (And whatever gift has come to you)"},
    {"Word (Arabic)": "قضاء", "Transliteration": "Qada’a", "Meaning": "Decree", "Example": "فَقَضۡنَآ إِلَيْهِ (And We decreed to him)"},
    {"Word (Arabic)": "مائدة", "Transliteration": "Ma’idah", "Meaning": "Table, Feast", "Example": "إِذْ قَالَ الْحَوَارِيُّونَ يَا عِيسَىٰ (When the disciples said, 'O Jesus')"},
    {"Word (Arabic)": "ضيافة", "Transliteration": "Diyafah", "Meaning": "Hospitality", "Example": "فَذُوقُوا۟ بِمَا كُنتُمْ تَكْسِبُونَ (Taste the punishment for what you used to earn)"},
    {"Word (Arabic)": "محراب", "Transliteration": "Mihrab", "Meaning": "Sanctuary, Niche", "Example": "وَدَخَلَ الْمِحْرَابَ فَصَلَّىٰ (And he entered the sanctuary and prayed)"},
    {"Word (Arabic)": "سعي", "Transliteration": "Sa’y", "Meaning": "Effort", "Example": "إِنَّ سَعْيَكُمْ لَشَتَّىٰ (Indeed, your efforts are diverse)"},
    {"Word (Arabic)": "إيمان", "Transliteration": "Iman", "Meaning": "Faith, Belief", "Example": "إِنَّمَآ أَمَٰنَكُمْ إِذَآ آمَنُوا۟ (Indeed, the true believers are those who believe in Allah)"},
    {"Word (Arabic)": "حكمة", "Transliteration": "Hikmah", "Meaning": "Wisdom", "Example": "يُؤْتِى ٱلْحِكْمَةَ مَن يَشَآءُ (He gives wisdom to whom He wills)"},
    {"Word (Arabic)": "غنى", "Transliteration": "Ghina", "Meaning": "Wealth, Self-sufficiency", "Example": "إِنَّ ٱللَّهَ غَنيٌّۭ حَمِيدٌ (Indeed, Allah is Free of need, Worthy of praise)"},
    {"Word (Arabic)": "صبر", "Transliteration": "Sabr", "Meaning": "Patience", "Example": "وَصَابِرِينَ وَصَابِرَٰتٍۢ (And the patient men and the patient women)"},
    {"Word (Arabic)": "رغبة", "Transliteration": "Raghbah", "Meaning": "Desire, Wish", "Example": "وَإِنَّمَآ أَمْرُهُۥٓ إِذَآ أَرَادَ (And indeed, His command is when He intends)"},
    {"Word (Arabic)": "ماء", "Transliteration": "Ma’a", "Meaning": "Water", "Example": "وَجَعَلْنَا مِنَ ٱلۡمَاءِ كُلَّ شَىْءٍۢ حَىٍّ (And We made from water every living thing)"},
    {"Word (Arabic)": "نعم", "Transliteration": "Na’am", "Meaning": "Blessing, Favor", "Example": "وَإِن تَعُدُّوا۟ نِعْمَتَ ٱللَّهِ لَا تُحۡصُوهَا (And if you count the favors of Allah, you will not be able to number them)"},
    {"Word (Arabic)": "طاعة", "Transliteration": "Ta’ah", "Meaning": "Obedience", "Example": "وَطَاعَتُهُۥ فِى دِينِهِۦۚ (And His obedience in His religion)"},
    {"Word (Arabic)": "كلمة", "Transliteration": "Kalima", "Meaning": "Word, Statement", "Example": "قَالَتِ ٱمْرَأَتُ فِرْعَوْنَ (The wife of Pharaoh said)"},
    {"Word (Arabic)": "دين", "Transliteration": "Din", "Meaning": "Religion, Way of life", "Example": "إِنَّ ٱلدِّينَ عِندَ ٱللَّهِ ٱلۡإِسْلَٰمُ (Indeed, the religion in the sight of Allah is Islam)"},
    {"Word (Arabic)": "سر", "Transliteration": "Sirr", "Meaning": "Secret", "Example": "قُلْ لِّذِينَ كَفَرُوا۟ إِن كَانَتْ فِى قُلُوبِهِۦٓمْ (Say to those who disbelieve, if they believe in what is hidden in their hearts)"},
    {"Word (Arabic)": "مؤمنون", "Transliteration": "Mu’minun", "Meaning": "Believers", "Example": "إِنَّ ٱلۡمُؤْمِنِينَ وَٱلۡمُؤْمِنَٰتِ (Indeed, the believing men and believing women)"},
    {"Word (Arabic)": "حلال", "Transliteration": "Halal", "Meaning": "Permissible", "Example": "وَأَحَلَّ اللَّهُ ٱلۡبَيِّ (And Allah has made lawful the sale)"},
    {"Word (Arabic)": "حرام", "Transliteration": "Haram", "Meaning": "Forbidden", "Example": "وَٱلۡخُمُرَ وَٱلْمَيْسِرَ حَرَّمَۚ (And intoxicants and gambling are forbidden)"},
    {"Word (Arabic)": "صلاة", "Transliteration": "Salah", "Meaning": "Prayer", "Example": "إِنَّمَآ أُمِرُوا۟ أَنْ يُصَلُّوا۟ (Indeed, they were commanded to pray)"},
    {"Word (Arabic)": "زكاة", "Transliteration": "Zakah", "Meaning": "Almsgiving", "Example": "وَأَقِيمُوا۟ ٱلصَّلَاةَ وَآتُوا۟ الزَّكَاةَ (And establish prayer and give zakah)"},
    {"Word (Arabic)": "الحق", "Transliteration": "Al-Haq", "Meaning": "The Truth", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلْحَقُّۚ (Indeed, Allah is the Truth)"},
    {"Word (Arabic)": "قدرة", "Transliteration": "Qudrah", "Meaning": "Power", "Example": "وَٱللَّهُ عَلَىٰ كُلِّ شَىْءٍۢ قَدِيرٌۭ (And Allah is capable of all things)"},
    {"Word (Arabic)": "قضاء", "Transliteration": "Qada", "Meaning": "Decree, Judgment", "Example": "وَقَضَىٰ رَبُّكَ (And your Lord has decreed)"},
    {"Word (Arabic)": "رحمة", "Transliteration": "Rahmah", "Meaning": "Mercy", "Example": "وَرَحْمَتُهُۥ وَرَحِيمٌۭ (His mercy is vast and all-encompassing)"},
    {"Word (Arabic)": "عذاب", "Transliteration": "Adhab", "Meaning": "Punishment", "Example": "فَذُوقُوا۟ بِمَا كُنتُمْ تَكْسِبُونَ (So taste the punishment for what you earned)"},
    {"Word (Arabic)": "إجابة", "Transliteration": "Ijabah", "Meaning": "Response, Answer", "Example": "وَإِذَا سَأَلَكَ عِبَادِى عَنِّىۚ (And when My servants ask you concerning Me)"},
    {"Word (Arabic)": "رسالة", "Transliteration": "Risalah", "Meaning": "Message", "Example": "إِنَّمَآ أُو۟حِىٓ إِلَىٰٓ (Indeed, I am sent only as a messenger)"},
    {"Word (Arabic)": "شكر", "Transliteration": "Shukr", "Meaning": "Gratitude", "Example": "فَاشْكُرُوا۟ لِى وَلَا تَكْفُرُونِ (So be grateful to Me and do not deny Me)"},
    {"Word (Arabic)": "فتنة", "Transliteration": "Fitnah", "Meaning": "Trial, Temptation", "Example": "وَٱلۡفِتْنَةُ أَشَدُّ مِنَ ٱلۡقَتْلِ (And trial is worse than killing)"},
    {"Word (Arabic)": "عقل", "Transliteration": "Aql", "Meaning": "Mind, Intellect", "Example": "إِنَّ فِى ذَٰلِكَ لَآيَٰتٍ لِّي أُو۟لِى ٱلْأَلْبَابِ (Indeed, in that are signs for those of understanding)"},
    {"Word (Arabic)": "أمانة", "Transliteration": "Amanah", "Meaning": "Trust, Deposit", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُمْ أَنْ تُؤَدُّوا۟ ٱلْأَمَٰنَٰتِ (Indeed, Allah commands you to return trusts)"},
    {"Word (Arabic)": "بركة", "Transliteration": "Barakah", "Meaning": "Blessing, Increase", "Example": "فَٱلَّذِينَ يَحْتَسُونَ ٱلْمَاءَ لَهُمْ فِيهِ بَرَكَهٌۭ (Those who drink the water will find blessings in it)"},
    {"Word (Arabic)": "هدى", "Transliteration": "Hudah", "Meaning": "Guidance", "Example": "وَإِنَّكَ لَتَهْدِىٓ إِلَىٰ صِرَٰطٍ مُسْتَقِيمٍ (And indeed, you guide to a straight path)"},
    {"Word (Arabic)": "شهادة", "Transliteration": "Shahadah", "Meaning": "Testimony, Witness", "Example": "شَهِدَ اللَّهُ أَنَّهُۥ لَآ إِلٰهَ إِلَّا هُوَ (Allah bears witness that there is no god but Him)"},
    {"Word (Arabic)": "خوف", "Transliteration": "Khauf", "Meaning": "Fear", "Example": "وَقُلْ رَبِّ أَعُوذُ بِكَ مِنْ خَوْفٍۢ (And say, 'My Lord, I seek refuge in You from fear')"},
    {"Word (Arabic)": "سلام", "Transliteration": "Salam", "Meaning": "Peace", "Example": "فَسَلاَمٌۭ لَكَ مِنْ أَصْحَابِ ٱلْيَمِينِ (So peace be upon you from the companions of the right)"},
    {"Word (Arabic)": "كفار", "Transliteration": "Kuffar", "Meaning": "Disbelievers", "Example": "إِنَّ ٱلۡمُكَذِّبِينَ بِالۡمِلَّةِ ٱلۡكُفَّارِ (Indeed, the disbelievers are the ones who deny the truth)"},
    {"Word (Arabic)": "سلامة", "Transliteration": "Salamah", "Meaning": "Safety, Health", "Example": "فَسَلِّمُوا۟ عَلَيْهِمْ بِسَلاَمٍۢ (Then greet them with a greeting of peace)"},
    {"Word (Arabic)": "عدل", "Transliteration": "Adl", "Meaning": "Justice, Fairness", "Example": "إِنَّ ٱللَّهَ يَأْمُرُكُمْ بِالْعَدْلِ وَالْإِحْسَٰنِ (Indeed, Allah commands justice and the doing of good)"},
    {"Word (Arabic)": "نور", "Transliteration": "Nur", "Meaning": "Light", "Example": "ٱللَّهُ وَلِيُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَىٰ النُّورِ (Allah is the protector of those who believe, He brings them out of darkness into the light)"},
    {"Word (Arabic)": "غضب", "Transliteration": "Ghadab", "Meaning": "Anger", "Example": "وَٱللَّهُ غَضِبَ عَلَيْهِمْ (And Allah became angry with them)"},
    {"Word (Arabic)": "قلب", "Transliteration": "Qalb", "Meaning": "Heart", "Example": "فِي قُلُوبِهِمْ مَرَضٌۭ (In their hearts is a disease)"},
    {"Word (Arabic)": "جنة", "Transliteration": "Jannah", "Meaning": "Paradise, Garden", "Example": "إِنَّ ٱلۡمُتَّقِينَ فِى جَنَّٰتٍ وَنَعِيمٍۢ (Indeed, the righteous will be in gardens and delight)"},
    {"Word (Arabic)": "كريم", "Transliteration": "Karim", "Meaning": "Generous, Noble", "Example": "إِنَّ رَبَّكُمْ لَذُو فَضْلٍۢ عَلَىٰ (Indeed, your Lord is full of bounty)"},
    {"Word (Arabic)": "عدو", "Transliteration": "Aduww", "Meaning": "Enemy", "Example": "إِنَّ عَدُوَّكُمُ الشَّيْطَٰنُ (Indeed, your enemy is the devil)"},
    {"Word (Arabic)": "صمت", "Transliteration": "Samt", "Meaning": "Silence", "Example": "وَمَنۢ صَمَتَ نَجَا (Whoever remains silent is safe)"},
    {"Word (Arabic)": "شكرًا", "Transliteration": "Shukran", "Meaning": "Thank you", "Example": "قُلْ شُكْرًا لِّلَّهِ (Say, 'Thank you to Allah')"},
    {"Word (Arabic)": "قوة", "Transliteration": "Quwwah", "Meaning": "Strength", "Example": "وَأَعِزَّنِى بِقُوَّتِهِۦ (And grant me strength through Your power)"},
    {"Word (Arabic)": "صراع", "Transliteration": "Sira’a", "Meaning": "Struggle", "Example": "وَمَآ كُنتُمُ فِى ٱلۡصِّرَاعِ (And you were not in the struggle)"},
    {"Word (Arabic)": "سورة", "Transliteration": "Surah", "Meaning": "Chapter, Surah", "Example": "وَقُرْءَٰنًا فَرَقْنَٰهُ لِيَتْلُوهُ عَلَىٰكُ (And a Qur’an that We have divided for you to recite)"},
    {"Word (Arabic)": "قضاء", "Transliteration": "Qada’a", "Meaning": "Decree", "Example": "قَدْ قَضَتْ قَضَاءًۭ وَإِنَّ اللَّٰهِ قَٰضٍۢ (He decreed it as a judgment, and indeed, Allah is the best of judges)"},
    {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "فَٱغْفِرْ لِىٰ إِنَّكَ أَنتَ ٱلْغَفُورُ (So forgive me, indeed, You are the Forgiving)"},

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
