
# [Bitwarden now accepts Proton Pass .json files](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import).
**This is no longer required.**

----

## ~~Convert Proton Pass json to Bitwarden csv~~

~~Converts Proton Pass password export (`.json`) to a a `.csv` that Bitwarden can understand.~~
~~Tested a grand total of once. Works on my machine. Created in Python 3.9.2, *probably* down to 3.6.x, but untested.~~

~~### Known issues:~~
 - ~~No support for multiple URLs, not sure how to put them in the Bitwarden format~~
 - ~~Assumes everything is a login, because I only had logins in PP. If you have aliases and notes in there, they will *try* to import as Logins and the program will probably just throw an exception~~
 - ~~Bitwarden seems to only take the TOTP key, so this program ignores the other TOTP information (algo, length, source... anything except the secret key)~~
 - ~~I coded this at like 2am so there's not exactly comments galore.~~
 - ~~Limited error handling~~

### ~~Instructions~~

~~Run `protonpass_json_to_bitwarden_csv.py` in the same folder as your `data.json` (which you will need to pull out of the `.zip`). Ideally launch using `-i` to catch any crashes.~~
