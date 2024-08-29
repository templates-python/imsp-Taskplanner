# Starten   

## Installation
Installiere die benötigten Pakete mit `pip`:
```bash
pip install -r requirements.txt
```

Erstelle ein lokales `.env` File mit den folgenden Variablen:
```bash
SECRET_KEY=your_secret_key
```
Best Practices für den `SECRET_KEY`

1. Verwende einen langen und zufälligen Schlüssel
Der `SECRET_KEY` sollte eine ausreichend lange und zufällige Zeichenfolge sein, um sicherzustellen, dass er schwer zu erraten ist. Idealerweise sollte der Schlüssel mindestens 50 Zeichen lang sein und eine Kombination aus Buchstaben, Zahlen und Sonderzeichen enthalten.

3. Erstelle den Schlüssel sicher
Verwende sichere Methoden zur Erstellung des `SECRET_KEY`, wie zum Beispiel die Python-Funktion `secrets.token_urlsafe(50)`:

```python
import secrets

secret_key = secrets.token_urlsafe(50)
print(secret_key)
```

## Ausführen
Starte die Applikation über die Flask CLI:
```bash 
flask run
```
Um mehr Ausgaben zu erhalten, aktiviere den debug mode:
```bash
flask run --debugger --reload
```

Oder via run.py einfach starten.
