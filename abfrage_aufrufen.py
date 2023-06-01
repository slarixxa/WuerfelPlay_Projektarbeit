def anzeigen():

	eingabe_wahr = True

	while eingabe_wahr==True:

		programm_ablauf = input("Prgramm jetzt beenden oder weiter?: ")

		if programm_ablauf == "weiter":
			print("Pogramm läuft weiter")
			eingabe_wahr = False

		elif programm_ablauf == "beenden":
			print("Pogramm beendet")
			exit()
		else:
			print("Falsche Eingabe")
			print("Versuchen Sie es erneut")