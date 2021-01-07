import random
waga = int(input("Podaj swoją wagę w kg: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
time = int(input("Ile maż codziennie na aktwyność fizyczną? [minuty] "))
inf = ""
def obliczBMI(waga, wzrost):
    BMI = round(waga / wzrost**2, 2)
    return BMI
def SkalaBMI(BMI):
    if BMI < 16:
        inf = "wygłodzenie"
    elif BMI > 16 and BMI < 16.99:
        inf = "wygłodzenie"
    elif BMI > 16 and BMI < 16.99:
        inf = "niedowaga"
    elif BMI > 17 and BMI < 18.49:
        inf = "wygłodzenie"
    elif BMI > 18.50 and BMI < 24.99:
        inf = "wartość prawidłowa"
    elif BMI > 25 and BMI < 29.99:
        inf = "nadwaga"
    elif BMI > 30.00 and BMI < 34.99:
        inf = "I stopień otyłości"
    elif BMI > 35.00 and BMI < 39.99:
        inf = "II stopień otyłości"
    else:
        inf = "otyłość skrajna"
    return inf

def aktywność(czas: int):
    listaaktywności = [
        "Aerobik ",
        "Aerobik w wodzie ",
        "Badminton",
        "Bieganie",
        "Ćwiczenia na siłowni ",
        "Chodzenie po sklepie ",
        'Golf ',
        'Gotowanie ',
        'Gra na pianinie 15 min. ',
        'Gra w kręgle ',
        'Gra w piłkę nożną ',
        'Yoga ',
        'Intensywna gimnastyka',
        'Jazda konna',
        'Jazda na deskorolce',
        'Jazda na nartach biegowych',
        'Jazda na nartach wodnych',
        'Jazda na nartach zjazdowych',

        'Jazda na rolkach ',
        'Jazda na rowerze (10 km/h) ',
        'Jazda na rowerze (20 km/h)',
        'Jogging ',
        'Kopanie, grabienie',
        'Koszykówka ',
        'Lekka gimnastyka',
        'Lekka praca biurowa',
        'Marszobieg',
        'Mycie okien',
        'Mycie podłogi',
        'Odkurzanie ',
        'Piłowanie drewna ',
        'Ping-pong',
        'Pływanie',
        'Praca ekspedientki',
        'Praca kamieniarska',
        'Praca w ogródku',
        'Pranie ręczne',
        'Prasowanie',
        'Prowadzenie samochodu',
        'Robienie na drutach',
        'Robienie zakupów',
        'Schodzenie ze schodów',
        'Ścieranie kurzy',

        'Siatkówka ',
        'Siatkówka plażowa ',
        'Skakanie na skakance ',
        'Słanie łóżka ',
        'Spacer szybkim tempie ',
        'Spacer w umiarkowanym tempie ',
        'Sen ',
        'Śpiew ',
        'Sprzątanie łazienki ',
        'Sprzątanie pokoju ',
        'Squash ',
        'Stanie na baczność ',
        'Stanie swobodne ',
        'Szorowanie podłóg ',
        'Szybki marsz 6 km/h',
        'Szycie na maszynie ',
        'Szycie ręczne ',
        'Taniec w dyskotece ',
        'Tenis ',
        'Trzepanie dywanów ',
        'Ubieranie się i rozbieranie ',
        'Układanie dokumentów ',
        'Wchodzenie po schodach ',
        'Wędkowani',
        'Wiosłowanie ',
        'Zamiatanie podłogi ',
        'Zmywanie naczyń ',
    ]
    if inf == "nadwaga":
        time = random.randint(10, czas + 1)
    elif inf == "I stopień otyłości":
        time = random.randint(15, czas + 1)
    elif inf == "II stopień otyłości":
        time = random.randint(15, czas + 1)
    elif inf == "otyłość skrajna":
        time = random.randint(20, czas + 1)
    else:
        time = random.randint(1, czas + 1)
    cwiczenie = random.choice(listaaktywności)
    return f"Twoje ćwicznie to {cwiczenie} przez {time} minut"
if __name__ == '__main__':
    BMI = obliczBMI(waga, wzrost)
    skala = SkalaBMI(BMI)
    zestaw = aktywność(time)
    print(f'Twoje BMI wynosi {BMI} i klasyfikuje się do kategori: {skala} \n  {zestaw}')

