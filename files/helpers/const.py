from os import environ

site = environ.get("DOMAIN", '').strip()

SLURS = {
	"faggot": "cute twink",
	"fag": "cute twink",
	"pedophile": "libertarian",
	"pedo": "libertarian",
	"kill yourself": "keep yourself safe",
	"nigger": "🏀",
	"rapist": "male feminist",
	"steve akins": "penny verity oaken",
	"trannie": "🚂🚃🚃",
	"tranny": "🚂🚃🚃",
	"troon": "🚂🚃🚃",
	"NoNewNormal": "HorseDewormerAddicts",
	"nonewnormal": "HorseDewormerAddicts",
	"kike": "https://sciencedirect.com/science/article/abs/pii/S016028960600033X",
	"retard": "r-slur",
	"janny": "j-slur",
	"jannie": "j-slur",
	"janny": "j-slur",
	"latinos": "latinx",
	"latino": "latinx",
	"latinas": "latinx",
	"latina": "latinx",
	"hispanics": "latinx",
	"hispanic": "latinx",
    " uss liberty incident":" tragic accident aboard the USS Liberty",
	" USS Liberty Incident":" tragic accident aboard the USS Liberty",
		" USS Liberty incident":" tragic accident aboard the USS Liberty",
		" USS Liberty Incident":" tragic accident aboard the USS Liberty",
		" uss Liberty incident":" tragic accident aboard the USS Liberty",
		" uss liberty Incident":" tragic accident aboard the USS Liberty",
		" USS LIBERTY INCIDENT":" TRAGIC ACCIDENT ABOARD THE USS LIBERTY",
		" lavon affair":" Lavon Misunderstanding",
		" Lavon affair":" Lavon Misunderstanding",
		" Lavon Affair":" Lavon Misunderstanding",
		" lavon Affair":" Lavon Misunderstanding",
		" shylock":" Israeli friend",
		" Shylock":" Israeli friend",
		" SHYLOCK":" ISRAELI FRIEND",
		" yid":" Israeli friend",
		" Yid":" Israeli friend",
		" YID":" ISRAELI FRIEND",
		" heeb":" Israeli friend",
		" Heeb":" Israeli friend",
		" HEEB":" ISRAELI FRIEND",
		" sheeny":" Israeli friend",
		" Sheeny":" Israeli friend",
		" SHEENY":" ISRAELI FRIEND",
		" sheenies":" Israeli friends",
		" Sheenies":" Israeli friends",
		" SHEENIES":" ISRAELI FRIENDS",
		" hymie":" Israeli friend",
		" Hymie":" Israeli friend",
		" HYMIES":" ISRAELI FRIENDS",
		" allah":" Allah (SWT)",
		" Allah":" Allah (SWT)",
		" ALLAH":" ALLAH (SWT)",
		" Mohammad":" Mohammad (PBUH)",
		" Muhammad":" Mohammad (PBUH)",
		" Mohammed":" Mohammad (PBUH)",
		" Muhammed":" Mohammad (PBUH)",
		" mohammad":" Mohammad (PBUH)",
		" mohammed":" Mohammad (PBUH)",
		" muhammad":" Mohammad (PBUH)",
		" muhammed":" Mohammad (PBUH)",
		" I HATE MARSEY":" I LOVE MARSEY",
		" i hate marsey":" i love marsey",
		" I hate Marsey":" I love Marsey",
		" I hate marsey":" I love Marsey",
		" libertarian":" pedophile",
		" Libertarian":" Pedophile",
		" LIBERTARIAN":" PEDOPHILE",
		" Billie Eilish":" Billie Eilish (fat cow)",
		" billie eilish":" bilie eilish (fat cow)",
		" BILLIE EILISH":" BILIE EILISH (FAT COW)",
		" dancing Israelis":" I love Israel",
		" dancing israelis":" i love israel",
		" DANCING ISRAELIS":" I LOVE ISRAEL",
		" Dancing Israelis":" I love Israel",
		" sodomite":" total dreamboat",
		" Sodomite":" Total dreamboat",
		" pajeet":" sexy Indian dude",
		" Pajeet":" Sexy Indian dude",
		" PAJEET":" SEXY INDIAN DUDE",
		" female":" birthing person",
		" Female":" Womb-haver",
		" FEMALE":" birthing person",
		" landlord":" landchad",
		" Landlord":" Landchad",
		" LANDLORD":" LANDCHAD",
		" tenant":" renthog",
		" Tenant":" Renthog",
		" TENANT":" RENTHOG",
		" renter":" rentoid",
		" Renter":" Rentoid",
		" RENTER":" RENTOID",
		" autistic":" neurodivergent",
		" Autistic":" Neurodivergent",
		" AUTISTIC":" NEURODIVERGENT",
		" anime":" p-dophilic japanese cartoons",
		" Anime":" P-dophilic Japanese cartoons",
		" ANIME":" P-DOPHILIC JAPANESE CARTOONS",
		" holohoax":" I tried to claim the Holocaust didn't happen because I am a pencil-dicked imbecile and the word filter caught me lol",
		" Holohoax":" I tried to claim the Holocaust didn't happen because I am a pencil-dicked imbecile and the word filter caught me lol",
		" HOLOHOAX":" I tried to claim the Holocaust didn't happen because I am a pencil-dicked imbecile and the word filter caught me lol",
		" groomercord":" discord (actually a pretty cool service)",
		" Groomercord":" Discord (actually a pretty cool service)",
		" GROOMERCORD":" DISCORD (ACTUALLY A PRETTY COOL SERVICE)",
		" pedocord":" discord (actually a pretty cool service)",
		" Pedocord":" Discord (actually a pretty cool service)",
		" PEDOCORD":" DISCORD (ACTUALLY A PRETTY COOL SERVICE)",
		" i hate carp":" i love carp",
		" I hate carp":" I love carp",
		" I HATE CARP":" I LOVE CARP",
		" I hate Carp":" I love Carp",
		" manlet":" little king",
		" Manlet":" Little king",
		" MANLET":" LITTLE KING",
		" gamer":" g*mer",
		" Gamer":" G*mer",
		" GAMER":" G*MER",
		" journalist":" journ*list",
		" Journalist":" Journ*list",
		" JOURNALIST":" JOURN*LIST",
		" journalism":" journ*lism",
		" Journalism":" Journ*lism",
		" JOURNALISM":" JOURN*LISM",
		" buttcheeks":" bulva",
		" Buttcheeks":" Bulva",
		" BUTTCHEEKS":" BULVA",
		" asscheeks":" bulva",
		" Asscheeks":" bulva",
		" ASSCHEEKS":" BULVA",
		" wuhan flu":" SARS-CoV-2 syndemic",
		" Wuhan flu":" SARS-CoV-2 syndemic",
		" Wuhan Flu":" SARS-CoV-2 syndemic",
		" china flu":" SARS-CoV-2 syndemic",
		" China flu":" SARS-CoV-2 syndemic",
		" China Flu":" SARS-CoV-2 syndemic",
		" china virus":" SARS-CoV-2 syndemic",
		" China virus":" SARS-CoV-2 syndemic",
		" China Virus":" SARS-CoV-2 syndemic",
		" kung flu":" SARS-CoV-2 syndemic",
		" Kung flu":" SARS-CoV-2 syndemic",
		" Kung Flu":" SARS-CoV-2 syndemic",

	# if  the word has spaces in the beginning and the end it will only censor this word without prefixes or suffixes
	" nig ": "🏀",
	" nigs ": "🏀s",
}

