# Programarea unui joc de ghicit

Să ne avântăm în Rust lucrând împreună la un proiect direct aplicabil! În acest capitol o să te familiarizezi cu câteva concepte uzitate în Rust, arătându-ți cum să le aplici într-un program concret. Îți vei însuși cunoștințe despre `let`, `match`, metode, funcții asociate, crate-uri externe și mai mult! În capitolele ce urmează, vom aprofunda aceste idei. Pentru moment, ne vom concentra pe exersarea noțiunilor fundamentale.

Vom pune în aplicare o problemă emblematică pentru începătorii în programare: un joc de ghicit. Iată în ce constă: programul va genera un număr întreg aleatoriu între 1 și 100. Va solicita apoi jucătorului să introducă o ghicire. După ce un număr a fost introdus, programul va specifica dacă acesta este prea mic sau prea mare. Dacă răspunsul este corect, jocul va afișa un mesaj de felicitare și se va închide.

## Formarea unui proiect nou

Pentru a forma un proiect nou, mergi la directoriul *proiecte* pe care l-ai creat în Capitolul 1 și fă un proiect nou folosind Cargo, astfel:

```console
$ cargo new guessing_game
$ cd guessing_game
```

Prima comandă, `cargo new`, ia numele proiectului (`guessing_game`) ca prim argument. A doua comandă trece la directoriul noului proiect.

Aruncă o privire la fișierul *Cargo.toml* generat:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial
rm -rf no-listing-01-cargo-new
cargo new no-listing-01-cargo-new --name guessing_game
cd no-listing-01-cargo-new
cargo run > output.txt 2>&1
cd ../../..
-->

<span class="filename">Numele fișierului: Cargo.toml</span>

```toml
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/Cargo.toml}}
```

După cum ai văzut în Capitolul 1, `cargo new` generează un program “Salut, lume!” pentru tine. Verifică fișierul *src/main.rs*:

<span class="filename">Numele fișierului: src/main.rs</span>

```rust
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/src/main.rs}}
```

Acum să compilăm acest program „Salut, lume!" și să îl rulăm în același pas folosind comanda `cargo run`:

```console
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-01-cargo-new/output.txt}}
```

Comanda `run` este utilă când ai nevoie să iterezi rapid pe un proiect, așa cum vom face în acest joc, testând rapid fiecare iterație înainte de a trece la următoarea.

Deschide din nou fișierul *src/main.rs*. Vei scrie tot codul în acest fișier.

## Procesarea unei ghiciri

Prima parte a programului de ghicit va cere intrarea utilizatorului, va procesa acea intrare și va verifica dacă intrarea este în forma așteptată. Pentru început, vom permite jucătorului să introducă o ghicire. Introdu codul din Listare 2-1 în *src/main.rs*.

<span class="filename">Numele fișierului: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:all}}
```

<span class="caption">Lstarea 2-1: Cod care obține o ghicire de la utilizator și o tipărește</span>

Acest cod conține o mulțime de informații, deci să-l parcurgem linie cu linie. Pentru a obține intrarea utilizatorului și apoi a printa rezultatul ca ieșire, avem nevoie să aducem biblioteca `io` de intrare/ieșire în scopul nostru. Biblioteca `io` vine din biblioteca standard, cunoscută sub numele de `std`:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:io}}
```

În mod implicit, Rust are un set de elemente definite în librăria standard pe care le introduce în domeniul de vizibilitatea al fiecărui program. Acest set se numește *prelude*, și poți vedea tot ce se află în el [în documentația librăriei standard][prelude].

Dacă un tip pe care dorești să-l folosești nu se află în prelude, trebuie să introduci acel tip explicit în domeniu cu o instrucțiune `use`. Utilizarea librăriei `std::io` îți oferă un număr de caracteristici utile, inclusiv capacitatea de a accepta intrarea utilizatorului.

După cum ai văzut în Capitolul 1, funcția `main` este punctul de intrare în program:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:main}}
```

Sintaxa `fn` declară o nouă funcție; parantezele, `()`, indică faptul că nu există parametri; iar paranteza rotundă, `{`, începe corpul funcției.

Așa cum ai învățat și în Capitolul 1, `println!` este o macrocomandă care tipărește un string pe ecran:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:print}}
```

Acest cod afișează un prompt care indică ce joc este și solicită intrare de la utilizator.

### Păstrarea valorilor cu variabile

În continuare, vom crea o *variabilă* pentru a stoca input-ul utilizatorului, astfel:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:string}}
```

Acum programul devine interesant! Se întâmplă multe în această mică linie. Folosim declarația `let` pentru a crea variabila. Iată un alt exemplu:

```rust,ignore
let apples = 5;
```

Această linie de cod creează o nouă variabilă numită `apples` și o leagă de valoarea 5. În Rust, variabilele sunt imutabile în mod implicit, ceea ce înseamnă că odată ce dăm variabilei o valoare, valoarea nu se va schimba. Vom discuta acest concept în detaliu în secțiunea [„Variabile și mutabilitate”][variables-and-mutability]<!-- ignore --> din Capitolul 3. Pentru a face o variabilă mutabilă, adăugăm `mut` înainte de numele variabilei:

```rust,ignore
let apples = 5; // imutabil
let mut bananas = 5; // mutabil
```

> Notă: Sintaxa `//` începe un comentariu care continuă până la sfârșitul liniei. Rust ignoră totul în comentarii. Vom discuta comentariile în mai multe detalii în [Capitolul 3][comments]<!-- ignore -->.

