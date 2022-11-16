from scrapper import *


def test_titreVideo():
    url = "https://www.youtube.com/watch?v=fmsoym8I-3o"
    soup, driver = init(url)
    assert titreVideo(soup) == 'Pierre Niney : L’interview face cachée par HugoDécrypte'

def test_auteur():
    url = "https://www.youtube.com/watch?v=fmsoym8I-3o"
    soup, driver = init(url)
    assert auteur(soup) == "HugoDécrypte"

# Test inutile car le nombre de likes change tout le temps
"""
def test_like():
    url = "https://www.youtube.com/watch?v=fmsoym8I-3o"
    soup, driver = init(url)
    assert like(soup) == "30,528 "
"""

def test_description(): 
    url = "https://www.youtube.com/watch?v=fmsoym8I-3o"
    soup, driver = init(url)
    assert description(soup,driver).text == "🍿 L'acteur Pierre Niney est dans L’interview face cachée ! Ces prochains mois, le format revient plus fort avec des artistes, sportifs, etc.\n🔔 Abonnez-vous pour ne manquer aucune vidéo.\n\nInterview réalisée à l’occasion de la sortie du film « Mascarade » réalisé par Nicolas Bedos, le 1er novembre 2022 au cinéma. Avec Pierre Niney, Isabelle Adjani, François Cluzet, Marine Vacth.\n\nChaleureux remerciements au cinéma mk2 Bibliothèque pour son accueil.\n\n—\n\n00:00 Intro\n00:22 1\n03:32 2\n10:11 3\n14:09 4\n17:28 5\n20:10 6\n23:13 7\n39:22 8\n\n—\n\nPrésenté par Hugo Travers\n\nRéalisateur : Julien Potié\nJournalistes : Benjamin Aleberteau, Blanche Vathonne\n\nChargée de production déléguée : Romane Meissonnier\nAssistant de production déléguée : Clément Chaulet\nChargée de production exécutive : Marie Delvallée\n\nChef OPV : Lucas Stoll\nOPV : Pierre Amilhat, Vanon Borget\nElectricien : Alex Henry\nChef OPS : Victor Arnaud\nStagiaire image : Magali Faizeau\n\nMaquilleuse : Kim Desnoyers\nPhotographe plateau : Erwann Tanguy\n\nMonteur-étalonneur : Stan Duplan\nMixeuse : Romane Meissonnier\n\nCheffe de projets partenariats : Mathilde Rousseau\nAssistante cheffe de projets partenariats : Manon Montoriol\n\n—\n\n© HugoDécrypte / 2022"

def test_idVideo():
    url = "https://www.youtube.com/watch?v=fmsoym8I-3o"
    soup, driver = init(url)
    assert idVideo(url) == "fmsoym8I-3o"

def test_commentaires():
    url = "https://www.youtube.com/watch?v=fmsoym8I-3o"
    soup, driver = init(url)
    assert commentaires(soup, driver) == ['Pensez à vous abonner pour ne pas louper les vidéos suivantes et me soutenir. ', 'Hugo Décrypte + Pierre Niney = forcément une super interview ! Merci à vous deux ', 'C’est très plaisant et plutôt rare de trouver des journalistes aussi intéressés et impliqués, il n’y avait que de bonnes questions! Cette interview est de qualité, avec un invité de qualité! Merci beaucoup pour le travail derrière de l’équipe, merci pour ce partage! (Et hâte de te voir faire l’arbre )', 'Oh la la !! Le "mauvais doublage" fait par Pierre, on en veut encoooore ! C\'était hilarant !', 'Pierre Niney est clairement le meilleur acteur de sa génération.', "Incroyable le boulot fourni, merci Hugo, le crack de l'info de notre génération", "vidéo que j'ai fortement apprécié, les sujets abordés sont pertinents et les réponses font réfléchies. J'aime la tournure diversifiée que prend ce format et espère la revoir prochainement.", "Encore un travail de grande qualité merci à toute l'équipe !! Hâte de découvrir Mascarade !", 'On veut une "Actu en bref" fait par Pierre Niney ! \nMerci pour ce moment incroyable :D', '"Ça me paraît naturel que ce soit moi ensuite." \nJ\'adore Pierre, vraiment. Merci pour cette interview.']