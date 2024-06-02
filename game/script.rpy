# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image bg Small_Apartment_Kitchen = "images/BG_appartement/Small_Apartment_Kitchen.png"
image bg Subway_morning = "images/BG_subway/subway-morning.jpg"
image bg Bureau_lisa = "images/BG_office/bureau_lisa.jpg"
image bg Restaurant_lunch = "images/BG_autre/Restaurant.png"
image bg Cafeteria_morning = "images/BG_office/Kitchen_Day.png"
image bg Reserve = "images/BG_office/Reserve.jpg"
image bg Reunion = "images/BG_office/Reunion.jpg"
image bg Kitchen_Day = "images/BG_office/Kitchen_Day.png"

# Déclarez les personnages utilisés dans le jeu.
define l = Character('Lisa', color="#ecac3e")
define c = Character('Charlene', color="#b02424")
define s = Character('Sophie', color="#ff3ce5")
define j = Character('Jean', color="#4177ff")
define b = Character('M.Bourbon', color="#168609")
define v = Character('Vielle dame', color="#e471b4")

transform resize_char:
    zoom 0.7
    ypos 950

# Variable pour suivre si l'action a été effectuée
default manger_jean = False
default reunion_preparer = False
default charlene_archive = False
default amour = False
default nb_boucle = 0
default nb_travail = 0

default tuer_jean = False
default tuer_charlene = False
default tuer_sophie = False
default tuer_bourbon = False
default tuer_charlene_restaurant = False

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
    l "J'espère qu'aujourd'hui sera différent"
    l "Bon ! Il ne faut pas que je traîne pour partir au travail"
    l "Un petit café avec du lait et on est parti"
    "{i}Lisa va dans la cuisine et ouvre le réfrigérateur{/i}"

    show lisa_shocked:
        center
        resize_char
    hide lisa_normal

    l "Tiens ?"
    l "J'ai racheté du lait hier ?"
    l "Je ne me souviens pas"
    l "Mais non ! Cette brique est aussi périmée. Exactement comme la brique d'hier"

    show lisa_angry:
        center
        resize_char
    hide lisa_shocked

    l "Je suis sûre de l'avoir jetée ... Bizarre"
    "{i}Lisa n'a finalement plus le temps pour un café et part donc au bureau confuse{/i}"
    jump subway_morning

# ----------------------------------------------------------------------------
#                                   SUBWAY
# ----------------------------------------------------------------------------

label subway_morning:

    $ manger_jean = False
    $ reunion_preparer = False
    $ charlene_archive = False
    $ amour = False
    $ tuer_jean = False
    $ tuer_charlene = False
    $ tuer_charlene_restaurant = False
    $ tuer_sophie = False
    $ tuer_bourbon = False
    $ nb_travail = 0

    scene bg Subway_morning
    show lisa_sad:
        right
        resize_char
    hide lisa_angry

    "{i}Lisa est dans le métro. Attendant son arrêt comme tous les travailleurs et autres personnes autour d'elle. Elle soupire avant de voir une vieille dame s'approcher d'elle{/i}"
    if nb_boucle >= 2:
        l "Et c'est reparti pour un tour de boucle"

    show vieille_smile:
        left
        resize_char

    v "Excusez-moi mademoiselle. Mon dos me fait mal. Est-ce que vous voulez bien me donner votre place s'il vous plaît ?"

    menu:
        v "Excusez-moi jeune demoiselle. Mon dos me fait mal. Est-ce que vous voulez bien me donner votre place s'il vous plaît ?"

        "Laisser la place à la vieille dame":
            jump subway_laisser

        "Ne pas laisser sa place":
            jump subway_pas_laisser

        "J'ai l'impression que vous me cachez quelque chose" if nb_boucle >= 3:
            jump subway_revelation

label subway_laisser:

    show lisa_smile:
        right
        resize_char
    hide lisa_sad

    l "Oui madame, pas de souci"

    show vieille_smile_2:
        left
        resize_char
    hide vieille_smile

    v "Merci beaucoup jeune fille"

    show lisa_smile:
        left
        resize_char

    show vieille_smile_2:
        right
        resize_char

    l "Avec cette bonne action, j'espère que ma journée sera meilleure"
    jump office_morning

label subway_pas_laisser:

    show lisa_angry:
        right
        resize_char
    hide lisa_sad

    l "Eh bien… Ecoutez madame, je suis une femme occupée et fatiguée… j’aimerais si cela ne vous dérange pas, pourvoir rester assise."

    show vieille_angry:
        left
        resize_char

    v "Quel toupet ! Les jeunes gens de nos jours non plus de respect pour leur ainés ! Vous auriez pu me dire non pour me céder la place d’une autre manière."

    show lisa_sad:
        right
        resize_char
    hide lisa_angry

    l "Je… hum… "

    hide vieille_smile
    hide vieille_angry

    v "…"

    show lisa_sad:
        right
        resize_char

    l "Mince… J’aurais vraiment pas du le dire comme cela… La routine me rend mauvaise."

    jump office_morning

label subway_revelation:

    show lisa_normal:
        right
        resize_char
    hide lisa_sad

    show vieille_normal:
        left
        resize_char
    hide vieille_smile

    v "Cela ce vois tant que cela ?"

    show lisa_shocked:
        right
        resize_char
    hide lisa_normal

    $ nb_boucle_str = "Je sais aussi que vous êtes coincée dans cette journée déjà {} fois.".format(nb_boucle)

    l "!!!"
    v "Effectivement je sais, je sais à propos de votre condition actuelle."
    v "[nb_boucle_str]"

    show lisa_sad:
        right
        resize_char
    hide lisa_shocked

    $ nb_boucle_str = "déjà… {} fois ?".format(nb_boucle)

    l "[nb_boucle_str]"
    v "Oui, et cela commence à vous affecter à mon avis."
    v "… "
    v "Écoute jeune fille, je ne peux pas t’aider à sortir de ce cauchemar. Je ne suis qu’une pauvre veille femme… spectatrice de ton désarroi."
    v "Cependant je peux te donner conseil, après tout je ne suis plus bonne qu’à ça, alors écoute bien."

    show lisa_normal:
        right
        resize_char
    hide lisa_sad

    "{i}Lisa hoche la tête vers la vielle dame, un peu réconforté que quelqu’un soit aussi au courant de ce qu’il lui arrive. La dame d’un belle age poursuivie{/i}"
    v "Pour te sortir de la, aussi étrangement que cliché, tu doit vivre une journée idéal."

    show lisa_shocked:
        right
        resize_char
    hide lisa_ normal

    l "IDÉAL ?! Je vois pas en quoi cette journée pourrais être idéal !"
    v "Pas la peine de crier jeune fille, nous somme toujours dans le métro"

    show lisa_normal:
        right
        resize_char
    hide lisa_shocked

    l "O-oui pardon"
    v "…"
    l "Du coup vous disiez ?"
    v "…"
    l "…?"
    v "…"

    show lisa_shocked:
        right
        resize_char
    hide lisa_normal

    l "Quoi c’est tout ?!"
    v "Tu t’attendais à quoi gamine ? Je suis pas dans ta tête !"
    v "Réfléchis un peu voyons, une journée idéal pour toi… Cela ressemblerais a quoi ?"

    show lisa_normal:
        right
        resize_char
    hide lisa_shocked

    l "Ma journée idéal… ?"
    "{i}Lisa ce mit à réfléchir aux paroles de la vielle dame… une journée idéal ?{/i}"

    hide vieille_normal

    "… "

    show lisa_shocked:
        right
        resize_char
    hide lisa_normal

    l "Elle… elle est partie ?"
    l "…"

    show lisa_normal:
        right
        resize_char
    hide lisa_angry

    l "Bon réfléchissons… J’ai envie…"
    l "De passer plus de temps avec Jean"
    l "Avoir une promotion ? Pourquoi faire ? Je vais juste avoir plus de responsabilité dans une entreprise inintéressante. Au moins garder mon travail me suffirais"
    l "Et enfin… "
    l "…"

    show lisa_angry:
        right
        resize_char
    hide lisa_normal

    l "J’ai besoin de violence !"
    jump office_morning

