# Topics

topics = { 
# Letter A 
"Amor post mortem" : ["Love beyond death.", "The nature of love is eternal, a bond that goes beyond physical death."]
, "Amor bonus" : ["Good love.", "The nature of love is good."]
, "Amor ferus" : ["Fiery love.", "A negative nature of the physical love, reference to passionate, rough sex."]
, "Amor mixtus" : ["Mix love.", "The complex nature of love when the physical and spiritual parts merge."]

# Letter B 

, "Beatus ille" : ["Blissful thee.", "A praise to the simple life, farm and rural instead of the hustle of the modern life."]

# Letter C 

, "Carpe diem" : ["Seize the day.", "To enjoy the present and not worry about the future; to live in the moment."]
, "Collige virgo rosas" : ["Grab the roses, virgin.", "The irrecoverable nature of youth and beauty; an invitation to enjoy love (represented in the symbol of a rose) before time takes away our youth."]
, "Contempus mundi" : ["Contempt to the world.", "Contempt to the world and the terrenal life, nothing but a valley of pain and tears."]

# Letter D 

, "Descriptio puellae" : ["Description of a young girl.", "Description of a young girl in a descendant order, head, neck, chest, ..."]
, "Dum vivimus, vivamus" : ["While we're alive, we live.", "The idea of life as something transient and inalienable, hence an invitation to enjoy and seize it."]

# Letter F 

, "Fugit irreparabile tempus" : ["Time passes irredeemably.", "The idea of time as something that cannot be recovered, life itself is fleeting and transient."]

, "Furor amoris" : ["Passionate love.", "The idea of love as a disease that negates all reason and logic."]

# Letter H 

, "Homo viator" : ["Traveling man.", "The idea of the living man as an itinerant being, consider your existence as a journey through life."]

# Letter I

, "Ignis amoris" : ["The fire of love.", "The idea of love as a fire that burns inside you."]

# Letter L 

, "Locus amoenus" : ["A nice scene.", "The mythical nature of the ideal scene described by its bucolic elements, almost always related to love."]

# Letter M 

, "Memento mori" : ["Reminder of your death.", "Death is certain, the end of everyone's life, a reminder to never forget."]

, "Militia est vita hominis super terra" : ["The life of men on this earth is a struggle.", "The idea of life as a military thing, a field of war against everyone; society, other men, love, destiny, ..."]

, "Militia species amor est" : ["Love is a struggle.", "The idea of love as a struggle between the two lovers."]

# Letter O 

, "Omnia mors aequat" : ["Death sets everyone equal.", "Death as an equality force, it doesn't care about hierarchy, richness or power; upon its arrival all humans are the same."]
, "Oculos Sicarii" : ["Murdering eyes.", "The idea of a stare that would kill you if it could."]

# Letter P

, "Peregrinatio vitae" : ["Life as a journey.", "The idea of life as a journey, a road which where the man must walk through."]

# Letter Q

, "Quodomo fabula, sic vita" : ["Life is like theater.", "The idea that life is a play with the man itself as protagonist."]
, "Quotidie morimur" : ["We die every day.", "Life has a determined time, by each moment that passes we're closer to the end of our journey which is death."]

# Letter R

, "Recusatio" : ["Rejection.", "Reject others values and actions."]
, "Religio amoris" : ["Worship love.", "Love is a cult which man is bound to serve, as such we must free ourselves from it."]
, "Ruit hora" : ["Time runs.", "By nature time is fleeting, hence life is too. As such we're running towards our inevitable death."]

# Letter S 

, "Sic transit gloria mundi" : ["Glory is mundane and it passes by.", "Fortune, glory and reputation are all fleeting, death takes everything away."]
, "Somnium, imago mortis" : ["Sleep, an image of death.", "When a man sleeps it's as though he was dead."]

# Letter T

, "Theatrum mundi" : ["The world, a theater.", "The idea of the world and life as a play, think of them as different dramatic scenarios in which actors -mankind- represent their lives on an already written play."]

# Letter U

, "Ubi sunt" : ["Where are they?", "The idea of the unkown, beyond death nothing is certain."]

# Letter V

, "Vanitas vanitatis" : ["Vanity of vanities.", "Looks are decieving, human ambitions are vain, thus they should be rejected."]
, "Varium et mutabile semper femina" : ["Wayward and unsettled, women are.", "Women have a wayward nature, they change and never settle."]
, "Venatus amoris" : ["The hunt for love.", "Love is presented as a hunt, where one hunts for its lover."]
, "Vita flumen" : ["Life is a river.", "Existence is a river that always goes foward, never stopping, until it reaches the sea. Death."]
, "Vita somnium" : ["Life is a dream.", "Life is irreal, strange and fleeting, much like a dream."]

}

first_word = []

for phrase in topics:
	templo = phrase.split(" ",1)[0].lower()
	tempup = phrase.split(" ",1)[0].capitalize()
	first_word.append(templo)
	first_word.append(tempup)