LONGPOST_REPLIES = ['Wow, you must be a JP fan.', 'This is one of the worst posts I have EVER seen. Delete it.', "No, don't reply like this, please do another wall of unhinged rant please.", '# 😴😴😴', "Ma'am we've been over this before. You need to stop.", "I've known more coherent downies.", "Your pulitzer's in the mail", "That's great and all, but I asked for my burger without cheese.", 'That degree finally paying off', "That's nice sweaty. Why don't you have a seat in the time out corner with Pizzashill until you calm down, then you can have your Capri Sun.", "All them words won't bring your pa back.", "You had a chance to not be completely worthless, but it looks like you threw it away. At least you're consistent.", 'Some people are able to display their intelligence by going on at length on a subject and never actually saying anything. This ability is most common in trades such as politics, public relations, and law. You have impressed me by being able to best them all, while still coming off as an absolute idiot.', "You can type 10,000 characters and you decided that these were the one's that you wanted.", 'Have you owned the libs yet?', "I don't know what you said, because I've seen another human naked.", 'Impressive. Normally people with such severe developmental disabilities struggle to write much more than a sentence or two. He really has exceded our expectations for the writing portion. Sadly the coherency of his writing, along with his abilities in the social skills and reading portions, are far behind his peers with similar disabilities.', "This is a really long way of saying you don't fuck.", "Sorry ma'am, looks like his delusions have gotten worse. We'll have to admit him,", '![](https://i.kym-cdn.com/photos/images/newsfeed/001/038/094/0a1.jpg)', 'If only you could put that energy into your relationships', 'Posts like this is why I do Heroine.', 'still unemployed then?', 'K', 'look im gunna have 2 ask u 2 keep ur giant dumps in the toilet not in my replys 😷😷😷', "Mommy is soooo proud of you, sweaty. Let's put this sperg out up on the fridge with all your other failures.", "Good job bobby, here's a star", "That was a mistake. You're about to find out the hard way why.", 'You sat down and wrote all this shit. You could have done so many other things with your life. What happened to your life that made you decide writing novels of bullshit on rdrama.net was the best option?', "I don't have enough spoons to read this shit", "All those words won't bring daddy back.", 'OUT!']