# ----------------------------------------------------------------------------
#                               OFFICE MORNING
# ----------------------------------------------------------------------------

label office_morning:

    scene bg Bureau_lisa:
        zoom 1.9
    show lisa_smile:
        left
        resize_char

    "{i}Lisa arrive dans son bureau et voit sa collègue et amie Charlene{/i}"

    show charlene_smile_2:
        right
        resize_char

    c "Bonjour Lisa ! Belle matinée n'est-ce pas ?"
    l "Bonjour Charlene. Oui c'est vrai qu'il fait beau aujourd'hui"
    c "Apparemment ce sera comme ça toute la semaine"

    show charlene_smile:
        right
        resize_char

    c "C'est l'arrivée des beaux jours. On pourrait aller déjeuner dehors si tu veux. Tu me préviendras si ça t'intéresse"
    l "Je n'oublierai pas promis"

    menu:
        "{i}Que va faire Lisa maintenant ?{/i}"

        "Se mettre au travail":
            jump office_morning_travaille

        "Aller prendre un café avant le travail":
            jump office_morning_cafe

        "Aller faire quelques photocopies pour la réunion de ce soir":
            jump office_morning_imprimante

# ----------------------------------------------------------------------------
#                           TRAVAILLE MORNING
# ----------------------------------------------------------------------------

label office_morning_travaille:

    "{i}Vous appuyez machinalement sur le clavier.{/i}"

    show lisa_normal:
        left
        resize_char

    show charlene_normal:
        right
        resize_char

    l "Alors, sur quoi tu es en train de bosser, Charlene ?"
    c "Rien de spécial, juste la routine matinale comme d'habitude."

    show charlene_sad:
        right
        resize_char

    c "Cependant, avec la pression que nous met le patron sur le dos, ça commence à être compliqué."

    hide charlene_sad

    show charlene_normal:
        right
        resize_char

    c "En parlant de ça d'ailleurs, tu dois bien te rappeler qu'il y a une réunion avec M. Bourbon ce soir ?"

    menu:
        "..."

        "Oui, je m'en souviens":
            jump office_morning_positive

        "Non, j'avais complètement oublié !":
            jump office_morning_negative

        "{color=#8A0303}Tuer Charlene{/color}" if nb_boucle >= 3:
            jump kill_scene

label office_morning_positive:

    show lisa_normal:
        left
        resize_char
    hide charlene_normal
    show charlene_smile:
        right
        resize_char

    c "Parfait ! Alors, ça te dirait qu'on se mette à préparer cette réunion ce matin ?"

    menu:
        "hmmm... devrais-je préparer cette réunion ?"

        "Oui, tu as raison, préparons cette réunion, cela va nous faire gagner de l'assurance face à l'épreuve de ce soir !":
            jump black_skip_lunch_positive

        "Non désolée, j'avais prévu de me concentrer sur d'autres projets avant d'aller manger.":
            jump black_skip_lunch_negative

label office_morning_negative:
    show lisa_shocked:
        left
        resize_char
    show charlene_annoyed:
        right
        resize_char

    c "Ah la la, je sais qu'avec le patron qui nous met la pression tu dois être fatiguée, mais songe à te reposer... surtout si ça te fait oublier des réunions !"

    show lisa_sad:
        left
        resize_char

    l "Oui, tu as raison..."

    hide lisa_shocked
    hide lisa_sad
    hide charlene_annoyed

    show charlene_normal:
        right
        resize_char

    show lisa_normal:
        left
        resize_char

    c "Enfin bref, maintenant que tu sais qu'il y a une réunion, est-ce que tu voudrais préparer cette réunion avec moi pour qu'on soit prêtes ce soir ?"

    menu:
        "hmmm... devrais-je préparer cette réunion ?"

        "Oui, tu as raison, préparons cette réunion, cela va nous faire gagner de l'assurance face à l'épreuve de ce soir !":
            jump black_skip_lunch_positive

        "Non désolée, j'avais prévu de me concentrer sur d'autres projets avant d'aller manger.":
            jump black_skip_lunch_negative

label black_skip_lunch_negative:
    scene black

    "{i}Vous vous attelez à votre travail matinal quotidien, vos projets ne sont pas évidents mais rien d'infaisable.{/i}"

    jump office_morning_retour

label black_skip_lunch_positive:
    scene black

    "{i}Vous et Charlene vous attelez à la préparation de la réunion.{/i}"

    $ reunion_preparer = True
    $ nb_travail += 1

    jump office_morning_retour

label kill_scene:
    show lisa_angry_2:
        left
        resize_char

    show charlene_shocked:
        right
        resize_char

    c "...!"

    scene black

    "{i}Vous prenez votre ciseau et regardez Charlene droit dans les yeux.{/i}"
    "{i}Votre respiration s'accélère alors que vous avancez lentement vers elle.{/i}"
    "{i}Charlene, toujours sous le choc, n'a pas le temps de réagir.{/i}"
    "{i}D'un geste rapide, vous tranchez sa gorge. Le sang jaillit, tâchant vos vêtements et le sol.{/i}"
    "{i}Charlene tente de crier, mais aucun son ne sort de sa bouche.{/i}"
    "{i}Elle s'effondre lentement, ses yeux fixant les vôtres, implorants.{/i}"
    "{i}Vous ressentez un mélange étrange de satisfaction et de regret alors que vous regardez le corps sans vie de votre amie.{/i}"
    "{i}Vous cachez le cadavre de Charlene dans l'armoire, en essayant de ne pas penser à ce que vous venez de faire.{/i}"
    "{i}Vous nettoyez rapidement le sang, espérant que personne ne remarquera son absence tout de suite.{/i}"
    "{i}Après avoir rangé les ciseaux et ajusté vos vêtements, vous quittez la pièce, le cœur battant.{/i}"

    $ tuer_charlene = True
    $ nb_tuer_charlene += 1
    jump office_morning_retour

# ----------------------------------------------------------------------------
#                               CAFE MORNING
# ----------------------------------------------------------------------------

