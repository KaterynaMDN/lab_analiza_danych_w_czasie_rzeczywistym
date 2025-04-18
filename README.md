#REST API z regułą decyzyjną

Ten projekt to przykładowe REST API stworzone z wykorzystaniem Flask w Pythonie na potrzeby laboratorium.

Po uruchomieniu API będzie dostępne pod adresem:  
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

##Endpointy

| Endpoint                           | Opis                                                                 |
|-----------------------------------|----------------------------------------------------------------------|
| `/`                               | Zwraca: `Witaj w moim API!`                                          |
| `/mojastrona`                     | Zwraca: `To jest moja strona!`                                      |
| `/hello?name=Imię`                | Zwraca np.: `Hello Natalia!`                                        |
| `/api?x=3&y=5`                    | Porównuje `x` i `y`, zwraca wynik reguły decyzyjnej                 |
| `/api/v1.0/predict?num1=3&num2=4` | Prosty "model ML": jeśli `num1 + num2 > 5.8` → `prediction = 1`, w przeciwnym razie `0` |

---