Revenind la programul de ghicit, acum știi că `let mut guess` va introduce o variabilă mutabilă denumită `guess`. Semnul egal (`=`) spune lui Rust că dorim să legăm ceva la variabilă acum. Pe dreapta semnului egal se află valoarea la care `guess` este legată, care este rezultatul apelării functiei `String::new`, o funcție care returnează o nouă instanță a unui `String`. [`String`][string]<!-- ignore --> este un tip de string furnizat de librăria standard care este un text codificat UTF-8 care poate să crească.

Sintaxa `::` din linia `::new` indică că `new` este o funcție asociată tipului `String`. O *funcție asociată* este o funcție care este implementată pe un tip, în acest caz `String`. Această funcție `new` creează un string nou și gol. Vei găsi o funcție `new` în multe tipuri deoarece este un nume obișnuit pentru o funcție care face o valoare nouă de un anume fel.

În întregime, linia `let mut guess = String::new();` a creat o variabilă mutabilă care este în prezent legată de o nouă instanță goală a unui `String`. Uf!

### Primirea datelor introduse de utilizator

Ține minte că am inclus funcționalitatea de intrare/ieșire din biblioteca standard cu `use std::io;` pe prima linie a programului. Acum vom apela funcția `stdin` din modulul `io`, care ne va permite să gestionăm datele introduse de utilizator:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:read}}
```

Dacă nu am fi importat biblioteca `io` cu `use std::io;` la începutul programului, am putea totuși să folosim funcția scriind acest apel de funcție ca `std::io::stdin`. Funcția `stdin` returnează o instanță a [`std::io::Stdin`][iostdin]<!-- ignore -->, care este un tip care reprezintă un handle la intrarea standard pentru terminalul tău.

Următoarea linie, `.read_line(&mut guess)` apelează metoda [`read_line`][read_line]<!-- ignore --> pe handle-ul de intrare standard pentru a primi datele introduse de utilizator. De asemenea, trimitem `&mut guess` ca argument pentru `read_line`, pentru a-i spune în ce string să stocheze datele introduse de utilizator. Rolul principal al `read_line` este de a prelua tot ceea ce tapează utilizatorul în intrarea standard și de a adăuga aceste date într-un string (fără a-i suprascrie conținutul), deci vom trimite acest string ca argument. String-ul de argument trebuie să fie mutabil pentru ca metoda să poată schimba conținutul lui.

Simbolul `&` indică faptul că acest argument este o *referință*, care îți oferă o modalitate de a permite mai multor părți ale codului tău să acceseze o singură piesă de date fără a avea nevoie să copiezi acele date în memorie de mai multe ori. Referințele sunt o caracteristică complexă, iar unul dintre principalele avantaje ale Rust este cât de sigur și ușor e de utilizat referințele. Nu ai nevoie să știi o mulțime de acele detalii pentru a termina acest program. Deocamdată, tot ce trebuie să știi este că, la fel ca variabilele, referințele sunt imutabile în mod implicit. De aceea, trebuie să scrii `&mut guess` în loc de `&guess` pentru a-l face mutabil. (Capitolul 4 va explica referințele mai detaliat.)

<!-- Old heading. Do not remove or links may break. --> <a id="handling-potential-failure-with-the-result-type"></a>

### Gestionarea potențialelor eșecuri cu `Result`

Încă lucrăm la această linie de cod. Acum discutăm despre a treia linie de text, dar reține că aceasta face încă parte dintr-o singură linie logică de cod. Partea următoare este această metodă:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:expect}}
```

Am fi putut scrie acest cod astfel:

```rust,ignore
io::stdin().read_line(&mut guess).expect("Failed to read line");
```

Cu toate acestea, o linie lungă este dificil de citit, deci este cel mai bine să o împărțim. Este adesea înțelept să introduci o linie nouă și alte spații albe pentru a ajuta la divizarea liniilor lungi atunci când apelezi o metodă cu sintaxa `.nume_metoda()`. Acum să discutăm ce face această linie.

După cum am menționat mai devreme, `read_line` introduce ceea ce introduce utilizatorul în string-ul pe care îl transmitem, dar returnează și o valoare de tip `Result`. [`Result`][result]<!-- ignore --> este o [*enumerare*][enums]<!-- ignore -->, adesea numită și *enum*, care este un tip care poate fi într-una din multiple stări posibile. Fiecare stare posibilă o numim *variantă*.

[Capitolul 6][enums]<!-- ignore --> va acoperi enumerările în mai mult detaliu. Scopul acestor tipuri `Result` este de a codifica informațiile de gestionare a erorilor.

Variantele `Result` sunt `Ok` și `Err`. Varianta `Ok` indică faptul că operațiunea a fost reușită, iar în interiorul `Ok` se află valoarea generată cu succes. Varianta `Err` înseamnă că operațiunea a eșuat, iar `Err` conține informații despre cum sau de ce a eșuat operațiunea.