label office_morning_cafe:

    scene bg Kitchen_Day

    "{i}Lisa alla donc à la cuisine pour se servir un bon café. Elle y croisa alors Sophie, une autre collègue de travail. Elles ne s'aiment pas. Sophie fait toutes les magouilles possibles pour embêter ses collègues. Même si Jean est épargné 'bizarrement'.{/i}"

    show lisa_normal:
        right
        resize_char

    show sophie_smug:
        left
        resize_char

    s "Tiens tiens tiens~"
    l "Oh non."
    s "On vient se prendre un petit café ?"
    l "Oui Sophie. Je n'ai pas d'autre objectif que de prendre un café."
    s "Et bien en attendant tu gâches le mien. Adieu moment de sérénité~ Tu as été gâché par un thon sorti de l'eau."
    l "S'il te plaît, arrête ça."
    s "Vois la vérité en face ! C'est pour ça que Jean est beaucoup plus intéressé par moi que par toi~"
    "{i}Lisa soupire en s'approchant de la machine à café. Ce genre de discours est très courant chez Sophie, ce n'est absolument pas la première fois.{/i}"
    "{i}Le café coule dans sa tasse alors que Sophie continue de parler.{/i}"
    s "J'ai entendu dire que le patron avait l'intention de promouvoir quelqu'un."

    show sophie_smug_2:
        left
        resize_char

    show lisa_sad:
        right
        resize_char

    s "C'est évident que ce sera moi~"
    s "Après tout, on s'entend bien, Monsieur Bourbon et moi."

    menu:
        "   "

        "L'ignorer":
            "{i}Une fois le saint café servi, Lisa prend sa tasse et part de la cuisine.{/i}"
            s "Vas-y, fuis~ Tu es tellement pathétique."
            jump office_morning_retour

        "Surenchérir":
            jump dispute_cafe

        "{color=#8A0303}Tuer Sophie{/color}" if nb_boucle >= 3:
            jump cafe_tuer

label dispute_cafe:

    scene bg Kitchen_Day

    show lisa_angry:
        right
        resize_char

    show sophie_smug:
        left
        resize_char

    l "Sophie, tu es vraiment insupportable ! Pourquoi tu dois toujours faire des remarques désagréables ?"

    show sophie_angry:
        left
        resize_char

    s "Oh, Lisa, ne sois pas si sensible. Si tu ne supportes pas un peu de critique, tu ne survivras jamais ici."
    l "Ce ne sont pas des critiques, ce sont des attaques personnelles ! Tu passes ton temps à rabaisser tout le monde pour te sentir supérieure."
    s "Si tu veux appeler ça des attaques, fais-le. Mais peut-être que tu devrais te regarder dans un miroir avant de critiquer les autres."

    show lisa_angry_2:
        right
        resize_char

    l "Tu penses vraiment que tu es meilleure que tout le monde, n'est-ce pas ? C'est pathétique. Tout le monde sait que tu n'es qu'une hypocrite."

    show sophie_angry_2:
        left
        resize_char

    s "Et toi, tu crois que tu es une sainte ? Toujours à te plaindre, à chercher des excuses pour tes échecs. C'est pitoyable."
    l "Au moins, je ne trahis pas mes collègues pour m'attirer les faveurs du patron. Tu es prête à tout pour obtenir ce que tu veux, même à marcher sur les autres."
    s "C'est ce qu'il faut pour réussir. Tu devrais essayer, peut-être que tu arrêterais d'être une perdante."
    l "Je préfère être une perdante honnête qu'une gagnante malhonnête."
    s "On verra qui rira le dernier. Mais une chose est sûre, ce ne sera pas toi."
    l "Tu ne me fais pas peur, Sophie. Un jour, tout le monde verra qui tu es vraiment."
    s "Bonne chance avec ça, Lisa. Tu vas en avoir besoin."
    "{i}La dispute continue encore et encore{/i}"
    "{i}Tellement que quand les deux femmes se séparent pour retoruner dans leur bureau respective, la matinée été déjà bien avancé{/i}"
    jump office_morning_retour

label cafe_tuer:

    show lisa_angry:
        right
        resize_char
    show sophie_smug:
        left
        resize_char

    "{i}La colère monte en Lisa, chaque mot de Sophie étant comme une aiguille qui la pique de plus en plus profondément.{/i}"
    l "Tu ne sais vraiment pas quand t'arrêter, n'est-ce pas, Sophie ?"
    s "Oh, tu as enfin trouvé ta langue ? Trop tard, pathétique fille."
    "{i}Lisa, poussée à bout, attrape soudainement la carafe de la machine à café, encore brûlante. Sophie, prise par surprise, n'a pas le temps de réagir avant que le liquide bouillant ne soit jeté sur son visage.{/i}"

    scene black
    hide lisa_angry

    s "AAAAAAAAAAAAAAAAH !!!"
    "{i}Les cris de Sophie résonnent dans la cuisine alors qu'elle tombe au sol, se tenant le visage brûlé. Lisa, dans un état de rage incontrôlable, se saisit d'un couteau à proximité et s'approche de Sophie.{/i}"
    "{i}Les yeux de Sophie, remplis de douleur et de peur, rencontrent ceux de Lisa une dernière fois.{/i}"
    s "Non... non, s'il te plaît..."
    l "C'est pour toutes les fois où tu nous as pourri la vie, Sophie."
    "{i}Sans hésitation, Lisa enfonce le couteau dans la poitrine de Sophie, encore et encore, jusqu'à ce que les cris cessent et que le corps de Sophie soit immobile, baignant dans une mare de sang.{/i}"
    "{i}Lisa, essoufflée, reprend ses esprits et regarde le corps sans vie de Sophie. Elle réalise ce qu'elle vient de faire. Elle se nettoie en panique avec lévier et essaye de se calmer.{/i}"
    "{i}Elle sort de la cuisine, son café à la main, laissant derrière elle le corps de Sophie, et retourne tranquillement à son bureau comme si de rien n'était.{/i}"
    $ tuer_sophie = True
    $ nb_tuer_sophie += 1
    jump office_morning_retour

# ----------------------------------------------------------------------------
#                               IMPRIMANTE MORNING
# ----------------------------------------------------------------------------

label office_morning_imprimante:

    scene bg Reserve:
        zoom 1.5

    "{i}Lisa alla donc à la réserve où se trouve l'imprimante pour y faire des photocopies. Elle y croisa alors Jean, un autre collègue de travail qu'elle aime en secret.{/i}"

    show lisa_smile:
        right
        resize_char

    show jean_smile:
        left
        resize_char

    l "Oh ! Bonjour Jean. Je ne savais pas que l'imprimante était prise."
    j "Bonjour Lisa. Ne t'inquiète pas ! J'ai bientôt fini. Tu vas imprimer quoi ?"
    l "Juste quelques documents pour la réunion de ce soir."
    j "C'est vrai que c'est toi qui l'animes !"

    show jean_smile_2:
        left
        resize_char
    hide jean_smile

    j "Bonne chance"

    show lisa_smile_2:
        right
        resize_char
    hide lisa_smile

    l "Merci, merci"

    menu:
        "   "

        "Parler des futures vacances":
            jump imprimante_vacance

        "Demander à Jean de manger ensemble":
            jump imprimante_manger

        "{color=#8A0303}Tuer Jean{/color}" if nb_boucle >= 3:
            jump imprimante_tuer


label imprimante_vacance:

    l "Tu as prévu quelque chose pour les vacances qui arrivent ?"
    j "Oui, j'ai voulu placer une semaine de congé pour aller voir ma famille, mais le patron a refusé."

    show jean_sad:
        left
        resize_char

    show lisa_sad:
        right
        resize_char

    l "Je suis désolée pour toi. Pourquoi a-t-il refusé ?"
    j "Je ne sais pas vraiment... Enfin... Il m'a dit pourquoi mais c'était plus une excuse qu'autre chose."

    show lisa_shocked:
        right
        resize_char

    l "Ah bon !? Il t'a dit quoi ?"
    j "Comme quoi j'avais mal choisi la période car il y aurait beaucoup de choses à faire."

    show lisa_angry:
        right
        resize_char

    l "Mais !... Mais Sophie part en vacances sur cette même période ! C'est injuste !"
    j "Je sais... Mais Sophie est ici depuis plus longtemps. C'est peut-être pour ça."
    l "Mais ce n'est pas la première fois que le patron fait du favoritisme avec Sophie."
    j "Et on ne peut rien faire."
    l "Courage, Jean."
    jump fin_imprimante

