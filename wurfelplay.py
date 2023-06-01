import random, time, abfrage_aufrufen

class Wurfelplayer:
    
    
    def __init__(self, playerone, playertwo):
        
        self.playerone = playerone
        self.playertwo = playertwo

class Wurfelplay(Wurfelplayer):

    def playgame(self):
        print("-------------------------------------------------------------------------------")
        print(f"Der erste Spieler ist {self.playerone} der zweite Spieler ist {self.playertwo}")
        print("-------------------------------------------------------------------------------")


def abrufen_eingabe():

    player1 = None
    player2 = None
   
    while player1 == None and player2 == None:

        try:

            player1 = input("Erster Spielername: ")
            player2 = input("Zweiter Spielername: ")

        except:

            print("Bitte geben Sie einen Namen ein:")

    return player1, player2 

abrufen = abrufen_eingabe()

    
spieler = Wurfelplay(abrufen[0], abrufen[1])
spieler.playgame()

abfrage_aufrufen.anzeigen()

class AnzahlDerWurfel(Wurfelplay):

    def wurfeln(self):

        print("                       ")
        print("Wie viele Würfel wollen Sie?")
        print("(1) Einen Würfel")
        print("(2) Zwei Würfel")
        print("(3) Drei Würfel")

        eingabe_anzahl_wurfel = None

        eingabe_wahr = True

        while eingabe_wahr==True:

            try:
                eingabe_anzahl_wurfel = int(input("Zur Auswahl gibt es einen, zwei oder drei Würfel: "))
                
                if eingabe_anzahl_wurfel >= 1 and eingabe_anzahl_wurfel <= 3:

                    eingabe_wahr = False

                    print(eingabe_anzahl_wurfel)   

                else:

                    print("Bitte eine Zahl von 1-3 eingeben! ")        

            except:

                print("Bitte eine Zahl eingeben! ")

        return eingabe_anzahl_wurfel

    
    
anzahlwurfel = AnzahlDerWurfel(abrufen[0], abrufen[1])
speicherung_der_anzahl_wuerfel = anzahlwurfel.wurfeln()
print("Sie haben", speicherung_der_anzahl_wuerfel,"Würfel ausgewählt.")


class EinenWurfel(AnzahlDerWurfel):

    def __init__(self, playerone, playertwo):
        super().__init__(playerone, playertwo)
        
    def punkteanzeigen(self, punktezahl = []):

        self.punktezahl = punktezahl

    def wurfelen(self, anzahl_wurfel):

        self.anzahl_wurfel = anzahl_wurfel

        janein = input("Möchtest du den Würfel würfel? J steht für Ja, N steht für Nein: ")

        round1 = 0
        self.punktezahl = []

        if anzahl_wurfel==1:
                
            while round1 < 3:    

                if janein == "J":

                    print("Der Würfel wird gewürfelt...")
                    augenzahl = random.randint(1, 6)
                    time.sleep(2)
                    print("Der Würfel rollt...")
                    time.sleep(1)
                    print("...und rollt...")
                    time.sleep(1)
                    print("...und die Augenzahl beträgt...")
                    time.sleep(1)
                    print(augenzahl)
                    round1 = 1 + round1
                    self.punktezahl.append(augenzahl)

                elif janein == "N":

                    print("Programm beendet")
                    exit()

                else:

                    print("Ungültige Eingabe, Programm muss beenden, starten Sie erneut")
                    exit()
                    

            
            print(f"Die Augenzahlen die vom Spieler 1 gewürfelt wurden betragen {self.punktezahl}")
            summe1 = sum(self.punktezahl)
            print(f"{self.playerone} hat insgesamt {summe1} Punkte")

            janein = input("Möchtest du den Würfel würfel? J steht für Ja, N steht für Nein: ")

            round2 = 0
            self.punktezahl.clear()

            while round2 < 3:

                if janein == "J":
                
                    print("Der Würfel wird gewürfelt...")
                    augenzahl = random.randint(1, 6)
                    time.sleep(2)
                    print("Der Würfel rollt...")
                    time.sleep(1)
                    print("...und rollt...")
                    time.sleep(1)
                    print("...und die Augenzahl beträgt...")
                    time.sleep(1)
                    print(augenzahl)
                    round2 = 1 + round2
                    self.punktezahl.append(augenzahl)

                elif janein == "N":

                    print("Pogramm beendet")
                    exit()

                else:

                    print("Ungültige Eingabe")

            print(f"Die Augenzahlen die vom Spieler 2 gewürfelt wurden betragen {self.punktezahl}")
            summe2 = sum(self.punktezahl)
            print(f"{self.playertwo} hat insgesamt {summe2} Punkte")

            if summe1>summe2:
                print(f"Der Spieler {self.playerone} hat gewonnen mit {summe1} Punkte")
                exit()

            elif summe1<summe2:
                print(f"Der Spieler {self.playertwo} hat gewonnen mit {summe2} Punkten")
                exit()

            elif summe1==summe2:
                print("Unendschieden")
                exit()        