Valorile de tip `Result`, ca și valorile de orice alt tip, au metode definite asupra lor. O instanță a `Result` are o metodă [`expect`][expect]<!-- ignore --> pe care o poți apela. Dacă această instanță a `Result` este o valoare `Err`, `expect` va provoca căderea programului și afișarea mesajului pe care l-ai transmis ca argument către `expect`. Dacă metoda `read_line` întoarce o `Err`, ar fi probabil rezultatul unei erori provenite de la sistemul de operare de baza. Dacă această instanță a `Result` este o valoare `Ok`, `expect` va prelua valoarea de return pe care `Ok` o deține și îți va returna doar acea valoare pentru a o putea folosi. În acest caz, acea valoare este numărul de octeți în intrarea utilizatorului.

Dacă nu apelezi `expect`, programul se va compila, dar vei primi un avertisment:

```console
{{#include ../listings/ch02-guessing-game-tutorial/no-listing-02-without-expect/output.txt}}
```

Rust avertizează că nu ai folosit valoarea `Result` returnată de `read_line`, indicând faptul că programul nu a gestionat o posibilă eroare.

Modul corect de a suprima avertismentul este de a scrie într-adevăr cod de gestionare a erorilor, dar în cazul nostru dorim doar să prăbușim acest program atunci când apare o problemă, așa că putem folosi `expect`. Vei învăța despre recuperarea din erori în [Capitolul 9][recover]<!-- ignore -->.

### Afișarea valorilor cu substituții `println!`

Afară de acolada de închidere, nu ne-a mai rămas decât un singur rând de discutat din codul de până acum:

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-01/src/main.rs:print_guess}}
```

Acest rând afișează șirul de caractere care conține acum intrarea utilizatorului. Setul de acolade `{}` este un substituent: consideră `{}` ca fiind niște clești de crab care țin o valoare pe loc. La afișarea valorii unei variabile, numele variabilei poate intra în acolade. La afișarea rezultatului evaluării unei expresii, plasați acoladele goale în string-ul de format, apoi urmați string-ul de format cu o listă separată prin virgulă cu expresii care trebuie afișate în fiecare substituent de acolade goale, în aceeași ordine. Afișarea unei variabile și a rezultatului unei expresii într-un singur apel către `println!` ar arăta astfel:

```rust
let x = 5;
let y = 10;

println!("x = {x} and y + 2 = {}", y + 2);
```

Acest cod ar afișa `x = 5 and y + 2 = 12`.

### Testarea primei părți

Să testăm prima parte a jocului de ghicit. Rulează-l folosind `cargo run`:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-01/
cargo clean
cargo run
input 6 -->

```console
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 6.44s
     Running `target/debug/guessing_game`
