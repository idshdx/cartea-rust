<!-- Old headings. Do not remove or links may break. -->

<a id="installing-binaries-from-cratesio-with-cargo-install"></a>

## Instalarea binarelor cu `cargo install`

Comanda `cargo install` îți permite să instalezi și să utiliezi crate-uri binare local. Aceasta nu este gândită să substituie pachetele sistemului; este destinată să fie o metodă comodă pentru dezvoltatorii Rust de a instala uneltele pe care alții le-au pus la dispoziție pe [crates.io](https://crates.io/)<!-- ignore -->. Este important să notezi că se pot instala numai pachetele care conțin target-uri binare. Un *target binar* este programul executabil creat atunci când un crate conține un fișier *src/main.rs* sau un alt fișier desemnat ca binar, spre deosebire de un target de tip librărie, care nu poate fi executat independent, dar poate fi integrat în alte programe. În mod obișnuit, crate-urile includ în fișierul *README* informații despre dacă un crate este o librărie, dacă include un target binar sau dacă are amândouă.

Toate binarele instalate prin intermediul `cargo install` sunt depozitate în directoriul *bin* al rădăcinii de instalare. Dacă ai instalat Rust folosind *rustup.rs* și nu ai configurări personalizate, acest directoriu va fi *$HOME/.cargo/bin*. Pentru a putea executa programele instalate cu `cargo install`, directoriul acesta trebuie să fie inclus în variabila de mediu `$PATH`.

De exemplu, în Capitolul 12 am adus în discuție faptul că există o variantă Rust a instrumentului `grep` numit `ripgrep`, utilizată pentru căutarea în fișiere. Pentru a instala `ripgrep`, executăm următoarea comandă:

<!-- manual-regeneration
cargo install something you don't have, copy relevant output below
-->

```console
$ cargo install ripgrep
    Updating crates.io index
  Downloaded ripgrep v14.1.1
  Downloaded 1 crate (213.6 KB) in 0.40s
  Installing ripgrep v14.1.1
--snip--
   Compiling grep v0.3.2
    Finished `release` profile [optimized + debuginfo] target(s) in 6.73s
  Installing ~/.cargo/bin/rg
   Installed package `ripgrep v14.1.1` (executable `rg`)
```

Penultima linie a afișajului indică locația și numele binarului instalat, care în cazul `ripgrep` este `rg`. Dacă directoriul de instalare este inclus în variabila ta de mediu `$PATH`, cum am menționat anterior, poți apoi folosi comanda `rg --help` și începe să utilizezi un instrument mai eficient și specific limbajului Rust pentru căutarea în fișiere!
