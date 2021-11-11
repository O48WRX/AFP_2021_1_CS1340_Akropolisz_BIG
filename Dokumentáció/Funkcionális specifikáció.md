# Funkcionális specifikáció

## 1. Bevezetés
Egy olyan Python+Kivy alkalmazást fejlesztünk, amely az egyik nagyon elterjedt vizuális média, a videó kollázs létrehozását teszi egyszerűvé.
A szolgáltatást teljesen ingyen és regisztrációmentesen (ezáltal nem használunk fel semmilyen személyes adatot a felhasználótól.), viszont letöltést igényelve állítjuk a felhasználó elé.
A célunk a szolgáltatással, hogy megkönnyítsük az átlag ember számára egy videó kollázs létrehozását, egy egyszerűen kezelhető felülettel.
Az alkalmazás a letöltés után bármikor elérhető, internetelérést nem igényel a teljes felhasználáshoz.

## 2. Jelenlegi helyzet
A megrendelő egy egyszerű videólejátszó programot szeretne, amely egyszerre több videófájlt játszik le, állítható késleltetéssel. Az említett alkalmazást a megrendelő asztali alkalmazás formájában szeretné használni, bármilyen külső kapcsolat nélkül. Az ügyfél ragaszkodott egy egyszerű, kevés beletanulást igénylő felülethez, ami azoknak is könnyűvé teszi a kollázs elkészítését, aki semmilyen videókészítő tapasztalattal nem rendelkezik. Az ügyfél ragaszkodott még ahhoz is, hogy az oldal közepén legyen egy szerkeszthető leírás, valamint a videók elrendezése a videók számától függően változzon. Jelenleg a program létrehozásához, elkészítéséhez szükséges adatokat, tevékenységeket discord segítségével, minden héten, hetente többször is egyeztetjük.

## 3. Vágyálom rendszer
A csoport célja egy szinkronizált videólejátszó programot létrehozni, amelynek felületén állítható az egyes videók indításának késleltetése. Az egyes videók alatt elérhető lesz még annak is a lehetősége, hogy kiválasszuk, hogy a kiválasztottak közül melyik videó hangja kerüljön lejátszásra. A kollázs elkészítése előtt lehetőség lesz még egy címet/leírást adni a videócsoportnak, tetszőlegesen változtatható betűtípussal. A célunk a lehető legkevesebb kezelhető felülettel egy széleskörűen alkalmazható videószerkesztő program létrehozása.

## 4. Feltételek
Az alkalmazásunk létrehozásának alapfeltétele, hogy Python programozási nyelven, illetve annak valamilyen keretrendszerében készítsük a programot és a kezelőfelületét (a választásunk a Kivy-re és a PyCharm-ra esett könnyű kezelhetőségük miatt), valamint egy vagy több külső mappa, amelyben tároljuk a lejátszásra kerülő videókat.

## 5. Jelenlegi üzleti folyamatok modellje
A mai világban a legtöbb embernek nincs elegendő ideje ahhoz, hogy egy nagyobb videószerkesztő programot megtanuljon helyesen kezelni, anélkül hogy ki kellene mozdulnia az illető komfortzónájából, bár van egy csomó online felületen elérhető platform, ezeknek a legfőbb hátránya a bonyolult regisztráció és a túlkomplikált kezelőfelület, valamint kötelező internetelérés. Mindezek tekintetében arra jutottunk, hogy egy ingyenes, regisztrációmentes, könnyen kezelhető videókollázs programot hozunk létre, amely egyszerű kezelőfelülettel rendelkezik, mégis minőségi kombinációkat lehet benne létrehozni. 

## 6. Igényelt üzleti folyamatok modellje
Ezt a programot azért hozzuk létre, hogy a (videokollázsokat szerető) emberek a szabad időjükben tudjanak ilyeneket készíteni költségvetés, regisztráció és személyi adatok kiadása nélkül. A projektünk mappákkal lesz kapcsolatban, melyek lokális módon lesznek majd elérhetőek, az adott számítógépen. A regisztrációmentes előnynek köszönhetően, percek alatt már a programfelületet logikusan tudjuk kezelni, a mappák neve, a program kialakítása és kezelőfelülete nem igényel különösebb hozzáértést az alkalmi felhasználóktól.

## 7. Használati esetek
A felhasználó az alábbi tevékenységeket végezheti:
- A kiválasztott videók lejátszása
- A videók elrendezésének beállítása
- A videók elindítási késleltetésének beállítása
- Annak beállítása, hogy melyik videó hangja kerüljön lejátszásra
- A hangerő változtatása programon belül
- A kollázs címének megadása
- A cím/leírás betűtípusának beállítása

## 8. Képernyőtervek

## 9. Forgatókönyvek

### Kollázskészítés forgatókönyve
Szereplők: az asztali alkalmazás
Az alkalmazás elindításakor a program beolvassa, hogy hány videót kell megjeleníteni, és kialakítja azok elrendezését.
A felhasználó által végezhető műveletek:
- Késleltetés beállítása (egyenként)
- Hang kiválasztása és hangerő beállítása
- Leírás elkészítése
Amennyiben a felhasználó végzett a lejátszásokkal, egy gombbal ki tud lépni a programból