Guess the number!
Please input your guess.
6
You guessed: 6
```

Până în acest punct, prima parte a jocului este gata: noi primim input de la tastatură și apoi îl afișăm.

## Generarea unui număr secret

În continuare, trebuie să generăm un număr secret pe care utilizatorul va încerca să îl ghicească. Numărul secret ar trebui să fie diferit de fiecare dată pentru ca jocul să fie distractiv de jucat de mai multe ori. Vom folosi un număr aleatoriu între 1 și 100 astfel încât jocul să nu fie prea dificil. Rust nu include încă funcționalitatea numerelor aleatorii în biblioteca sa standard. Cu toate acestea, echipa Rust oferă un [crate `rand`][randcrate] cu această funcționalitate.

### Utilizarea unui crate pentru a obține mai multă funcționalitate

Este important să ținem minte că un crate este o colecție de fișiere sursă Rust. Proiectul nostru este un *crate binar*, adică un executabil. În contrast, crate-ul `rand` este un *crate de bibliotecă*, conținând cod destinat să fie utilizat în cadrul altor programe și care nu poate fi executat de sine stătător.

Capacitatea lui Cargo de a coordona crate-uri externe este aspectul în care Cargo se evidențiază cu adevărat. Pentru a putea scrie cod ce folosește `rand`, este necesar să facem o ajustare în fișierul *Cargo.toml*, incluzând crate-ul `rand` între dependențe. Deschide fișierul chiar acum și adaugă la partea de jos următoarea linie, dedesubtul secțiunii `[dependencies]` pe care Cargo a generat-o automat pentru tine. E vital să specifici `rand` exact cum e indicat aici, cu această versiune, deoarece în caz contrar exemplele de cod din acest tutorial pot să nu funcționeze normal:

<!-- When updating the version of `rand` used, also update the version of
`rand` used in these files so they all match:
* ch07-04-bringing-paths-into-scope-with-the-use-keyword.md
* ch14-03-cargo-workspaces.md
-->

<span class="filename">Numele fișierului: Cargo.toml</span>

```toml
{{#include ../listings/ch02-guessing-game-tutorial/listing-02-02/Cargo.toml:8:}}
```

În fișierul *Cargo.toml*, tot ce se află după un antet aparține acelei secțiuni care continuă până când o altă secțiune începe. În `[dependencies]` indicăm lui Cargo care crate-uri externe sunt necesare proiectului tău și ce versiuni ale acestor crate-uri trebuie utilizate. În acest caz, specificăm crate-ul `rand` cu specificatorul de versiune semantică `0.8.5`. Cargo cunoaște [Versionarea semantică][semver]<!-- ignore --> (adesea numit *SemVer*), care e un standard pentru a scrie numerele de versiune. Specificantul `0.8.5` este de fapt o scurtătură pentru `^0.8.5`, ceea ce înseamnă orice versiune cel puțin 0.8.5 dar mai mică de 0.9.0.

Cargo consideră aceste versiuni ca având API-uri publice compatibile cu versiunea 0.8.5, iar această specificare garantează că vei obține cea mai recentă versiune cu patch-uri compatibile care vor compila corect cu codul din acest capitol. Nu este garantat ca versiunile 0.9.0 sau mai mari să păstreze același API ca exemplele utilizate aici.

Acum, fără a modifica vreun cod, să construim proiectul, așa cum este ilustrat în Listarea 2-2.

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-02/
rm Cargo.lock
cargo clean
cargo build -->

<Listing number="2-2" caption="The output from running `cargo build` after adding the `rand` crate as a dependency">

```console
$ cargo build
  Updating crates.io index
   Locking 15 packages to latest Rust 1.85.0 compatible versions
    Adding rand v0.8.5 (available: v0.9.0)
 Compiling proc-macro2 v1.0.93
 Compiling unicode-ident v1.0.17
 Compiling libc v0.2.170
 Compiling cfg-if v1.0.0
 Compiling byteorder v1.5.0
 Compiling getrandom v0.2.15
 Compiling rand_core v0.6.4
 Compiling quote v1.0.38
 Compiling syn v2.0.98
 Compiling zerocopy-derive v0.7.35
 Compiling zerocopy v0.7.35
 Compiling ppv-lite86 v0.2.20
 Compiling rand_chacha v0.3.1
 Compiling rand v0.8.5
 Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
  Finished `dev` profile [unoptimized + debuginfo] target(s) in 2.48s
```

<span class="caption">Listarea 2-2: Afișajul rezultat după executarea `cargo build` în urma adăugării crate-ului rand ca dependență</span>

Poți întâlni numere de versiuni diferite (dar toate vor fi compatibile cu codul, datorită SemVer!) și linii diferite (care vor varia în funcție de sistemul de operare), iar ordinea liniilor poate fi diferită.

Atunci când introducem o dependență externă, Cargo caută și descarcă versiunile cele mai recente ale tuturor elementelor necesare acelei dependențe din *registru*, o copie a datelor de pe [Crates.io][cratesio]. Crates.io este platforma unde comunitatea Rust își publică proiectele Rust open source, disponibile pentru folosirea de către toți.

Cargo verifică secțiunea `[dependencies]` după ce actualizează registrul și descarcă crate-urile enumerate ce nu au fost încă descărcate. Deși am specificat doar `rand` ca dependență, Cargo a descărcat și alte crate-uri de care `rand` are nevoie pentru funcționarea sa. Odată ce crate-urile sunt descărcate, Rust le compilează, și apoi compilarea proiectului nostru are loc cu aceste dependențe incluse.

Dacă rulezi `cargo build` din nou imediat, fără a modifica ceva, nu vei obține niciun afișaj în afară de linia `Finished`. Cargo știe că a descărcat și compilat deja dependențele și că tu nu ai modificat nimic în fișierul *Cargo.toml*. De asemenea, Cargo înțelege că nici codul tău nu a fost schimbat, așadar nu recompilează nimic. Neavând ce să facă, se închide simplu.

Dacă ești în *src/main.rs*, faci o mică schimbare, salvezi și compilezi din nou, vei observa doar două linii de afișaj:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-02/
touch src/main.rs
cargo build -->

```console
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.13s
```

Aceste linii arată că Cargo actualizează build-ul doar cu micuța ta modificare la fișierul *src/main.rs*. Dependențele tale nu s-au schimbat, așa că Cargo știe că poate reutiliza ceea ce deja a descărcat și compilat pentru acestea.

#### Asigurarea compilărilor reproductibile cu fișierul *Cargo.lock*

Cargo are un mecanism care garantează că poți reconstrui același artefact de fiecare dată când tu sau altcineva compilați codul: Cargo va utiliza doar versiunile specificate de dependențe, până nu decizi altceva. De exemplu, presupunem că săptămâna viitoare va fi lansată versiunea 0.8.6 a crate-ului `rand` și că aceasta include o reparație critică de bug, dar totodată și o regresie care îți va afecta codul. Pentru a gestiona aceasta, Rust generează fișierul *Cargo.lock* prima oară când execuți `cargo build`, deci acum îl avem în directoriul *guessing_game*.

La prima compilare a proiectului, Cargo determină toate versiunile compatibile pentru dependențe și le înscrie în fișierul *Cargo.lock*. La compilările ulterioare, Cargo va recunoaște prezența fișierului *Cargo.lock* și va folosi versiunile înregistrate acolo, evitând astfel munca repetitivă de selecție a versiunilor. Astfel, construcția proiectului tău devine reproductibilă automat. În alte cuvinte, proiectul va rămâne la versiunea 0.8.5 până când alegi explicit să faci o actualizare, datorită existenței fișierului *Cargo.lock*. Fiind esențial pentru reproduceri consecvente, fișierul *Cargo.lock* este adesea inclus în controlul de versiune alături de restul codului proiectului tău.

#### Actualizarea unui crate pentru a obține o versiune nouă

Atunci când dorești să actualizezi un crate, Cargo pune la dispoziție comanda `update`, care va ignora fișierul *Cargo.lock* și va determina cele mai recente versiuni ce se potrivesc specificațiilor din *Cargo.toml*. Cargo va înregistra aceste versiuni în fișierul *Cargo.lock*. Implicit, Cargo caută versiuni care sunt mai mari decât 0.8.5 și mai mici de 0.9.0. Dacă crate-ul `rand` a introdus două noi versiuni, 0.8.6 și 0.9.0, ai vedea următorul rezultat dacă ai executa `cargo update`:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-02/
cargo update
assuming there is a new 0.8.x version of rand; otherwise use another update
as a guide to creating the hypothetical output shown here -->

```console
$ cargo update
    Updating crates.io index
     Locking 1 package to latest Rust 1.85.0 compatible version
    Updating rand v0.8.5 -> v0.8.6 (available: v0.999.0)
```

Cargo va ignora lansarea versiunii 0.9.0. De asemenea, ai remarca o modificare în fișierul tău *Cargo.lock*, care arată că acum folosești versiunea 0.8.6 a crate-ului `rand`. Pentru a utiliza versiunea `rand` 0.9.0 sau orice altă versiune din seria 0.9.*x*, trebuie să actualizezi fisierul *Cargo.toml* astfel:

```toml
[dependencies]
rand = "0.999.0"
```


Data următoare când rulezi `cargo build`, Cargo va actualiza lista de crate-uri disponibile și va reevalua cerința ta pentru `rand` în funcție de noua versiune pe care ai specificat-o.

Există multe alte lucruri de spus despre [Cargo][doccargo]<!-- ignore --> și [ecosistemul său][doccratesio]<!-- ignore -->, pe care le vom discuta în Capitolul 14. Până acum, aceste informații sunt tot ce trebuie să știi. Cargo facilitează în mare măsură reutilizarea bibliotecilor, ceea ce permite programatorilor Rust să creeze proiecte mai compacte, compuse din diverse pachete.

### Generarea unui număr aleatoriu

Să începem folosirea bibliotecii `rand` pentru a genera un număr de ghicit. Următorul pas este să actualizăm fișierul *src/main.rs*, așa cum se arată în Listarea 2-3.

<span class="filename">Numele fișierului: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-03/src/main.rs:all}}
```

<span class="caption">Listarea 2-3: Adăugarea de cod pentru a genera un număr aleatoriu</span>

În primul rând, adăugăm linia `use rand::Rng;`. Trăsătura `Rng` definește metodele pe care le implementează generatorii de numere aleatorii și trebuie să fie în domeniul de vizibilitate pentru a folosi acele metode. Trăsăturile vor fi explicate în detaliu în Capitolul 10.

Următoarea parte implică adăugarea a două linii noi în cod. În prima linie apelăm funcția `rand::thread_rng`, care ne oferă generatorul de numere aleatorii specific firului de execuție curent și care este inițiat de sistemul de operare. Apoi utilizăm metoda `gen_range` de la acel generator de numere. Metoda `gen_range`, definită de trăsătura `Rng` adusă în context cu instrucțiunea `use rand::Rng;`, primește o expresie de diapazon și generează un număr aleatoriu în interiorul acelui diapazon. Expresia de diapazon pe care o utilizăm este `start..=end`, care este inclusivă pentru ambele limite, deci specificăm `1..=100` pentru a obține un număr între 1 și 100.

> Notă: Nu vei cunoaște întotdeauna care trăsături trebuie utilizate și ce
> metode și funcții să apelezi de la un crate, prin urmare, fiecare crate vine
> echipat cu propria documentație și instrucțiuni pentru a te ghida în
> utilizarea sa. O funcționalitate practică a Cargo este că executarea comenzii
> `cargo doc --open` va genera documentația furnizată de toate dependențele
> tale local și o va deschide în navigatorul web. Dacă ai curiozitatea de a
> explora alte funcții ale crate-ului `rand`, de exemplu, execută
> `cargo doc --open` și selectează `rand` din bara laterală din partea stângă.

Cea de-a doua linie nouă afișează numărul secret, ceea ce este util pe durata dezvoltării programului pentru a-l putea testa, însă o vom șterge în versiunea finală. Nu se poate spune că este un joc prea incitant dacă programul dezvăluie soluția imediat ce este lansat.

Încearcă să rulezi programul de câteva ori:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-03/
cargo run
4
cargo run
5
-->

```console
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 7
Please input your guess.
4
You guessed: 4

$ cargo run
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.02s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 83
Please input your guess.
5
You guessed: 5
```

Ar trebui să obții numere aleatorii diferite, iar toate ar trebui să fie numere între 1 și 100. Excelentă treabă!

## Compararea ghicirii cu numărul secret

Acum că avem o intrare de la utilizator și un număr aleator, le putem compara. Acest pas este arătat în Listarea 2-4. Reține că acest cod nu se va compila încă, așa cum vom explica.

<span class="filename">Numele fișierului: src/main.rs</span>

```rust,ignore,does_not_compile
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-04/src/main.rs:here}}
```

<span class="caption">Listarea 2-4: Gestionarea posibilelor rezultate ale comparării a două numere</span>

Mai întâi, adăugăm o altă declarație `use`, introducând în scopul nostru un tip numit `std::cmp::Ordering` din biblioteca standard. Tipul `Ordering` este o altă enumerare și are variantele `Less`, `Greater` și `Equal`. Acestea sunt cele trei rezultate posibile când compari două valori.

Apoi, adăugăm cinci linii noi la final care utilizează tipul `Ordering`. Metoda `cmp` compară două valori și poate fi apelată pe orice tip de valori comprabile. E primește o referință la ce se dorește de a fi comparat: aici se face compararea între `guess` și `secret_number`. Apoi returnează o variantă a enumerației `Ordering` pe care am adus-o în scop cu declarația `use`. Folosim o expresie [`match`][match]<!-- ignore --> pentru a decide ce să facem în continuare bazat pe ce variantă a `Ordering` a fost returnată de apelul la `cmp` cu valorile din `guess` și `secret_number`.

O expresie `match` este compusă din *brațe*. Un braț constă dintr-un *model* (numit și pattern) pentru care se face potrivirea, și din codul care ar trebui să ruleze dacă valoarea dată lui `match` se potrivește cu modelul acelui braț. Rust ia valoarea dată lui `match` și o compară cu modelul fiecărui braț pe rând. Modelele și constructul `match` reprezintă caracteristici forte ale lui Rust: îți permit să exprimi o varietate de situații pe care codul tău le-ar putea întâlni și se asigură că le gestionezi pe toate. Aceste caracteristici vor fi acoperite în detaliu în Capitolul 6 și Capitolul 18, respectiv.

Acum să trecem printr-un exemplu cu expresia `match` pe care o folosim aici. Să presupunem că utilizatorul a ghicit numărul 50 și de data aceasta numărul secret generat aleator este 38. 

Atunci când codul compară numărul 50 cu 38, metoda `cmp` va returna `Ordering::Greater`, deoarece 50 este mai mare decât 38. Expresia `match` primește valoarea `Ordering::Greater` și începe să verifice modelul pentru fiecare braț. Analizează primul tipar de braț, `Ordering::Less`, și vede că valoarea `Ordering::Greater` nu se potrivește cu `Ordering::Less`, deci ignoră codul din acel braț și trece la brațul următor. Modelul următorului braț este `Ordering::Greater`, care *se potrivește* cu `Ordering::Greater`! Codul asociat acestui braț va fi executat și va imrima pe ecran `Too big!`. Expresia `match` se încheie după prima potrivire reușită, deci nu se va uita la ultimul braț în acest scenariu.

Totuși, codul din Listarea 2-4 încă nu se va compila. Să încercăm:

<!--
The error numbers in this output should be that of the code **WITHOUT** the
anchor or snip comments
-->

```console
{{#include ../listings/ch02-guessing-game-tutorial/listing-02-04/output.txt}}
```

Esența erorii indică existența unor *tipuri incompatibile*. Rust se bazează pe un sistem de tipuri puternic și tipizat static. În același timp, Rust suportă inferență de tipuri. Atunci când am scris `let mut guess = String::new()`, Rust a inferat că `guess` ar trebui să fie un `String` fără să fie necesar să specificăm tipul. Pe de altă parte, `secret_number` este de un tip numeric. Există mai multe tipuri numerice în Rust care pot avea valori între 1 și 100: `i32`, un număr pe 32 de biți; `u32`, un număr nesemnat pe 32 de biți; `i64`, un număr pe 64 de biți; printre altele. Dacă nu se indică altfel, Rust alege `i32` în mod implicit, care este tipul pentru `secret_number` dacă nu adăugăm informații despre tip în altă parte care ar determina Rust să infereze un alt tip numeric. Eroarea apare pentru că Rust nu poate face comparație între un string și un tip numeric.

Pentru a o rezolva, intenționăm să convertim `String`-ul primit ca input într-un tip numeric real, astfel încât să putem face comparația numerică cu numărul secret. Acest lucru se realizează adăugând următoarea linie în corpul funcției `main`:

<span class="filename">Numele fișierului: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-03-convert-string-to-number/src/main.rs:here}}
```

Linia este:

```rust,ignore
let guess: u32 = guess.trim().parse().expect("Please type a number!");
```

Creăm o variabilă numită `guess`. Dar așteaptă, nu există deja o variabilă cu numele `guess` în program? Da, dar, convenabil, Rust ne permite să umbrim precedentul `guess` cu unul nou. *Umbrirea* ne permite să reutilizăm numele variabilei `guess` în loc să fim obligați să creăm două variabile diferite, cum ar fi `guess_str` și `guess`, de exemplu. Vom detalia acest concept în [Capitolul 3][shadowing]<!-- ignore -->, dar pentru moment, să știi că această funcționalitate este adesea folosită când vrei să convertești o valoare dintr-un tip în altul.

Noua variabilă este asociată expresiei `guess.trim().parse()`. Partea `guess` din cadrul expresiei se referă la variabila originală `guess` care conținea input-ul ca un string. Metoda `trim` pe o instanță `String` va elimina orice spațiu alb (whitespace) de la început și sfârșitul string-ului, lucru necesar pentru a putea compara string-ul cu un `u32`, ce poate conține doar date numerice. Utilizatorul trebuie să apese <span class="keystroke">enter</span> pentru a completa `read_line` și așa să introducă ghicirea sa, adăugând prin asta un caracter de linie nouă la string. De exemplu, dacă utilizatorul scrie <span class="keystroke">5</span> și apasă <span class="keystroke">enter</span>, `guess` arată așa: `5\n`. `\n` reprezintă „newline” (linie nouă). (Pe Windows, apăsarea <span class="keystroke">enter</span> aduce un carriage return și un newline, `\r\n`.) Metoda `trim` înlătură `\n` sau `\r\n`, lăsând doar `5`.

Metoda [`parse` de pe string-uri][parse]<!-- ignore --> transformă un string într-un alt tip. În acest caz, o utilizăm pentru a converti un string într-un număr. Trebuie să specificăm în Rust tipul exact de număr pe care îl dorim, utilizând `let guess: u32`. Două puncte (`:`) care urmează după `guess` indică faptul că vom adnota tipul variabilei. Rust include diferite tipuri de numere; `u32`, pe care îl vedem aici, reprezintă un întreg pozitiv fără semn și de 32 de biți. Este o opțiune predilectă pentru reprezentarea unui număr mic și pozitiv. Despre alte tipuri de numere vei afla în [Capitolul 3][integers]<!-- ignore -->.

De asemenea, prin folosirea adnotării `u32` în acest exemplu și prin comparația cu `secret_number`, Rust va înțelege că și `secret_number` trebuie să fie `u32`. Astfel, comparația se va face între două valori de același tip!

Metoda `parse` este aplicabilă doar caracterelor ce pot fi convertite în mod logic către numere și, prin urmare, este susceptibilă de erori. Dacă, spre exemplu, string-ul ar conţine `A👍%`, nu ar exista nicio modalitate de a-l converti într-un număr. Fiind posibil să eșueze, metoda `parse` returnează un tip `Result`, într-un mod similar cu metoda `read_line` (abordată anterior în [„Tratarea eșecurilor potențiale cu `Result`”](#handling-potential-failure-with-result)<!-- ignore -->). Vom reacționa în fața acestui `Result` în același mod, utilizând din nou metoda `expect`. Dacă `parse` întoarce o variantă de `Err` a tipului `Result`, deoarece nu a putut transforma string-ul într-un număr, apelul `expect` va opri jocul și va tipări mesajul specificat de noi. În situația în care `parse` reușește să convertească string-ul într-un număr cu succes, va returna varianta `Ok` a `Result`, iar metoda `expect` va extrage numărul dorit din valoarea `Ok`.

Să rulăm acum programul:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/no-listing-03-convert-string-to-number/
touch src/main.rs
cargo run
  76
-->

```console
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.26s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 58
Please input your guess.
  76