label imprimante_manger:

    $ manger_jean = True

    "{i}Lisa prend son courage à deux mains et décide de passer aux choses sérieuses avec Jean. Après tout, ça fait déjà depuis un moment que les deux s'envoient des sourires plus que cordiaux.{/i}"

    show lisa_blush:
        right
        resize_char

    l "Jean ! Heum... Il fait vraiment beau dehors. Je compte manger au petit restaurant à côté du bureau. Tu voudrais m'accompagner ?"

    show jean_smile_3:
        left
        resize_char

    j "Ça me ferait très plaisir ! C'est une très bonne idée."
    l "Vraiment ? Merci. On se retrouve devant l'entrée à midi du coup."
    j "Oui ! J'ai hâte."
    jump fin_imprimante

label imprimante_tuer:

    "{i}La folie gagne Lisa. Le dos de Jean penché au-dessus de l'imprimante est tellement attirant pour elle.{/i}"

    show lisa_blush:
        right
        resize_char

    l "Oh Jean, tu es tellement beau~"

    show jean_shocked:
        left
        resize_char

    j "Pardon !?"
    l "Je t'aime tellement fort, Jean."
    j "Vraiment ? J-je ne m'attendais pas à une déclaration comme ça."
    l "Hihihi, je veux te donner un cadeau aussi gros que mon amour."
    j "Heu, d'accord, merci beaucoup."
    l "Ferme les yeux~"

    scene black

    "{i}Jean ferme alors les yeux.{/i}"
    "{i}Lisa se rapproche doucement de son cher et tendre.{/i}"
    l "Aah~ Je suis tellement heureuse."
    j "Content de l'entendre. Moi aussi je veux ton bonheur."
    l "Tu es tellement mignon."
    "{i}Un petit moment passe avant d'entendre de l'agitation.{/i}"
    j "Lisa ? Qu'est-ce que tu-"
    "{i}Jean commence à crier, mais sa voix est étouffée alors que Lisa le frappe violemment à la tête avec un objet lourd trouvé sur la table. Jean tombe au sol, sonné et saignant abondamment.{/i}"
    "{i}Lisa, avec un sourire dément, se penche sur lui, ses yeux brillants de folie.{/i}"
    l "Ne t'inquiète pas, mon amour. Ça ne sera pas long."
    "{i}Elle prend alors une paire de ciseaux dans l'un des tiroirs de la réserve. Jean, à moitié conscient, essaie de se débattre, mais il est trop faible.{/i}"
    j "Lisa... pourquoi..."
    l "Parce que je t'aime, Jean."
    $ tuer_jean = True
    $ nb_tuer_jean += 1
    "{i}Puis, plus un bruit. On ne peut entendre que le souffle de Lisa. Et après quelques minutes, Lisa retourne tranquillement à son bureau en fermant avec soin la porte de la réserve.{/i}"
    jump office_morning_retour

label fin_imprimante:

    show jean_smile:
        left
        resize_char

    show lisa_smile:
        right
        resize_char

    "TIT TIT TIT"
    j "Ah ? J'ai fini d'imprimer mes documents. L'imprimante est à toi. Je te dis à plus tard."
    l "Merci et à plus tard."
    "{i}Jean sort alors de la pièce et Lisa se retrouve seule avec l'imprimante. Elle imprime tout ce dont elle a besoin avant de sortir.{/i}"
    $ nb_travail += 1
    "{i}Après ça, elle retourne dans son bureau.{/i}"
    jump office_morning_retour

# ----------------------------------------------------------------------------
#                               OFFICE MORNING 2
# ----------------------------------------------------------------------------

label office_morning_retour:

    scene bg Bureau_lisa:
        zoom 1.9
    show lisa_smile:
        left
        resize_char

    "{i}Lisa est donc dans le bureau. Le temps passe tranquillement et vient le moment de manger.{/i}"

    if tuer_sophie:
        hide lisa_smile
        scene black
        "{i}Lisa est donc dans le bureau. Le temps passe tranquillement et vient le moment de manger.{/i}"
        "{i}Cependant, pendant que vous vous rendiez à la caféteria, vous êtes soudainement interpellée par un agent de police,{/i}"
        "{i}en effet, il se trouve que quelqu'un a apperçu le cadavre de Sophie gisant dans la cuisine, et à cause de l'aide de témoins, la police est rémontée jusqu'à vous.{/i}"
        "{i}Avec toutes les preuves accablantes vous êtes placée en tant que suspecte numéro une, bien que, tout le monde sait qu'avec le contentieux que vous avez avec Sophie,{/i}"
        "{i}c'est vous qui l'avez probablement tuée.{/i}"
        jump meurtre_découvert
    menu:
        "{i}Lisa est donc dans le bureau. Le temps passe tranquillement et vient le moment de manger.{/i}"

        "Manger seule":
            jump manger_seul

        "Manger avec Charlene" if tuer_charlene == False and manger_jean == False:
            jump manger_charlene

        "Manger avec Jean" if manger_jean == True:
            jump manger_jean

# ----------------------------------------------------------------------------
#                               MANGER AVEC CHARLENE
# ----------------------------------------------------------------------------

label manger_charlene:

    scene black

    "{i}Les deux amies partent alors ensemble à midi pour manger.{/i}"
    "{i}L'adresse qu'elles ont choisie est un petit restaurant pas très loin du bureau, très agréable, avec des prix raisonnables.{/i}"
    "{i}Elles s'installent à une table tranquillement et regardent le menu.{/i}"

    scene bg Restaurant_lunch
    show lisa_normal:
        left
        resize_char
    show charlene_normal:
        right
        resize_char

    c "Espérons que ce soit bon..."
    l "Il ne devrait pas y avoir de souci, toutes les personnes qui en ont parlé ne se sont pas plaintes."

    if reunion_preparer:
        hide charlene_normal
        show charlene_smile:
            right
            resize_char
        c "Ah, je suis contente que nous nous soyons préparées pour la réunion !"
        l "Moi de même, mon stress s'est dissipé grâce à notre préparation. Je suis fin prête."
    else:
        c "Alors, tu as progressé sur tes projets ce matin ?"

        hide lisa_normal
        show lisa_smile:
            left
            resize_char

        l "Oui, je me suis bien avancée, ce n'était clairement pas du temps perdu."

        hide charlene_normal
        show charlene_smile:
            right
            resize_char

    c "Tant mieux ! Alors, que vas-tu commander ?"

    menu:
        "Je me demande bien ce qui a l'air le plus appétissant..."

        "Je vais prendre les crevettes au curry, je pense !":
            jump charlene_black_skip

        "Je vais partir sur des spaghettis bolognaise, je pense !":
            jump charlene_black_skip

        "Hmmm... je vais tenter de prendre un bar fumé":
            jump charlene_black_skip

        "{color=#8A0303}Empoisonner Charlene{/color}" if nb_boucle >= 3:
            jump manger_tuer_charlene

