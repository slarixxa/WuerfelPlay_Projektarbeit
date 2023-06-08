import random, time, abfrage_aufrufen

#Ich erstelle als erstes eine Klasse für die jeweilgen Spieler
class Wurfelplayer:
    
    #Funktion erstellt
    def __init__(self, playerone, playertwo):
        
        self.playerone = playerone
        self.playertwo = playertwo

#Extra Klasse erstellt für die Ausgabe der Spieler, die Klasse erbet
class Wurfelplay(Wurfelplayer):

    def playgame(self):
        print("-------------------------------------------------------------------------------")
        print(f"Der erste Spieler ist {self.playerone} der zweite Spieler ist {self.playertwo}")
        print("-------------------------------------------------------------------------------")


#Einfache Methode ersetllt um die Spielernamen einzutippen
def abrufen_eingabe():

    player1 = None
    player2 = None
   
    #Solange noch keine Eingabe folgt soll die Schleife laufen
    while player1 == None and player2 == None:

        player1 = input("Erster Spielername: ")
        player2 = input("Zweiter Spielername: ")


    return player1, player2 

#Hier habe ich eine extra Klasse erstellt, die von Wurfelplay erbet
class AnzahlDerWurfel(Wurfelplay):

    #Methode
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
                #Hier tue ich die Abfrage in einem try und except Block, falls hier eine Zeichenkette eingetippt wird
                eingabe_anzahl_wurfel = int(input("Zur Auswahl gibt es einen, zwei oder drei Würfel: "))
                
                #Es darf nur eine Zahl von 1-3 eingegeben werden, nicht darunter und nicht darüber
                if eingabe_anzahl_wurfel >= 1 and eingabe_anzahl_wurfel <= 3:
                    
                    #Wenn richtig, endet die Abfrage hier
                    eingabe_wahr = False

                    print(eingabe_anzahl_wurfel)   

                else:
                    #Wenn falsche eingetppt
                    print("Bitte eine Zahl von 1-3 eingeben! ")        

            except:
                #Fehler wird aufgefangen, wenn String eingetppt wird, und fragt nochmal
                print("Bitte eine Zahl eingeben! ")

        return eingabe_anzahl_wurfel

    
    



#Hier ist die Klasse für einen Wurfel, erbt von der Anzahl Klasse
class EinenWurfel(AnzahlDerWurfel):

    #Hier hole ich die Namen raus
    def __init__(self, playerone, playertwo):
        super().__init__(playerone, playertwo)

    #Punkte werden in einem Array gespeichert    
    def punkteanzeigen(self, punktezahl = []):

        self.punktezahl = punktezahl

    def wurfelen(self, anzahl_wurfel):

        self.anzahl_wurfel = anzahl_wurfel

        janein = input("Möchtest du den Würfel würfel? J steht für Ja, N steht für Nein: ")

        #Runde wird auf 0 gesetzt, man kann 3 mal würfeln
        round1 = 0
        self.punktezahl = []

        #Wenn 1 Würfel ausgewählt wird
        if anzahl_wurfel==1:

            #3 Runden    
            while round1 < 3:    

                #Wenn input auf Ja
                if janein == "J":

                    print("Der Würfel wird gewürfelt...")
                    #Random die augenzahl von 1-6
                    augenzahl = random.randint(1, 6)
                    #Sleep eingesetzt für den Effekt
                    time.sleep(2)
                    print("Der Würfel rollt...")
                    time.sleep(1)
                    print("...und rollt...")
                    time.sleep(1)
                    print("...und die Augenzahl beträgt...")
                    time.sleep(1)
                    print(augenzahl)
                    #Runde wird + 1
                    round1 = 1 + round1
                    #Augenzahl wird der Punktezahl ins Array gesetzt
                    self.punktezahl.append(augenzahl)
                #Wenn Nein, dann Programm beendet
                elif janein == "N":

                    print("Programm beendet")
                    exit()

                else:
                    #Falls was falsches eingegeben wird, muss das Programm beenden
                    print("Ungültige Eingabe, Programm muss beenden, starten Sie erneut")
                    exit()
                    

            
            print(f"Die Augenzahlen die vom Spieler 1 gewürfelt wurden betragen {self.punktezahl}")
            #Punkte werden zusammen gerechnet
            summe1 = sum(self.punktezahl)
            print(f"{self.playerone} hat insgesamt {summe1} Punkte")

            #Zweite Runde beginnt, für den Spieler 2
            janein = input("Möchtest du den Würfel würfel? J steht für Ja, N steht für Nein: ")

            round2 = 0
            #Punkte im Array werden gelöscht
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

            #Hier werden die Summe der Spieler verglichen, der Spieler mit der höheren Punktzahl hat gewonnen
            if summe1>summe2:
                print(f"Der Spieler {self.playerone} hat gewonnen mit {summe1} Punkte")
                exit()

            elif summe1<summe2:
                print(f"Der Spieler {self.playertwo} hat gewonnen mit {summe2} Punkten")
                exit()

            elif summe1==summe2:
                print("Unendschieden")
                exit()        



#Klasse für 2 Würfel
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

        #Hier für 2 Würfel
        if anzahl_wurfel==2:
                
            while round1 < 3:    

                if janein == "J":

                    print("Zwei Würfel werden gewürfelt...")
                    #Zwei Augenzahlen, für 2 Würfel
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
                    #Beide Augenzahlen werden im Array Punktezahl hinzugefügt 
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



#Klasse für die 3 Würfel
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

        #Selbe Prinzip...wenn 3 Würfel gewählt wurden sind
        if anzahl_wurfel==3:
                
            for round1 in range(3):    

                if janein == "J":

                    print("Drei Würfel werden gewürfelt...")
                    #3 Augenzahlen für 3 Würfel
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
                    #Alle drei Augenzahlen werden hinzugefügt
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

            

            for round2 in range(3):

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



abrufen = abrufen_eingabe()

spieler = Wurfelplay(abrufen[0], abrufen[1])
spieler.playgame()

#Hier wird das Paket aufgerufen, außerhalb wurde eine txt Datei ersetllt (oben wird sie importiert)
abfrage_aufrufen.anzeigen()

anzahlwurfel = AnzahlDerWurfel(abrufen[0], abrufen[1])

speicherung_der_anzahl_wuerfel = anzahlwurfel.wurfeln()

print("Sie haben", speicherung_der_anzahl_wuerfel,"Würfel ausgewählt.")

if speicherung_der_anzahl_wuerfel == 1:

    aufrufen1 = EinenWurfel(abrufen[0], abrufen[1])

    aufrufen1.wurfelen(speicherung_der_anzahl_wuerfel)

elif speicherung_der_anzahl_wuerfel == 2:

    aufrufen2 = Zwei_Wurfel(abrufen[0], abrufen[1])

    aufrufen2.wurfelen(speicherung_der_anzahl_wuerfel)

elif speicherung_der_anzahl_wuerfel == 3:

    aufrufen3 = Drei_Wurfel(abrufen[0], abrufen[1])
    aufrufen3.wurfelen(speicherung_der_anzahl_wuerfel)

else:
    print("No valid input")

           




        



    