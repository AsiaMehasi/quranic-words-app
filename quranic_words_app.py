import streamlit as st
import pandas as pd

quranic_words = [
    {"Word (Arabic)": "و", "Transliteration": "Wa", "Meaning": "And", "Example": "وَٱلۡعَصۡرِ (By Time)"},
    {"Word (Arabic)": "في", "Transliteration": "Fi", "Meaning": "In, Inside", "Example": "فِي ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِ (In the heavens and the earth)"},
    {"Word (Arabic)": "من", "Transliteration": "Min", "Meaning": "From, Of", "Example": "مِنَ ٱلۡجِنَّةِ وَٱلنَّاسِ (From among the jinn and mankind)"},
    {"Word (Arabic)": "على", "Transliteration": "'Ala", "Meaning": "On, Upon", "Example": "وَعَلَىٰ ٱللَّهِ فَلۡيَتَوَكَّلِ ٱلۡمُؤۡمِنُونَ (And upon Allah let the believers rely)"},
    {"Word (Arabic)": "إلى", "Transliteration": "Ila", "Meaning": "To, Towards", "Example": "يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُواْ تُوبُوٓاْ إِلَى ٱللَّهِ (O believers, repent to Allah)"},
    {"Word (Arabic)": "الله", "Transliteration": "Allah", "Meaning": "God", "Example": "إِنَّ ٱللَّهَ غَفُورٞ رَّحِيمٞ (Indeed, Allah is Forgiving and Merciful)"},
    {"Word (Arabic)": "كتاب", "Transliteration": "Kitab", "Meaning": "Book", "Example": "ذَٰلِكَ ٱلۡكِتَٰبُ لَا رَيۡبَ فِيهِ (That is the Book, there is no doubt in it)"},
    {"Word (Arabic)": "يوم", "Transliteration": "Yawm", "Meaning": "Day", "Example": "مَٰلِكِ يَوۡمِ ٱلدِّينِ (Master of the Day of Judgment)"},
    {"Word (Arabic)": "خلق", "Transliteration": "Khalaqa", "Meaning": "He created", "Example": "خَلَقَ ٱللَّهُ ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضَ (Allah created the heavens and the earth)"},
    {"Word (Arabic)": "جنة", "Transliteration": "Jannah", "Meaning": "Paradise", "Example": "وَسِيقَ ٱلَّذِينَ ٱتَّقَوۡاْ رَبَّهُمۡ إِلَى ٱلۡجَنَّةِ زُمَرًا (And those who feared their Lord were driven to Paradise in groups)"},
    {"Word (Arabic)": "نار", "Transliteration": "Naar", "Meaning": "Fire (Hellfire)", "Example": "وَقُودُهَا ٱلنَّاسُ وَٱلۡحِجَارَةُ (Its fuel is people and stones)"},
    {"Word (Arabic)": "رحمة", "Transliteration": "Rahma", "Meaning": "Mercy", "Example": "وَرَحۡمَتِي وَسِعَتۡ كُلَّ شَيۡءٖ (And My Mercy encompasses all things)"},
    {"Word (Arabic)": "قال", "Transliteration": "Qala", "Meaning": "He said", "Example": "قَالَ إِنِّيٓ أَعۡلَمُ مَا لَا تَعۡلَمُونَ (He said, 'Indeed, I know what you do not know')"},
    {"Word (Arabic)": "كان", "Transliteration": "Kana", "Meaning": "He was", "Example": "كَانَ ٱللَّهُ غَفُورٗا رَّحِيمٗا"},
    {"Word (Arabic)": "عمل", "Transliteration": "'Amila", "Meaning": "He did, Worked", "Example": "وَعَمِلُواْ ٱلصَّٰلِحَٰتِ"},
    {"Word (Arabic)": "علم", "Transliteration": "'Alima", "Meaning": "He knew", "Example": "وَٱللَّهُ يَعۡلَمُ مَا فِي قُلُوبِكُمۡ"},
    {"Word (Arabic)": "سمع", "Transliteration": "Sami'a", "Meaning": "He heard", "Example": "إِنَّ رَبِّي لَسَمِيعُ ٱلدُّعَآءِ"},
    {"Word (Arabic)": "هدى", "Transliteration": "Huda", "Meaning": "Guidance", "Example": "هُدًى لِّلۡمُتَّقِينَ (A guidance for the righteous)"},
    {"Word (Arabic)": "عذاب", "Transliteration": "Azaab", "Meaning": "Punishment", "Example": "وَإِنَّ عَذَابِي هُوَ ٱلۡعَذَابُ ٱلۡأَلِيمُ (Indeed, My punishment is the painful punishment)"},
    {"Word (Arabic)": "نور", "Transliteration": "Noor", "Meaning": "Light", "Example": "يَهۡدِي ٱللَّهُ لِنُورِهِۦ مَن يَشَآءُ (Allah guides to His light whom He wills)"},
    {"Word (Arabic)": "حق", "Transliteration": "Haqq", "Meaning": "Truth, Right", "Example": "ذَٰلِكَ بِأَنَّ ٱللَّهَ هُوَ ٱلۡحَقُّ (That is because Allah is the Truth)"},
    {"Word (Arabic)": "صبر", "Transliteration": "Sabr", "Meaning": "Patience", "Example": "وَٱصۡبِرۡ وَمَا صَبۡرُكَ إِلَّا بِٱللَّهِ (Be patient, and your patience is only through Allah)"},
    {"Word (Arabic)": "خير", "Transliteration": "Khayr", "Meaning": "Good", "Example": "إِنۡ أَرَدتُّمُ ٱلۡخَيۡرَ (If you seek good)"},
    {"Word (Arabic)": "شر", "Transliteration": "Shar", "Meaning": "Evil", "Example": "وَشَرٌّ مُّسۡتَطِيرٞ (Evil is widespread)"},
    {"Word (Arabic)": "سلام", "Transliteration": "Salaam", "Meaning": "Peace", "Example": "سَلَٰمٌ هِيَ حَتَّىٰ مَطۡلَعِ ٱلۡفَجۡرِ (Peace it is until the emergence of dawn)"},
    {"Word (Arabic)": "ملك", "Transliteration": "Malik", "Meaning": "King, Owner", "Example": "مَٰلِكِ يَوۡمِ ٱلدِّينِ (Master of the Day of Judgment)"},
    {"Word (Arabic)": "علم", "Transliteration": "'Ilm", "Meaning": "Knowledge", "Example": "وَعَلَّمَ ٱدَمَ ٱلۡأَسۡمَآءَ كُلَّهَا (And He taught Adam the names - all of them)"},
    {"Word (Arabic)": "صلاة", "Transliteration": "Salah", "Meaning": "Prayer", "Example": "إِنَّ ٱلصَّلَوٰةَ كَانَتۡ عَلَى ٱلۡمُؤۡمِنِينَ كِتَٰبٗا مَّوۡقُوتٗا (Indeed, prayer has been decreed upon the believers at specified times)"},
    {"Word (Arabic)": "نفس", "Transliteration": "Nafs", "Meaning": "Soul, Self", "Example": "كُلُّ نَفۡسٖ ذَآئِقَةُ ٱلۡمَوۡتِ (Every soul will taste death)"},
    {"Word (Arabic)": "عذاب", "Transliteration": "Azaab", "Meaning": "Punishment", "Example": "إِنَّ عَذَابَ رَبِّكَ لَوَٰقِعٞ (Indeed, the punishment of your Lord will occur)"},
    {"Word (Arabic)": "آمن", "Transliteration": "Aamana", "Meaning": "He believed", "Example": "فَأَمَّا ٱلَّذِينَ ءَامَنُواْ وَعَمِلُواْ ٱلصَّٰلِحَٰتِ (As for those who believed and did righteous deeds)"},
    {"Word (Arabic)": "ظلم", "Transliteration": "Zalama", "Meaning": "He wronged", "Example": "وَمَا ظَلَمُونَا وَلَٰكِن كَانُوٓاْ أَنفُسَهُمۡ يَظۡلِمُونَ (And they did not wrong Us, but they were wronging themselves)"},
    {"Word (Arabic)": "نار", "Transliteration": "Naar", "Meaning": "Fire", "Example": "وَٱلۡقَوۡدُهَا ٱلنَّاسُ وَٱلۡحِجَارَةُ (Its fuel is people and stones)"},
    {"Word (Arabic)": "أرض", "Transliteration": "Ard", "Meaning": "Earth", "Example": "ٱلۡأَرۡضَ بَعۡدَ مَوۡتِهَا (The earth after its lifelessness)"},
    {"Word (Arabic)": "نبي", "Transliteration": "Nabi", "Meaning": "Prophet", "Example": "يَٰٓأَيُّهَا ٱلنَّبِيُّ إِنَّآ أَرۡسَلۡنَٰكَ (O Prophet, indeed We have sent you)"},
    {"Word (Arabic)": "إيمان", "Transliteration": "Iman", "Meaning": "Faith, Belief", "Example": "إِنَّ ٱلَّذِينَ ءَامَنُواْ وَعَمِلُواْ ٱلصَّٰلِحَٰتِ (Indeed, those who believe and do righteous deeds)"},
    {"Word (Arabic)": "كفر", "Transliteration": "Kufr", "Meaning": "Disbelief", "Example": "إِنَّ ٱلَّذِينَ كَفَرُواْ (Indeed, those who disbelieve)"},
    {"Word (Arabic)": "رسول", "Transliteration": "Rasool", "Meaning": "Messenger", "Example": "وَمَآ أَرۡسَلۡنَا مِن قَبۡلِكَ مِن رَّسُولٖ (We have not sent before you any messenger)"},
    {"Word (Arabic)": "رب", "Transliteration": "Rabb", "Meaning": "Lord", "Example": "ٱلۡحَمۡدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ (All praise is due to Allah, Lord of the worlds)"},
    {"Word (Arabic)": "دين", "Transliteration": "Deen", "Meaning": "Religion", "Example": "إِنَّ ٱلدِّينَ عِندَ ٱللَّهِ ٱلۡإِسۡلَٰمُ (Indeed, the religion with Allah is Islam)"},
    {"Word (Arabic)": "صراط", "Transliteration": "Sirat", "Meaning": "Path, Way", "Example": "ٱهۡدِنَا ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ (Guide us to the Straight Path)"},
    {"Word (Arabic)": "شرك", "Transliteration": "Shirk", "Meaning": "Associating partners (with Allah)", "Example": "إِنَّ ٱلشِّرۡكَ لَظُلۡمٌ عَظِيمٌ (Indeed, associating others with Allah is a great injustice)"},
    {"Word (Arabic)": "نعم", "Transliteration": "Ni'mah", "Meaning": "Blessing, Favor", "Example": "وَأَسۡبَغَ عَلَيۡكُمۡ نِعَمَهُۥ (And He has perfected His blessings upon you)"},
    {"Word (Arabic)": "ملكوت", "Transliteration": "Mulk", "Meaning": "Kingdom", "Example": "تَبَارَكَ ٱلَّذِي بِيَدِهِ ٱلۡمُلۡكُ (Blessed is He in whose hand is the dominion)"},
    {"Word (Arabic)": "شيطان", "Transliteration": "Shaytan", "Meaning": "Satan", "Example": "إِنَّ ٱلشَّيۡطَٰنَ لَكُمۡ عَدُوّٞ (Indeed, Satan is an enemy to you)"},
    {"Word (Arabic)": "عدل", "Transliteration": "'Adl", "Meaning": "Justice", "Example": "وَأَقِيمُواْ ٱلۡوَزۡنَ بِٱلۡقِسۡطِ (And establish weight in justice)"},
    {"Word (Arabic)": "حرام", "Transliteration": "Haram", "Meaning": "Forbidden", "Example": "إِنَّهُۥ كَانَ حَرَامًا (Indeed, it was forbidden)"},
    {"Word (Arabic)": "حلال", "Transliteration": "Halal", "Meaning": "Permissible", "Example": "وَكُلُواْ مِمَّا رَزَقَكُمُ ٱللَّهُ حَلَٰلٗا طَيِّبٗا (And eat from what Allah has provided you [of] lawful and good)"},
    {"Word (Arabic)": "جنة", "Transliteration": "Jannah", "Meaning": "Paradise", "Example": "وَأُدۡخِلُواْ ٱلۡجَنَّةَ فَزُمَرَا (They will be admitted to Paradise in groups)"},
    {"Word (Arabic)": "نار", "Transliteration": "Naar", "Meaning": "Hellfire", "Example": "فَٱلنَّارُ مَثۡوَىٰكُمۡ (Then the Fire is your abode)"},
    {"Word (Arabic)": "ذكر", "Transliteration": "Dhikr", "Meaning": "Remembrance", "Example": "وَلَذِكۡرُ ٱللَّهِ أَكۡبَرُ (And the remembrance of Allah is greater)"},
    {"Word (Arabic)": "هدى", "Transliteration": "Huda", "Meaning": "Guidance", "Example": "وَمَا عَلَيۡنَآ إِلَّا ٱلۡبَلَٰغُ وَٱلۡهُدَىٰ (And upon us is only the duty of clear notification and guidance)"},
    {"Word (Arabic)": "آخرة", "Transliteration": "Akhirah", "Meaning": "Hereafter", "Example": "وَلَدَارُ ٱلۡأٓخِرَةِ خَيۡرٞ لِّلَّذِينَ يَتَّقُونَ (And the home of the Hereafter is better for those who fear Allah)"},
    {"Word (Arabic)": "بشر", "Transliteration": "Bashar", "Meaning": "Human, Mankind", "Example": "وَجَعَلۡنَٰكُمۡ شُعُوبٗا وَقَبَآئِلَ (And made you peoples and tribes)"},
    {"Word (Arabic)": "رزق", "Transliteration": "Rizq", "Meaning": "Provision", "Example": "وَفِي ٱلسَّمَآءِ رِزۡقُكُمۡ (And in the sky is your provision)"},
    {"Word (Arabic)": "نبي", "Transliteration": "Nabi", "Meaning": "Prophet", "Example": "وَإِذۡ قَالَ نَبِيُّكُمۡ (When your prophet said)"},
    {"Word (Arabic)": "قوم", "Transliteration": "Qawm", "Meaning": "People, Nation", "Example": "فَإِن كَذَّبَكَ قَوۡمُكَ (If your people deny you)"},
    {"Word (Arabic)": "عبد", "Transliteration": "'Abd", "Meaning": "Servant, Slave", "Example": "وَٱلۡعَبۡدُ ٱلصَّالِحُ (The righteous servant)"},
    {"Word (Arabic)": "حق", "Transliteration": "Haqq", "Meaning": "Truth, Right", "Example": "وَبِٱلۡحَقِّ أَنزَلۡنَٰهُ (And in truth, We have sent it down)"},
    {"Word (Arabic)": "نور", "Transliteration": "Noor", "Meaning": "Light", "Example": "وَجَعَلۡنَا لَهُۥ نُورًا (And We appointed for him light)"},
    {"Word (Arabic)": "سماء", "Transliteration": "Samaa", "Meaning": "Heaven, Sky", "Example": "وَٱلسَّمَآءِ ذَاتِ ٱلۡبُرُوجِ (By the sky containing great stars)"},
    {"Word (Arabic)": "أرض", "Transliteration": "Ard", "Meaning": "Earth", "Example": "إِنَّ فِي ٱلۡأَرۡضِ لَءَايَٰتٖ (Indeed, on the earth are signs)"},
    {"Word (Arabic)": "يوم", "Transliteration": "Yawm", "Meaning": "Day", "Example": "وَذَكِّرۡهُم بِأَيَّٰمِ ٱللَّهِ (And remind them of the days of Allah)"},
    {"Word (Arabic)": "ليل", "Transliteration": "Layl", "Meaning": "Night", "Example": "وَٱلَّيۡلِ إِذَا يَغۡشَىٰ (By the night as it conceals)"},
    {"Word (Arabic)": "نهار", "Transliteration": "Nahar", "Meaning": "Daytime", "Example": "وَٱلنَّهَارِ إِذَا تَجَلَّىٰ (And the day as it appears)"},
    {"Word (Arabic)": "عين", "Transliteration": "'Ayn", "Meaning": "Eye", "Example": "تَجۡرِي بِأَعۡيُنِنَا (Flowing under Our observation)"},
    {"Word (Arabic)": "يد", "Transliteration": "Yad", "Meaning": "Hand", "Example": "مِمَّا عَمِلَتۡ أَيۡدِينَآ (From what Our hands have made)"},
    {"Word (Arabic)": "قدم", "Transliteration": "Qadam", "Meaning": "Foot", "Example": "فَسَيَطَـُٔونَ أَقۡدَامَهُمۡ (And they will step on their feet)"},
    {"Word (Arabic)": "صلاة", "Transliteration": "Salah", "Meaning": "Prayer", "Example": "إِنَّ ٱلصَّلَوٰةَ تَنۡهَىٰ (Indeed, prayer prohibits [immorality])"},
    {"Word (Arabic)": "زكاة", "Transliteration": "Zakah", "Meaning": "Charity", "Example": "وَأَقِيمُواْ ٱلصَّلَوٰةَ وَءَاتُواْ ٱلزَّكَوٰةَ (Establish prayer and give charity)"},
    {"Word (Arabic)": "صيام", "Transliteration": "Siyam", "Meaning": "Fasting", "Example": "كُتِبَ عَلَيۡكُمُ ٱلصِّيَامُ (Fasting is prescribed for you)"},
    {"Word (Arabic)": "حج", "Transliteration": "Hajj", "Meaning": "Pilgrimage", "Example": "وَأَذِّنۡ فِي ٱلنَّاسِ بِٱلۡحَجِّ (Proclaim the pilgrimage among the people)"},
    {"Word (Arabic)": "أمر", "Transliteration": "Amr", "Meaning": "Command, Matter", "Example": "وَإِلَىٰ ٱللَّهِ تُرۡجَعُ ٱلۡأُمُورُ (And to Allah will all matters be returned)"},
    {"Word (Arabic)": "خلق", "Transliteration": "Khalaq", "Meaning": "Create, Creation", "Example": "ٱلَّذِي خَلَقَ فَسَوَّىٰ (The One who created and proportioned)"},
    {"Word (Arabic)": "علم", "Transliteration": "'Ilm", "Meaning": "Knowledge", "Example": "إِنَّ ٱللَّهَ عَلِيمٌ (Indeed, Allah is Knowing)"},
    {"Word (Arabic)": "رزق", "Transliteration": "Rizq", "Meaning": "Provision, Sustenance", "Example": "وَمَا مِن دَآبَّةٍ فِي ٱلۡأَرۡضِ إِلَّا عَلَى ٱللَّهِ رِزۡقُهَا (There is no creature on earth but its provision is upon Allah)"},
    {"Word (Arabic)": "رحمة", "Transliteration": "Rahmah", "Meaning": "Mercy", "Example": "وَرَبُّكَ ٱلۡغَفُورُ ذُو ٱلرَّحۡمَةِ (Your Lord is the Forgiving, the Possessor of Mercy)"},
    {"Word (Arabic)": "عدل", "Transliteration": "'Adl", "Meaning": "Justice, Fairness", "Example": "وَأَقِيمُواْ ٱلۡوَزۡنَ بِٱلۡقِسۡطِ (And establish weight in justice)"},
    {"Word (Arabic)": "سمع", "Transliteration": "Sam'a", "Meaning": "Hearing", "Example": "إِنَّ ٱللَّهَ هُوَ ٱلسَّمِيعُ ٱلۡبَصِيرُ (Indeed, Allah is the Hearing, the Seeing)"},
    {"Word (Arabic)": "بصر", "Transliteration": "Basr", "Meaning": "Sight", "Example": "وَجَعَلۡنَا لَهُمۡ سَمۡعٗا وَأَبۡصَٰرٗا (And We gave them hearing and vision)"},
    {"Word (Arabic)": "هدى", "Transliteration": "Huda", "Meaning": "Guidance", "Example": "إِنَّ هَٰذَا ٱلۡقُرۡءَانَ يَهۡدِي لِلَّتِي هِيَ أَقۡوَمُ (Indeed, this Quran guides to that which is most upright)"},
    {"Word (Arabic)": "خير", "Transliteration": "Khayr", "Meaning": "Goodness", "Example": "وَإِنَّهُۥ لَحُبِّ ٱلۡخَيۡرِ لَشَدِيدٌ (Indeed, he loves wealth immensely)"},
    {"Word (Arabic)": "شر", "Transliteration": "Shar", "Meaning": "Evil, Badness", "Example": "وَجَعَلۡنَا لِكُلِّ نَبِيٍّ عَدُوًّا شَيَٰطِينَ ٱلۡإِنسِ وَٱلۡجِنِّ (And We made for every prophet an enemy, devils from mankind and jinn)"},
    {"Word (Arabic)": "نار", "Transliteration": "Naar", "Meaning": "Fire", "Example": "وَتُصۡلَىٰ نَارًا حَامِيَةٗ (And he will enter a blazing Fire)"},
    {"Word (Arabic)": "جنة", "Transliteration": "Jannah", "Meaning": "Paradise", "Example": "جَنَّٰتُ عَدۡنٍ تَجۡرِي مِن تَحۡتِهَا ٱلۡأَنۡهَٰرُ (Gardens of Eternity beneath which rivers flow)"},
    {"Word (Arabic)": "صبر", "Transliteration": "Sabr", "Meaning": "Patience", "Example": "وَٱصۡبِرۡ عَلَىٰ مَآ أَصَابَكَ (And be patient over what befalls you)"},
    {"Word (Arabic)": "عمل", "Transliteration": "'Amal", "Meaning": "Deed, Action", "Example": "فَمَن يَعۡمَلۡ مِثۡقَالَ ذَرَّةٍ خَيۡرٗا يَرَهُۥ (Whoever does an atom's weight of good will see it)"},
    {"Word (Arabic)": "ذنب", "Transliteration": "Dhanb", "Meaning": "Sin, Fault", "Example": "فَٱغۡفِرۡ لِي ذَنۢبِي (So forgive my sin)"},
    {"Word (Arabic)": "أمانة", "Transliteration": "Amanah", "Meaning": "Trust", "Example": "إِنَّ ٱللَّهَ يَأۡمُرُكُمۡ أَن تُؤَدُّواْ ٱلۡأَمَٰنَٰتِ (Indeed, Allah commands you to render trusts to their owners)"},
    {"Word (Arabic)": "صدق", "Transliteration": "Sidq", "Meaning": "Truthfulness", "Example": "وَٱصۡدِقۡنِي وَصۡدَقٗا (And grant me sincerity in my speech)"},
    {"Word (Arabic)": "كذب", "Transliteration": "Kadhb", "Meaning": "Lying, Falsehood", "Example": "فَٱجۡتَنِبُواْ ٱلرِّجۡسَ مِنَ ٱلۡأَوۡثَٰنِ وَٱجۡتَنِبُواْ قَوۡلَ ٱلزُّورِ (Avoid false speech)"},
    {"Word (Arabic)": "شكر", "Transliteration": "Shukr", "Meaning": "Gratitude", "Example": "لَئِن شَكَرۡتُمۡ لَأَزِيدَنَّكُمۡ (If you are grateful, I will surely increase you)"},
    {"Word (Arabic)": "قوة", "Transliteration": "Quwwah", "Meaning": "Strength", "Example": "إِنَّ ٱللَّهَ قَوِيٌّ عَزِيزٌ (Indeed, Allah is Strong and Mighty)"},
    {"Word (Arabic)": "ضعف", "Transliteration": "Du'af", "Meaning": "Weakness", "Example": "وَخُلِقَ ٱلۡإِنسَٰنُ ضَعِيفًا (Mankind was created weak)"},
    {"Word (Arabic)": "حياة", "Transliteration": "Hayah", "Meaning": "Life", "Example": "إِنَّ ٱللَّهَ يُحۡيِي ٱلۡمَوۡتَىٰ (Indeed, Allah gives life to the dead)"},
    {"Word (Arabic)": "موت", "Transliteration": "Mawt", "Meaning": "Death", "Example": "كُلُّ نَفۡسٖ ذَآئِقَةُ ٱلۡمَوۡتِ (Every soul will taste death)"},
    {"Word (Arabic)": "أمان", "Transliteration": "Aman", "Meaning": "Safety, Security", "Example": "ٱلَّذِينَ ءَامَنُواْ وَلَمۡ يَلۡبِسُوٓاْ إِيمَٰنَهُم بِظُلۡمٍ أُوْلَٰٓئِكَ لَهُمُ ٱلۡأَمۡنُ (They will have security)"},
    {"Word (Arabic)": "عذاب", "Transliteration": "'Adhab", "Meaning": "Punishment", "Example": "وَٱتَّقُواْ يَوۡمٗا لَّا تَجۡزِي نَفۡسٌ عَن نَّفۡسٖ شَيۡـٔٗا وَلَا يُقۡبَلُ مِنۡهَا شَفَٰعَةٞ (And fear a day when no soul will suffice for another)"},
    {"Word (Arabic)": "شفاعة", "Transliteration": "Shafa'ah", "Meaning": "Intercession", "Example": "مَن ذَا ٱلَّذِي يَشۡفَعُ عِندَهُۥٓ إِلَّا بِإِذۡنِهِۦ (Who is it that can intercede with Him except by His permission?)"},
    {"Word (Arabic)": "عفو", "Transliteration": "'Afw", "Meaning": "Pardon, Forgiveness", "Example": "فَٱعۡفُ عَنۡهُمۡ وَصَفَحۡ (So pardon them and overlook)"},
    {"Word (Arabic)": "فتح", "Transliteration": "Fath", "Meaning": "Victory, Opening", "Example": "إِنَّا فَتَحۡنَا لَكَ فَتۡحٗا مُّبِينٗا (Indeed, We have given you a clear conquest)"},
    {"Word (Arabic)": "صراط", "Transliteration": "Sirat", "Meaning": "Path", "Example": "ٱهۡدِنَا ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ (Guide us to the straight path)"},
    {"Word (Arabic)": "خير", "Transliteration": "Khayr", "Meaning": "Good, Blessing", "Example": "لَكُمۡ خَيۡرٌ إِن كُنتُمۡ تَعۡلَمُونَ (It is better for you if you only knew)"},
    {"Word (Arabic)": "شر", "Transliteration": "Shar", "Meaning": "Evil", "Example": "فَإِن تَوَلَّيۡتُمۡ فَإِنَّمَا هُوَ شَرٌّ (But if you turn away, it is only an evil for you)"},
    {"Word (Arabic)": "صراط", "Transliteration": "Sirat", "Meaning": "Path", "Example": "وَهُدُوٓاْ إِلَىٰ صِرَٰطِ ٱلۡحَمِيدِ (And guided to the path of the Praiseworthy)"},
    {"Word (Arabic)": "نصر", "Transliteration": "Nasr", "Meaning": "Help, Victory", "Example": "إِذَا جَآءَ نَصۡرُ ٱللَّهِ وَٱلۡفَتۡحُ (When the victory of Allah has come)"},
    {"Word (Arabic)": "فتنة", "Transliteration": "Fitnah", "Meaning": "Trial, Temptation", "Example": "وَٱتَّقُواْ فِتۡنَةٗ لَّا تُصِيبَنَّ ٱلَّذِينَ ظَلَمُواْ (Fear a trial that will not strike only the wrongdoers among you)"},
    {"Word (Arabic)": "دين", "Transliteration": "Deen", "Meaning": "Religion", "Example": "لَكُمۡ دِينُكُمۡ وَلِيَ دِينِ (For you is your religion, and for me is mine)"},
    {"Word (Arabic)": "إيمان", "Transliteration": "Iman", "Meaning": "Faith", "Example": "إِنَّمَا ٱلۡمُؤۡمِنُونَ ٱلَّذِينَ ءَامَنُواْ (The believers are only those who have faith)"},
    {"Word (Arabic)": "كفر", "Transliteration": "Kufr", "Meaning": "Disbelief", "Example": "وَٱلۡكَٰفِرُونَ هُمُ ٱلظَّٰلِمُونَ (And the disbelievers are the wrongdoers)"},
    {"Word (Arabic)": "عبد", "Transliteration": "'Abd", "Meaning": "Servant", "Example": "وَٱللَّهُ خَيۡرٞ لِّعِبَادِهِۦ (And Allah is best for His servants)"},
    {"Word (Arabic)": "أجر", "Transliteration": "Ajr", "Meaning": "Reward", "Example": "إِنَّ ٱلۡمُتَّقِينَ لَهُمۡ أَجۡرٌ كَبِيرٞ (Indeed, for the righteous is a great reward)"},
    {"Word (Arabic)": "نور", "Transliteration": "Nur", "Meaning": "Light", "Example": "ٱللَّهُ نُورُ ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِ (Allah is the Light of the heavens and the earth)"},
    {"Word (Arabic)": "ظلم", "Transliteration": "Zulm", "Meaning": "Oppression, Darkness", "Example": "وَٱلظَّٰلِمُونَ هُمۡ أَصۡحَٰبُ ٱلنَّارِ (And the wrongdoers are the companions of the Fire)"},
    {"Word (Arabic)": "شهادة", "Transliteration": "Shahada", "Meaning": "Testimony, Witness", "Example": "شَهِدَ ٱللَّهُ أَنَّهُۥ لَآ إِلَٰهَ إِلَّا هُوَ (Allah bears witness that there is no deity except Him)"},
    {"Word (Arabic)": "حق", "Transliteration": "Haq", "Meaning": "Truth, Right", "Example": "وَبِٱلۡحَقِّ أَنزَلۡنَٰهُ وَبِٱلۡحَقِّ نَزَلَ (And with the truth We have sent it down, and with the truth it has descended)"},
    {"Word (Arabic)": "باطل", "Transliteration": "Batil", "Meaning": "Falsehood", "Example": "وَقُلۡ جَآءَ ٱلۡحَقُّ وَزَهَقَ ٱلۡبَٰطِلُ (Say, 'Truth has come, and falsehood has departed')"},
    {"Word (Arabic)": "عين", "Transliteration": "'Ayn", "Meaning": "Eye, Spring", "Example": "عَلَىٰٓ أَعۡيُنِنَا (Under Our observation)"},
    {"Word (Arabic)": "يد", "Transliteration": "Yad", "Meaning": "Hand", "Example": "بَلۡ يَدَاهُ مَبۡسُوطَتَانِ (Rather, His hands are outstretched)"},
    {"Word (Arabic)": "لسان", "Transliteration": "Lisan", "Meaning": "Tongue", "Example": "وَجَعَلۡنَا لَهُمۡ لِسَانَ صِدۡقٍ (And We granted them a tongue of truth)"},
    {"Word (Arabic)": "نفس", "Transliteration": "Nafs", "Meaning": "Soul, Self", "Example": "كُلُّ نَفۡسٍ ذَآئِقَةُ ٱلۡمَوۡتِ (Every soul will taste death)"},
    {"Word (Arabic)": "عين", "Transliteration": "'Ayn", "Meaning": "Eye, Spring", "Example": "إِنَّكَ بِأَعۡيُنِنَا (Indeed, you are under Our observation)"},
    {"Word (Arabic)": "حمد", "Transliteration": "Hamd", "Meaning": "Praise", "Example": "ٱلۡحَمۡدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ (Praise be to Allah, Lord of all worlds)"},
    {"Word (Arabic)": "شيء", "Transliteration": "Shay'", "Meaning": "Thing", "Example": "إِنَّ ٱللَّهَ عَلَىٰ كُلِّ شَيۡءٍ قَدِيرٌ (Indeed, Allah is over all things competent)"},
    {"Word (Arabic)": "بيت", "Transliteration": "Bayt", "Meaning": "House", "Example": "وَطَهِّرۡ بَيۡتِيَ لِلطَّآئِفِينَ (And purify My house for those who perform Tawaf)"},
    {"Word (Arabic)": "سماء", "Transliteration": "Sama'", "Meaning": "Sky, Heaven", "Example": "وَٱلسَّمَآءَ بَنَيۡنَٰهَا بِأَيۡدٖ (And the heaven We constructed with strength)"},
    {"Word (Arabic)": "أرض", "Transliteration": "Ard", "Meaning": "Earth", "Example": "وَٱلۡأَرۡضَ مَدَدۡنَٰهَا (And the earth – We have spread it out)"},
    {"Word (Arabic)": "ليل", "Transliteration": "Layl", "Meaning": "Night", "Example": "وَٱلَّيۡلِ إِذَا يَغۡشَىٰ (By the night as it covers)"},
    {"Word (Arabic)": "نهار", "Transliteration": "Nahar", "Meaning": "Day", "Example": "وَٱلنَّهَارِ إِذَا تَجَلَّىٰ (And by the day as it appears in brightness)"},
    {"Word (Arabic)": "شمس", "Transliteration": "Shams", "Meaning": "Sun", "Example": "وَٱلشَّمۡسِ وَضُحَىٰهَا (By the sun and its brightness)"},
    {"Word (Arabic)": "قمر", "Transliteration": "Qamar", "Meaning": "Moon", "Example": "وَٱلۡقَمَرِ إِذَا تَلَاهَا (And by the moon when it follows it)"},
    {"Word (Arabic)": "نجوم", "Transliteration": "Nujum", "Meaning": "Stars", "Example": "وَٱلۡنُّجُومِ إِذَا هَٰوَتْ (And by the stars when they fall)"},
    {"Word (Arabic)": "حجر", "Transliteration": "Hajar", "Meaning": "Stone", "Example": "فَأَمَّا ٱلۡحَجَرُ (As for the stone)"},
    {"Word (Arabic)": "شجرة", "Transliteration": "Shajrah", "Meaning": "Tree", "Example": "وَفَجَّرْنَا ٱلۡأَرۡضَ عُيُونًا فَٱلۡتَقَى ٱلۡمَآءُ عَلَىٰٓ أَمۡرٍ قَدَرٍ (And We caused the earth to gush forth with springs, so the waters met for a matter already predestined)"},
    {"Word (Arabic)": "ماء", "Transliteration": "Ma'", "Meaning": "Water", "Example": "وَجَعَلۡنَا مِنَ ٱلۡمَآءِ كُلَّ شَىْءٍ حَىٍّ (And We made from water every living thing)"},
    {"Word (Arabic)": "غيم", "Transliteration": "Ghaym", "Meaning": "Cloud", "Example": "وَٱلۡغَيۡمِ إِذَا فَجَّجۡنَٰهُ (And by the clouds when We split them)"},
    {"Word (Arabic)": "مطر", "Transliteration": "Matar", "Meaning": "Rain", "Example": "وَأَمۡطَرْنَا عَلَيۡهِمۡ مِّنَ ٱلۡمَنِّ وَٱلسَّلۡوَىٰ (And We sent upon them rain from the sky and quails)"},
    {"Word (Arabic)": "طعام", "Transliteration": "Ta'am", "Meaning": "Food", "Example": "وَإِذَا قُرِئَ عَلَيۡهِمُ ٱلۡقُرۡآنُ (And when the Quran is recited to them)"},
    {"Word (Arabic)": "فقراء", "Transliteration": "Fuqara", "Meaning": "Poor", "Example": "إِنَّمَا ٱلۡمُصَدِّقَٰتُ لِلۡفُقَرَآءِ وَٱلۡمَسَٰكِينِ (Indeed, the charities are for the poor and the needy)"},
    {"Word (Arabic)": "يوم", "Transliteration": "Yawm", "Meaning": "Day", "Example": "وَجَاءَتْ سَكْرَةُ ٱلْمَوْتِ بِٱلۡحَقِّ (The agony of death will bring the truth)"},
    {"Word (Arabic)": "آية", "Transliteration": "Ayah", "Meaning": "Sign, Verse", "Example": "إِنَّ فِي ذَٰلِكَ لَآيَٰتٍ (Indeed, in that are signs)"},
    {"Word (Arabic)": "فجر", "Transliteration": "Fajr", "Meaning": "Dawn", "Example": "وَٱلۡفَجۡرِ وَٰلَيَالٍ عَشْرٍ (By the dawn and the ten nights)"},
    {"Word (Arabic)": "توبة", "Transliteration": "Tawbah", "Meaning": "Repentance", "Example": "إِنَّ ٱللَّهَ يَحْبُوْا تَوَّابِينَ (Indeed, Allah loves those who repent)"},
    {"Word (Arabic)": "قلب", "Transliteration": "Qalb", "Meaning": "Heart", "Example": "إِنَّ فِي قُلُوبِهِمْ مَرَضٌ (Indeed, in their hearts is a disease)"},
    {"Word (Arabic)": "عمل", "Transliteration": "Amal", "Meaning": "Action, Deed", "Example": "وَمَنۡ أَعۡمَلَ صَٰلِحًۭا (And whoever does righteous deeds)"},
    {"Word (Arabic)": "صلاة", "Transliteration": "Salat", "Meaning": "Prayer", "Example": "إِنَّ ٱلۡصَّلَوٰةَ كَانَتْ عَلَى ٱلۡمُؤْمِنِينَ كِتَٰبًا مَّوۡقُوتًا (Indeed, prayer has been decreed upon the believers a decree of specified times)"},
    {"Word (Arabic)": "زكاة", "Transliteration": "Zakah", "Meaning": "Charity, Almsgiving", "Example": "وَأَقِيمُواْ ٱلصَّلَوٰةَ وَءٰتُواْ ٱلزَّكَٰةَ (And establish prayer and give zakah)"},
    {"Word (Arabic)": "حج", "Transliteration": "Hajj", "Meaning": "Pilgrimage", "Example": "وَأَذِّنْ فِي ٱلنَّاسِ بِالۡحَجِّ يَأْتُوكَ رِجَالًۭا (And proclaim to the people the Hajj)"},
    {"Word (Arabic)": "إجماع", "Transliteration": "Ijmā'", "Meaning": "Consensus", "Example": "وَإِذَا جَاءَكُمُ ٱلۡفَسَقُ (And when the evil-doers come to you)"},
    {"Word (Arabic)": "فاقة", "Transliteration": "Faqah", "Meaning": "Need, Poverty", "Example": "وَمَآ أَنتُم بِمُؤْمِنِينَ إِلَّآ كَذَٰلِكَ لَا تُحِبُّونَ (And you do not like)"},
    {"Word (Arabic)": "صدق", "Transliteration": "Sadaq", "Meaning": "Truth, Veracity", "Example": "إِنَّمَا يُؤْمِنُ بِهِۦ الَّذِينَ آمَنُواْ وَفِى قُلُوبِهِمْ (Only those who believe and have true faith in their hearts)"},
    {"Word (Arabic)": "شكر", "Transliteration": "Shukr", "Meaning": "Thankfulness, Gratitude", "Example": "فَٱشۡكُرُونِىٓ أَشۡكُرۡ لَكُم (So thank Me, and I will thank you)"},
    {"Word (Arabic)": "نصر", "Transliteration": "Nasr", "Meaning": "Help, Victory", "Example": "إِذَا جَآءَ نَصۡرُ ٱللَّهِ وَٱلۡفَتۡحُ (When the victory of Allah has come and the conquest)"},
    {"Word (Arabic)": "أمة", "Transliteration": "Umm", "Meaning": "Nation, Community", "Example": "إِنَّ هَٰذِهِۦٓ أُمَّتُكُمْ أُمَّةً وَٰحِدَةً (Indeed, this is your religion, one religion)"},
    {"Word (Arabic)": "خوف", "Transliteration": "Khauf", "Meaning": "Fear", "Example": "وَإِذَا بَشَّرَكُمُ ٱللَّهُ فَٱخْشَوْآأ (And when Allah gives you glad tidings, fear him)"},
    {"Word (Arabic)": "رجاء", "Transliteration": "Raja", "Meaning": "Hope, Desire", "Example": "فَٱلۡيَوْمَ لَا تُظۡلَمُ نَفۡسٌ شَيۡـٔٗا (So today no soul will be wronged)"},
    {"Word (Arabic)": "لطف", "Transliteration": "Lutf", "Meaning": "Kindness, Gentleness", "Example": "وَقَالَتِ ٱمۡرَأَتُ فِرۡعَوۡنَ (And the wife of Pharaoh said)"},
    {"Word (Arabic)": "سورة", "Transliteration": "Surah", "Meaning": "Chapter, Section", "Example": "ٱلۡحَمۡدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ (All praise is due to Allah, the Lord of the worlds)"},
    {"Word (Arabic)": "قائمة", "Transliteration": "Qaimah", "Meaning": "Standing, Upright", "Example": "وَقُومُوا۟ لِلَّهِ قَٰنِتِينَ (And stand before Allah, devoutly obedient)"},
    {"Word (Arabic)": "آباء", "Transliteration": "Aba'", "Meaning": "Fathers", "Example": "وَإِذْ قَالَ رَبُّكَ لِمَلَائِكَتِهِۦٓ إِنِّىٓ خَٰلِقٌۭ بَشَرًۭا مِّن صَلۡصَٰلٍ (When your Lord said to the angels, 'I am creating a human from clay')"},
    {"Word (Arabic)": "عمل", "Transliteration": "Amal", "Meaning": "Action, Deed", "Example": "فَمَن يَعْمَلْ مِثۡقَالَ ذَرَّةٍۢ خَيۡرًا يَرَهُۥ (Whoever does an atom's weight of good will see it)"},
    {"Word (Arabic)": "ذنب", "Transliteration": "Dhanb", "Meaning": "Sin", "Example": "فَيَغۡفِرُ لِمَن يَشَاءُ وَيُعَذِّبُ مَن يَشَاءُ (He forgives whom He wills and punishes whom He wills)"},
    {"Word (Arabic)": "رحمة", "Transliteration": "Rahmah", "Meaning": "Mercy", "Example": "إِنَّ رَحْمَتَ اللَّهِ قَرِيبٌۭ مِّنَ ٱلۡمُحۡسِنِينَ (Indeed, the mercy of Allah is near to the doers of good)"},
    {"Word (Arabic)": "جزء", "Transliteration": "Juz", "Meaning": "Part, Section", "Example": "إِنَّا جَعَلْنَا فِى السَّمَاء فُرُوجًا لِتَسِيرُوا۟ فِى (Indeed, We placed in the sky signs to guide you)"},
    {"Word (Arabic)": "إيمان", "Transliteration": "Iman", "Meaning": "Faith, Belief", "Example": "إِنَّمَآ أَمَانِۢكُمْ فِيٓ سَعِيدِ (The believers are in a blessed state)"},
    {"Word (Arabic)": "خاتم", "Transliteration": "Khatam", "Meaning": "Seal", "Example": "ٱمْسَكِ بِيَدِكُمْ فَفَصَاحُوا۟ (Hold tightly to the seal of your testimony)"},
    {"Word (Arabic)": "مؤمن", "Transliteration": "Mu'min", "Meaning": "Believer", "Example": "إِنَّ ٱللَّهَ مَعَ ٱلۡمُؤۡمِنِينَ (Indeed, Allah is with the believers)"},
    {"Word (Arabic)": "كافر", "Transliteration": "Kafir", "Meaning": "Disbeliever", "Example": "إِنَّ ٱللَّهَ لَا يَهْدِىۡ مَنۡ كَانَ فِى ٱلۡكُفۡرِ (Indeed, Allah does not guide the disbeliever)"},
    {"Word (Arabic)": "ظلم", "Transliteration": "Zulm", "Meaning": "Injustice, Oppression", "Example": "وَلَا تَظْلِمُوۡا۟ فِي ٱلۡأَرۡضِ (And do not commit injustice upon the earth)"},
    {"Word (Arabic)": "صبر", "Transliteration": "Sabr", "Meaning": "Patience, Endurance", "Example": "وَٱصْبِرْ لِحُكْمِ رَبِّكَ (And be patient for the judgment of your Lord)"},
    {"Word (Arabic)": "غفر", "Transliteration": "Ghafir", "Meaning": "Forgive", "Example": "إِنَّ اللَّهَ غَفُورٌۭ رَّحِيمٌۭ (Indeed, Allah is Forgiving, Merciful)"},
    {"Word (Arabic)": "جهنم", "Transliteration": "Jahannam", "Meaning": "Hell", "Example": "وَٱلۡجَحِيمَ وَٱلۡمُدۡحِرَةِ (And Hell, with its roaring flames)"},
    {"Word (Arabic)": "جنة", "Transliteration": "Jannah", "Meaning": "Paradise, Heaven", "Example": "إِنَّ الۡمُتَّقِينَ فِى جَنَّٰتٍ وَنَهَرٍ (Indeed, the righteous are in gardens and rivers)"},
    {"Word (Arabic)": "سعيد", "Transliteration": "Sa'id", "Meaning": "Happy, Successful", "Example": "فَسَتُدْنَىٰ جَنَّةُ الرَّبِّ (And will bring near the garden of your Lord)"},
    {"Word (Arabic)": "شرك", "Transliteration": "Shirk", "Meaning": "Polytheism, Associating partners with Allah", "Example": "إِنَّ ٱللَّهَ لَا يَغۡفِرُ أَن يُشۡرَكَ بِهِۦ (Indeed, Allah does not forgive associating others with Him)"},
    {"Word (Arabic)": "سورة", "Transliteration": "Surah", "Meaning": "Chapter, Section", "Example": "يُحْشَرُونَ فِى جُمُودٍ (They will be gathered in the chapters)"},
    {"Word (Arabic)": "عذاب", "Transliteration": "Adhab", "Meaning": "Punishment, Torture", "Example": "إِنَّ عَذَابَ رَبِّكَ لَشَدِيدٌۭ (Indeed, the punishment of your Lord is severe)"},
    {"Word (Arabic)": "تقوى", "Transliteration": "Taqwa", "Meaning": "God-consciousness, Piety", "Example": "وَٱتَّقُوا۟ ٱللَّهَ لَعَلَّكُمۡ تُفۡلِحُونَ (And fear Allah that you may succeed)"},
    {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "وَمَن يَغْفِرُ ٱلذُّنُوبَ إِلَّآ أَنتَ (And who forgives sins except You)"},
    {"Word (Arabic)": "فاسق", "Transliteration": "Fasiq", "Meaning": "Rebellious, Corrupt", "Example": "إِنَّ ٱلۡفَٰسِقِينَ فِى جَحَنَّمَ (Indeed, the corrupt are in Hell)"},
    {"Word (Arabic)": "صحابة", "Transliteration": "Sahabah", "Meaning": "Companions", "Example": "إِنَّۢا۟ مَعَكُمۡ مِّنَ ٱلۡمُؤۡمِنِينَ (Indeed, We are with you among the believers)"},
    {"Word (Arabic)": "حدود", "Transliteration": "Hudud", "Meaning": "Limits, Boundaries", "Example": "وَلَا تَقْرَبُوا۟ ٱلۡفَوَٰحِشَ مَا ظَهَرَ مِنْهَا وَمَا بَطَنَ (And do not approach immorality, what is apparent of it and what is concealed)"},
    {"Word (Arabic)": "سجود", "Transliteration": "Sujud", "Meaning": "Prostration", "Example": "وَٱسْجُدْ لِرَبِّكَ وَٱتَّبِعۡ (And prostrate to your Lord and follow)"},
    {"Word (Arabic)": "سورة", "Transliteration": "Surah", "Meaning": "Chapter", "Example": "وَلَقَدْ جَاءَكُمۡ مِّنَ ٱللَّهِ أَمْرٌۭ (Indeed, there has come to you from Allah a command)"},
    {"Word (Arabic)": "إبليس", "Transliteration": "Iblis", "Meaning": "Satan", "Example": "إِنَّۢا لَكَ مِنَ ٱلۡمُبَشِّرِينَ (Indeed, I am of the bringers of good news)"},
    {"Word (Arabic)": "مؤمنين", "Transliteration": "Mu'minin", "Meaning": "Believers", "Example": "إِنَّ ٱللَّهَ فَضَّلَ ٱلۡمُؤۡمِنِينَ عَلَى ٱلۡمُنَٰفِقِينَ (Indeed, Allah has preferred the believers over the hypocrites)"},
    {"Word (Arabic)": "ضلال", "Transliteration": "Dhalal", "Meaning": "Misguidance", "Example": "وَمَنۡ يَكُنۡ فِى ضَلَٰلٍۢ فَلَا تُضِلَّهُۥٓ (And whoever is in misguidance, do not misguide him)"},
    {"Word (Arabic)": "وعد", "Transliteration": "Wa'ad", "Meaning": "Promise", "Example": "وَفِي ٱلۡوَعۡدِ إِنَّكُمْ لَفِى فَجَائِهۦٓ (And in the promise, indeed you are in its depths)"},
    {"Word (Arabic)": "فريق", "Transliteration": "Fareeq", "Meaning": "Group, Party", "Example": "وَفِى قُلُوبِهِمْ نَعْتٌۭ (And in their hearts, there is a description)"},
    {"Word (Arabic)": "عزّة", "Transliteration": "Izzah", "Meaning": "Honor, Power", "Example": "إِنَّآ فَجَّرْنَا ٱلۡمَآءَ فَٱلۡتَقَىٰٓ (Indeed, We caused the water to gush forth and it met)"},
    {"Word (Arabic)": "غضب", "Transliteration": "Ghadab", "Meaning": "Anger", "Example": "فَجَاءَ غَضَبُ رَبِّكُمْ (So came the anger of your Lord)"},
    {"Word (Arabic)": "عبادة", "Transliteration": "Ibadah", "Meaning": "Worship", "Example": "إِنَّمَا يُؤْمِنُونَ بِهِۦ (Indeed, they believe in it)"},
    {"Word (Arabic)": "نفق", "Transliteration": "Nafaq", "Meaning": "Hypocrisy", "Example": "إِنَّ ٱلَّذِينَ يُنَافِقُونَ (Indeed, those who practice hypocrisy)"},
    {"Word (Arabic)": "ظلم", "Transliteration": "Zulm", "Meaning": "Oppression, Injustice", "Example": "فَٱلۡحَقُّ مَعَهُمْ (And the truth is with them)"},
    {"Word (Arabic)": "مع", "Transliteration": "Ma'a", "Meaning": "With", "Example": "وَمَآ أَنتُم بِمُؤْمِنِينَ إِلَّآ كَذَٰلِكَ (And you are not believers unless you do this)"},
    {"Word (Arabic)": "عبد", "Transliteration": "Abd", "Meaning": "Servant, Slave", "Example": "يُحِبُّونَ ٱللَّهَ وَٱلۡرَّسُولَ (They love Allah and His Messenger)"},
    {"Word (Arabic)": "غني", "Transliteration": "Ghaniyy", "Meaning": "Wealthy, Rich", "Example": "وَٱللَّهُ غَنِىٌّۭ حَمِيدٌۭ (And Allah is Rich, Praiseworthy)"},
    {"Word (Arabic)": "غفور", "Transliteration": "Ghafur", "Meaning": "Forgiving", "Example": "إِنَّ ٱللَّهَ غَفُورٌۭ رَّحِيمٌۭ (Indeed, Allah is Forgiving and Merciful)"},
    {"Word (Arabic)": "عالم", "Transliteration": "Alam", "Meaning": "World, Universe", "Example": "وَٱلۡمَسَٰكِينَ فِىۡ أَرَۡضِهِۦ (And the poor in His land)"},
    {"Word (Arabic)": "إسلام", "Transliteration": "Islam", "Meaning": "Submission, Islam", "Example": "إِنَّ ٱللَّهَ فَضَّلَ ٱلۡمُؤۡمِنِينَ عَلَى ٱلۡمُنَٰفِقِينَ (Indeed, Allah has preferred the believers over the hypocrites)"},
    {"Word (Arabic)": "غلب", "Transliteration": "Ghalab", "Meaning": "Victory, Overcome", "Example": "يُغْلِبُونَ كُلَّ مَنۡ يَشَاءُ (They overcome all who they want)"},
    {"Word (Arabic)": "جنة", "Transliteration": "Jannah", "Meaning": "Paradise", "Example": "وَٱلۡجَنَّٰتِ وَٱلۡمُدۡحِرَةِ (And the gardens and the flames)"},
    {"Word (Arabic)": "كفر", "Transliteration": "Kufr", "Meaning": "Disbelief, Denial", "Example": "إِنَّ اللَّهَ لَا يَغۡفِرُ لِمَنۡ يَشۡرِكُ (Indeed, Allah does not forgive whoever associates others with Him)"},
    {"Word (Arabic)": "قرآن", "Transliteration": "Quran", "Meaning": "Quran", "Example": "إِنَّا۟ جَعَلْنَاهُ قُرْآنًۭا عَرَبِييًّۭا (Indeed, We have made it an Arabic Quran)"},
    {"Word (Arabic)": "دين", "Transliteration": "Din", "Meaning": "Religion", "Example": "إِنَّ دِينَ ٱللَّهِ ٱلۡإِسْلَامُ (Indeed, the religion in the sight of Allah is Islam)"},
    {"Word (Arabic)": "شهر", "Transliteration": "Shahr", "Meaning": "Month", "Example": "شَهۡرُ رَمَضَٰنَ ٱلَّذِىٓ أُنزِلَ فِيهِ ٱلۡقُرۡآنُ (The month of Ramadan in which was revealed the Quran)"},
    {"Word (Arabic)": "فرح", "Transliteration": "Farah", "Meaning": "Happiness, Joy", "Example": "فَٱمْسَكُوۡا۟ فِىٓ (Hold fast in joy)"},
    {"Word (Arabic)": "شهادة", "Transliteration": "Shahadah", "Meaning": "Testimony, Witness", "Example": "وَأَشْهَدُ أَنْ لَا إِلٰهَ إِلَّا اللَّهُ (And I bear witness that there is no god but Allah)"},
    {"Word (Arabic)": "عقل", "Transliteration": "Aql", "Meaning": "Mind, Reason", "Example": "إِنَّمَا يَتَفَكَّرُ فِىٓ أَهۡلِهِۦ (Only the one who thinks will consider it)"},
    {"Word (Arabic)": "روح", "Transliteration": "Ruh", "Meaning": "Spirit, Soul", "Example": "وَفَجَّرْنَا فِي السَّمَاء بِحَمِيمٍ (We sent down from the sky hot water)"},
    {"Word (Arabic)": "حكمة", "Transliteration": "Hikmah", "Meaning": "Wisdom", "Example": "وَإِنَّمَا يَفْهَمُونَ بِهِۦ (They understand through it)"},
    {"Word (Arabic)": "رؤية", "Transliteration": "Ru'ya", "Meaning": "Vision, Sight", "Example": "لِيُبَيِّنَ لَكُم مَّا أَحَلَّ (To make clear to you that which is lawful)"},
    {"Word (Arabic)": "جلال", "Transliteration": "Jalal", "Meaning": "Majesty, Glory", "Example": "فَذُو جَلاَلٍ وَإكْرَامٍ (He is the Lord of majesty and honor)"},
    {"Word (Arabic)": "دين", "Transliteration": "Din", "Meaning": "Religion, Way of Life", "Example": "إِنَّا دِينُنَا فِى الْوَجْهِ لِلَّهِ (Indeed, our religion is only for Allah)"},
    {"Word (Arabic)": "هدى", "Transliteration": "Huda", "Meaning": "Guidance", "Example": "إِنَّ هَٰذَا لَفِى كِتَابٍ مَّسْطُورٍ (Indeed, this is in an upright book)"},
    {"Word (Arabic)": "نور", "Transliteration": "Nur", "Meaning": "Light", "Example": "اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ (Allah is the Light of the heavens and the earth)"},
    {"Word (Arabic)": "كلمة", "Transliteration": "Kalima", "Meaning": "Word", "Example": "لِيَجْتَفِىٰ بِهِۦۦ اللَّهُ (Let them argue the words in truth)"},
    {"Word (Arabic)": "سميع", "Transliteration": "Sami'", "Meaning": "All-Hearing", "Example": "إِنَّ اللَّهَ سَمِيعٌ عَلِيمٌ (Indeed, Allah is All-Hearing, All-Knowing)"},
    {"Word (Arabic)": "بصير", "Transliteration": "Baseer", "Meaning": "All-Seeing", "Example": "إِنَّ اللَّهَ بَصِيرٌ بِمَا يَفْعَلُونَ (Indeed, Allah is All-Seeing of what they do)"},
    {"Word (Arabic)": "ملك", "Transliteration": "Malik", "Meaning": "King, Sovereign", "Example": "قُلِ ٱللَّهُ مَلِكُ ٱلۡمُلْكِ (Say: Allah is the King of the kingdom)"},
    {"Word (Arabic)": "قدير", "Transliteration": "Qadir", "Meaning": "All-Powerful", "Example": "إِنَّهُۥ عَلَىٰ كُلِّ شَىْءٍ قَدِيرٌۭ (Indeed, He is capable of everything)"},
    {"Word (Arabic)": "مؤمن", "Transliteration": "Mu'min", "Meaning": "Believer", "Example": "إِنَّمَا ٱلۡمُؤۡمِنُونَ إِخۡوَةٌۭ (The believers are but brothers)"},
    {"Word (Arabic)": "صدق", "Transliteration": "Sadaq", "Meaning": "Truth, Sincerity", "Example": "إِنَّهُۥ لَحَقٌۭ (Indeed, it is the truth)"},
    {"Word (Arabic)": "مغفره", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "إِنَّكُمۡ فِى غَفۡرٍۢ (Indeed, you are in forgiveness)"},
    {"Word (Arabic)": "شكر", "Transliteration": "Shukr", "Meaning": "Gratitude", "Example": "لَئِن شَكَرْتُمْ لَأَزِيدَنَّكُمْ (If you are grateful, I will increase your favor)"},
    {"Word (Arabic)": "خاتم", "Transliteration": "Khatim", "Meaning": "Seal", "Example": "فَٱلۡمَلَائِكَةُۥ يَأۡتُونَ فِيٓ (Then the angels will come in, sealed)"},
    {"Word (Arabic)": "وعد", "Transliteration": "Wa'd", "Meaning": "Promise", "Example": "إِنَّ وَعْدَ اللَّـهِ حَقٌۭ (Indeed, the promise of Allah is true)"},
    {"Word (Arabic)": "ثواب", "Transliteration": "Thawab", "Meaning": "Reward, Recompense", "Example": "وَفِى عِبَادَتِهِۦ لَهُمْ ثَوَابٌۭ (And in His worship is their reward)"},
    {"Word (Arabic)": "فتنة", "Transliteration": "Fitnah", "Meaning": "Trial, Temptation", "Example": "إِنَّمَآ أَمۡوَٰلُكُمۡ وَأَولَٰدُكُمۡ فِتْنَةٌۭ (Indeed, your wealth and your children are but a trial)"},
    {"Word (Arabic)": "قادر", "Transliteration": "Qadir", "Meaning": "Able, Powerful", "Example": "إِنَّكَ عَلَىٰ كُلِّ شَىْءٍ قَدِيرٌۭ (Indeed, You are capable of everything)"},
    {"Word (Arabic)": "بر", "Transliteration": "Birr", "Meaning": "Righteousness", "Example": "فَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَاةَ (Establish prayer and give zakah)"},
    {"Word (Arabic)": "آية", "Transliteration": "Ayah", "Meaning": "Sign, Verse", "Example": "وَفِى كُلِّ أَمْرٍۢ (And in every matter there is a sign)"},
    {"Word (Arabic)": "خوف", "Transliteration": "Khauf", "Meaning": "Fear", "Example": "وَإِذَا لَمْ تَأْتِ فِى (If you do not come forward)"},
    {"Word (Arabic)": "علم", "Transliteration": "Ilm", "Meaning": "Knowledge", "Example": "وَعَلَّمَ أَدَمَ ٱلْأَسْمَٰٓءَ كُلَّهَا (And taught Adam the names of all things)"},
    {"Word (Arabic)": "أمانة", "Transliteration": "Amanah", "Meaning": "Trust, Integrity", "Example": "إِنَّ ٱللَّهَ يَأۡمُرُكُمۡ أَن تُؤَدُّوا۟ ٱلۡأَمَٰنَٰتِ (Indeed, Allah commands you to return trusts)"},
    {"Word (Arabic)": "شكر", "Transliteration": "Shukr", "Meaning": "Gratitude, Thankfulness", "Example": "فَٱشْكُرُوا۟ لِى وَلَا تَكْفُرُونِ (So be grateful to Me and do not deny Me)"},
    {"Word (Arabic)": "رشد", "Transliteration": "Rushd", "Meaning": "Guidance, Right Path", "Example": "وَأَمَرُهُمْ شُورَىٰ بَيْنَهُمْ (And their affair is one of consultation among them)"},
    {"Word (Arabic)": "خيرات", "Transliteration": "Khayrat", "Meaning": "Goodness, Blessings", "Example": "وَقُولُوا۟ لِلنَّاسِ حُسْنًا (And speak to people kindly)"},
    {"Word (Arabic)": "عباد", "Transliteration": "Ibad", "Meaning": "Servants, Worshipers", "Example": "إِنَّمَا يَخْشَىٰ ٱللَّهَ مِنۡ عِبَادِهِۦٓ (Indeed, those who fear Allah are His servants)"},
    {"Word (Arabic)": "صبر", "Transliteration": "Sabr", "Meaning": "Patience, Perseverance", "Example": "يَا أَيُّهَا الَّذِينَ آمَنُوا۟ صَبِرُوا۟ (O you who have believed, be patient)"},
    {"Word (Arabic)": "نعمة", "Transliteration": "Ni'mah", "Meaning": "Blessing, Favor", "Example": "فَٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ (Remember the blessing of Allah upon you)"},
    {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "إِنَّكَ أَنتَ ٱلْغَفُورُ ٱلرَّحِيمُ (Indeed, You are the Forgiving, the Merciful)"},
    {"Word (Arabic)": "عدل", "Transliteration": "Adl", "Meaning": "Justice", "Example": "إِنَّ ٱللَّهَ يَأۡمُرُكُم بِالۡعَدْلِ (Indeed, Allah commands you to act justly)"},
    {"Word (Arabic)": "سجود", "Transliteration": "Sujud", "Meaning": "Prostration", "Example": "وَسَجَدُوا۟ لِرَبِّهِۦٓ (And they prostrated to their Lord)"},
    {"Word (Arabic)": "خوف", "Transliteration": "Khauf", "Meaning": "Fear", "Example": "وَلَا تَخَافُونَ إِلَّاۢ ٱللَّهَ (And do not fear anyone except Allah)"},
    {"Word (Arabic)": "يوم", "Transliteration": "Yawm", "Meaning": "Day", "Example": "يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ (The Day when neither wealth nor children will avail)"},
    {"Word (Arabic)": "جهاد", "Transliteration": "Jihad", "Meaning": "Struggle, Striving", "Example": "فَجَاهِدُوا۟ فِى سَبِيلِ ٱللَّهِ (So strive in the way of Allah)"},
    {"Word (Arabic)": "مغفرة", "Transliteration": "Maghfirah", "Meaning": "Forgiveness", "Example": "إِنَّ رَبَّنَا غَفُورٌۭ رَّحِيمٌۭ (Indeed, our Lord is Forgiving, Merciful)"},
    {"Word (Arabic)": "شرك", "Transliteration": "Shirk", "Meaning": "Polytheism, Association", "Example": "إِنَّ ٱللَّهَ لَا يَغْفِرُ أَنْ يُشْرَكَ بِهِۦ (Indeed, Allah does not forgive association with Him)"},
    {"Word (Arabic)": "إيمان", "Transliteration": "Iman", "Meaning": "Faith, Belief", "Example": "إِنَّ ٱلَّذِينَ آمَنُوا۟ وَعَمِلُوا۟ الصَّٰلِحَٰتِ (Indeed, those who have believed and done righteous deeds)"},
    {"Word (Arabic)": "الرحمن", "Transliteration": "Ar-Rahman", "Meaning": "The Most Merciful", "Example": "وَٱلرَّحْمَٰنُ ٱلۡمَلِكُ (The Most Merciful, the King)"},
    {"Word (Arabic)": "صلاة", "Transliteration": "Salat", "Meaning": "Prayer, Salah", "Example": "وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَاةَ (Establish prayer and give zakah)"},
    {"Word (Arabic)": "صدق", "Transliteration": "Sadaq", "Meaning": "Truth, Honesty", "Example": "إِنَّۢا۟ صَٰدِقُونَ (Indeed, we are truthful)"},
    {"Word (Arabic)": "عذاب", "Transliteration": "Adhab", "Meaning": "Punishment", "Example": "إِنَّۢا عَذَّبْنَٰهُ عَذَابًا شَدِيدًۭا (Indeed, We punished him with a severe punishment)"},
    {"Word (Arabic)": "ماء", "Transliteration": "Ma'a", "Meaning": "Water", "Example": "وَفَجَّرْنَا ٱلۡمَآءَ فَٱلۡتَقَىٰٓ (And We caused water to gush forth)"},
    {"Word (Arabic)": "بر", "Transliteration": "Birr", "Meaning": "Righteousness, Goodness", "Example": "إِنَّ فِىۡ ذَٰلِكَ لَبَرَٰٓةٌۭ (Indeed, in that is righteousness)"},
    {"Word (Arabic)": "شمس", "Transliteration": "Shams", "Meaning": "Sun", "Example": "وَجَعَلَ ٱلشَّمْسَ سِرَاجًا وَقَمَرًا مُنِيرًۭا (And made the sun a shining lamp and the moon a light)"},
    {"Word (Arabic)": "ليل", "Transliteration": "Layl", "Meaning": "Night", "Example": "وَجَعَلَ ٱللَّهُ لَكُمُ ٱلَّيْلَ لِبَاسًۭا (And Allah made the night for you a covering)"},
    {"Word (Arabic)": "صبح", "Transliteration": "Subh", "Meaning": "Morning", "Example": "وَأَذَّنَ فِى ٱلۡمَسَٰجِدِ (And announce in the mosques)"},
    {"Word (Arabic)": "رسول", "Transliteration": "Rasul", "Meaning": "Messenger", "Example": "وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًۭا (And We have sent to every nation a messenger)"},
    {"Word (Arabic)": "إحسان", "Transliteration": "Ihsan", "Meaning": "Excellence, Goodness", "Example": "إِنَّ اللَّهَ يُحِبُّ ٱلۡمُحْسِنِينَ (Indeed, Allah loves the doers of good)"},
    {"Word (Arabic)": "دين", "Transliteration": "Din", "Meaning": "Religion, Faith", "Example": "إِنَّ فِيٓهِۦ دِينٌۭ (Indeed, it is a faith)"},
    {"Word (Arabic)": "كذب", "Transliteration": "Kadhab", "Meaning": "Lying, Falsehood", "Example": "وَمَا كَانَ فِي قُلُوبِهِۦٓ (And what was in their hearts was false)"},
    {"Word (Arabic)": "زكاة", "Transliteration": "Zakat", "Meaning": "Charity, Almsgiving", "Example": "وَأَقِيمُوا۟ ٱلزَّكَاةَ وَءَاتُوا۟ ٱلۡمَٰكَةَ (And establish zakah and give to the poor)"},
    {"Word (Arabic)": "حياة", "Transliteration": "Hayat", "Meaning": "Life", "Example": "وَمَنۡ أَحْيَآهَا فَكَأَنَّمَآ أَحۡيَا النَّاسَ جَمِيعًۭا (And whoever saves a life, it is as if he saved mankind)"},
    {"Word (Arabic)": "موت", "Transliteration": "Mawt", "Meaning": "Death", "Example": "إِنَّكَ مَيِّتٌۭ وَإِنَّهُمْ مَّيِّتُونَ (Indeed, you will die and they will die)"},
    {"Word (Arabic)": "وعد", "Transliteration": "Wa'ad", "Meaning": "Promise", "Example": "إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ (Indeed, the promise of Allah is true)"},
    {"Word (Arabic)": "عدو", "Transliteration": "Adhuww", "Meaning": "Enemy", "Example": "وَقَالَ ٱللَّهُ تَعَٰلَىٰٓ (Allah said)"},
    {"Word (Arabic)": "أسود", "Transliteration": "Aswad", "Meaning": "Black", "Example": "وَإِذَا سَحَقَ ٱلۡشَّيْطَٰنُ وَمَلَأَنَآ (And when the devil suffocates and fills)"},
    {"Word (Arabic)": "عدل", "Transliteration": "Adl", "Meaning": "Justice, Fairness", "Example": "إِنَّ ٱللَّهَ يَأۡمُرُكُم بِٱلۡعَدْلِ (Indeed, Allah commands you to act justly)"},
    {"Word (Arabic)": "إجابة", "Transliteration": "Ijabah", "Meaning": "Response, Answer", "Example": "وَأَجَابَ رَبُّكُمۡ (And your Lord responded to you)"},
    {"Word (Arabic)": "غفر", "Transliteration": "Ghafr", "Meaning": "Forgiveness", "Example": "إِنَّكَ أَنتَ ٱلْغَفُورُ (Indeed, You are the Forgiving)"},
    {"Word (Arabic)": "شهادة", "Transliteration": "Shahada", "Meaning": "Testimony, Witness", "Example": "وَفَضَّلَكُمۡ عَلَىٰٓ (And chose you over)"},
    {"Word (Arabic)": "يَقِين", "Transliteration": "Yaqin", "Meaning": "Certainty", "Example": "وَكُونُوا۟ عَلَىٰ أَفْرَاجٍۢ (And be certain in His sight)"},
    {"Word (Arabic)": "خوف", "Transliteration": "Khauf", "Meaning": "Fear", "Example": "وَلاَ تَخَافُونهَا (And do not fear it)"},
    {"Word (Arabic)": "رحمة", "Transliteration": "Rahma", "Meaning": "Mercy", "Example": "إِنَّا۟ رَحْمَتِيۡ وَسِعَتْ كُلَّ شَىۡءٍۢ (My mercy encompasses all things)"},
    {"Word (Arabic)": "قرآن", "Transliteration": "Quran", "Meaning": "The Quran", "Example": "إِنَّۢا نَحْنُ نَزَّلْنَا ٱلۡقُرْآنَ (Indeed, We have sent down the Quran)"},
    {"Word (Arabic)": "موسى", "Transliteration": "Musa", "Meaning": "Moses", "Example": "وَفَجَّرْنَا ٱلۡمَآءَ فَٱلۡتَقَىٰٓ (And We parted the sea for Musa)"},
    {"Word (Arabic)": "إبراهيم", "Transliteration": "Ibrahim", "Meaning": "Abraham", "Example": "وَإِذۡ قَالَ إِبۡرَٰهِيمُ (And when Ibrahim said)"},
    {"Word (Arabic)": "ملاك", "Transliteration": "Malak", "Meaning": "Angel", "Example": "وَأَرۡسَلۡنَآ إِلَيْهِمْ رُسُلَنَا (And We sent to them Our messengers)"},
    {"Word (Arabic)": "حق", "Transliteration": "Haq", "Meaning": "Truth, Right", "Example": "وَقُولُوا۟ لِلنَّاسِ حُسْنًۭا (And speak to people kindly)"},
    {"Word (Arabic)": "صالح", "Transliteration": "Salih", "Meaning": "Righteous, Good", "Example": "إِنَّكَ إِذَا لَّمْ تَكُنْ مِنَ الصَّٰلِحِينَ (Indeed, you are among the righteous)"},
    {"Word (Arabic)": "إمام", "Transliteration": "Imam", "Meaning": "Leader", "Example": "وَجَعَلْنَا۟كِ لِلنَّاسِ إِمَامًا (And We made you a leader for the people)"},
    {"Word (Arabic)": "شهر", "Transliteration": "Shahr", "Meaning": "Month", "Example": "شَهۡرُ رَمَضَٰنَ (The month of Ramadan)"},
    {"Word (Arabic)": "أب", "Transliteration": "Ab", "Meaning": "Father", "Example": "وَقَالَ أَبُوهُمَا (And their father said)"},
    {"Word (Arabic)": "أم", "Transliteration": "Um", "Meaning": "Mother", "Example": "أُمُّهُۥٓ (His mother)"},
]





# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(quranic_words)

# Handle missing values for filtering
df['Word (Arabic)'] = df['Word (Arabic)'].fillna("")
df['Meaning'] = df['Meaning'].fillna("")

# Set the number of words per page
words_per_page = 15

# Initialize session state variables if not already set
if 'current_page' not in st.session_state:
    st.session_state.current_page = 0
if 'search_query' not in st.session_state:
    st.session_state.search_query = ""

# Search bar to filter words
search_query = st.text_input("Search for a Quranic word (Arabic or Meaning):", st.session_state.search_query)
st.session_state.search_query = search_query

# Filter words based on the search query
if search_query:
    df_filtered = df[
        df['Word (Arabic)'].str.contains(search_query, case=False) |
        df['Meaning'].str.contains(search_query, case=False)
    ].drop_duplicates()
else:
    df_filtered = df

# Calculate the total number of pages for the filtered data
total_pages = len(df_filtered) // words_per_page + (1 if len(df_filtered) % words_per_page > 0 else 0)

# Calculate the starting and ending index for the current page
start_index = st.session_state.current_page * words_per_page
end_index = start_index + words_per_page

# Get the words to display for the current page
page_words = df_filtered.iloc[start_index:end_index]

# Display the words for the current page with numbers
for idx, (index, row) in enumerate(page_words.iterrows(), 1):  # Start numbering from 1
    # Arabic word in green color with a number in front
    st.markdown(f"<h2 style='color: #2C6E49;'>{idx}. {row['Word (Arabic)']}</h2>", unsafe_allow_html=True)
    st.write(f"**Transliteration**: {row['Transliteration']}")
    st.write(f"**Meaning**: {row['Meaning']}")
    st.write(f"**Example**: {row['Example']}")
    st.write("---")

# Navigation buttons with callbacks
def prev_page():
    if st.session_state.current_page > 0:
        st.session_state.current_page -= 1

def next_page():
    if st.session_state.current_page < total_pages - 1:
        st.session_state.current_page += 1

col1, col2, col3 = st.columns([1, 5, 1])

# Show 'Previous' button only if not on the first page
with col1:
    st.button("Previous", on_click=prev_page, key="prev_btn", help="Go to previous page")

# Show the page number
with col2:
    st.markdown(f"<h3 style='text-align: center; color: #2C6E49;'>Page {st.session_state.current_page + 1} of {total_pages}</h3>", unsafe_allow_html=True)

# Show 'Next' button only if more pages exist
with col3:
    st.button("Next", on_click=next_page, key="next_btn", help="Go to next page")

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
        padding: 10px 10px;
        border-radius: 12px;
        border: 1px solid #ddd;
        width: 50%; /* Resize to half its size */
        height: 40px; /* Set height for vertical centering */
        line-height: 40px; /* Match height for text centering */
        margin: 0 auto; /* Center horizontally */
    }

    .stMarkdown h1 {
        color: #2C6E49;
        font-family: 'Georgia', serif;
    }

    .stMarkdown h3 {
        color: #2C6E49;
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