label manger_tuer_charlene:

    scene black

    "{i}Lisa et Charlene commandent leurs plats respectifs. Lisa, animée par une sombre détermination, attend patiemment le bon moment pour agir.{/i}"
    "{i}Lorsque Charlene se lève pour aller aux toilettes, Lisa saisit discrètement un petit flacon de poison qu'elle a caché dans son sac.{/i}"
    "{i}Les mains tremblantes, elle verse une petite dose de poison dans le verre d'eau de Charlene, puis remet rapidement le flacon dans son sac.{/i}"

    scene bg Restaurant_lunch
    show lisa_normal:
        left
        resize_char
    show charlene_smile:
        right
        resize_char

    "{i}Charlene revient quelques minutes plus tard, sans se douter de rien, et reprend sa place à table.{/i}"
    c "J'ai tellement faim ! J'espère que ça ne va pas tarder."
    l "Oui, moi aussi."

    "{i}Les plats arrivent enfin et les deux amies commencent à manger.{/i}"
    c "Cette salade César est vraiment délicieux !"
    l "Je suis contente que ça te plaise."

    "{i}Lisa observe Charlene avec une inquiétude mêlée d'anticipation. Elle se demande si le poison fera effet comme prévu.{/i}"

    show charlene_sad:
        right
        resize_char

    c "Je ne me sens pas très bien... Peut-être que c'est le plat..."

    $ tuer_charlene_restaurant = True
    $ nb_tuer_charlene += 1

    l "Tu veux que je t'accompagne voir un médecin ?"
    c "Non, ça va aller. Je pense que je vais juste rentrer chez moi pour me reposer."
    "{i}Charlene se lève lentement, visiblement mal en point, et se dirige vers la sortie.{/i}"

    hide charlene_normal
    hide charlene_sad
    show lisa_smile:
        left
        resize_char

    l "Repose-toi bien, Charlene. J'espère que tu te sentiras mieux bientôt."
    "{i}Une fois Charlene partie, Lisa ressent un mélange de soulagement et de culpabilité. Elle retourne tranquillement au bureau, se demandant si quelqu'un découvrira ce qu'elle a fait.{/i}"
    jump retour_bureau

label charlene_black_skip:

    show charlene_smile:
        right
        resize_char

    c "Formidable ! Moi, je vais sûrement prendre une salade César."
    l "Plus qu'à attendre le serveur, donc."

    scene black

    "{i}Vous attendez avec impatience votre repas.{/i}"
    "{i}Après avoir mangé, vous retournez toutes les deux au travail, prêtes à affronter l'après-midi, en espérant ne pas coincer la bulle...{/i}"
    jump retour_bureau


# ----------------------------------------------------------------------------
#                               MANGER SEULE
# ----------------------------------------------------------------------------

label manger_seul:

    scene bg Kitchen_Day
    show lisa_sad:
        center
        resize_char

    "{i}Lisa se dirige seule vers la cuisine des bureaux pour manger. Elle prend son repas préparé et s'assoit à une table vide. La solitude l'envahit alors qu'elle commence à manger en silence.{/i}"
    l "Encore une journée identique... Combien de fois vais-je revivre ce même jour ?"
    "{i}Elle laisse échapper un soupir profond, la sensation d'être piégée dans cette boucle temporelle devient de plus en plus insupportable. Chaque jour se répète inlassablement, sans aucune échappatoire en vue.{/i}"
    l "Personne ne comprendrait ce que je traverse... même si j'essayais de leur expliquer."
    "{i}Les murs de la cuisine, habituellement confortants, semblent se refermer sur elle. La réalité de sa situation est accablante. Elle se sent isolée, incapable de partager son fardeau avec qui que ce soit.{/i}"
    l "Je suis seule dans cette épreuve... seule avec mes pensées et mes peurs."
    "{i}Elle pique distraitement dans son repas, l'appétit lui manquant. Les mêmes visages, les mêmes conversations, le même travail, encore et encore. La monotonie est écrasante.{/i}"
    l "Comment sortir de cette boucle infernale ? Y a-t-il seulement une issue ?"

    show lisa_crying:
        center
        resize_char

    "{i}Des larmes commencent à couler silencieusement sur ses joues. La frustration, la tristesse et le désespoir se mêlent en un tourbillon d'émotions qu'elle ne peut plus contenir.{/i}"
    l "Je dois trouver une solution... mais comment ?"

    if tuer_charlene == True:
        l "Comment ai-je pu faire ça à mon amie ?"
        l "Je l'ai tuée."
        l "Et même si je la revois demain... Je me sens tellement mal."

    if tuer_jean == True:
        l "Je n'arrive pas à croire que j'ai tué Jean."
        l "Il ne méritait pas ça. Personne ne mérite ça."
        l "La culpabilité me ronge... Comment pourrais-je me pardonner ?"

    if tuer_sophie == True:
        l "J'ai mis fin à la vie de Sophie... même si elle était odieuse, personne ne mérite une telle fin."
        l "Chaque jour je revis cette horreur. Comment puis-je continuer à vivre avec ce poids sur ma conscience ?"

    "{i}Lisa se sent perdue, désemparée. Chaque jour est une lutte pour ne pas sombrer davantage dans la dépression. Elle sait qu'elle doit continuer à chercher un moyen de briser cette boucle, mais la force lui manque.{/i}"
    l "Je ne peux pas abandonner... Je dois continuer, même si c'est difficile."
    "{i}Après avoir terminé son repas, Lisa se lève lentement, le cœur lourd. Elle sait qu'elle doit retourner au travail, faire semblant que tout va bien, même si chaque jour est une épreuve de plus.{/i}"
    jump retour_bureau


# ----------------------------------------------------------------------------
#                               MANGER AVEC JEAN
# ----------------------------------------------------------------------------

label manger_jean:

    scene black

    "{i}Lisa retrouve donc Jean devant l'entrée comme convenu.{/i}"
    "{i}L'adresse qu'ils ont choisie est un petit restaurant pas très loin du bureau, très agréable, avec des prix raisonnables.{/i}"
    "{i}Ils s'installent ensemble à une table tranquillement et regardent le menu.{/i}"

    scene bg Restaurant_lunch
    show lisa_smile:
        left
        resize_char
    show jean_smile:
        right
        resize_char

    menu:
        "   "

        "Engager une conversation légère":
            jump conversation_legere
        "Exprimer ses sentiments":
            jump exprimer_sentiments

label conversation_legere:

    show lisa_smile_2:
        left
        resize_char

    l "C'est sympa de pouvoir manger ensemble, n'est-ce pas ?"
    j "Oui, vraiment. C'est agréable de sortir un peu du bureau."
    l "Oui, ça change un peu de notre routine quotidienne."

    show lisa_smile:
        left
        resize_char

    "{i}Un moment de silence s'installe alors, mais il n'est pas gênant. Au contraire, il est confortable, empli d'une douce tension.{/i}"
    l "Jean, je voulais te dire que... je suis contente qu'on ait eu l'occasion de se rapprocher un peu ces derniers temps."

    show lisa_blush:
        left
        resize_char

    "{i}Lisa sent son cœur battre un peu plus fort alors qu'elle prononce ces mots. Elle se sent vulnérable mais aussi libérée de pouvoir enfin exprimer ce qu'elle ressent.{/i}"

    show jean_smile_3:
        right
        resize_char

    j "Moi aussi, Lisa. C'est agréable de passer du temps avec toi en dehors du travail."
    l "Tu sais, je trouve que tu es vraiment une personne spéciale, Jean."

    show jean_smile_2:
        right
        resize_char

    j "Merci, Lisa. C'est très gentil de ta part de le dire."

    hide jean_smile_2
    show jean_smile:
        right
        resize_char

    "{i}Leurs regards se croisent, et dans ce moment, ils semblent se comprendre sans avoir besoin de mots.{/i}"
    "{i}Le serveur arrive pour prendre leur commande, interrompant le moment magique. Mais même cette interruption ne peut pas briser l'atmosphère chaleureuse entre eux.{/i}"
    "{i}Lisa et Jean passent le reste du repas à discuter, à rire et à partager des histoires sur leur vie. Ils se sentent de plus en plus à l'aise l'un avec l'autre, comme s'ils avaient enfin trouvé quelqu'un avec qui ils pouvaient être totalement eux-mêmes.{/i}"
    "{i}À la fin du repas, ils se quittent avec un sourire timide mais heureux. Ils se sentent tous les deux impatients de se revoir, de passer plus de temps ensemble et de découvrir où cette nouvelle relation les mènera.{/i}"
    "{i}Peut-être que, grâce à cette boucle temporelle, Lisa et Jean ont enfin trouvé l'amour qu'ils recherchaient depuis si longtemps.{/i}"
    "{i}Leur histoire ne fait que commencer...{/i}"
    jump retour_bureau