aufrufen = EinenWurfel(abrufen[0], abrufen[1])
aufrufen.wurfelen(speicherung_der_anzahl_wuerfel)



class Zwei_Wurfel(AnzahlDerWurfel):

    def __init__(self, playerone, playertwo):
        super().__init__(playerone, playertwo)
        
    def punkteanzeigen(self, punktezahl = []):

        self.punktezahl = punktezahl

    def wurfelen(self, anzahl_wurfel):

        self.anzahl_wurfel = anzahl_wurfel

        janein = input("Möchtest du den Würfel würfel? J steht für Ja, N steht für Nein: ")

        if janein == "N":

            print("Programm beendet")
            exit()

        round1 = 0
        self.punktezahl = []

        if anzahl_wurfel==2:
                
            while round1 < 3:    

                if janein == "J":

                    print("Zwei Würfel werden gewürfelt...")
                    augenzahl = random.randint(1, 6)
                    augenzahl2 = random.randint(1, 6)
                    time.sleep(2)
                    print("Die Würfel rollen...")
                    time.sleep(1)
                    print("...und rollen...")
                    time.sleep(1)
                    print("...und die Augenzahlen betragen...")
                    time.sleep(1)
                    print(augenzahl)
                    print(augenzahl2)

                    round1 = 1 + round1
                    self.punktezahl.append(augenzahl)
                    self.punktezahl.append(augenzahl2)


                else:

                    print("Ungültige Eingabe, Programm muss beenden, starten Sie erneut")
                    exit()
                    

            
            print(f"Die Augenzahlen die vom Spieler 1 gewürfelt wurden betragen {self.punktezahl}")
            summe1 = sum(self.punktezahl)
            print(f"{self.playerone} hat insgesamt {summe1} Punkte")

            janein = input("Möchtest du den Würfel würfel? J steht für Ja, N steht für Nein: ")

            if janein == "N":
                print("Pogramm beendet")
                exit()

            round2 = 0
            self.punktezahl.clear()

            while round2 < 3:

                if janein == "J":

                    print("Zwei Würfel werden gewürfelt...")
                    augenzahl = random.randint(1, 6)
                    augenzahl2 = random.randint(1, 6)
                    time.sleep(2)
                    print("Die Würfel rollen...")
                    time.sleep(1)
                    print("...und rollen...")
                    time.sleep(1)
                    print("...und die Augenzahlen betragen...")
                    time.sleep(1)
                    print(augenzahl)
                    print(augenzahl2)

                    round2 = 1 + round2
                    self.punktezahl.append(augenzahl)
                    self.punktezahl.append(augenzahl2)
                

                else:

                    print("Ungültige Eingabe")

            print(f"Die Augenzahlen die vom Spieler 2 gewürfelt wurden betragen {self.punktezahl}")
            summe2 = sum(self.punktezahl)
            print(f"{self.playertwo} hat insgesamt {summe2} Punkte")

            if summe1>summe2:
                print(f"Der Spieler {self.playerone} hat gewonnen mit {summe1} Punkte")
                exit()


            elif summe1<summe2:
                print(f"Der Spieler {self.playertwo} hat gewonnen mit {summe2} Punkten")
                exit()

            elif summe1==summe2:
                print("Unendschieden")
                exit()        