You guessed: 76
Too big!
```

Foarte bine! Deși au fost adăugate spații înainte de ghicire, programul a reușit totuși să-și dea seama că utilizatorul a ghicit numărul 76. Rulează programul de câteva ori pentru a verifica comportamentul diferit cu diferite tipuri de input: ghicește numărul corect, ghicește un număr care este prea mare sau ghicește un număr care este prea mic.

Acum avem majoritatea jocului funcțional, dar utilizatorul poate face doar o singură ghicire. Să schimbăm asta adăugând o buclă!

## Permiterea multiplelor ghiciri cu bucle

Cuvântul cheie `loop` creează o buclă infinită. Vom adăuga o buclă pentru a oferi utilizatorilor mai multe încercări de a ghici numărul:

<span class="filename">Numele fișierului: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-04-looping/src/main.rs:here}}
```

După cum se poate observa, am mutat tot de la promptul de introducere a ghicirii într-o buclă. Asigură-te că liniile din interiorul buclei sunt indentate cu patru spații suplimentare fiecare și rulează din nou programul. Acum programul va solicita o nouă ghicire la nesfârșit, ceea ce introduce efectiv o nouă problemă: pare că utilizatorul nu are posibilitatea să părăsească programul!

Utilizatorul poate întrerupe întotdeauna programul utilizând combinația de taste <span class="keystroke">ctrl-c</span>. Există însă și o altă cale de a se elibera de acest ciclu infinit, așa cum am menționat în discuția despre `parse` din secțiunea [“Compararea ghicirii cu numărul secret”](#comparing-the-guess-to-the-secret-number)<!--ignore-->: dacă utilizatorul scrie ceva ce nu este un număr, atunci programul va da eroare și se va opri. Putem folosi acest comportament ca o metodă prin care utilizatorul poate opri programul, după cum urmează:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/no-listing-04-looping/
touch src/main.rs
cargo run
(too small guess)
(too big guess)
(correct guess)
quit
-->

```console
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.23s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 59
Please input your guess.
45
You guessed: 45
Too small!
Please input your guess.
60
You guessed: 60
Too big!
Please input your guess.
59
You guessed: 59
You win!
Please input your guess.
adio
thread 'main' panicked at 'Please type a number!: ParseIntError { kind: InvalidDigit }', src/main.rs:28:47
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Dacă introduci `adio`, jocul se va opri, însă vei observa că se va întâmpla același lucru dacă introduci orice alt input care nu e un număr. Aceasta este departe de a fi ideal; ne dorim ca jocul să se încheie și atunci când numărul ghicit este cel corect.

### Terminarea jocului la o ghicire corectă

Să programăm jocul să se termine atunci când utilizatorul câștigă, prin adăugarea unei instrucțiuni `break`:

<span class="filename">Numele fișierului: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/no-listing-05-quitting/src/main.rs:here}}
```

Introducerea liniei `break` imediat după `You win!` determină programul să părăsească bucla atunci când utilizatorul ghicește numărul secret în mod corect. Părăsirea buclei înseamnă de asemenea finalizarea programului, deoarece bucla reprezintă ultima secțiune a funcției `main`.

### Procesarea intrărilor non-valide

Pentru a îmbunătăți comportamentul jocului, în loc de a opri programul când utilizatorul introduce ceva ce nu este un număr, putem configura jocul să ignore acest tip de input, permițând utilizatorului să continue să ghicească. Acest lucru poate fi realizat modificând linia în care valoarea `guess` este convertită din `String` în `u32`, așa cum este ilustrat în Listarea 2-5.

<span class="filename">Numele fișierului: src/main.rs</span>

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-05/src/main.rs:here}}
```

<span class="caption">Listarea 2-5: Ignorarea unui input care nu este un număr și solicitarea unei noi încercări în locul oprii programului</span>

Trecem de la o funcție `expect` la o expresie `match` pentru a gestiona erorile în locul oprii programului. Este important să ne amintim că `parse` returnează un tip `Result` și că `Result` este o enumerare cu variantele `Ok` și `Err`. Folosim o expresie `match`, la fel ca atunci când lucrăm cu `Ordering` rezultatul metodei `cmp`.

Când `parse` poate să convertească în mod eficient string-ul într-un număr, ne întoarce o valoare `Ok` care include numărul rezultat. Această valoare `Ok` se va potrivi cu modelul din primul caz al expresiei `match`, iar ca rezultat, vom primi numărul creat de `parse` și inclus în `Ok`. Numărul va fi pus exact unde trebuie în noua variabilă `guess` pe care o definim.

Dacă `parse` nu poate să convertească string-ul într-un număr, ne va da o valoare `Err` care deține detalii despre eroare. Valoarea `Err` nu se potrivește cu modelul `Ok(num)` din primul caz al `match`, dar se potrivește cu `Err(_)` din cel de-al doilea caz. Folosind `_` ca wildcard, spunem că dorim să captăm orice fel de valoare `Err`, fără a ne preocupa de conținutul acesteia. Programul va rula codul corespunzător celui de-al doilea caz, adică `continue`, care comandă programului să treacă la următoarea iterație a buclei `loop` și să solicite o încercare nouă. Astfel, ignorăm orice posibilă eroare care ar putea apărea în timpul funcției `parse`.

Acum totul în program ar trebui să funcționeze conform așteptărilor. Să încercăm:

<!-- manual-regeneration
cd listings/ch02-guessing-game-tutorial/listing-02-05/
cargo run
(too small guess)
(too big guess)
foo
(correct guess)
-->

```console
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.13s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 61
Please input your guess.
10
You guessed: 10
Too small!
Please input your guess.
99
You guessed: 99
Too big!
Please input your guess.
foo
Please input your guess.
61
You guessed: 61
You win!
```

Minunat! Cu o mică ultimă ajustare, vom termina jocul de ghicit. Amintește-ți că programul încă afișează numărul secret. Acest lucru a funcționat bine pentru testare, dar strică jocul. Să ștergem `println!` care afișează numărul secret. Listarea 2-6 arată codul final.

<Listing number="2-6" file-name="src/main.rs" caption="Complete guessing game code">

```rust,ignore
{{#rustdoc_include ../listings/ch02-guessing-game-tutorial/listing-02-06/src/main.rs}}
```

<span class="caption">Listarea 2-6: Codul complet al jocului de ghicire</span>

La acest moment, ai reușit să construiești cu succes jocul de ghicire. Felicitări!

## Sumar

Acest proiect a fost o modalitate practică de a face cunoștință cu multe concepte noi din Rust: `let`, `match`, funcții, utilizarea crate-urilor externe, și multe altele. În următoarele câteva capitole, vei învăța despre aceste concepte în mai multe detalii. Capitolul 3 acoperă funcționalități pe care majoritatea limbajelor de programare le au, cum ar fi variabile, tipuri de date și funcții, și arată cum să le folosești în Rust. Capitolul 4 explorează posesiunea (ownership), o caracteristică ce distinge Rust de alte limbaje. Capitolul 5 discută despre structuri și sintaxa metodelor, iar Capitolul 6 explică cum funcționează enumerările.

[prelude]: ../std/prelude/index.html
[variables-and-mutability]: ch03-01-variables-and-mutability.html#variables-and-mutability
[comments]: ch03-04-comments.html
[string]: ../std/string/struct.String.html
[iostdin]: ../std/io/struct.Stdin.html
[read_line]: ../std/io/struct.Stdin.html#method.read_line
[result]: ../std/result/enum.Result.html
[enums]: ch06-00-enums.html
[expect]: ../std/result/enum.Result.html#method.expect
[recover]: ch09-02-recoverable-errors-with-result.html
[randcrate]: https://crates.io/crates/rand
[semver]: http://semver.org
[cratesio]: https://crates.io/
[doccargo]: https://doc.rust-lang.org/cargo/
[doccratesio]: https://doc.rust-lang.org/cargo/reference/publishing.html
[match]: ch06-02-match.html
[shadowing]: ch03-01-variables-and-mutability.html#shadowing
[parse]: ../std/primitive.str.html#method.parse
[integers]: ch03-02-data-types.html#integer-types