label exprimer_sentiments:

    show lisa_blush:
        left
        resize_char

    l "Jean, je... je voulais te dire quelque chose."
    j "Oui, Lisa ? Qu'est-ce qu'il y a ?"
    l "C'est juste... Je sais que ça peut sembler étrange, mais... je me sens vraiment bien quand je suis avec toi."
    "{i}Lisa sent son cœur battre la chamade alors qu'elle se livre à Jean. Elle craint sa réaction, mais en même temps, elle sait qu'elle doit être honnête avec ses sentiments.{/i}"

    show jean_smile_2:
        right
        resize_char

    j "Je ressens la même chose, Lisa. Tu es une personne spéciale pour moi."
    l "Tu sais, j'ai vraiment apprécié tous ces moments passés ensemble, même au travail."
    j "Moi aussi, Lisa. Je pense que tu es vraiment une femme formidable."

    hide jean_smile_2
    show jean_smile:
        right
        resize_char

    "{i}Leurs regards se croisent, et dans ce moment, ils semblent se comprendre sans avoir besoin de mots.{/i}"
    "{i}Le serveur arrive pour prendre leur commande, interrompant le moment magique. Mais même cette interruption ne peut pas briser l'atmosphère chaleureuse entre eux.{/i}"
    "{i}Lisa et Jean passent le reste du repas à discuter, à rire et à partager des histoires sur leur vie. Ils se sentent de plus en plus à l'aise l'un avec l'autre, comme s'ils avaient enfin trouvé quelqu'un avec qui ils pouvaient être totalement eux-mêmes.{/i}"
    "{i}À la fin du repas, ils se quittent avec un sourire timide mais heureux. Ils se sentent tous les deux impatients de se revoir, de passer plus de temps ensemble et de découvrir où cette nouvelle relation les mènera.{/i}"
    "{i}Peut-être que, grâce à cette boucle temporelle, Lisa et Jean ont enfin trouvé l'amour qu'ils recherchaient depuis si longtemps.{/i}"
    "{i}Leur histoire ne fait que commencer...{/i}"

    $ amour = True
    jump retour_bureau

# ----------------------------------------------------------------------------
#                               RETOUR AU BUREAU
# ----------------------------------------------------------------------------

label retour_bureau:
    scene bg Bureau_lisa:
        zoom 1.9

    "{i}Lisa reprend son travail en combattant son envie de dormir suite au repas{/i}"

    show lisa_normal:
        center
        resize_char

    if tuer_charlene_restaurant or tuer_charlene:

        "{i}Vous travaillez donc seule jusqu'a la réunion...{/i}"
        "{i}Cela aurait été le cas si vous ne saviez pas que Sophie allait venir...{/i}"
        hide lisa_normal

    else:

        if nb_boucle >= 3:
            menu:
                "{i}Ce n'est pas  la première fois que vous vivez ceci...{/i}"

                "Demander à Charlene d'aller chercher des documents dans les archives":
                    $ charlene_archive = True

                "Ne rien faire":
                    pass

        if charlene_archive == False:
            l "ah... je sais pas toi Charlene, mais moi je suis entrain de m'endormir !"

            hide lisa_normal

            show lisa_normal:
                left
                resize_char
            show charlene_normal:
                right
                resize_char

            c "Ne t'en fais pas tu n'est pas la seule !"
            c "De toute façon c'est toujours comme ça après avoir mangée, il faut juste tenir une heure puis après ça ira mieux..."
            l "C'est vrai, bon, plus qu'a..."

            hide charlene_normal

            "{i}Votre phrase est interrompue par Sophie qui rentre dans la salle{/i}"
        else:
            hide lisa_normal
            show lisa_normal:
                left
                resize_char
            show charlene_normal:
                right
                resize_char

            l "Charlene est ce que tu peux aller chercher des documents dans les archives s'il-te-plait ?"

            hide charlene_normal
            show charlene_smile:
                right
                resize_char

            c "Pas de problème ! je reviens tout de suite."

            hide charlene_smile

            "{i}Charlene quitte la salle, vous attendez l'arrivée de Sophie.{/i}"
    show sophie_smile:
        right
        resize_char

    s "Alors, tu as bien mangée ? j'imagine, vu tes formes..."
    if tuer_charlene == True:
        jump retour_bureau_charlene_off
    if charlene_archive == True or tuer_charlene_restaurant == True:

        s "Tiens Charlene n'est pas là... enfin peu importe, vous ne valez pas plus l'une que l'autre."

    show lisa_annoyed:
        left
        resize_char

    l "Pff si tu est juste là pour faire des remarques tu peux partir..."

    hide sophie_smile
    show sophie_normal:
        right
        resize_char

    s "Mais non, je ne suis pas là juste pour ça..."
    s "En effet en tant qu'amie~, je voulais bien te rappeler de la réunion de ce soir,"

    hide sophie_normal
    show sophie_smug:
        right
        resize_char

    s "Et notament le fait que c'est moi qui recevrai une promotion à ta place, enfin non pas que cela soit une compétition avec ton travail..."

    menu:
        "{i}Lisa commence à perdre son sang froid{/i}"

        "Garder son calme":
            jump af_bureau_calme
        "Perdre son sang froid":
            jump af_bureau_dispute

        "{color=#8A0303}Tuer Sophie{/color}" if nb_boucle >= 3:
            jump af_tuer_sophie

label retour_bureau_charlene_off:
    scene bg Bureau_lisa:
        zoom 1.9

    show sophie_smile:
        right
        resize_char

    show lisa_normal:
        left
        resize_char

    "{i}Sophie regarde attentivement la salle, en effet quelque chose lui semble étrange...{/i}"
    s "..."
    s "..."

    hide sophie_smile
    show sophie_shocked:
        right
        resize_char

    s "...!"
    "{i}Sophie regarde l'armoire et remarque une trace de sang dégoulinant de celle-ci{/i}"
    s "Tiens on dirait... qu'il y a du sang !"
    "{i}Sophie décide d'ouvrir l'armoire et c'est avec éffroi qu'elle tombe nez à nez avec le corps sans vie de Charlene.{/i}"

    hide sophie_shocked

    "{i}Prise de panique elle s'enfuie de la salle avant même que vous ne puissiez réagir,{/i}"
    "{i}Il est évident qu'elle est allée prévenir la police, et cela tombe sous le sens qu'ils ont fait de vous la suspecte numéro une.{/i}"
    jump meurtre_découvert

label af_bureau_calme:
    show lisa_normal:
        left
        resize_char
    show sophie_smug:
        right
        resize_char

    l "Ecoute Sophie, je n'ai pas le temps pour tes remarques, et je n'ai pas envie de t'accorder du temps, maintenant si tu peux me laisser et vaquer à tes occupations"
    l "...cela m'arrangerais au plus haut point."

    hide sophie_smug
    show sophie_annoyed:
        right
        resize_char

    s "Oui c'est ça tu a raison tu vaux pas mon temps !"
    s "Je te laisse profiter de ton après midi avant la réunion !"

    $ nb_travail += 1

    jump reunion

