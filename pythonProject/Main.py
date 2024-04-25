from Statystyki import srednia_ocen, najlepsza_ocena, najgorsza_ocena

def wprowadz_oceny():
    oceny = []
    while True:
        ocena = input("Wprowadź ocenę (lub zostaw puste, aby zakończyć): ")
        if ocena == "":
            break
        if ocena.isdigit() and 1 <= int(ocena) <= 6:
            oceny.append(int(ocena))
        else:
            print("Nieprawidłowa ocena. Wprowadź liczbę od 1 do 6.")
    return oceny

def wybor_przedmiotu():
    przedmioty = {
        'm': 'matematyka',
        'i': 'informatyka',
        'p': 'język_polski',
        'a': 'język_angielski'
    }
    while True:
        kod = input("Wybierz przedmiot (m: matematyka, i: informatyka, p: język polski, a: język angielski): ")
        if kod in przedmioty:
            return przedmioty[kod]
        else:
            print("Nieprawidłowy kod przedmiotu. Spróbuj ponownie.")

def zapisz_oceny_do_pliku(imie, nazwisko, przedmiot, oceny):
    filename = f"{imie}_{nazwisko}_{przedmiot}_oceny.txt"
    with open(filename, 'w') as plik:
        plik.write(f"Oceny z {przedmiot}:\n")
        plik.write("\n".join(str(ocena) for ocena in oceny))
        if oceny:
            srednia = srednia_ocen(oceny)
            najlepsza = najlepsza_ocena(oceny)
            najgorsza = najgorsza_ocena(oceny)
            plik.write(f"\nŚrednia ocen: {srednia:.2f}\n")
            plik.write(f"Najlepsza ocena: {najlepsza}\n")
            plik.write(f"Najgorsza ocena: {najgorsza}\n")
        else:
            plik.write("\nBrak ocen.\n")
    print(f"Oceny z {przedmiot} zostały zapisane w pliku {filename}.")

def main():
    print("Program do obliczania średniej i najlepszej oceny ucznia oraz zapisywania ocen do pliku z podziałem na przedmioty.")
    imie = input("Podaj imię ucznia: ")
    nazwisko = input("Podaj nazwisko ucznia: ")
    while True:
        przedmiot = wybor_przedmiotu()
        oceny = wprowadz_oceny()
        zapisz_oceny_do_pliku(imie, nazwisko, przedmiot, oceny)
        kontynuacja = input("Czy chcesz wprowadzić oceny z innego przedmiotu? (tak/nie): ")
        if kontynuacja.lower() != 'tak':
            break

if __name__ == "__main__":
    main()
