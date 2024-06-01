# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image bg Small_Apartment_Kitchen = "images/BG_appartement/Small_Apartment_Kitchen.png"
image bg Subway_morning = "images/BG_subway/subway-morning.jpg"
image bg Bureau_lisa = "images/BG_office/bureau_lisa.jpg"

# Déclarez les personnages utilisés dans le jeu.
define l = Character('Lisa', color="#ecac3e")
define c = Character('Charlene', color="#b02424")
define s = Character('Sophie', color="#ff3ce5")
define j = Character('Jean', color="#4177ff")
define b = Character('M.Bourbon', color="#168609")

transform resize_char:
    zoom 0.7
    ypos 950

# Variable pour suivre si l'action a été effectuée
default manger_jean = False
default tuer_jean = False
default tuer_charlene = False
default tuer_sophie = False
default tuer_bourbon = False
default nb_boucle = 1
default nb_tuer_jean = 0
default nb_tuer_charlene = 0
default nb_tuer_sophie = 0
default nb_tuer_bourbon = 0


# Le jeu commence ici
label start:

    scene bg Small_Apartment_Kitchen
    show lisa_normal:
        center
        resize_char

    l "Encore une journée qui commence"

    l "Métro ... Boulot ... Dodo"

    l "J'espère qu'aujour'hui sera différent"

    l "Bon ! Il ne faut pas que je traine pour partir au travail"

    l "Un petit café avec du lait et on est parti"

    "{i}Lisa va dans la cuisine et ouvre le réfrégirateur{/i}"

    show lisa_shocked:
        center
        resize_char

    l "Tiens ?"

    l "J'ai racheté du lait hier ?"

    l "Je ne me souviens pas"

    l "Mais non ! Cette brique est aussi périmée. Exactement comme la brique d'hier que j'ai jetté"

    show lisa_angry:
        center
        resize_char

    l "Je suis sur de l'avoir jetté ... Bizarre"

    "{i}Lisa n'a finalement plus le temps pour un café et part donc au bureau confuse{/i}"

    jump subway_morning

label subway_morning:

    scene bg Subway_morning
    show lisa_sad:
        right
        resize_char

    "{i}Lisa est donc dans le métro. Attendant son arrêt comme tous les travailleurs et autres personnes autour d'elle. Elle soupir avant de voir une vielle dame s'approcher d'elle{/i}"

    if nb_boucle >= 2:
        l "Et c'est reparti pour un tour de boucle"

    show bourbon_normal:
        left
        resize_char

    b "Excusez moi ma petite dame. Mon dos me fait mal. Est ce que vous voulez bien me donner votre place s'il vous plaît ?"

    menu:
        b "Excusez moi ma petite dame. Mon dos me fait mal. Est ce que vous voulez bien me donner votre place s'il vous plaît ?"

        "Laisser la place à la vielle dame":
            jump subway_laisser

        "Ne pas laisser sa place":
            jump subway_pas_laisser

        "J'ai l'impression que vous me cachez quelque chose" if nb_boucle >= 3:
            jump subway_revelation

label subway_laisser:

    show lisa_smile:
        right
        resize_char
        Dissolve(.2)

    l "Oui madame, pas de souci"

    show bourbon_smirk:
        left
        resize_char

    b "Merci beaucoup jeune fille"

    hide lisa_sad
    hide bourbon_normal

    show lisa_smile:
        left
        resize_char

    show bourbon_smirk:
        right
        resize_char

    l "Avec cette bonne action, j'espère que ma journée sera meilleur"

    jump office_morning

label subway_pas_laisser:

    show lisa_angry:
        right
        resize_char

    l "Je suis aussi fatiguée que vous"

    jump office_morning

label subway_revelation:

    show lisa_normal:
        right
        resize_char

    b "hihihihi"

    jump office_morning

label office_morning:

    scene bg Bureau_lisa:
        zoom 1.9
    show lisa_smile:
        left
        resize_char

    "{i}Lisa arrive dans son bureau et vois sa collègue et amie Charlene{/i}"

    show charlene_smile_2:
        right
        resize_char

    c "Bonjour Lisa ! Belle matinée n'est ce pas ?"

    l "Bonjour Charlene. Oui c'est vrai qu'il fait beau aujourd'hui"

    c "Apparement ce sera comme ça toute la semaine"

    show charlene_smile:
        right
        resize_char

    c "C'est l'arriver des beaux jours. On pourrais allez déjeuner dehors si tu veux. Tu me préviendra si ça t'intéresse"

    l "Je n'oublirai pas promis"

    menu:
        "{i}Que va faire Lisa maintenant ?{/i}"

        "Se mettre au travaille":
            jump office_morning_travaille

        "Aller prendre un café avant le travaille":
            jump office_morning_cafe

        "Aller faire quelques photocopies pour la réunion de ce soir":
            jump office_morning_imprimante


label office_morning_travaille:

label office_morning_cafe:

label office_morning_imprimante:


    return