label af_bureau_dispute:
    show lisa_angry:
        left
        resize_char
    show sophie_smug:
        right
        resize_char

    l "Sophie j'en ai plus qu'asser de tes remarque ! tu ne vaut même pas mon temps ! avec tes grands air alors que l'on sait tous ici que la seule raison pour laquelle tu n'est pas encore virée,"
    l "c'est que le patron t'a à la bonne !"

    hide sophie_smug
    show sophie_angry_2:
        right
        resize_char

    s "Tu ne sais même pas de quoi tu parle !"
    s "Je ne me laisserais pas marcher dessus par un thon sortie de l'eau !"

    menu:
        "{i}Votre sang froid est de plus en plus difficile à gérer...{/i}"

        "Dire à Sophie de partir":
            jump sophie_depart

        "{color=#8A0303}Tuer Sophie{/color}" if nb_boucle >= 3:
            jump af_tuer_sophie

label sophie_depart:
    show lisa_angry_2:
        left
        resize_char
    show sophie_angry_2:
        right
        resize_char

    l "Cela suffit !"
    l "Maintenant part c'est encore mon bureau que je sache !"
    s "Tu ne paie rien pour attendre, gros thon !"
    "{i}Sophie part.{/i}"
    "{i}Vous ne pouvez vous empechez de dire que c'était moins une...{/i}"

    if nb_boucle >= 3:
        "{i}Un peu plus et vous auriez mis fin à ses jours{/i}"
    jump reunion

label af_tuer_sophie:
    show lisa_angry_2:
        left
        resize_char
    show sophie_angry_2:
        right
        resize_char

    "{i}Vous ne supportez les dires de Sophie plus longtemps, vous l'avez suffisament entendue, un trop grand nombre de fois.{/i}"

    hide sophie_angry_2
    show sophie_shocked:
        right
        resize_char

    "{i}Vous saisissez le ciseau le plus proches et tranchez d'un coup sec la gorge de Sophie{/i}"

    hide sophie_shocked
    hide lisa_angry_2
    scene black

    "{i}Elle éssaie de se mettre les mains sur la gorge, mais vous vous jetez sur elle et la regardez ce vider de son sang, vous la tenez car elle se débat{/i}"
    "{i}Après quelques secondes, ça y est, elle est morte.{/i}"
    "{i}Un soulagement profond vous envahie, mais vous n'avez pas le temps de savourer cet instant ou même de penser à ce que vous venez de faire, il faut cacher le corps.{/i}"
    "{i}Vous cachez le corps de Sophie dans l'armoire et nettoyez le sang.{/i}"

    $ tuer_sophie = True
    $ nb_tuer_sophie += 1

    if charlene_archive == True:
        "{i}Quand Charlenne revient, elle ne se doute de rien.{/i}"
        "{i}Vous vous sentez soulagée de son ignorance."
        jump reunion

    if charlene_archive == False and tuer_charlene_restaurant == False:
        scene bg Bureau_lisa:
            zoom 1.9
        show lisa_angry:
            left
            resize_char
        show charlene_shocked:
            right
            resize_char

        "{i}Charlenne regarde la scène, choquée de ce que vous venez de faire.{/i}"
        "{i}Perdue dans votre frénésie, vous n'aviez pas remarquée que vous n'étiez pas seule.{/i}"

        hide charlene_shocked

        "{i}Charlenne ce précipite vers la porte de sortie, vous n'avez pas le temps de l'arrêter.{/i}"

        hide lisa_angry
        scene black

        "{i}La police vous arrête immédiatement, votre culpabilitée étant évidente{/i}"
        jump meurtre_découvert

# ----------------------------------------------------------------------------
#                               REUNION
# ----------------------------------------------------------------------------

label reunion:

    if reunion_preparer == True:
        $ nb_travail += 1

    if tuer_charlene_restaurant == True:
        $ tuer_charlene = True

    scene black

    "{i}Il est maintenant 17 heures. La réunion va commencer.{/i}"

    if tuer_charlene == True:
        "{i}Charlene est absente...{/i}"
    if tuer_jean == True:
        "{i}Jean est absent...{/i}"
    if tuer_sophie == True:
        "{i}Sophie est absente...{/i}"

    if tuer_charlene == True or tuer_jean == True or tuer_sophie == True:
        "{i}... Et Lisa sait pourquoi.{/i}"
        "{i}Le patron, Monsieur Bourbon, s'interroge et pose des questions.{/i}"
        "{i}Mais Lisa feint l'ignorance et la réunion commence.{/i}"

    # $ nb_travail_str = "nb_travail {}".format(nb_travail)

    # l "[nb_travail_str]"

    if nb_travail >= 2:
        "{i}Lisa fait une exelente présentation{/i}"
        jump super_presentation

    elif nb_travail == 1:
        "{i}Lisa fait sa présentation sans problème{/i}"
        jump bonne_presentation

    elif nb_travail == 0:
        "{i}La présentation de Lisa s'est très mal passée{/i}"
        jump mauvaise_presentation

label super_presentation:

    scene bg Reunion:
        zoom 3
    show lisa_smile:
        center
        resize_char

    l "Et voilà, c'est tout pour ma présentation. J'espère que cela vous a plu et que vous avez trouvé les informations utiles."

    if tuer_charlene == False or tuer_jean == False or tuer_sophie == False:
        "{i}Les collègues de Lisa applaudissent chaleureusement. Monsieur Bourbon se lève et lui adresse un sourire.{/i}"

    show bourbon_smirk:
        right
        resize_char

    b "Excellent travail, Lisa. Pouvez-vous rester ici après la réunion ? J'aimerais discuter de quelque chose avec vous."

    show lisa_shocked:
        left
        resize_char
    hide lisa_smile

    l "Bien sûr, Monsieur Bourbon."

    scene black

    "{i}Après la réunion, Lisa reste avec Monsieur Bourbon.{/i}"

    scene bg Reunion:
        zoom 3
    show bourbon_smirk:
        right
        resize_char

    b "Lisa, je voulais vous féliciter pour votre présentation. Vous avez montré des compétences exceptionnelles et je pense que vous êtes prête pour plus de responsabilités."

    show lisa_smile:
        left
        resize_char

    l "Merci beaucoup, Monsieur Bourbon."
    b "J'aimerais vous offrir une promotion. Vous seriez en charge de plusieurs projets importants."

    show lisa_shocked:
        left
        resize_char
    hide lisa_smile

    l "C'est incroyable ! Merci pour cette opportunité, Monsieur Bourbon. Je ne vous décevrai pas."

    scene black

    "{i}Lisa quitte le bureau de Monsieur Bourbon avec un sentiment de fierté et de réussite. Cette journée est décidément différente des autres.{/i}"
    jump fin_reunion

label bonne_presentation:

    scene bg Reunion:
        zoom 3
    show lisa_smile:
        center
        resize_char

    l "Et voilà, c'est tout pour ma présentation. Merci de votre attention."

    if tuer_charlene == False or tuer_jean == False or tuer_sophie == False:
        "{i}Les collègues de Lisa applaudissent poliment. Monsieur Bourbon hoche la tête en signe d'approbation.{/i}"

    show bourbon_smirk:
        right
        resize_char

    b "Bien joué, Lisa. Vous avez bien présenté les informations. Continuons à travailler dur."

    show lisa_smile:
        left
        resize_char

    l "Merci, Monsieur Bourbon."

    scene black

    "{i}La réunion continue sans incident majeur, et Lisa se sent soulagée d'avoir bien fait sa présentation.{/i}"
    jump fin_reunion

