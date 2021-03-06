# Követelmény specifikáció

## 1. Áttekintés
A projektünk egy Python Video Creator,
ami lehetővé teszi, hogy egy címmel ellátott, szinkronizált videó kollázst hozzunk létre.
A megvalósításához Python + Kivy kombinációt fogunk használni.
A szolgáltatás teljesen ingyenes és minimalista felülettel rendelkezik átláthatóság miatt.

## 2. Jelenlegi helyzet
Manapság a videókollázsok felléptek népszerűségben, azonban ezek létrehozása az esetek nagyrészében nagyon körülményes, gyakran nehezebben tanulható szoftver használata is feltétel az elkészítéséhez, mellesleg ezek a programok (legalábbis a legtöbb hasznos funkciót nyújtó programok) egyszeri vagy havi díjat igényelnek regisztráció mellett és általában nehezen is kezelhetőek. Az előbb felsorolt problémákra szeretnénk megoldást nyújtani a szolgáltatásunkkal, ami egy letisztult felületű, könnyen kezelhető, ingyenesen elérhető, regisztrációt nem igénylő alkalmazás.

## 3. Vágyálomrendszer
Csoportunk célja, hogy létrehozzunk egy olyan szolgáltatást a videókollázsok létrehozásához, amely a felhasználók számára a legkényelmesebb, legkönnyebb kezelhetőséget nyújtja. A vágyálomrendszerünk része, hogy a programunk rendelkezik egy menüvel, amiben esélye a van a felhasználónak létrehozni egy saját videókollázst, tallózással elérni a használni kívánt videóit, illetve címet adni a kollázsnak, ezenkívül megnézni egy 'Demo' funkcióval, hogy, hogyan néz ki a program végterméke, valamint egy 'Segítség/Súgó' funkcióval, ami a felhasználó számára segítséget nyújt a program használatához és egy 'kilépés' gomb, ami bezárja az applikációt.


## 4. Funkcionális követelmények
A projekt egy asztali alkalmazás, amihez Python-t és Kivy-t használunk, így funkcionális követelménynek mondható, hogy a felhasználó számítógépe képes legyen python állományokat futtatni. Nem igényel internetet, így offline is bármikor használható.
TL;DR:
- Python állományok futtatására képesnek kell lennie a gépnek.
- NEM igényel internetet, így offline is használható.

Egyéb követelményekről (2021.11.11) nem beszélhetünk.


## 5. Rendszerre vonatkozó törvények, szabványok, ajánlások
A projekt egy szimpla szoftveres alkalmazásnak felel meg, ami egyetemi hallgatói licensszel készül egyetemi kurzusra, így sem legálisan, sem morálisan nem lenne megfelelő a csapat részéről, ha nem ingyenesen és open-source fejlesztésben végeznénk. Lényegében egy videószerkesztő/kollázskészítő program.

- A projekt hallgatói licenszen készül, egyetemi kurzusra.
- Teljesen ingyenes.
- Open-source
- Videószerkesztő/kollázskészítő program.


## 6. Jelenlegi üzleti folyamatok modellje
Mostanság egyedül a videószerkesztő szoftverekkel lehet videókollázst létrehozni, de ezek használata általában többet igényel egy szimpla súgónál, sőt teljes szakmák és egyetemi kurzusok alakultak ki körülöttük, pl.: Adobe Premier, Adobe After Effects, Sony Vegas stb. Az előbb felsorolt programok nagy része és ezek hasznos funkciókkal rendelkező disztribúciói manapság a videókollázsok felléptek népszerűségben, azonban ezek létrehozása az esetek nagyrészében nagyon nehéz, esetlegesen komplikáltabb szoftver használata is valószínűleg feltétel az elkészítéséhez, mellesleg havi prémiumot vagy egyszeri megvásárlást igényeltek (felhasználók adatainak tárolása mellett) és felhasználói felületeik nehezen kezelhetőek.
Az előbb felsoroltak miatt nagyon sok ember videó- és videókollázs-készítési inspirációi alacsonyröptűekké váltak.

## 7. Igényelt üzleti folyamatok modellje
Projektünkkel igyekszünk egy letisztult, könnyen kezelhető asztali szoftvert nyújtani a felhasználók számára. A szolgáltatásunk nem igényel regisztrációt, sem financiális beruházást további használat után sem. Az applikáció egy jól megszokott, valamint új felhasználók számára könnyen értelmezhető menürendszer alapján működik, amiben el lehet érni az alkalmazás különböző funkcióit, pl.: Saját Kollázs, Demo Kollázs, Súgó/segítség, Kilépés.
Az alkalmazásunk könnyű kezelhetőségével, minimális szoftverismereti igényével szeretnénk kitűnni a versenytársaink közül, többek között azzal is, hogy tudjuk mennyire fontos a magánszemélyek számára az adataik védelme, így mi nem is kérünk semmilyen adatot a felhasználóinktól. A szolgáltatásunk internetet sem igényel, mivel nem kommunikál semmilyen szerverrel, hanem "helyben", a számítógépen fut, és ebből következően offline is használható.

![Igényelt üzleti folyamatok](https://user-images.githubusercontent.com/82958011/141682268-23bf3298-7ac4-4085-a341-8a482c8d05f5.png)

## 8.Fogalomszótár

### 8.1.1 TL;DR
'Too long, didn't read', fordítva: Túl hosszú, nem olvastam.
Mivel hosszú leírást adtunk néhány helyen, így szükségesnek éreztük, egy lista bevezetésére, amivel gyorsabban átláthatóvá tesszük a szöveget, vázlatolva.

### 8.1.2 Demo
Ebben az esetben a programunk, egy előre elkészített sikeres működésének bemutatása a felhasználó számára (a demonstráció szóból).

### 8.1.3 Open-source
Olyan kód/alkalmazás, ami bármikor publikusan elérhető, bárki láthatja, módosíthatja és megoszthatja, amikor akarja.

### 8.1.4 Python
A Python egy multi-paradigmás programozási nyelv.

### 8.1.5 Kivy
A Kivy egy open-source Python keretrendszer, mobilos és egyéb applikációk fejlesztésére alkalmas.