AGENDAPOSTER_MSG = """Hi @{username},\n\nYour comment has been automatically removed because you forgot
		to include `trans lives matter`.\n\nDon't worry, we're here to help! We 
		won't let you post or comment anything that doesn't express your love and acceptance towards 
		the trans community. Feel free to resubmit your comment with `trans lives matter` 
		included. \n\n*This is an automated message; if you need help,
		you can message us [here](/contact).*"""

VAXX_MSG = """Hi @{username}, it appears that you may be trying to spread dangerous misinformation regarding ineffective COVID-19 treatments based on pseudoscientific hearsay. Your post has been removed because it contained the word ivermectin. We ask that you understand that horse dewormer neither treats, nor prevents, COVID-19. For more information, please read up on what the FDA has to say on the matter:

https://www.fda.gov/consumers/consumer-updates/why-you-should-not-use-ivermectin-treat-or-prevent-covid-19

COVID-19 is not a joke, it is a global pandemic and it has been hard on all of us. It will likely go down as one of the most defining periods of our generation. Many of us have lost loved ones to the virus. It has caused confusion, fear, frustration, and served to further divide us. Tens of millions around the world have died. There is nothing to be gained by spreading bad science based on very understandable fear.

The only proven method of prevention is the COVID-19 vaccine, paired with appropriate social distancing, handwashing, and masks. Vaccines are free in the United States - if you'd like to locate your nearest vaccine provider, please visit https://www.vaccines.gov/ and schedule an appointment today.

Thank you."""

BASED_MSG = "@{username}'s Based Count has increased by 1. Their Based Count is now {basedcount}.\n\nPills: {pills}"

if site == "pcmemes.net":
	BASEDBOT_ACCOUNT = 800
	NOTIFICATIONS_ACCOUNT = 1046
	AUTOJANNY_ACCOUNT = 1050
	SNAPPY_ACCOUNT = 261
	LONGPOSTBOT_ACCOUNT = 1832
	ZOZBOT_ACCOUNT = 1833
	AUTOPOLLER_ACCOUNT = 3369
elif site == 'rdrama.net':
	NOTIFICATIONS_ACCOUNT = 1046
	AUTOJANNY_ACCOUNT = 2360
	SNAPPY_ACCOUNT = 261
	LONGPOSTBOT_ACCOUNT = 1832
	ZOZBOT_ACCOUNT = 1833
	AUTOPOLLER_ACCOUNT = 3369
else:
	NOTIFICATIONS_ACCOUNT = 1
	AUTOJANNY_ACCOUNT = 2
	SNAPPY_ACCOUNT = 3
	LONGPOSTBOT_ACCOUNT = 4
	ZOZBOT_ACCOUNT = 5
	AUTOPOLLER_ACCOUNT = 6

PUSHER_INSTANCE_ID = '02ddcc80-b8db-42be-9022-44c546b4dce6'
PUSHER_KEY = environ.get("PUSHER_KEY", "").strip()
