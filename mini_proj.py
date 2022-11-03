
Afrique = ["Ghana","Nigeria","Burkina"] 
Amerique = ["usa","Peru","Cuba"]
Europe = ["france","Belgique","Italie"]
Zone = ["Afrique", "Amerique", "Europe"]
Food = {"thiep yapp" :30,"neen bakhaal" :50, "soup":60  ,"ndambé" :40}

def greetings():
    name = input("Quel est votre nom complet ?\t")
    print("Bienvenue {}\n".format(name))
    age= int(input("Quel est votre age ?\t"))
    area = input("Dans quel zone souhaitez-vous aller ?\n")
    if area not in Zone:
        print("les vols en destination de {} ne sont pas par ici\n ".format(area))
    else:
        country = input("Dans quel pays souhaitez-vous aller ?\t")
        if country not in Afrique and country not in Europe and country not in Amerique:
            print("Ces vols ne sont pas en destination du {}\n".format(country))
        elif (area == "Afrique" and country not in Afrique) or (area == "Amerique" and country not in Amerique) or (area == "Europe" and country not in Europe):
            print("{} ne fait par partie du continent {}\n".format(country, area))     
        else:
            ticket = int(input("Quel type de billet souhaitez-vous:Allez simple ou Allez retour?. Répondez par {} ou {}\t".format(1, 2)))  
            if ticket == 1:
                if area == "Europe":
                    print("le billet aller-simple dans la zone Europe coute{}£. Si vous voulez voyager en classe VIP, vous payerez {}£.\n".format(2000, 2100))
                elif area == "Afrique":
                    print("le billet aller-simple dans la zone Afrique coute {}cfa. Si vous voulez voyager en classe VIP, vous payerez {}cfa.\n".format(450000, 510000))
                else:
                    print("le billet aller-simple dans la zone Amérique coute {}$.Si vous voulez voyager en classe VIP, vous payerez {}$\n".format(1900, 2000)) 
            elif ticket == 2:
                if area == "Europe":
                    print("le billet aller-retour dans la zone Europe coute{}£.Si vous voulez voyager en classe VIP, vous payerez {}£\n".format(1800, 1900))
                elif area == "Afrique":
                    print("le billet aller-retour dans la zone Afrique coute {}cfa.Si vous voulez voyager en classe VIP, vous payerez {}cfa\n".format(290000, 340000))
                else:
                    print("le billet aller-retour dans la zone Amérique coute {}$.Si vous voulez voyager en classe VIP, vous payerez {}$\n".format(1300, 1400))
            else:
                print("réponse erronée")
            meals = input("voulez-vous du gouté? Répondez par oui ou non\t")
            if meals == "oui":
                print("voici les plats disponibles:plat:(thiep yapp, neen bakhaal, soup ,ndambé)")
                dish = input("Quel plat souhaitez-vous ?\t")
                if dish in Food:
                    print("le plat de {} coute {}$\n".format(dish, Food[dish])) 
                else:
                    print("Nous n'avons pas ce plat à bord\n") 
            if meals == "non":
                print("ok")        
            print("Bienvenue au {}\n".format(country)) 


greetings()                         