aufrufen = Zwei_Wurfel(abrufen[0], abrufen[1])
aufrufen.wurfelen(speicherung_der_anzahl_wuerfel)


class Drei_Wurfel(AnzahlDerWurfel):

    def __init__(self, playerone, playertwo):
        super().__init__(playerone, playertwo)
        
    def punkteanzeigen(self, punktezahl = []):

        self.punktezahl = punktezahl

    def wurfelen(self, anzahl_wurfel):

        self.anzahl_wurfel = anzahl_wurfel

        janein = input("Möchtest du den Würfel würfel? J steht für Ja, N steht für Nein: ")

        if janein == "N":

            print("Programm beendet")
            exit()

        round1 = 0
        self.punktezahl = []

        if anzahl_wurfel==3:
                
            while round1 < 3:    

                if janein == "J":

                    print("Drei Würfel werden gewürfelt...")
                    augenzahl = random.randint(1, 6)
                    augenzahl2 = random.randint(1, 6)
                    augenzah3 = random.randint(1, 6)
                    time.sleep(2)
                    print("Die Würfel rollen...")
                    time.sleep(1)
                    print("...und rollen...")
                    time.sleep(1)
                    print("...und die Augenzahlen betragen...")
                    time.sleep(1)
                    print(augenzahl)
                    print(augenzahl2)
                    print(augenzah3)

                    round1 = 1 + round1
                    self.punktezahl.append(augenzahl)
                    self.punktezahl.append(augenzahl2)
                    self.punktezahl.append(augenzah3)


                else:

                    print("Ungültige Eingabe, Programm muss beenden, starten Sie erneut")
                    exit()
                    

            
            print(f"Die Augenzahlen die vom Spieler 1 gewürfelt wurden betragen {self.punktezahl}")
            summe1 = sum(self.punktezahl)
            print(f"{self.playerone} hat insgesamt {summe1} Punkte")

            janein = input("Möchtest du den Würfel würfel? J steht für Ja, N steht für Nein: ")

            if janein == "N":
                print("Pogramm beendet")
                exit()

            round2 = 0
            self.punktezahl.clear()

            

            while round2 < 3:

                if janein == "J":

                    print("Drei Würfel werden gewürfelt...")
                    augenzahl = random.randint(1, 6)
                    augenzahl2 = random.randint(1, 6)
                    augenzah3 = random.randint(1, 6)
                    time.sleep(2)
                    print("Die Würfel rollen...")
                    time.sleep(1)
                    print("...und rollen...")
                    time.sleep(1)
                    print("...und die Augenzahlen betragen...")
                    time.sleep(1)
                    print(augenzahl)
                    print(augenzahl2)
                    print(augenzah3)

                    round2 = 1 + round2
                    self.punktezahl.append(augenzahl)
                    self.punktezahl.append(augenzahl2)
                    self.punktezahl.append(augenzah3)
                

                else:

                    print("Ungültige Eingabe")

            print(f"Die Augenzahlen die vom Spieler 2 gewürfelt wurden betragen {self.punktezahl}")
            summe2 = sum(self.punktezahl)
            print(f"{self.playertwo} hat insgesamt {summe2} Punkte")

            if summe1>summe2:
                print(f"Der Spieler {self.playerone} hat gewonnen mit {summe1} Punkte")
                exit()


            elif summe1<summe2:
                print(f"Der Spieler {self.playertwo} hat gewonnen mit {summe2} Punkten")
                exit()

            elif summe1==summe2:
                print("Unendschieden")
                exit()        


aufrufen = Drei_Wurfel(abrufen[0], abrufen[1])
aufrufen.wurfelen(speicherung_der_anzahl_wuerfel)


           




        



    