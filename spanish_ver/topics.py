# Topics

topics = { 
# Letter A 
"Amor post mortem" : ["Amor más allá de la muerte.", "Carácter eterno del amor, sentimiento que perdura después de la muerte física."]
, "Amor bonus" : ["Amor bueno.", "Carácter positivo del amor espiritual."]
, "Amor ferus" : ["Amor salvaje.", "Carácter negativo del amor físico, de la pasión sexual."]
, "Amor mixtus" : ["Amor mixto", "Carácter complejo del amor físico y espiritual, cuando se dan conjuntamente."]

# Letter B 

, "Beatus ille" : ["Dichoso aquel.", "Elogio de la vida campesina, rural, frente al ajetreo urbano y cortesano."]

# Letter C 

, "Carpe diem" : ["Goza de este día.", "Invitación al goce de los años de juventud (= día) y al aprovechamiento del momento, antes de que el inevitable paso del tiempo nos conduzca a la vejez y a la muerte."]
, "Collige virgo rosas" : ["Coge, virgen, las rosas.", "Carácter irrecuperable de la juventud y la belleza: invitación a gozar del amor (simbolizado en la rosa) antes de que el tiempo robe nuestros mejores años."]
, "Contempus mundi" : ["Desprecio del mundo.", "Menosprecio del mundo y de la vida terrena que no son otra cosa que un valle de lágrimas y de dolor."]

# Letter D 

, "Descriptio puellae" : ["Descripción de la joven.", "Descripción física enumerativa-gradativa de una joven siguiendo un orden descendente: cabeza, cuello, manos..."]
, "Dum vivimus, vivamus" : ["Mientras vivimos, vivamos.", "Concepción de la vida humana como algo pasajero e irrenunciable con la consiguiente invitación a su goce y disfrute."]

# Letter F 

, "Fugit irreparabile tempus" : ["El tiempo pasa irremediablemente.", "Carácter irrecuperable del tiempo vivido: evocación de la condición fugaz de la vida humana."]
, "Furor amoris" : ["El amor apasionado.", "Concepción del amor como una enfermedad que niega todo poder a la razón."]

# Letter H 

, "Homo viator" : ["El hombre viajero.", "Carácter itinerante del vivir humano, considerada la existencia como camino, viaje o peregrinación."]

# Letter I

, "Ignis amoris" : ["El fuego del amor.", "Concepción del amor como fuego interior."]

# Letter L 

, "Locus amoenus" : ["Lugar agradable.", "Carácter mítico del paisaje ideal, descrito bucólicamente a través de sus diversos componentes (prado, arroyo, árbol...) y relacionado, casi siempre, con el sentimiento amoroso."]

# Letter M 

, "Memento mori" : ["Recuerda que has de morir.", "Carácter cierto de la muerte como fin de la vida: advertencia aleccionadora."]

, "Militia est vita hominis super terra" : ["La vida de los hombres sobre la tierra es lucha.", "Carácter bélico de la vida humana, entendida como campo de batalla en el que se desarrolla una continua lucha frente a todo: los hombres, la sociedad, el destino..."]

, "Militia species amor est" : ["El amor es un tipo de lucha.", "Carácter bélico del sentimiento amoroso, visto como contienda o enfrentamiento entre dos adversarios: los enamorados."]

# Letter O 

, "Omnia mors aequat" : ["La muerte iguala a todos.", "Carácter igualitario de la muerte que, en su poder, no discrimina a sus víctimas ni respeta jerarquías."]
, "Oculos Sicarii" : ["Ojos homicidas.", "Carácter simbólicamente asesino de la mirada."]

# Letter P

, "Peregrinatio vitae" : ["El viaje de la vida.", "Carácter pasajero de la vida humana, entendida como camino que el hombre debe recorrer."]

# Letter Q

, "Quodomo fabula, sic vita" : ["Así como el teatro es la vida.", "Carácter representativo de la vida humana: dramatización única e irrepetible de nuestra existencia."]
, "Quotidie morimur" : ["Morimos casa día.", "Carácter determinante del tiempo en la vida humana, considerada como camino que debe recorrerse hacia su meta: la muerte. Según ello, cada momento de nuestra existencia es un paso hacia la muerte."]

# Letter R

, "Recusatio" : ["Rechazo.", "Rechazo de valores y actitudes ajenas."]
, "Religio amoris" : ["Culto al amor.", "Carácter alienante del sentimiento amoroso, presentado como una enfermedad o servidumbre de la que el hombre debe liberarse."]
, "Ruit hora" : ["El tiempo corre.", "Carácter efímero del tiempo y, por extensión, de la vida, que nos precipita hacia la muerte irremediablemente."]

# Letter S 

, "Sic transit gloria mundi" : ["Así pasa la gloria mundana.", "Carácter pasajero de la fortuna o reputación humana, condenada a verse arrastrada por la muerte."]
, "Somnium, imago mortis" : ["El sueño, imagen de la muerte.", "Carácter de muerte aparente que ofrece el cuerpo humano en actitud de reposo, cuando el hombre duerme."]

# Letter T

, "Theatrum mundi" : ["El teatro del mundo.", "Carácter representativo del mundo y de la vida, entendidos como escenarios dramáticos en que diversos actores -los hombres- representan los papeles de una obra ya escrita."]

# Letter U

, "Ubi sunt" : ["¿Dónde están?", "Carácter desconocido del más allá, de la otra orilla de la muerte, materializado en interrogaciones retóricas acerca del destino o paradero de grandes hombres que han muerto."]

# Letter V

, "Vanitas vanitatis" : ["Vanidad de vanidades.", "Carácter engañoso de las apariencias, que exige el rechazo o renuncia de toda ambición humana, por considerarla vana."]
, "Varium et mutabile semper femina" : ["Variable y mudable, siempre es la mujer", "Carácter inestable de la mujer, presentada desde una perspectiva misógina como ser cambiante e indeciso."]
, "Venatus amoris" : ["Caza de amor.", "La relación amorosa es presentada como cacería del ser amado."]
, "Vita flumen" : ["La vida como río.", "Carácter fluyente de la existencia humana, equiparada a un río que avanza, sin detenerse, hasta fundirse en el mar, su muerte."]
, "Vita somnium" : ["La vida como sueño.", "Carácter onírico de la vida humana, entendida como un sueño irreal, una ficción extraña y pasajera."]

}

first_word = []

for phrase in topics:
	templo = phrase.split(" ",1)[0].lower()
	tempup = phrase.split(" ",1)[0].capitalize()
	first_word.append(templo)
	first_word.append(tempup)