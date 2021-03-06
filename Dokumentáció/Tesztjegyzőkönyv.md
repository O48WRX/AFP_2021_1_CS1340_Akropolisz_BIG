# Tesztjegyzőkönyv

## 1. Bevezetés
A tesztelés az alkalmazás fejlesztés egyik, hanem a legfontosabb mellékteendője,
mivel ezekből a tesztekből derül ki, hogy mik vannak teljesen készen, és miket kell a későbbiekben javítani.
Ezeket a teszteket a fejlsztők hajtják végre, általában a saját részükön, hogy pontosan tudják,
hogy hol keressék az esetleges hibákat.

## 2. Tesztelési terv hatóköre, célja:
Ahogy a bevezetésben is leírtuk,a tesztelés legfontosabb célja, hogy a fejlesztők kiszűrjék a program hibáit
és azokat minnél hamarabb és minnél hatékonyabban javítsák ki.
A frontend fejlesztők a frontend részt nézik át, a backend fejlesztők pedig a saját, backend részüket tesztelik.

## 3. Tesztek
A tesztelést és hibajavítűst mind a 4 fejlesztőre kiosztottuk, a saját terület-felelősségük alapján.

## 3.1 Kardos Zsolt -O48WRX

### Sikeres Tesztek

| Sorszám | Teszt neve | Leírása |
|---|---|---|
| 1. | **Logikai teszt** | A program logikai hátterének sikeres működéstesztje. |
| 2. | **Függvény teszt** | A program függvényeinek működésének és helyes meghívásának sikeres tesztje. |
| 3. | **Gomb-link teszt** | A gombok helyes hivatkozási irányának tesztelése. |
| 4. | **.KV beolvasás teszt** | A '.kv' kiterjesztésű fájl sikeres beolvasásának tesztje. |
| 5. | **Videól működésének tesztje** | A kivy videókezelő tesztelése különböző 'source'-okkal. |

### Hibás tesztek

| Sorszám | Teszt neve | Leírása |
|---|---|---|
| 1. | **Crash Course teszt** | A programnak a videóforrás megadásakor abszurd fájlokat adtunk meg, és ez megzavarta a program helyes működését. |
| 2. | **Crash Course 2 teszt** | A videók sliderjéhez abszurd értékeket adtunk meg és ez megzavarta a videók lejátszását. Ez később javítva lett. |
| 3. | **Lejátszás teszt** | A lejátszónak abszurd hosszúságú videókat (több órás) adtunk meg, ez megzavarta a sliderek helyes működését és pontosságát. |

## 3.2 Riczkó Henrik -D5GPJ6

### Sikeres Tesztek

| Sorszám | Teszt neve | Leírása |
|---|---|---|
| 1. | **Felhasználói felület megjelenítése** | A program megfelelően megjelent windows10 és ubuntu operációs rendszeren. |
| 2. | **Betűstílusok** | A programon belüli karakterek megfelelően megjelentek. |
| 3. | **Gombok méretei, kinézetei** | A gombok megjelenése és megfelelő mérete. |

### Hibás tesztek

| Sorszám | Teszt neve | Leírása |
|---|---|---|
| 1. | **Lejátszó teszt** | A program a videók lejátszása előtt fehér téglalapokat jelenített meg. Ez javítva lett. |
| 2. | **Videó tallózás** | A program tallózás menüje helytelenül jelent meg, ez javítva lett. |

## 3.3 Balogh Mihály Viktor - GUFVXA

### Sikeres Tesztek

| Sorszám | Teszt neve | Leírása |
|---|---|---|
| 1. | **Megfelelő szöveg megjelenítés** | A program ablakában a segítséget nyújtó szöveg jól megjelenik. |
| 2. | **Megjelenési mechanika** | Az alkalmazásban rendezetten jelennek meg a program elemei. |

### Hibás tesztek

| Sorszám | Teszt neve | Leírása |
|---|---|---|
| 1. | **Felületi hiba** | A program felületén nem megfelelően jelentek meg a szöveg sorai. |

## 3.4 Hadobás Dávid - TB3376

### Sikeres Tesztek

| Sorszám | Teszt neve | Leírása |
|---|---|---|
| 1. | **Felhasználói felület használhatósága** | A program minden (felhasználó által kezelhető) eleme megfelelően jelenik meg és használatra alkalmas. |
| 2. | **Késleltetés teszt** | A videók lejátszásakor a hozzájuk csatlakoztatott slider megfelelően átadja a beírt értéket gombnyomáskor. |
| 3. | **Egységteszt** | A program megfelelő működése a vissza gombok megnyomásakor sem szakad meg. |

### Hibás tesztek

| Sorszám | Teszt neve | Leírása |
|---|---|---|
| 1. | **Tallózás gomb tesztje** | A program kollázsképernyőjén a tallózás gombot "elfedte" a slider hitboxa, ez a probléma javítva lett később |
| 2. | **Videó tallózás** | A fejlesztői környezet hibát jelzett ki minden alkalommal, amikor egy videót tallóztunk, annak ellenére, hogy minden további nélkül lejátsza azt a program |
