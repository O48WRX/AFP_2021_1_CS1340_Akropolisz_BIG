# ﻿Rendszerterv

## 1. Rendszer célja

A rendszer célja, hogy egy videó lejátszására alkalmas felületet adjon vissza. A program minimalista felülettel fog rendelkezni a könnyen kezelhetőség érdekében. A felhasználó 2-4 videóból készíthet egy kollázst. A célja a programnak, hogy a videókból összeállított kollázst ugyanakkor játssza le, mintha egy folytonos videó lenne. A program használata során a felhasználónak ki kell tallóznia a videókat, amikből a kollázst szeretné létrehozni, ezen kívül más bevitelt nem vár a program. Az alkalmazás python és kivy nyelven valósul meg, ezért a legtöbb rendszerrel kompatibilis lesz.

## 2. Követelmények

        - A fejlesztés Python illetve kivy segítségével történik
        - Az alkalmazás kompatibilis minden operációs rendszerrel ami képes Pythont futtatni
        - Az alkalmazás minimális gépigénnyel rendelkezik
        - Gyors, hatékony működés
 
## 3. Projekt terv

A projekt elkülönül dizájn és logika részekre. Ezeken a részeken más-más emberek dolgoznak:

        -Dizájn: Egyszerű, felhasználóbarát felület
                -Felelősök: Riczkó Henrik (D5GPJ6), Hadobás Dávid (TB3376)
        -Logika: Hatékony, gyorsan működő program megvalósítása
                -Felelősök: Kardos Zsolt (O48WRX), Balogh Mihály Viktor (GUFVXA)
                TODO

## 4. Üzleti folyamatok modellje

![ÜzletiFolyamatok](https://user-images.githubusercontent.com/82958011/141307230-9507f4b8-3976-4adc-9f6e-af649e7c0579.png)


## 5. Fizikai környezet

A rendszer fejlesztése python és kivy segítségével történik. 
Minimális gépigényre van szükség a program futtatásához.
Bármilyen operációs rendszeren futtatható.

## 6. Funkcionális terv

Rendszerszereplő: - Felhasználó: A programnak nincs más szereplője, csak az alkalmazás felhasználója, aki kiválasztja a videókat amikből létre szeretné hozzni a kollázst.

## 7. Architekturális terv

A rendszerhez mindössze egy .exe állomány futtatására van szükség, nem igényel egyéb futtatáshoz szükséges követelményeket. 

## 8. Tesztterv

A fejlesztés során szükséges a folytonos tesztelés. Ellenőrizni kell a gombok működését, a videók tallózását valamint a kollázs készítését. TODO: Tesztek

## 9. Telepítési terv

Az alkalmazás nem igényel telepítést, a .exe állomány futtatásával indítható.

## 10. Karbantartási terv

Az alkalmazás bővítése tervbe van. Négynél több videóból álló kollázsok készítése a későbbiekben.

## 11. Implementációs terv

A program Python és Kivy nyelven valósul meg a felhasználóbarát dizájn és logika elkészítése érdekében. 
