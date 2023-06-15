# Digital-Signature

Oto lista kroków dla użytkownika:

1. Uruchom program.
2. Wybierz jedną z opcji:
   - Wpisz `1`, jeśli chcesz podpisać plik.
   - Wpisz `2`, jeśli chcesz sprawdzić podpis pliku.
   - Wpisz `3`, jeśli chcesz wyjść z programu.
3. Jeśli wybrałeś opcję `1` (Podpisać plik):
   - Wyświetli się lista plików w bieżącym katalogu.
   - Wybierz plik, który chcesz podpisać.
   - Jeśli plik nie istnieje, program wyświetli odpowiednie powiadomienie.
   - Wygenerowane zostaną klucze prywatny i publiczny.
   - Plik zostanie podpisany przy użyciu klucza prywatnego.
   - Podpisany plik zostanie zapisany w katalogu "signed".
   - Program wyświetli komunikat potwierdzający podpisanie pliku.
4. Jeśli wybrałeś opcję `2` (Sprawdzić plik):
   - Wyświetli się lista podpisanych plików w katalogu "signed".
   - Wybierz plik, którego podpis chcesz zweryfikować.
   - Jeśli plik nie istnieje, program wyświetli odpowiednie powiadomienie.
   - Jeśli klucz jest uszkodzony, program wyświetli odpowiednie powiadomienie.
   - Program sprawdza, czy podpis pliku zgadza się z kluczem publicznym.
   - Program wyświetli komunikat informujący o poprawności podpisu.
5. Jeśli wybrałeś opcję `3` (Wyjść):
   - Program zakończy działanie.

Pamiętaj, aby dostosować ścieżki plików w kodzie do własnego środowiska.