label mauvaise_presentation:

    scene bg Reunion:
        zoom 3
    show lisa_sad:
        center
        resize_char

    l "Euh... voilà, c'est tout pour ma présentation. Merci de votre attention."

    if tuer_charlene == False or tuer_jean == False or tuer_sophie == False:
        "{i}Les collègues de Lisa sont silencieux, visiblement mal à l'aise. Monsieur Bourbon fronce les sourcils et se lève lentement.{/i}"

    show bourbon_angry:
        right
        resize_char

    b "Lisa, pourriez-vous rester ici après la réunion ? Nous devons parler."

    show lisa_shocked:
        left
        resize_char
    hide lisa_sad

    l "O-oui, Monsieur Bourbon."

    scene black

    "{i}Après la réunion, Lisa reste nerveusement dans la salle avec Monsieur Bourbon.{/i}"

    scene bg Reunion:
        zoom 3
    show bourbon_angry:
        right
        resize_char

    b "Lisa, votre présentation était inacceptable. Cela montre un manque flagrant de préparation et de compétence."

    show lisa_sad:
        left
        resize_char

    l "Je suis désolée, Monsieur Bourbon. Je ferai mieux la prochaine fois."
    b "Il n'y aura pas de prochaine fois. Vous êtes licenciée. Veuillez récupérer vos affaires."

    show lisa_shocked:
        left
        resize_char
    hide lisa_sad

    l "Monsieur Bourbon, je... Je comprends."

    scene black

    "{i}Lisa quitte le bureau de Monsieur Bourbon en larmes, consciente que cette journée est un échec complet.{/i}"
    "{i}Elle récupère ses affaires, bien déterminé à faire mieux 'demain'"
    jump retour_de_boucle

label fin_reunion:

    scene bg Bureau_lisa:
        zoom 1.9
    show lisa_sad:
        center
        resize_char

    l "Quelle journée éprouvante... J'espère que demain sera meilleur."

    if tuer_bourbon == True or tuer_charlene == True or tuer_sophie == True:
        if amour == True:
            jump fin

    jump retour_de_boucle

# ----------------------------------------------------------------------------
#                         MEURTRE DECOUVERT
# ----------------------------------------------------------------------------

label meurtre_découvert:

    scene black

    "{i}La police vous a arrêtée, vous êtes en garde à vue et attendez votre jugement.{/i}"

    if nb_boucle >= 2:
        "{i}Enfin...{/i}"
        "{i}Si vous saviez que vous n'étiez pas dans une boucle temporelle bien évidemment...{/i}"
        "{i}Vous réfléchissez déjà à ce que vous allez faire lors de la prochaine itération...{/i}"

        if nb_boucle >= 3:
            "{i}...Vos actions ne vous impactant pas vraiment...{/i}"

    jump retour_de_boucle

# ----------------------------------------------------------------------------
#                         RETOUR DE BOUCLE
# ----------------------------------------------------------------------------

label retour_de_boucle:

    scene bg Small_Apartment_Kitchen

    $ nb_boucle += 1

    show lisa_sad:
        center
        resize_char

    if nb_boucle == 2:
        hide lisa_sad
        show lisa_angry:
            center
            resize_char

        "{i}Cette bouteille de lait dans le frigo...{/i}"
        l "Ah !"
        l "Mais je me souviens de tout cela ! c'était hier et avant-hier !"
        l "Mais que ce passe t-il ?!"
        "{i}Peut être que ce n'est qu'un rêve ?{/i}"
        "{i}Peu importe, vous devez faire un choix.{/i}"

        menu:
            "Peut être que cela est du au travail ?"

            "Aller au travail":
                jump subway_morning

            "Rester à la maison en espérant que ce manège s'arrête":
                $ nb_boucle = nb_boucle + 1
                jump retour_de_boucle
    else:
        "{i}Vous vous retrouvez une nouvelle fois dans cet appartement, la même journée, avec cette même brique de lait périmée, ce même temps, ces même personnes,{/i}"
        if nb_boucle == 3:
            "{i}Vous ne savez pas combien de temps vous pourrez tenir, la folie vous guette{/i}"

        if nb_boucle == 6:
            "{i}Vous êtes complétement brisée mentalement, mais peu importe, il faut que vous sortiez de cette boucle, quel qu'en soit le prix.{/i}"

        "{i}Vous espérez que cette journée soit la dernière de cette boucle infernale.{/i}"

        hide lisa_sad
        show lisa_normal:
            center
            resize_char

        l "ahh.... Espérons que cette fois ci soit la bonne..."
        l "aller en route pour le métro !"

        hide lisa_normal
        show lisa_annoyed:
            center
            resize_char

        l "je vais encore devoir parler à cette vieille dame..."
        jump subway_morning

# ----------------------------------------------------------------------------
#                                   FIN
# ----------------------------------------------------------------------------

label fin:

    scene bg Small_Apartment_Kitchen

    show lisa_normal:
        center
        resize_char

    l "Encore une journée qui commence... Attends..."

    show lisa_shocked:
        center
        resize_char
    hide lisa_normal

    l "La date a changé ! Je suis sortie de la boucle !"

    show lisa_crying:
        center
        resize_char
    hide lisa_shocked

    l "Je n'arrive pas à y croire... Enfin libre de cette répétition infernale."
    "{i}Lisa est tellement heureuse qu'elle laisse échapper des larmes de joie. Elle savoure le moment, ressentant un mélange de soulagement et de bonheur pur.{/i}"

    if tuer_charlene == True:
        show lisa_sad:
            center
            resize_char
        hide lisa_happy

        l "Mais à quel prix ? J'ai tuer une amie qui m'étais chère ... Et dire que je ne la reverrais plus"

    if tuer_sophie == True:
        show lisa_sad:
            center
            resize_char
        hide lisa_smile_2

        l "Mais à quel prix ? J'ai tuer Sophie ... Même si c'étais une horrible vipère, je ne pourrais jamais oublier ce que j'ai fait"

    l "Heureusement, Jean et moi... Nous nous sommes trouvés dans cette folie. Nous sommes ensemble maintenant, et c'est une consolation précieuse."
    "{i}Lisa se rappelle de toutes les épreuves qu'elle a traversées, des moments de désespoir et des décisions difficiles. Elle prend une grande inspiration et se prépare à affronter la nouvelle journée, cette fois sans la crainte de la répétition.{/i}"

    hide lisa_sad
    show lisa_smile:
        center
        resize_char

    l "La monotonie de la vie peut parfois nous sembler une boucle sans fin, une répétition de jours identiques. Mais c'est dans ces moments que nous devons chercher le changement, créer nos propres différences et trouver du sens à travers nos actions."
    l "Même dans la routine, il y a des opportunités de grandir, d'aimer et de se découvrir. La vie n'est pas toujours une aventure grandiose, mais chaque petit moment compte."
    "{i}Avec cette pensée réconfortante, Lisa se sent prête à embrasser la nouvelle journée, appréciant chaque instant pour ce qu'il est, unique et précieux.{/i}"
    l "Je vais vivre chaque jour comme une nouvelle opportunité. Aujourd'hui est le premier jour du reste de ma vie."
    "{i}Et avec cette résolution, Lisa se prépare à sortir, le cœur léger et l'esprit ouvert, prête à affronter le monde avec une nouvelle perspective.{/i}"

    return
