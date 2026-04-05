# ═══════════════════════════════════════════════════════════════════════════
# DEUTSCH B1 — 5 vollständige Übungstests
# Je Test: 20 MC (Teil 1) + 10 Richtig/Falsch (Teil 2) + 15 Textauswahl (Teil 3)
# Gesamt: 225 einzigartige Fragen
# Grammatik geprüft nach Duden und Goethe-Institut B1-Standard
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# TEST 1 — Thema: Alltag & Grundgrammatik
# ───────────────────────────────────────────────────────────────────────────
TEST1 = [

  # ── Teil 1: Multiple Choice ──────────────────────────────────────────────
  {
    "id":101,"test":1,"teil":1,"type":"mc",
    "question":"Was bedeutet 'die Veranstaltung'?",
    "options":["Ein Gebäude","Ein organisiertes Event oder eine Feier","Ein Nahrungsmittel"],
    "correct":1,
    "explanation":"'Veranstaltung' bezeichnet ein geplantes, öffentliches oder privates Ereignis."
  },
  {
    "id":102,"test":1,"teil":1,"type":"mc",
    "question":"Maria arbeitet seit drei Jahren als Lehrerin. Was drückt 'seit' aus?",
    "options":["Einen Zeitpunkt in der Vergangenheit, der bis heute andauert","Eine Handlung, die kurz dauerte","Eine Handlung in der Zukunft"],
    "correct":0,
    "explanation":"'Seit' + Präsens beschreibt etwas, das in der Vergangenheit begann und noch andauert."
  },
  {
    "id":103,"test":1,"teil":1,"type":"mc",
    "question":"Welcher Satz ist grammatikalisch richtig?",
    "options":["Ich habe gestern ins Kino gegangen.","Ich bin gestern ins Kino gegangen.","Ich hatte gestern ins Kino gegangen."],
    "correct":1,
    "explanation":"Bewegungsverben wie 'gehen' bilden das Perfekt mit dem Hilfsverb 'sein'."
  },
  {
    "id":104,"test":1,"teil":1,"type":"mc",
    "question":"Er liest _____ Anzeige in der Zeitung.",
    "options":["ein","eine","einen"],
    "correct":1,
    "explanation":"'Anzeige' ist feminin. Im Akkusativ lautet der unbestimmte Artikel 'eine'."
  },
  {
    "id":105,"test":1,"teil":1,"type":"mc",
    "question":"Wie formuliert man höflich: 'Kannst du mir helfen?'",
    "options":["Hilf mir sofort!","Könntest du mir bitte helfen?","Du musst mir jetzt helfen."],
    "correct":1,
    "explanation":"Der Konjunktiv II ('könntest') macht Bitten höflicher und indirekter."
  },
  {
    "id":106,"test":1,"teil":1,"type":"mc",
    "question":"Der Zug hat _____ Verspätung. Er kommt 20 Minuten später.",
    "options":["eine","einen","ein"],
    "correct":0,
    "explanation":"'Verspätung' ist feminin. Im Akkusativ: 'eine Verspätung'."
  },
  {
    "id":107,"test":1,"teil":1,"type":"mc",
    "question":"Was bedeutet 'sich beschweren'?",
    "options":["Sich entspannen","Seine Unzufriedenheit äußern","Etwas genießen"],
    "correct":1,
    "explanation":"'Sich beschweren' bedeutet, gegenüber jemandem Unmut oder Kritik zu äußern."
  },
  {
    "id":108,"test":1,"teil":1,"type":"mc",
    "question":"'Ich freue mich _____ das Wochenende.' Welche Präposition passt?",
    "options":["für","auf","über"],
    "correct":1,
    "explanation":"'Sich freuen auf' + Akkusativ drückt Vorfreude auf etwas Zukünftiges aus."
  },
  {
    "id":109,"test":1,"teil":1,"type":"mc",
    "question":"Lisa hat ihre Tasche verloren. Was soll sie zuerst tun?",
    "options":["Eine neue Tasche kaufen","Das Fundbüro anrufen","Nach Hause gehen"],
    "correct":1,
    "explanation":"Das Fundbüro (lost-and-found office) ist die erste Anlaufstelle bei verlorenen Gegenständen."
  },
  {
    "id":110,"test":1,"teil":1,"type":"mc",
    "question":"'Er hat die Prüfung nicht bestanden, _____ er viel gelernt hatte.'",
    "options":["weil","obwohl","damit"],
    "correct":1,
    "explanation":"'Obwohl' leitet einen konzessiven Nebensatz ein: trotz des Lernens kein Erfolg."
  },
  {
    "id":111,"test":1,"teil":1,"type":"mc",
    "question":"Was ist ein 'Bewerbungsschreiben'?",
    "options":["Ein Beschwerdebrief an eine Behörde","Ein Motivationsschreiben für eine Arbeitsstelle","Eine Einladung zu einem Vorstellungsgespräch"],
    "correct":1,
    "explanation":"Ein Bewerbungsschreiben erklärt, warum man für eine Stelle geeignet ist."
  },
  {
    "id":112,"test":1,"teil":1,"type":"mc",
    "question":"Was drückt der Ausruf 'Das gibt es doch nicht!' aus?",
    "options":["Zustimmung","Überraschung oder Unglaube","Ablehnung"],
    "correct":1,
    "explanation":"Dieser Ausruf drückt Staunen oder Überraschung über etwas Unerwartetes aus."
  },
  {
    "id":113,"test":1,"teil":1,"type":"mc",
    "question":"'Wenn ich mehr Zeit _____, würde ich mehr reisen.' Welche Form ist korrekt?",
    "options":["habe","hätte","haben werde"],
    "correct":1,
    "explanation":"Konjunktiv II ('hätte') drückt eine irreale Bedingung in der Gegenwart aus."
  },
  {
    "id":114,"test":1,"teil":1,"type":"mc",
    "question":"'Familie Müller zieht nächsten Monat um.' Was bedeutet 'umziehen'?",
    "options":["In den Urlaub fahren","Den Wohnsitz wechseln","Neue Möbel kaufen"],
    "correct":1,
    "explanation":"'Umziehen' (trennbar: zieht um) bedeutet, in eine andere Wohnung oder ein anderes Haus zu wechseln."
  },
  {
    "id":115,"test":1,"teil":1,"type":"mc",
    "question":"Was drückt 'obwohl' in einem Satz aus?",
    "options":["Einen Grund","Einen Gegensatz (trotz eines Hindernisses)","Ein Ziel"],
    "correct":1,
    "explanation":"'Obwohl' ist eine konzessive Konjunktion: etwas passiert trotz eines Hindernisses."
  },
  {
    "id":116,"test":1,"teil":1,"type":"mc",
    "question":"'Sie geht _____ Arzt.' Welche Formulierung ist korrekt?",
    "options":["in den","zu dem","zum"],
    "correct":2,
    "explanation":"'Zum Arzt gehen' (zu + dem = zum) ist die feste, idiomatische Formulierung auf Deutsch."
  },
  {
    "id":117,"test":1,"teil":1,"type":"mc",
    "question":"Was bedeutet 'pünktlich'?",
    "options":["Zu spät erscheinen","Genau zur vereinbarten Zeit erscheinen","Sehr schnell arbeiten"],
    "correct":1,
    "explanation":"'Pünktlich' bedeutet, zur exakt abgemachten Zeit zu erscheinen — weder zu früh noch zu spät."
  },
  {
    "id":118,"test":1,"teil":1,"type":"mc",
    "question":"'Gestern _____ ich meinen alten Freund zufällig _____.' Perfekt korrekt?",
    "options":["habe … getroffen","habe getroffen …","getroffen … habe"],
    "correct":0,
    "explanation":"Perfektstruktur: Hilfsverb (habe) an Position 2, Partizip II (getroffen) am Satzende."
  },
  {
    "id":119,"test":1,"teil":1,"type":"mc",
    "question":"Was enthält ein 'Lebenslauf'?",
    "options":["Eine persönliche Lebensgeschichte","Berufliche Erfahrungen und persönliche Daten","Einen Reisebericht"],
    "correct":1,
    "explanation":"Ein Lebenslauf (CV/Résumé) listet Ausbildung, Berufserfahrung und Kontaktdaten auf."
  },
  {
    "id":120,"test":1,"teil":1,"type":"mc",
    "question":"'Er arbeitet fleißig, _____ er sehr müde ist.' Welches Wort passt?",
    "options":["weil","obwohl","wenn"],
    "correct":1,
    "explanation":"'Obwohl' leitet einen Konzessivsatz ein: trotz der Müdigkeit wird weitergearbeitet."
  },

  # ── Teil 2: Richtig / Falsch ──────────────────────────────────────────────
  {
    "id":121,"test":1,"teil":2,"type":"rf",
    "context":"E-Mail von Sophie:\n\nLiebe Anna,\nleider kann ich am Freitag nicht zu deiner Party kommen. Ich muss arbeiten. Tut mir wirklich leid! Können wir uns vielleicht nächste Woche treffen?\nViele Grüße, Sophie",
    "question":"Sophie kann nicht zur Party kommen, weil sie krank ist.",
    "correct":False,
    "explanation":"Falsch. Im Text steht: 'Ich muss arbeiten.' — Krankheit wird nicht erwähnt."
  },
  {
    "id":122,"test":1,"teil":2,"type":"rf",
    "context":"(Gleicher Text wie Aufgabe 121)",
    "question":"Sophie schlägt vor, sich nächste Woche zu treffen.",
    "correct":True,
    "explanation":"Richtig. Sophie fragt: 'Können wir uns vielleicht nächste Woche treffen?'"
  },
  {
    "id":123,"test":1,"teil":2,"type":"rf",
    "context":"Ansage im Supermarkt:\n\nAchtung liebe Kunden! Unsere Bäckerei schließt heute um 18:00 Uhr. Die Kasse bleibt bis 20:00 Uhr geöffnet. Wir bitten um Ihr Verständnis.",
    "question":"Der gesamte Supermarkt schließt um 18:00 Uhr.",
    "correct":False,
    "explanation":"Falsch. Nur die Bäckerei schließt um 18 Uhr. Die Kasse bleibt bis 20 Uhr geöffnet."
  },
  {
    "id":124,"test":1,"teil":2,"type":"rf",
    "context":"(Gleicher Text wie Aufgabe 123)",
    "question":"Die Kasse ist bis 20:00 Uhr geöffnet.",
    "correct":True,
    "explanation":"Richtig. Die Ansage sagt ausdrücklich: 'Die Kasse bleibt bis 20:00 Uhr geöffnet.'"
  },
  {
    "id":125,"test":1,"teil":2,"type":"rf",
    "context":"Notiz von Klaus:\n\nHeute Abend komme ich gegen 22 Uhr nach Hause. Bitte warte nicht mit dem Essen auf mich. Im Kühlschrank ist Suppe für mich.\nKuss, Klaus",
    "question":"Klaus möchte, dass jemand mit dem Essen auf ihn wartet.",
    "correct":False,
    "explanation":"Falsch. Klaus schreibt ausdrücklich: 'Bitte warte nicht mit dem Essen auf mich.'"
  },
  {
    "id":126,"test":1,"teil":2,"type":"rf",
    "context":"(Gleicher Text wie Aufgabe 125)",
    "question":"Für Klaus ist Essen im Kühlschrank.",
    "correct":True,
    "explanation":"Richtig. Klaus schreibt: 'Im Kühlschrank ist Suppe für mich.'"
  },
  {
    "id":127,"test":1,"teil":2,"type":"rf",
    "context":"Mitteilung der Sprachschule:\n\nDer Kurs Deutsch B1 beginnt am 5. März. Kursgebühr: 250 Euro. Anmeldungen sind ausschließlich online möglich. Telefonische Anfragen werden leider nicht bearbeitet — bitte per E-Mail.",
    "question":"Man kann sich für den Kurs telefonisch anmelden.",
    "correct":False,
    "explanation":"Falsch. Die Anmeldung ist 'ausschließlich online möglich'. Telefonische Anfragen werden nicht bearbeitet."
  },
  {
    "id":128,"test":1,"teil":2,"type":"rf",
    "context":"(Gleicher Text wie Aufgabe 127)",
    "question":"Die Kursgebühr beträgt 250 Euro.",
    "correct":True,
    "explanation":"Richtig. Im Text steht: 'Kursgebühr: 250 Euro.'"
  },
  {
    "id":129,"test":1,"teil":2,"type":"rf",
    "context":"Pressemitteilung:\n\nLaut einer neuen Studie sind 72 Prozent der Deutschen regelmäßig körperlich aktiv. Besonders beliebt sind Radfahren und Schwimmen. Nur 28 Prozent der Befragten treiben gar keinen Sport.",
    "question":"Mehr als die Hälfte der Befragten macht keinen Sport.",
    "correct":False,
    "explanation":"Falsch. Nur 28 Prozent machen keinen Sport. Die Mehrheit (72 %) ist aktiv."
  },
  {
    "id":130,"test":1,"teil":2,"type":"rf",
    "context":"(Gleicher Text wie Aufgabe 129)",
    "question":"Schwimmen ist laut der Studie eine beliebte Sportart.",
    "correct":True,
    "explanation":"Richtig. Schwimmen wird ausdrücklich als eine der besonders beliebten Sportarten genannt."
  },

  # ── Teil 3: Leseverstehen / Textauswahl ──────────────────────────────────
  {
    "id":131,"test":1,"teil":3,"type":"text",
    "context":"TEXT A — Homeoffice\nDas Arbeiten von zu Hause hat stark zugenommen. Viele Arbeitnehmer schätzen die Flexibilität, weil sie ihren Tag selbstständiger planen und lange Arbeitswege sparen können. Gleichzeitig berichten manche von Einsamkeit, fehlendem Austausch im Team und Schwierigkeiten, Beruf und Privatleben klar zu trennen. Viele Firmen testen deshalb Modelle, bei denen sich Büro- und Heimarbeit abwechseln.\n\nTEXT B — Urlaub in den Alpen\nIm Sommer fahren viele Deutsche in die Alpen, um dort zu wandern, Rad zu fahren oder einfach frische Luft zu genießen. Die Region lockt mit klaren Seen, gut ausgeschilderten Wanderwegen und traditionellen Gasthäusern. Besonders Bayern und Tirol profitieren vom Tourismus. In beliebten Ferienorten sind Hotels und Ferienwohnungen oft schon lange vor Beginn der Saison ausgebucht.\n\nTEXT C — Digitale Bezahlmethoden\nBargeld wird in Deutschland immer seltener eingesetzt, vor allem in Großstädten und im Online-Handel. Viele Menschen zahlen heute mit Karte, Smartphone oder Smartwatch, weil das schneller und bequemer ist. Banken und Geschäfte investieren stark in kontaktlose Technik. Experten gehen davon aus, dass Bargeld in einigen Jahren nur noch in bestimmten Situationen eine größere Rolle spielen wird.",
    "question":"In welchem Text geht es um Veränderungen beim Bezahlen?",
    "options":["Text A","Text B","Text C"],
    "correct":2,
    "explanation":"Text C behandelt den Rückgang von Bargeld und den Aufstieg digitaler Zahlungsmethoden."
  },
  {
    "id":132,"test":1,"teil":3,"type":"text",
    "context":"(Gleiche Texte A, B, C wie Aufgabe 131)",
    "question":"Welcher Text erwähnt negative Auswirkungen einer modernen Arbeitsform?",
    "options":["Text A — Einsamkeit im Homeoffice","Text B — Probleme in den Bergen","Text C — Risiken beim Bezahlen"],
    "correct":0,
    "explanation":"Text A erwähnt Einsamkeit und fehlenden Kollegenkontakt als Nachteile des Homeoffice."
  },
  {
    "id":133,"test":1,"teil":3,"type":"text",
    "context":"(Gleiche Texte A, B, C wie Aufgabe 131)",
    "question":"In welchem Text wird ein Urlaubsziel in der Natur beschrieben?",
    "options":["Text A","Text B — Alpen und Wandern","Text C"],
    "correct":1,
    "explanation":"Text B beschreibt die Alpen als beliebtes Urlaubsziel mit Natur und Wanderwegen."
  },
  {
    "id":134,"test":1,"teil":3,"type":"text",
    "context":"TEXT D — Gesunde Ernährung\nImmer mehr Menschen achten bewusst auf ihre Ernährung und informieren sich über Herkunft, Inhaltsstoffe und Herstellung von Lebensmitteln. Bio-Produkte sind gefragt, vegane Gerichte finden sich heute selbst in kleinen Kantinen. Gleichzeitig bleiben traditionelle Fleischgerichte besonders bei älteren Generationen beliebt. Ernährungsberater beobachten deshalb, dass sich Essgewohnheiten je nach Alter, Lebensstil und sozialem Umfeld deutlich unterscheiden können.\n\nTEXT E — Öffentlicher Nahverkehr\nDie Bundesregierung investiert Milliarden in den Ausbau des Nahverkehrs, um Städte zu entlasten und klimafreundliche Mobilität zu fördern. Das 49-Euro-Ticket war ein großer Erfolg und wurde von Millionen Menschen für den Weg zur Arbeit, zur Schule oder in der Freizeit genutzt. Viele Verkehrsverbünde melden steigende Fahrgastzahlen. Kritiker fordern trotzdem pünktlichere Verbindungen und bessere Angebote im ländlichen Raum.\n\nTEXT F — Lernen als Erwachsener\nErwachsene lernen anders als Kinder, weil sie neues Wissen meist mit konkreten Zielen und Alltagssituationen verbinden möchten. Reine Theorie reicht oft nicht aus; praktische Anwendung und Wiederholung sind entscheidend. Experten empfehlen, täglich mindestens 20 Minuten konzentriert zu üben und kleine Lernschritte fest einzuplanen. Wer regelmäßig dranbleibt, erzielt meist deutlich bessere Fortschritte als mit seltenen, langen Lerneinheiten.",
    "question":"Welcher Text beschreibt ein günstiges Mobilitätsangebot?",
    "options":["Text D","Text E — 49-Euro-Ticket","Text F"],
    "correct":1,
    "explanation":"Text E beschreibt das 49-Euro-Ticket als günstiges und erfolgreiches Nahverkehrsangebot."
  },
  {
    "id":135,"test":1,"teil":3,"type":"text",
    "context":"(Gleiche Texte D, E, F wie Aufgabe 134)",
    "question":"Welcher Text beschreibt Unterschiede im Essverhalten zwischen Generationen?",
    "options":["Text D — Fleisch vs. vegan","Text E","Text F"],
    "correct":0,
    "explanation":"Text D erwähnt, dass jüngere Menschen veganer essen, ältere häufiger Fleisch."
  },
  {
    "id":136,"test":1,"teil":3,"type":"text",
    "context":"(Gleiche Texte D, E, F wie Aufgabe 134)",
    "question":"Welcher Text gibt eine konkrete Empfehlung für regelmäßiges Lernen?",
    "options":["Text D","Text E","Text F — 20 Minuten täglich"],
    "correct":2,
    "explanation":"Text F empfiehlt ausdrücklich, täglich mindestens 20 Minuten zu üben."
  },
  {
    "id":137,"test":1,"teil":3,"type":"text",
    "context":"TEXT G — Wohnungsmarkt in Großstädten\nIn München, Berlin und Hamburg steigen die Mieten seit Jahren stark an, obwohl ständig neue Wohnungen gebaut werden. Besonders für Studenten, Auszubildende und junge Berufstätige wird es immer schwieriger, eine eigene Wohnung zu finden. Viele weichen deshalb auf Wohngemeinschaften oder kleinere Wohnungen am Stadtrand aus. Sozialverbände fordern mehr bezahlbaren Wohnraum und strengere Regeln gegen Spekulation.\n\nTEXT H — Klimawandel und Extremwetter\nHitzewellen, Überschwemmungen und heftige Stürme treten in Deutschland häufiger auf als noch vor einigen Jahrzehnten. Wissenschaftler sehen darin deutliche Folgen des Klimawandels und warnen vor erheblichen Risiken für Städte, Landwirtschaft und Gesundheit. Ohne eine schnelle Reduktion von CO₂-Emissionen könnten Schäden und Kosten weiter steigen. Auch Versicherungen rechnen mit mehr Extremereignissen und höheren Belastungen für viele Haushalte.\n\nTEXT I — Soziale Medien und Jugendliche\nJugendliche verbringen täglich mehrere Stunden in sozialen Netzwerken, um sich zu informieren, zu kommunizieren oder sich zu unterhalten. Studien zeigen jedoch, dass viele unter Schlafproblemen, Konzentrationsschwierigkeiten und sozialem Druck leiden. Besonders belastend sind ständige Vergleiche mit scheinbar perfekten Bildern anderer. Pädagogen empfehlen deshalb klare Handyzeiten, mehr Medienkompetenz und bewusste Pausen vom digitalen Alltag.",
    "question":"Welcher Text beschreibt psychische Belastungen durch digitale Medien?",
    "options":["Text G","Text H","Text I — Schlaf und Druck"],
    "correct":2,
    "explanation":"Text I erwähnt Schlafprobleme und sozialen Druck als Folge der Nutzung sozialer Netzwerke."
  },
  {
    "id":138,"test":1,"teil":3,"type":"text",
    "context":"(Gleiche Texte G, H, I wie Aufgabe 137)",
    "question":"In welchem Text wird über steigende Wohnkosten in Städten berichtet?",
    "options":["Text G — Mieten steigen","Text H","Text I"],
    "correct":0,
    "explanation":"Text G beschreibt die stark steigenden Mieten in deutschen Großstädten."
  },
  {
    "id":139,"test":1,"teil":3,"type":"text",
    "context":"(Gleiche Texte G, H, I wie Aufgabe 137)",
    "question":"Welcher Text thematisiert Naturkatastrophen als Folge des Klimawandels?",
    "options":["Text G","Text H — Extremwetter","Text I"],
    "correct":1,
    "explanation":"Text H beschreibt Hitzewellen, Überschwemmungen und Stürme als Klimafolgen."
  },
  {
    "id":140,"test":1,"teil":3,"type":"text",
    "context":"TEXT J — Ehrenamt in Deutschland\nJeder dritte Deutsche engagiert sich regelmäßig ehrenamtlich, zum Beispiel in Vereinen, Schulen, Kirchengemeinden oder sozialen Projekten. Ohne diese Arbeit könnten viele Angebote für Kinder, Senioren oder Bedürftige kaum bestehen. Besonders aktiv sind Rentner, weil sie Zeit und Erfahrung mitbringen, aber auch viele Schüler helfen mit. Experten sehen im Ehrenamt deshalb einen wichtigen Beitrag zum gesellschaftlichen Zusammenhalt.\n\nTEXT K — Digitale Technologie im Alltag\nSmartphones, Sprachassistenten und KI-Programme erleichtern vielen Menschen den Alltag, etwa beim Übersetzen, Navigieren oder Organisieren von Terminen. Gleichzeitig warnen Datenschutzexperten davor, dass persönliche Informationen oft im Hintergrund gesammelt und ausgewertet werden. Viele Nutzer wissen nicht genau, welche Daten Apps speichern oder weitergeben. Deshalb fordern Verbraucherschützer mehr Transparenz, strengere Regeln und verständlichere Einstellungen zum Datenschutz.\n\nTEXT L — Sport und Gesellschaft\nGroße Sportereignisse wie die Fußball-WM oder Olympische Spiele verbinden Menschen auf der ganzen Welt und schaffen gemeinsame Gesprächsthemen. Fans erleben starke Gefühle, feiern Siege und identifizieren sich mit ihren Mannschaften. Kritiker bemängeln jedoch die zunehmende Kommerzialisierung, riesige Werbeverträge und astronomische Gehälter im Profisport. Sie fragen, ob sportliche Werte heute noch wichtiger sind als wirtschaftliche Interessen.",
    "question":"Welcher Text warnt vor dem Missbrauch persönlicher Daten?",
    "options":["Text J","Text K — Datenmissbrauch","Text L"],
    "correct":1,
    "explanation":"Text K warnt, dass Nutzerdaten ohne ausdrückliche Zustimmung gesammelt werden."
  },
  {
    "id":141,"test":1,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 140)",
    "question":"In welchem Text geht es um freiwilliges soziales Engagement?",
    "options":["Text J — Ehrenamt","Text K","Text L"],
    "correct":0,
    "explanation":"Text J beschreibt ehrenamtliches Engagement als wichtigen Teil des gesellschaftlichen Lebens."
  },
  {
    "id":142,"test":1,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 140)",
    "question":"Welcher Text kritisiert die Vermarktung des Sports?",
    "options":["Text J","Text K","Text L — Kommerzialisierung"],
    "correct":2,
    "explanation":"Text L kritisiert Kommerzialisierung und hohe Profigehälter im modernen Sport."
  },
  {
    "id":143,"test":1,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 140)",
    "question":"Laut Text J: Welche Gruppen sind beim Ehrenamt besonders aktiv?",
    "options":["Studenten und Manager","Rentner und Schüler","Ärzte und Ingenieure"],
    "correct":1,
    "explanation":"Text J nennt ausdrücklich Rentner und Schüler als besonders aktive Gruppen."
  },
  {
    "id":144,"test":1,"teil":3,"type":"text",
    "context":"(Alle Texte A bis L)",
    "question":"Welches übergreifende Thema erscheint in mehreren Texten?",
    "options":["Gesellschaftlicher Zusammenhalt und Gemeinschaft","Ausländische Sprachen lernen","Medizinische Forschung"],
    "correct":0,
    "explanation":"Gemeinschaft und gesellschaftliches Miteinander erscheinen in Texten zu Ehrenamt, Sport und Homeoffice."
  },
  {
    "id":145,"test":1,"teil":3,"type":"text",
    "context":"(Alle Texte A bis L)",
    "question":"Welcher Text hilft jemandem, der täglich günstiger zur Arbeit pendeln möchte?",
    "options":["Text A — Homeoffice","Text E — 49-Euro-Ticket","Text G — Wohnungsmarkt"],
    "correct":1,
    "explanation":"Text E informiert über das 49-Euro-Ticket als günstige Mobilitätsoption für den Alltag."
  },
]

# ───────────────────────────────────────────────────────────────────────────
# TEST 2 — Thema: Freizeit, Reisen & Konsumverhalten
# ───────────────────────────────────────────────────────────────────────────
TEST2 = [

  # ── Teil 1: Multiple Choice ──────────────────────────────────────────────
  {
    "id":201,"test":2,"teil":1,"type":"mc",
    "question":"Was ist ein 'Praktikum'?",
    "options":["Ein Vollzeitstudium an einer Universität","Eine befristete praktische Arbeitserfahrung in einem Betrieb","Ein dauerhaftes Arbeitsverhältnis"],
    "correct":1,
    "explanation":"Ein Praktikum ist eine zeitlich begrenzte Berufserfahrung, oft zur Ausbildung oder Studienzeit."
  },
  {
    "id":202,"test":2,"teil":1,"type":"mc",
    "question":"'Er hat das Buch gelesen.' In welcher Zeitform steht dieser Satz?",
    "options":["Präsens","Perfekt","Präteritum"],
    "correct":1,
    "explanation":"'Hat gelesen' ist das Perfekt: Hilfsverb 'haben' + Partizip II 'gelesen'."
  },
  {
    "id":203,"test":2,"teil":1,"type":"mc",
    "question":"Welches Wort beschreibt jemanden, der kaum Geld besitzt?",
    "options":["Wohlhabend","Geizig","Arm"],
    "correct":2,
    "explanation":"'Arm' bedeutet, dass jemand über sehr wenig oder kein Geld verfügt."
  },
  {
    "id":204,"test":2,"teil":1,"type":"mc",
    "question":"'Sie ist _____ Ärztin.' Welcher Artikel ist grammatikalisch korrekt?",
    "options":["eine","die","kein Artikel nötig"],
    "correct":2,
    "explanation":"Bei Berufsbezeichnungen nach 'sein' steht kein Artikel: 'Sie ist Ärztin.'"
  },
  {
    "id":205,"test":2,"teil":1,"type":"mc",
    "question":"Was bedeutet 'die Miete erhöhen'?",
    "options":["Den Mietpreis senken","Den monatlichen Mietpreis steigern","Die Wohnung kündigen"],
    "correct":1,
    "explanation":"'Die Miete erhöhen' bedeutet, den monatlichen Mietbetrag zu steigern."
  },
  {
    "id":206,"test":2,"teil":1,"type":"mc",
    "question":"'Ich würde gerne ins Kino gehen, _____ ich muss noch arbeiten.'",
    "options":["und","aber","weil"],
    "correct":1,
    "explanation":"'Aber' verbindet zwei Hauptsätze mit gegensätzlichem Inhalt (adversativ)."
  },
  {
    "id":207,"test":2,"teil":1,"type":"mc",
    "question":"Welcher Satz ist eine Entschuldigung?",
    "options":["'Ich komme morgen.'","'Es tut mir leid, das habe ich vergessen.'","'Könnten Sie das bitte erklären?'"],
    "correct":1,
    "explanation":"'Es tut mir leid' ist der gängige deutsche Ausdruck für eine aufrichtige Entschuldigung."
  },
  {
    "id":208,"test":2,"teil":1,"type":"mc",
    "question":"'Das Kind schläft, _____ seine Mutter kocht.' Welches Wort passt?",
    "options":["während","nachdem","bevor"],
    "correct":0,
    "explanation":"'Während' drückt Gleichzeitigkeit aus: beide Handlungen finden zur selben Zeit statt."
  },
  {
    "id":209,"test":2,"teil":1,"type":"mc",
    "question":"Welches Verb gehört zur Gruppe der starken Verben?",
    "options":["spielen","schreiben","kaufen"],
    "correct":1,
    "explanation":"'Schreiben' ist stark: schreibe – schrieb – geschrieben (Vokalwechsel im Präteritum)."
  },
  {
    "id":210,"test":2,"teil":1,"type":"mc",
    "question":"Was bedeutet 'einen Termin vereinbaren'?",
    "options":["Einen Termin absagen","Sich auf einen bestimmten Zeitpunkt einigen","Zu spät zu einem Termin kommen"],
    "correct":1,
    "explanation":"'Einen Termin vereinbaren' heißt, sich auf ein Datum und eine Uhrzeit für ein Treffen zu einigen."
  },
  {
    "id":211,"test":2,"teil":1,"type":"mc",
    "question":"'Trotz _____ schlechten Wetters gingen sie spazieren.' Welcher Artikel?",
    "options":["dem","des","die"],
    "correct":1,
    "explanation":"'Trotz' regiert den Genitiv. Maskulin/Neutrum im Genitiv: 'des schlechten Wetters'."
  },
  {
    "id":212,"test":2,"teil":1,"type":"mc",
    "question":"Was ist das Gegenteil von 'öffnen'?",
    "options":["Anfangen","Schließen","Beginnen"],
    "correct":1,
    "explanation":"Das direkte Antonym von 'öffnen' ist 'schließen'."
  },
  {
    "id":213,"test":2,"teil":1,"type":"mc",
    "question":"'Ich bin _____ München gefahren.' Welche Präposition ist korrekt?",
    "options":["nach","in","zu"],
    "correct":0,
    "explanation":"Bei Städtenamen ohne Artikel: 'nach München fahren'. 'Nach' + Ortsname = Richtung."
  },
  {
    "id":214,"test":2,"teil":1,"type":"mc",
    "question":"Welcher Satz verwendet den Dativ korrekt?",
    "options":["Er hilft seine Schwester.","Er hilft seiner Schwester.","Er hilft ihren Schwester."],
    "correct":1,
    "explanation":"'Helfen' regiert den Dativ. Feminin im Dativ: 'seiner Schwester' (Possessivartikel + Dativform)."
  },
  {
    "id":215,"test":2,"teil":1,"type":"mc",
    "question":"Was bedeutet 'umweltfreundlich'?",
    "options":["Schädlich für die Umwelt","Die Umwelt schonend oder nicht belastend","Unabhängig von der Umwelt"],
    "correct":1,
    "explanation":"'Umweltfreundlich' beschreibt Produkte oder Verhalten, die die Natur möglichst wenig belasten."
  },
  {
    "id":216,"test":2,"teil":1,"type":"mc",
    "question":"'Sie _____ seit zwei Stunden auf den Bus.' Welche Verbform ist korrekt?",
    "options":["wartet","hat gewartet","wartete"],
    "correct":0,
    "explanation":"Mit 'seit' + andauernder Handlung steht das Präsens: 'Sie wartet seit zwei Stunden.'"
  },
  {
    "id":217,"test":2,"teil":1,"type":"mc",
    "question":"'Der Arzt _____ dem Patienten, mehr Sport zu machen.' Welches Verb passt?",
    "options":["befiehlt","empfiehlt","verlangt"],
    "correct":1,
    "explanation":"'Empfehlen' ist die höfliche, fachliche Form eines ärztlichen Ratschlags."
  },
  {
    "id":218,"test":2,"teil":1,"type":"mc",
    "question":"Was ist ein 'Nebenjob'?",
    "options":["Der Hauptberuf","Eine bezahlte Tätigkeit zusätzlich zum Hauptberuf","Ein unbezahltes Ehrenamt"],
    "correct":1,
    "explanation":"Ein Nebenjob ist eine Beschäftigung, die man neben dem Hauptberuf ausübt."
  },
  {
    "id":219,"test":2,"teil":1,"type":"mc",
    "question":"'Je mehr er lernt, _____ besser werden seine Noten.'",
    "options":["desto","umso mehr","je"],
    "correct":0,
    "explanation":"Die Konstruktion 'je … desto' drückt eine Proportionalität aus: je mehr – desto besser."
  },
  {
    "id":220,"test":2,"teil":1,"type":"mc",
    "question":"Was bedeutet 'eine Prüfung ablegen'?",
    "options":["Eine Prüfung vorbereiten","Eine Prüfung offiziell absolvieren","Eine Prüfung absagen"],
    "correct":1,
    "explanation":"'Eine Prüfung ablegen' ist eine feste Wendung und bedeutet, die Prüfung offiziell zu absolvieren."
  },

  # ── Teil 2: Richtig / Falsch ──────────────────────────────────────────────
  {
    "id":221,"test":2,"teil":2,"type":"rf",
    "context":"Stellenanzeige:\n\nWir suchen eine motivierte Vollzeitkraft (40 Std./Woche) für unsere Buchhaltung. Voraussetzung: abgeschlossene kaufmännische Ausbildung. Berufsanfänger willkommen. Gehalt: 2.800 Euro brutto monatlich. Bewerbungen bitte ausschließlich per E-Mail.",
    "question":"Für diese Stelle ist Berufserfahrung zwingend erforderlich.",
    "correct":False,
    "explanation":"Falsch. Die Anzeige sagt ausdrücklich: 'Berufsanfänger willkommen.'"
  },
  {
    "id":222,"test":2,"teil":2,"type":"rf",
    "context":"(Gleiche Stellenanzeige wie Aufgabe 221)",
    "question":"Das monatliche Bruttogehalt beträgt 2.800 Euro.",
    "correct":True,
    "explanation":"Richtig. Die Anzeige nennt: 'Gehalt: 2.800 Euro brutto monatlich.'"
  },
  {
    "id":223,"test":2,"teil":2,"type":"rf",
    "context":"Wettervorhersage:\n\nFür Dienstag erwartet der Deutsche Wetterdienst Regenschauer in der Mitte Deutschlands. Im Süden bleibt es überwiegend sonnig mit Temperaturen bis 22 Grad. Im Norden kommen gegen Abend Winde auf.",
    "question":"Im gesamten Land wird am Dienstag Regen erwartet.",
    "correct":False,
    "explanation":"Falsch. Nur in der Mitte Deutschlands gibt es Regen. Im Süden ist es sonnig."
  },
  {
    "id":224,"test":2,"teil":2,"type":"rf",
    "context":"(Gleiche Wettervorhersage wie Aufgabe 223)",
    "question":"Im Süden Deutschlands sind bis zu 22 Grad möglich.",
    "correct":True,
    "explanation":"Richtig. Die Vorhersage nennt für den Süden 'Temperaturen bis 22 Grad'."
  },
  {
    "id":225,"test":2,"teil":2,"type":"rf",
    "context":"Restaurantbewertung:\n\nDas Essen war ausgezeichnet — frische Zutaten, kreative Gerichte. Der Service war leider sehr langsam; wir mussten 40 Minuten auf die Hauptspeise warten. Die Preise sind gehoben, aber gerechtfertigt.",
    "question":"Das Essen hat dem Gast gut gefallen.",
    "correct":True,
    "explanation":"Richtig. Der Gast beschreibt das Essen als 'ausgezeichnet' mit 'frischen Zutaten'."
  },
  {
    "id":226,"test":2,"teil":2,"type":"rf",
    "context":"(Gleiche Restaurantbewertung wie Aufgabe 225)",
    "question":"Der Service im Restaurant war sehr schnell.",
    "correct":False,
    "explanation":"Falsch. Der Gast kritisiert den 'sehr langsamen' Service und 40 Minuten Wartezeit."
  },
  {
    "id":227,"test":2,"teil":2,"type":"rf",
    "context":"Vereinsmitteilung:\n\nDer nächste Vereinsabend findet am Donnerstag, 14. November um 19:30 Uhr statt. Bitte bringt eure Mitgliedskarten mit. Gäste sind herzlich willkommen. Die Teilnahme ist kostenlos.",
    "question":"Gäste dürfen nicht am Vereinsabend teilnehmen.",
    "correct":False,
    "explanation":"Falsch. Die Mitteilung sagt ausdrücklich: 'Gäste sind herzlich willkommen.'"
  },
  {
    "id":228,"test":2,"teil":2,"type":"rf",
    "context":"(Gleiche Vereinsmitteilung wie Aufgabe 227)",
    "question":"Die Veranstaltung findet am Abend statt.",
    "correct":True,
    "explanation":"Richtig. Beginn ist um 19:30 Uhr — das ist abends."
  },
  {
    "id":229,"test":2,"teil":2,"type":"rf",
    "context":"Reisehinweis:\n\nFür die Einreise nach Kanada benötigen EU-Bürger kein Visum, müssen aber vorab online eine eTA (Electronic Travel Authorization) beantragen. Diese kostet 7 kanadische Dollar und ist 5 Jahre gültig.",
    "question":"EU-Bürger brauchen für die Einreise nach Kanada ein Visum.",
    "correct":False,
    "explanation":"Falsch. EU-Bürger brauchen kein Visum, aber eine eTA-Genehmigung."
  },
  {
    "id":230,"test":2,"teil":2,"type":"rf",
    "context":"(Gleicher Reisehinweis wie Aufgabe 229)",
    "question":"Die eTA-Genehmigung ist fünf Jahre gültig.",
    "correct":True,
    "explanation":"Richtig. Im Text steht ausdrücklich: 'ist 5 Jahre gültig'."
  },

  # ── Teil 3: Leseverstehen / Textauswahl ──────────────────────────────────
  {
    "id":231,"test":2,"teil":3,"type":"text",
    "context":"TEXT A — Stadtbibliothek\nDie Stadtbibliothek bietet nicht nur Bücher- und Medienverleih, sondern auch Lesungen, Workshops und kleine Sprachcafés für Menschen aus der Region an. Für viele Familien ist sie ein günstiger Treffpunkt zum Lernen und Lesen. Die Jahresmitgliedschaft kostet nur 20 Euro. Kinder und Jugendliche unter 18 Jahren erhalten kostenlosen Zugang und können zusätzlich an Ferienprogrammen teilnehmen.\n\nTEXT B — Fitnessstudio\nUnser Fitnessstudio ist an 365 Tagen im Jahr geöffnet und richtet sich an Anfänger ebenso wie an erfahrene Sportler. Neben modernem Gerätetraining gibt es Kurse, persönliche Trainingsberatung und spezielle Programme für Rücken, Ausdauer und Gewichtsreduktion. Mitglieder können flexibel trainieren, auch früh morgens oder spät abends. Der Monatsbeitrag beginnt bei 29 Euro und steigt je nach Zusatzangebot.\n\nTEXT C — Volkshochschule\nDie Volkshochschule bietet Kurse in Sprachen, EDV, Kochen, Kunst und beruflicher Weiterbildung an. Viele Angebote finden am Abend oder online statt, damit auch Berufstätige teilnehmen können. Besonders beliebt sind Deutsch- und Englischkurse auf verschiedenen Niveaustufen. Für Menschen mit geringem Einkommen gibt es oft Ermäßigungen oder Förderungen, sodass Weiterbildung auch mit kleinem Budget möglich bleibt.",
    "question":"Wo kann man preisgünstig eine Fremdsprache lernen?",
    "options":["Text A — Bibliothek","Text B — Fitnessstudio","Text C — Volkshochschule"],
    "correct":2,
    "explanation":"Text C erwähnt Sprachkurse an der VHS, auch mit möglichen Förderungen für Geringverdiener."
  },
  {
    "id":232,"test":2,"teil":3,"type":"text",
    "context":"(Gleiche Texte A, B, C wie Aufgabe 231)",
    "question":"Welcher Text beschreibt ein Angebot für sportliche Aktivitäten?",
    "options":["Text A","Text B — Fitnessstudio","Text C"],
    "correct":1,
    "explanation":"Text B beschreibt das Fitnessstudio mit Gerätetraining, Kursen und Beratung."
  },
  {
    "id":233,"test":2,"teil":3,"type":"text",
    "context":"(Gleiche Texte A, B, C wie Aufgabe 231)",
    "question":"Für wen ist die Mitgliedschaft in einem der Angebote kostenlos?",
    "options":["Für Studenten (Text A)","Für Kinder unter 18 Jahren (Text A)","Für Rentner (Text B)"],
    "correct":1,
    "explanation":"Text A sagt: 'Kinder unter 18 Jahren erhalten kostenlosen Zugang.'"
  },
  {
    "id":234,"test":2,"teil":3,"type":"text",
    "context":"TEXT D — Vegetarische Ernährung\nImmer mehr Menschen verzichten ganz oder teilweise auf Fleisch. Häufige Gründe sind Gesundheit, Tierwohl, Klimaschutz und der Wunsch nach einer bewussteren Lebensweise. In vielen Städten gibt es inzwischen zahlreiche vegetarische Restaurants, Kantinenangebote und Supermarktprodukte. Studien zeigen, dass besonders jüngere Erwachsene offen für diese Ernährungsform sind, während ältere Generationen oft stärker an klassischen Fleischgerichten festhalten.\n\nTEXT E — Fast Food und Gesundheit\nFast Food ist beliebt, weil es schnell verfügbar, günstig und fast überall zu kaufen ist. Viele Produkte enthalten jedoch viel Fett, Salz und Zucker, aber nur wenige wichtige Nährstoffe. Ernährungsexperten warnen davor, dass regelmäßiger Konsum das Risiko für Übergewicht, Herz-Kreislauf-Erkrankungen und Diabetes erhöhen kann. Wer sich langfristig gesund ernähren will, sollte Fast Food deshalb eher als Ausnahme betrachten.\n\nTEXT F — Intermittierendes Fasten\nBeim intermittierenden Fasten isst man nur innerhalb eines festgelegten Zeitfensters, zum Beispiel acht Stunden pro Tag. In der übrigen Zeit wird auf Nahrung verzichtet, Getränke ohne Kalorien sind aber erlaubt. Viele Menschen nutzen diese Methode, um ihr Gewicht zu kontrollieren oder bewusster zu essen. Studien zeigen positive Effekte auf Blutwerte und Stoffwechsel, betonen jedoch auch die Bedeutung einer insgesamt ausgewogenen Ernährung.",
    "question":"Welcher Text beschreibt gesundheitliche Risiken durch bestimmte Essgewohnheiten?",
    "options":["Text D","Text E — Fast Food und Gesundheitsrisiken","Text F"],
    "correct":1,
    "explanation":"Text E warnt vor Fast Food und seinen Risiken für Herz-Kreislauf-Erkrankungen und Diabetes."
  },
  {
    "id":235,"test":2,"teil":3,"type":"text",
    "context":"(Gleiche Texte D, E, F wie Aufgabe 234)",
    "question":"Welcher Text stellt eine Ernährungsmethode mit Zeitfenstern vor?",
    "options":["Text D","Text E","Text F — Intermittierendes Fasten"],
    "correct":2,
    "explanation":"Text F beschreibt das intermittierende Fasten als Methode mit festen Essenszeitfenstern."
  },
  {
    "id":236,"test":2,"teil":3,"type":"text",
    "context":"(Gleiche Texte D, E, F wie Aufgabe 234)",
    "question":"In welchem Text wird Umweltschutz als Grund für eine Ernährungsform genannt?",
    "options":["Text D — Umwelt als Grund für Vegetarismus","Text E","Text F"],
    "correct":0,
    "explanation":"Text D nennt 'Umwelt' ausdrücklich als einen der Gründe, vegetarisch zu leben."
  },
  {
    "id":237,"test":2,"teil":3,"type":"text",
    "context":"TEXT G — Lehrermangel in Deutschland\nDeutschland hat einen akuten Lehrermangel, besonders in Mathematik, Informatik, Naturwissenschaften und Technik. Viele Schulen suchen monatelang nach geeignetem Personal und können Unterricht nicht vollständig abdecken. Einige Bundesländer werben deshalb im Ausland oder stellen verstärkt Quereinsteiger ein. Bildungsexperten warnen jedoch, dass diese Maßnahmen das Problem nur teilweise lösen und langfristige Strategien nötig bleiben.\n\nTEXT H — Digitalisierung an Schulen\nTablets, digitale Tafeln und Lernplattformen gehören in vielen Schulen inzwischen zum Alltag. Sie erleichtern individuelles Lernen, schnellen Materialaustausch und neue Unterrichtsformen. Kritiker bemängeln aber, dass viele Lehrkräfte nicht ausreichend für den digitalen Unterricht geschult wurden. Außerdem fehlen mancherorts stabiles Internet, technische Betreuung und klare Konzepte für den sinnvollen Einsatz der Geräte.\n\nTEXT I — PISA-Studie\nDie neueste PISA-Studie zeigt, dass deutsche Schülerinnen und Schüler in Mathematik und Lesen im internationalen Vergleich zurückgefallen sind. Fachleute sehen darin ein Warnsignal für das Bildungssystem. Besonders problematisch sind große Unterschiede zwischen sozialen Gruppen und Bundesländern. Experten fordern deshalb mehr Investitionen in frühe Förderung, Sprachkompetenz, Lehrkräfte und moderne Lernbedingungen an Schulen.",
    "question":"Welcher Text thematisiert den internationalen Vergleich von Schulleistungen?",
    "options":["Text G","Text H","Text I — PISA-Studie"],
    "correct":2,
    "explanation":"Text I beschreibt die PISA-Studie und den Rückgang deutscher Schülerleistungen."
  },
  {
    "id":238,"test":2,"teil":3,"type":"text",
    "context":"(Gleiche Texte G, H, I wie Aufgabe 237)",
    "question":"In welchem Text wird ein Personalmangel in einem Berufsfeld beschrieben?",
    "options":["Text G — Lehrermangel","Text H","Text I"],
    "correct":0,
    "explanation":"Text G beschreibt den akuten Lehrermangel in Deutschland."
  },
  {
    "id":239,"test":2,"teil":3,"type":"text",
    "context":"(Gleiche Texte G, H, I wie Aufgabe 237)",
    "question":"Welcher Text beschreibt Vorteile und Kritik an neuen Unterrichtsmitteln?",
    "options":["Text G","Text H — Digitale Hilfsmittel","Text I"],
    "correct":1,
    "explanation":"Text H beschreibt digitale Lernmittel positiv, erwähnt aber Kritik an fehlender Ausbildung."
  },
  {
    "id":240,"test":2,"teil":3,"type":"text",
    "context":"TEXT J — Bahnreisen in Deutschland\nDie Deutsche Bahn betreibt eines der größten Schienennetze Europas und verbindet große Städte ebenso wie viele kleinere Regionen. Wer Fernreisen früh bucht, kann oft deutlich günstigere Tickets erhalten als kurz vor der Abfahrt. Viele Reisende schätzen außerdem die Möglichkeit, unterwegs zu arbeiten oder sich auszuruhen. Gleichzeitig bleiben Verspätungen, Ausfälle und überfüllte Züge ein häufig genanntes Problem.\n\nTEXT K — Carsharing\nCarsharing wächst in deutschen Städten rasant, weil viele Menschen ein Auto nur gelegentlich brauchen. Nutzer reservieren Fahrzeuge per App und zahlen nur für die tatsächliche Fahrzeit oder Strecke. Kosten für Versicherung, Wartung und Parkplatzsuche entfallen oft oder werden stark reduziert. Das Modell ist besonders attraktiv für Menschen, die flexibel mobil sein wollen, aber kein eigenes Auto besitzen möchten.\n\nTEXT L — Fahrradkultur\nDeutschland investiert stark in Fahrradinfrastruktur, um Städte lebenswerter und klimafreundlicher zu machen. In Orten wie Münster und Freiburg fahren bereits sehr viele Menschen regelmäßig mit dem Rad zur Arbeit oder zur Uni. Neue Radschnellwege, sichere Abstellplätze und breitere Radspuren sollen das Pendeln weiter erleichtern. Verkehrsplaner sehen im Fahrrad deshalb einen wichtigen Baustein moderner Stadtmobilität.",
    "question":"Welcher Text beschreibt ein Angebot, bei dem man kein eigenes Auto besitzen muss?",
    "options":["Text J","Text K — Carsharing","Text L"],
    "correct":1,
    "explanation":"Text K beschreibt Carsharing: Man nutzt ein Auto ohne es zu besitzen."
  },
  {
    "id":241,"test":2,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 240)",
    "question":"In welchem Text werden günstige Buchungsmöglichkeiten für Fernreisen erwähnt?",
    "options":["Text J — Frühbucher-Tickets","Text K","Text L"],
    "correct":0,
    "explanation":"Text J erwähnt günstige Tickets bei frühzeitiger Buchung."
  },
  {
    "id":242,"test":2,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 240)",
    "question":"Welcher Text beschreibt nachhaltige Stadtmobilität am deutlichsten?",
    "options":["Text J","Text K","Text L — Fahrradinfrastruktur"],
    "correct":2,
    "explanation":"Text L beschreibt den Ausbau der Fahrradinfrastruktur als nachhaltiges Stadtverkehrsmittel."
  },
  {
    "id":243,"test":2,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 240)",
    "question":"Laut Text J: Was ist ein bekanntes Problem der Deutschen Bahn?",
    "options":["Zu hohe Preise","Häufige Verspätungen","Zu wenige Stationen"],
    "correct":1,
    "explanation":"Text J nennt Verspätungen ausdrücklich als häufiges und bekanntes Problem."
  },
  {
    "id":244,"test":2,"teil":3,"type":"text",
    "context":"(Alle Texte A bis L)",
    "question":"Welche zwei Texte thematisieren beide Mobilität und Verkehr?",
    "options":["Texte A und B","Texte J und K","Texte D und E"],
    "correct":1,
    "explanation":"Text J (Bahn) und Text K (Carsharing) behandeln beide das Thema Mobilität und Verkehr."
  },
  {
    "id":245,"test":2,"teil":3,"type":"text",
    "context":"(Alle Texte A bis L)",
    "question":"Welcher Text hilft jemandem am meisten, der kostenlos Sport treiben möchte?",
    "options":["Text B — Fitnessstudio ab 29 Euro","Text C — VHS-Kurse","Text L — Radfahren als kostenfreie Alternative"],
    "correct":2,
    "explanation":"Text L beschreibt Radfahren als kostenfreie und gesunde Fortbewegungsform."
  },
]

# ───────────────────────────────────────────────────────────────────────────
# TEST 3 — Thema: Arbeit, Bildung & Gesundheit
# ───────────────────────────────────────────────────────────────────────────
TEST3 = [

  # ── Teil 1: Multiple Choice ──────────────────────────────────────────────
  {
    "id":301,"test":3,"teil":1,"type":"mc",
    "question":"Was bedeutet 'kündigen' im Arbeitskontext?",
    "options":["Einen neuen Vertrag abschließen","Das Arbeitsverhältnis offiziell beenden","Eine Gehaltserhöhung fordern"],
    "correct":1,
    "explanation":"'Kündigen' bedeutet, das bestehende Arbeitsverhältnis durch schriftliche Erklärung zu beenden."
  },
  {
    "id":302,"test":3,"teil":1,"type":"mc",
    "question":"'Er fährt _____ Fahrrad zur Arbeit.' Was fehlt?",
    "options":["mit dem","mit ein","im"],
    "correct":0,
    "explanation":"'Mit dem Fahrrad fahren' ist die korrekte Formulierung. Das Transportmittel steht mit 'mit + Dativ'."
  },
  {
    "id":303,"test":3,"teil":1,"type":"mc",
    "question":"Welches Adjektiv ist das direkte Gegenteil von 'laut'?",
    "options":["Ruhig","Leise","Still"],
    "correct":1,
    "explanation":"'Leise' ist das direkte Antonym von 'laut' auf der Lautstärkeskala."
  },
  {
    "id":304,"test":3,"teil":1,"type":"mc",
    "question":"'Das Konzert _____ um 20 Uhr.' Welche Verbform ist korrekt?",
    "options":["fängt an","beginnt","Beide Formen sind korrekt"],
    "correct":2,
    "explanation":"Sowohl 'fängt an' (anfangen) als auch 'beginnt' (beginnen) sind grammatikalisch korrekt und gleichbedeutend."
  },
  {
    "id":305,"test":3,"teil":1,"type":"mc",
    "question":"Was bedeutet 'nachhaltig'?",
    "options":["Kurzfristig und einmalig","Dauerhaft und ressourcenschonend","Teuer und aufwendig"],
    "correct":1,
    "explanation":"'Nachhaltig' bezeichnet Handlungen, die langfristig gut für Mensch und Umwelt sind."
  },
  {
    "id":306,"test":3,"teil":1,"type":"mc",
    "question":"'Sie hat _____ Brief noch nicht gelesen.' Welcher Artikel ist korrekt?",
    "options":["dem","den","der"],
    "correct":1,
    "explanation":"'Brief' ist maskulin. Im Akkusativ lautet der bestimmte Artikel 'den'."
  },
  {
    "id":307,"test":3,"teil":1,"type":"mc",
    "question":"Was ist ein 'Zeugnis'?",
    "options":["Ein Personalausweis","Ein offizielles Dokument mit Noten oder Beurteilungen","Eine Heiratsurkunde"],
    "correct":1,
    "explanation":"Ein Zeugnis bestätigt schulische oder berufliche Leistungen, z. B. Abschlusszeugnis oder Arbeitszeugnis."
  },
  {
    "id":308,"test":3,"teil":1,"type":"mc",
    "question":"'Er hat _____ Freunde in der neuen Stadt.' Welche Form passt?",
    "options":["viele","vielen","viel"],
    "correct":0,
    "explanation":"'Viele' wird beim Plural zählbarer Substantive ohne Artikel verwendet: 'viele Freunde'."
  },
  {
    "id":309,"test":3,"teil":1,"type":"mc",
    "question":"Was bedeutet 'eine Ausnahme machen'?",
    "options":["Immer dieselbe Regel anwenden","In einem besonderen Fall von der Regel abweichen","Einen Fehler korrigieren"],
    "correct":1,
    "explanation":"'Eine Ausnahme machen' bedeutet, in einem speziellen Fall anders zu handeln als üblich."
  },
  {
    "id":310,"test":3,"teil":1,"type":"mc",
    "question":"'_____ dem Essen räumte er den Tisch ab.' Welche Präposition?",
    "options":["Nach","Seit","Vor"],
    "correct":0,
    "explanation":"'Nach dem Essen' drückt zeitliche Abfolge aus: erst essen, dann abräumen."
  },
  {
    "id":311,"test":3,"teil":1,"type":"mc",
    "question":"Was sind 'Überstunden'?",
    "options":["Freizeitstunden nach der Arbeit","Arbeitsstunden über die reguläre Arbeitszeit hinaus","Bezahlte Pausen"],
    "correct":1,
    "explanation":"Überstunden sind Arbeitsstunden, die die vereinbarte Wochenarbeitszeit überschreiten."
  },
  {
    "id":312,"test":3,"teil":1,"type":"mc",
    "question":"'Ich freue mich _____ deinen Besuch.' Welche Präposition?",
    "options":["auf","über","für"],
    "correct":0,
    "explanation":"'Sich freuen auf' + Akkusativ bei zukünftigen Ereignissen: 'auf deinen Besuch'."
  },
  {
    "id":313,"test":3,"teil":1,"type":"mc",
    "question":"Welcher Satz ist im Passiv formuliert?",
    "options":["Er baut das Haus.","Das Haus wird gebaut.","Er hat das Haus gebaut."],
    "correct":1,
    "explanation":"Im Passiv Präsens: 'wird' + Partizip II. Das Subjekt des Aktivsatzes wird zum Agens im Passiv."
  },
  {
    "id":314,"test":3,"teil":1,"type":"mc",
    "question":"Was bedeutet 'gastfreundlich'?",
    "options":["Gäste herzlich empfangen und gut bewirten","Häufig in Restaurants gehen","Viel auf Reisen sein"],
    "correct":0,
    "explanation":"'Gastfreundlich' beschreibt Personen oder Kulturen, die Gäste herzlich und großzügig aufnehmen."
  },
  {
    "id":315,"test":3,"teil":1,"type":"mc",
    "question":"'Er ließ das Auto _____.' Welche Form ist nach 'lassen' korrekt?",
    "options":["repariert","reparieren","zu reparieren"],
    "correct":1,
    "explanation":"Nach 'lassen' steht der Infinitiv ohne 'zu': 'Er ließ das Auto reparieren.'"
  },
  {
    "id":316,"test":3,"teil":1,"type":"mc",
    "question":"Was ist 'der Feierabend'?",
    "options":["Ein gesetzlicher Feiertag","Das Ende des täglichen Arbeitstages","Ein Abendessen mit Kollegen"],
    "correct":1,
    "explanation":"'Feierabend' bezeichnet das Ende der täglichen Arbeitszeit: 'Ich mache jetzt Feierabend.'"
  },
  {
    "id":317,"test":3,"teil":1,"type":"mc",
    "question":"'Sie ist _____ als ihr Bruder.' Komparativ von 'alt'?",
    "options":["alterer","älter","am ältesten"],
    "correct":1,
    "explanation":"Komparativ von 'alt': 'älter' (mit Umlaut). 'Am ältesten' wäre der Superlativ."
  },
  {
    "id":318,"test":3,"teil":1,"type":"mc",
    "question":"Was bedeutet 'verhandeln'?",
    "options":["Etwas kaufen ohne Diskussion","Über Bedingungen diskutieren und eine Einigung erzielen","Etwas offiziell verbieten"],
    "correct":1,
    "explanation":"'Verhandeln' bedeutet, durch Gespräche und gegenseitige Zugeständnisse zu einer Einigung zu kommen."
  },
  {
    "id":319,"test":3,"teil":1,"type":"mc",
    "question":"'Obwohl er müde war, _____ er weiter.' Welche Verbform passt?",
    "options":["arbeitete","arbeitet","zu arbeiten"],
    "correct":0,
    "explanation":"Der Kontext steht in der Vergangenheit ('war'), daher Präteritum: 'arbeitete'."
  },
  {
    "id":320,"test":3,"teil":1,"type":"mc",
    "question":"Was ist 'die Krankenversicherung'?",
    "options":["Eine Diebstahlversicherung","Eine Versicherung, die Arztkosten und Behandlungen deckt","Eine Reiseversicherung"],
    "correct":1,
    "explanation":"Die Krankenversicherung übernimmt Kosten für Arztbesuche, Krankenhausaufenthalte und Medikamente."
  },

  # ── Teil 2: Richtig / Falsch ──────────────────────────────────────────────
  {
    "id":321,"test":3,"teil":2,"type":"rf",
    "context":"Kinoprogramm:\n\nFilm: 'Die stille Stadt'\nGenre: Drama\nVorstellung: 20:15 Uhr\nDauer: 118 Minuten\nAltersfreigabe: ab 12 Jahren\nTickets: online oder an der Kinokasse. Online-Buchung: 1 Euro Aufpreis pro Ticket.",
    "question":"Der Film beginnt um 20:00 Uhr.",
    "correct":False,
    "explanation":"Falsch. Der Film beginnt um 20:15 Uhr, nicht um 20:00 Uhr."
  },
  {
    "id":322,"test":3,"teil":2,"type":"rf",
    "context":"(Gleiche Kinoangaben wie Aufgabe 321)",
    "question":"Kinder unter 12 Jahren sind nicht für diesen Film zugelassen.",
    "correct":True,
    "explanation":"Richtig. Die Altersfreigabe ist 'ab 12 Jahren', also keine Kinder unter 12 zugelassen."
  },
  {
    "id":323,"test":3,"teil":2,"type":"rf",
    "context":"Wohnungsanzeige:\n\nSchöne 3-Zimmer-Wohnung in zentraler Lage, 75 m², 3. Etage, Balkon, Einbauküche. Kaltmiete: 950 Euro, Nebenkosten ca. 150 Euro. Kaution: 3 Monatsmieten. Haustiere nach Absprache möglich.",
    "question":"Die Wohnung liegt im Erdgeschoss.",
    "correct":False,
    "explanation":"Falsch. Die Wohnung befindet sich in der 3. Etage, nicht im Erdgeschoss."
  },
  {
    "id":324,"test":3,"teil":2,"type":"rf",
    "context":"(Gleiche Wohnungsanzeige wie Aufgabe 323)",
    "question":"Haustiere sind in dieser Wohnung grundsätzlich verboten.",
    "correct":False,
    "explanation":"Falsch. Die Anzeige sagt: 'Haustiere nach Absprache möglich' — also nicht generell verboten."
  },
  {
    "id":325,"test":3,"teil":2,"type":"rf",
    "context":"Stadtfestprogramm:\n\nSamstag, 20. Juli: Eröffnung um 14:00 Uhr mit Live-Musik. Eintritt frei. Food-Trucks und Handwerkermarkt. Parkplätze begrenzt — Anreise mit dem ÖPNV empfohlen. Bei schlechtem Wetter findet das Fest in der Stadthalle statt.",
    "question":"Für das Stadtfest wird Eintritt verlangt.",
    "correct":False,
    "explanation":"Falsch. Im Programm steht ausdrücklich: 'Eintritt frei.'"
  },
  {
    "id":326,"test":3,"teil":2,"type":"rf",
    "context":"(Gleiches Stadtfestprogramm wie Aufgabe 325)",
    "question":"Bei Regen findet das Fest in einem Gebäude statt.",
    "correct":True,
    "explanation":"Richtig. 'Bei schlechtem Wetter findet das Fest in der Stadthalle statt.'"
  },
  {
    "id":327,"test":3,"teil":2,"type":"rf",
    "context":"Arztbriefauszug:\n\nHerr Mayer, 52 Jahre, wurde wegen anhaltender Rückenschmerzen untersucht. Diagnose: Bandscheibenvorfall L4/L5. Empfehlung: Physiotherapie zweimal wöchentlich, körperliche Schonung, keine schweren Lasten heben. Kontrolltermin in 6 Wochen.",
    "question":"Herrn Mayer wird eine sofortige Operation empfohlen.",
    "correct":False,
    "explanation":"Falsch. Der Arzt empfiehlt Physiotherapie und Schonung, keine Operation."
  },
  {
    "id":328,"test":3,"teil":2,"type":"rf",
    "context":"(Gleicher Arztbrief wie Aufgabe 327)",
    "question":"Herr Mayer soll zweimal pro Woche zur Physiotherapie.",
    "correct":True,
    "explanation":"Richtig. Die Empfehlung lautet ausdrücklich: 'Physiotherapie zweimal wöchentlich'."
  },
  {
    "id":329,"test":3,"teil":2,"type":"rf",
    "context":"Bankbenachrichtigung:\n\nSehr geehrter Kunde, Ihre VISA-Karte läuft am 31.03. ab. Eine neue Karte wurde automatisch erstellt und wird Ihnen innerhalb von 7 Werktagen zugesandt. Bitte vernichten Sie die alte Karte nach Erhalt der neuen.",
    "question":"Der Kunde muss selbst eine neue Karte beantragen.",
    "correct":False,
    "explanation":"Falsch. Die neue Karte 'wurde automatisch erstellt' — kein Antrag nötig."
  },
  {
    "id":330,"test":3,"teil":2,"type":"rf",
    "context":"(Gleiche Bankbenachrichtigung wie Aufgabe 329)",
    "question":"Die neue Karte wird per Post zugeschickt.",
    "correct":True,
    "explanation":"Richtig. Sie 'wird Ihnen innerhalb von 7 Werktagen zugesandt' — also per Post."
  },

  # ── Teil 3: Leseverstehen / Textauswahl ──────────────────────────────────
  {
    "id":331,"test":3,"teil":3,"type":"text",
    "context":"TEXT A — Kaffeekultur in Deutschland\nDeutschland gehört zu den größten Kaffeekonsumländern der Welt. In vielen Städten eröffnen neue Kaffeehäuser und kleine Röstereien, die Wert auf Qualität, Herkunft und besondere Zubereitung legen. Filterkaffee ist vor allem bei jüngeren Menschen wieder modern geworden. Gleichzeitig achten viele Kunden stärker auf Nachhaltigkeit, fairen Handel und umweltfreundliche Verpackungen beim Kaffeekauf.\n\nTEXT B — Teekultur in Ostfriesland\nOstfriesland hat eine einzigartige Teekultur, die weit über die Region hinaus bekannt ist. Dort wird schwarzer Tee traditionell mit Kandiszucker und einem kleinen Schuss Sahne serviert, ohne anschließend umzurühren. Diese Form des Teetrinkens besteht seit Jahrhunderten und gehört zur regionalen Identität. Wegen ihrer kulturellen Bedeutung steht die ostfriesische Teekultur sogar unter besonderem europäischen Schutz.\n\nTEXT C — Craft-Beer-Bewegung\nKleine, unabhängige Brauereien gewinnen in Deutschland an Bedeutung und sprechen besonders Menschen an, die neue Geschmackserlebnisse suchen. Craft Biere zeichnen sich durch kreative Zutaten, experimentelle Aromen und handwerkliche Herstellung aus. Viele Brauereien verkaufen nicht nur Getränke, sondern bieten auch Führungen, Verkostungen und Veranstaltungen an. Dadurch wird Bier zunehmend als kulturelles und regionales Erlebnis präsentiert.",
    "question":"In welchem Text geht es um ein traditionelles regionales Getränk?",
    "options":["Text A","Text B — Ostfriesischer Tee","Text C"],
    "correct":1,
    "explanation":"Text B beschreibt die jahrhundertealte Teetradition Ostfrieslands mit EU-Schutzstatus."
  },
  {
    "id":332,"test":3,"teil":3,"type":"text",
    "context":"(Gleiche Texte A, B, C wie Aufgabe 331)",
    "question":"Welcher Text beschreibt eine neue Bewegung kleiner, handwerklicher Produzenten?",
    "options":["Text A","Text B","Text C — Craft Beer"],
    "correct":2,
    "explanation":"Text C beschreibt die Craft-Beer-Bewegung mit kleinen, unabhängigen Brauereien."
  },
  {
    "id":333,"test":3,"teil":3,"type":"text",
    "context":"(Gleiche Texte A, B, C wie Aufgabe 331)",
    "question":"In welchem Text wird Nachhaltigkeit als wichtiger Kauffaktor erwähnt?",
    "options":["Text A — Kaffee und Nachhaltigkeit","Text B","Text C"],
    "correct":0,
    "explanation":"Text A erwähnt, dass Nachhaltigkeit beim Kaffeekauf eine zunehmende Rolle spielt."
  },
  {
    "id":334,"test":3,"teil":3,"type":"text",
    "context":"TEXT D — KI im Büro\nKI-Werkzeuge verändern die Arbeitswelt spürbar. Texte werden automatisch entworfen, Daten in kurzer Zeit ausgewertet und Besprechungen direkt transkribiert. Für viele Unternehmen bedeutet das mehr Effizienz, aber auch neue Anforderungen an ihre Beschäftigten. Arbeitnehmer müssen lernen, digitale Werkzeuge sinnvoll zu nutzen, Ergebnisse kritisch zu prüfen und sich ständig weiterzubilden, um mit dem technischen Wandel Schritt zu halten.\n\nTEXT E — Homeoffice-Regelungen\nNach der Pandemie haben viele Unternehmen feste Homeoffice-Regelungen eingeführt, weil Beschäftigte flexiblere Arbeitsmodelle erwarten. Zwei bis drei Tage pro Woche von zu Hause zu arbeiten, ist in vielen Branchen inzwischen üblich. Gleichzeitig gibt es Firmen, die wieder stärker auf Anwesenheit im Büro setzen, um Teamarbeit und Unternehmenskultur zu stärken. Die Diskussion über das richtige Gleichgewicht ist daher noch nicht abgeschlossen.\n\nTEXT F — Viertagewoche\nMehrere Unternehmen in Deutschland testen die Viertagewoche ohne Lohnkürzung, um Fachkräfte zu gewinnen und Arbeitsprozesse effizienter zu gestalten. Erste Ergebnisse zeigen häufig eine höhere Zufriedenheit der Mitarbeiter, weniger Fehlzeiten und teilweise sogar bessere Produktivität. Befürworter sehen darin ein modernes Modell für die Zukunft. Kritiker fragen jedoch, ob sich dieses Konzept in allen Branchen und Berufen realistisch umsetzen lässt.",
    "question":"Welcher Text beschreibt ein Experiment mit kürzerer Arbeitszeit?",
    "options":["Text D","Text E","Text F — Viertagewoche"],
    "correct":2,
    "explanation":"Text F beschreibt Tests zur Viertagewoche ohne Gehaltsreduzierung und ihre positiven Ergebnisse."
  },
  {
    "id":335,"test":3,"teil":3,"type":"text",
    "context":"(Gleiche Texte D, E, F wie Aufgabe 334)",
    "question":"In welchem Text wird erwähnt, dass Arbeitnehmer neue Fähigkeiten erwerben müssen?",
    "options":["Text D — KI und neue Kompetenzen","Text E","Text F"],
    "correct":0,
    "explanation":"Text D sagt ausdrücklich: 'Arbeitnehmer müssen neue Kompetenzen erwerben.'"
  },
  {
    "id":336,"test":3,"teil":3,"type":"text",
    "context":"(Gleiche Texte D, E, F wie Aufgabe 334)",
    "question":"Welcher Text beschreibt unterschiedliche Unternehmensstrategien zur Anwesenheit?",
    "options":["Text D","Text E — Homeoffice vs. Präsenz","Text F"],
    "correct":1,
    "explanation":"Text E: Manche Firmen haben Homeoffice etabliert, andere kehren zum Präsenzbetrieb zurück."
  },
  {
    "id":337,"test":3,"teil":3,"type":"text",
    "context":"TEXT G — Das deutsche Schulsystem\nDas deutsche Schulsystem ist föderalistisch organisiert: Jedes der 16 Bundesländer entscheidet in vielen Bereichen selbst über Lehrpläne, Prüfungen und Schulformen. Befürworter sehen darin regionale Freiheit und Anpassung an lokale Bedürfnisse. Kritiker fordern jedoch mehr Einheitlichkeit, weil Familien bei einem Umzug oft auf große Unterschiede stoßen. Für Schülerinnen und Schüler kann ein Schulwechsel deshalb kompliziert und belastend sein.\n\nTEXT H — Duale Ausbildung\nDie duale Ausbildung kombiniert praktische Arbeit im Betrieb mit Unterricht in der Berufsschule und gilt international als Vorbild. Auszubildende sammeln früh Berufserfahrung und erhalten gleichzeitig theoretisches Wissen. Ein weiterer Vorteil ist, dass sie bereits während der Ausbildung ein Gehalt bekommen. Viele Unternehmen schätzen dieses Modell, weil sie Nachwuchskräfte früh kennenlernen und gezielt für ihre eigenen Anforderungen qualifizieren können.\n\nTEXT I — Hochschulzugang\nDas Abitur ist der klassische Weg an eine Universität oder Hochschule in Deutschland. Daneben gibt es weitere Möglichkeiten wie die Fachhochschulreife oder spezielle Zulassungsverfahren für beruflich Qualifizierte ohne klassisches Abitur. Dadurch sollen auch Menschen mit Berufserfahrung leichter studieren können. Bildungsexperten betonen, dass diese verschiedenen Wege helfen, das Hochschulsystem offener und durchlässiger zu gestalten.",
    "question":"Welcher Text beschreibt ein international anerkanntes Ausbildungsmodell?",
    "options":["Text G","Text H — Duale Ausbildung","Text I"],
    "correct":1,
    "explanation":"Text H beschreibt die duale Ausbildung als international anerkanntes Vorbild."
  },
  {
    "id":338,"test":3,"teil":3,"type":"text",
    "context":"(Gleiche Texte G, H, I wie Aufgabe 337)",
    "question":"Welcher Text kritisiert regionale Unterschiede im Bildungssystem?",
    "options":["Text G — Föderalismus und Kritik","Text H","Text I"],
    "correct":0,
    "explanation":"Text G erwähnt Kritiker, die mehr Einheitlichkeit im föderalen Schulsystem fordern."
  },
  {
    "id":339,"test":3,"teil":3,"type":"text",
    "context":"(Gleiche Texte G, H, I wie Aufgabe 337)",
    "question":"In welchem Text werden verschiedene Wege zum Studium beschrieben?",
    "options":["Text G","Text H","Text I — Hochschulzugang"],
    "correct":2,
    "explanation":"Text I beschreibt Abitur, Fachhochschulreife und Zulassung für Berufstätige als Wege zum Studium."
  },
  {
    "id":340,"test":3,"teil":3,"type":"text",
    "context":"TEXT J — Tourismus in Berlin\nBerlin gehört zu den beliebtesten Reisezielen Europas und zieht jedes Jahr Millionen Besucher aus dem In- und Ausland an. Viele interessieren sich für Museen, Geschichte, Architektur und das vielfältige Nachtleben der Stadt. Besonders bekannt sind die Mauer-Gedenkstätte, die Museumsinsel und politische Sehenswürdigkeiten im Zentrum. Tourismus ist deshalb ein wichtiger Wirtschaftsfaktor für Hotels, Gastronomie und Kulturangebote in Berlin.\n\nTEXT K — Oktoberfest München\nDas Oktoberfest in München ist das größte Volksfest der Welt und lockt jedes Jahr rund sechs Millionen Besucher an. Menschen aus vielen Ländern kommen, um bayerische Musik, traditionelle Kleidung, Fahrgeschäfte und Festzelte zu erleben. Für die Stadt München hat das Ereignis auch wirtschaftlich enorme Bedeutung. Hotels, Gastronomie, Einzelhandel und Verkehrsbetriebe profitieren von einem Umsatz in Milliardenhöhe.\n\nTEXT L — Romantische Straße\nDie Romantische Straße führt von Würzburg bis nach Füssen und verbindet historische Städte, Fachwerkhäuser, Kirchen und berühmte Schlösser miteinander. Viele Reisende entdecken die Route mit dem Auto, Bus oder Fahrrad und machen Zwischenstopps in kleineren Orten. Besonders bekannt ist Schloss Neuschwanstein am südlichen Ende der Strecke. Die Route gilt deshalb als beliebte Kombination aus Kultur, Landschaft und Geschichte.",
    "question":"Welcher Text beschreibt ein weltberühmtes Volksfest?",
    "options":["Text J","Text K — Oktoberfest","Text L"],
    "correct":1,
    "explanation":"Text K beschreibt das Oktoberfest als größtes Volksfest der Welt."
  },
  {
    "id":341,"test":3,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 340)",
    "question":"In welchem Text wird ein Schloss als Sehenswürdigkeit erwähnt?",
    "options":["Text J","Text K","Text L — Schloss Neuschwanstein"],
    "correct":2,
    "explanation":"Text L erwähnt das weltbekannte Schloss Neuschwanstein als Teil der Romantischen Straße."
  },
  {
    "id":342,"test":3,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 340)",
    "question":"Welcher Text erwähnt den wirtschaftlichen Nutzen eines Ereignisses?",
    "options":["Text J","Text K — 1 Milliarde Euro Umsatz","Text L"],
    "correct":1,
    "explanation":"Text K nennt rund 1 Milliarde Euro Umsatz als wirtschaftliche Bedeutung des Oktoberfests."
  },
  {
    "id":343,"test":3,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 340)",
    "question":"Welcher Text beschreibt eine Route durch historische Städte und Schlösser?",
    "options":["Text J","Text K","Text L — Romantische Straße"],
    "correct":2,
    "explanation":"Text L beschreibt die Romantische Straße als Touristenroute durch historische Orte."
  },
  {
    "id":344,"test":3,"teil":3,"type":"text",
    "context":"(Alle Texte A bis L)",
    "question":"Welche zwei Texte beschreiben kulturelle Traditionen in Deutschland?",
    "options":["Texte A und C","Texte B und K","Texte D und F"],
    "correct":1,
    "explanation":"Text B (Ostfriesischer Tee) und Text K (Oktoberfest) beschreiben beide kulturelle Traditionen."
  },
  {
    "id":345,"test":3,"teil":3,"type":"text",
    "context":"(Alle Texte A bis L)",
    "question":"Für wen sind die Informationen in Text H am nützlichsten?",
    "options":["Für Touristen auf Städtereise","Für Jugendliche nach dem Schulabschluss","Für ältere Arbeitnehmer"],
    "correct":1,
    "explanation":"Text H beschreibt die duale Ausbildung — besonders relevant für Jugendliche nach der Schule."
  },
]

# ───────────────────────────────────────────────────────────────────────────
# TEST 4 — Thema: Gesellschaft, Technik & Wirtschaft
# ───────────────────────────────────────────────────────────────────────────
TEST4 = [

  # ── Teil 1: Multiple Choice ──────────────────────────────────────────────
  {
    "id":401,"test":4,"teil":1,"type":"mc",
    "question":"Was bedeutet 'sich anmelden'?",
    "options":["Sich abmelden oder verabschieden","Sich registrieren oder einen Termin buchen","Sich beschweren"],
    "correct":1,
    "explanation":"'Sich anmelden' bedeutet, sich offiziell zu registrieren, z. B. für einen Kurs oder Termin."
  },
  {
    "id":402,"test":4,"teil":1,"type":"mc",
    "question":"'_____ du gestern Abend zu Hause?' Welche Verbform ist korrekt?",
    "options":["Bist","Warst","Hast"],
    "correct":1,
    "explanation":"'Warst' ist das Präteritum von 'sein': 'Warst du gestern Abend zu Hause?'"
  },
  {
    "id":403,"test":4,"teil":1,"type":"mc",
    "question":"Was ist 'die Quittung'?",
    "options":["Eine monatliche Rechnung","Ein Beleg, der eine geleistete Zahlung bestätigt","Ein Kaufvertrag"],
    "correct":1,
    "explanation":"Eine Quittung bestätigt schriftlich, dass eine Zahlung erfolgt ist."
  },
  {
    "id":404,"test":4,"teil":1,"type":"mc",
    "question":"'Darf ich _____ helfen?' Höfliche Anrede im Dativ?",
    "options":["Ihnen","Sie","Ihr"],
    "correct":0,
    "explanation":"'Ihnen' ist die Höflichkeitsform im Dativ: 'Darf ich Ihnen helfen?'"
  },
  {
    "id":405,"test":4,"teil":1,"type":"mc",
    "question":"Was bedeutet 'erschwinglich'?",
    "options":["Viel zu teuer","Zu einem annehmbaren, erschwinglichen Preis","Kostenlos"],
    "correct":1,
    "explanation":"'Erschwinglich' bedeutet, dass etwas zu einem Preis angeboten wird, den man sich leisten kann."
  },
  {
    "id":406,"test":4,"teil":1,"type":"mc",
    "question":"'Sie möchte _____ Ausland studieren.' Welche Präposition?",
    "options":["im","ins","nach"],
    "correct":0,
    "explanation":"'Im Ausland' (Dativ) bezeichnet den Ort: 'Sie möchte im Ausland studieren.'"
  },
  {
    "id":407,"test":4,"teil":1,"type":"mc",
    "question":"Was ist 'die Mehrwertsteuer' (MwSt.)?",
    "options":["Eine staatliche Subvention für Unternehmen","Eine Steuer auf den Konsum von Waren und Dienstleistungen","Ein Zollgebühr für importierte Waren"],
    "correct":1,
    "explanation":"Die Mehrwertsteuer ist eine indirekte Konsumsteuer, die auf Waren und Dienstleistungen erhoben wird."
  },
  {
    "id":408,"test":4,"teil":1,"type":"mc",
    "question":"'Es wird empfohlen, _____ Sport zu treiben.' Welche Form des Adverbs?",
    "options":["regelmäßig","regelmäßigen","regelmäßige"],
    "correct":0,
    "explanation":"'Regelmäßig' ist ein Adverb und wird nicht dekliniert. Es bezieht sich auf das Verb 'treiben'."
  },
  {
    "id":409,"test":4,"teil":1,"type":"mc",
    "question":"Was bedeutet 'aufgeschlossen'?",
    "options":["Offen und neugierig gegenüber Neuem","Verschlossen und schüchtern","Sehr müde und unkonzentriert"],
    "correct":0,
    "explanation":"'Aufgeschlossen' beschreibt eine Person, die offen für neue Ideen, Menschen und Erfahrungen ist."
  },
  {
    "id":410,"test":4,"teil":1,"type":"mc",
    "question":"'Er sprach, _____ ob er alles wüsste.' Welches Wort passt?",
    "options":["als","wie","so"],
    "correct":0,
    "explanation":"'Als ob' + Konjunktiv II leitet einen irrealen Vergleichssatz ein: 'als ob er alles wüsste'."
  },
  {
    "id":411,"test":4,"teil":1,"type":"mc",
    "question":"Was bedeutet 'einsparen'?",
    "options":["Mehr ausgeben als geplant","Kosten oder Ressourcen reduzieren","Geld für die Rente ansparen"],
    "correct":1,
    "explanation":"'Einsparen' bedeutet, Ausgaben oder den Verbrauch von Ressourcen gezielt zu reduzieren."
  },
  {
    "id":412,"test":4,"teil":1,"type":"mc",
    "question":"'Das Problem _____ schon lange bekannt.' Welche Verbform?",
    "options":["ist gewesen","war","ist"],
    "correct":1,
    "explanation":"'War' ist das Präteritum von 'sein' und wird für abgeschlossene Zustände in der Vergangenheit verwendet."
  },
  {
    "id":413,"test":4,"teil":1,"type":"mc",
    "question":"Was ist 'ein Streik'?",
    "options":["Eine Gehaltserhöhung","Eine kollektive Arbeitsniederlegung als Druckmittel","Ein Betriebsausflug"],
    "correct":1,
    "explanation":"Bei einem Streik legen Arbeitnehmer gemeinsam die Arbeit nieder, um Forderungen durchzusetzen."
  },
  {
    "id":414,"test":4,"teil":1,"type":"mc",
    "question":"'Wegen _____ schlechten Wetters blieb er zu Hause.' Genitiv korrekt?",
    "options":["des","dem","ein"],
    "correct":0,
    "explanation":"'Wegen' regiert den Genitiv. Neutrum im Genitiv: 'wegen des schlechten Wetters'."
  },
  {
    "id":415,"test":4,"teil":1,"type":"mc",
    "question":"Was bedeutet 'zuverlässig'?",
    "options":["Unberechenbar und unzuverlässig","Auf den man sich verlassen kann","Sehr kreativ und spontan"],
    "correct":1,
    "explanation":"'Zuverlässig' beschreibt Personen oder Dinge, auf die man sich verlassen kann."
  },
  {
    "id":416,"test":4,"teil":1,"type":"mc",
    "question":"'Er hat _____ Chef um einen freien Tag gebeten.' Richtiges Pronomen?",
    "options":["seinen","ihren","sein"],
    "correct":0,
    "explanation":"'Chef' ist maskulin. Akkusativ mit Possessivartikel: 'seinen Chef'."
  },
  {
    "id":417,"test":4,"teil":1,"type":"mc",
    "question":"Was ist 'der Kindergarten'?",
    "options":["Ein Spielzeuggeschäft","Eine vorschulische Bildungseinrichtung für Kinder","Ein Kinderbuchverlag"],
    "correct":1,
    "explanation":"Der Kindergarten ist eine vorschulische Einrichtung für Kinder im Alter von ca. 3 bis 6 Jahren."
  },
  {
    "id":418,"test":4,"teil":1,"type":"mc",
    "question":"'Je später der Abend, _____ interessanter die Gäste.' Welches Wort?",
    "options":["desto","umso","Beide sind korrekt"],
    "correct":2,
    "explanation":"Sowohl 'desto' als auch 'umso' sind in der 'je … desto/umso'-Konstruktion korrekt und austauschbar."
  },
  {
    "id":419,"test":4,"teil":1,"type":"mc",
    "question":"Was ist 'eine Abgabefrist'?",
    "options":["Eine Steuerart","Eine Deadline für die Einreichung von Dokumenten","Ein Umweltgesetz"],
    "correct":1,
    "explanation":"Eine Abgabefrist ist ein verbindlicher Termin, bis zu dem ein Dokument eingereicht werden muss."
  },
  {
    "id":420,"test":4,"teil":1,"type":"mc",
    "question":"'_____ wohnst du schon in Deutschland?' Welches Fragewort passt?",
    "options":["Wann","Wie lange","Woher"],
    "correct":1,
    "explanation":"'Wie lange' fragt nach der Dauer. Bei 'seit' + Präsens: 'Wie lange wohnst du schon hier?'"
  },

  # ── Teil 2: Richtig / Falsch ──────────────────────────────────────────────
  {
    "id":421,"test":4,"teil":2,"type":"rf",
    "context":"Bahnticket-Quittung:\n\nAbfahrt: Würzburg Hbf\nAnkunft: Frankfurt Hbf\nKlasse: 2. Klasse\nTicketpreis: 29,90 Euro\nBahnCard-Rabatt (10 %): −2,99 Euro\nEndpreis: 26,91 Euro\nZahlung: EC-Karte",
    "question":"Das Ticket wurde mit Bargeld bezahlt.",
    "correct":False,
    "explanation":"Falsch. Laut Quittung wurde per EC-Karte bezahlt."
  },
  {
    "id":422,"test":4,"teil":2,"type":"rf",
    "context":"(Gleiche Quittung wie Aufgabe 421)",
    "question":"Der Fahrgast besitzt eine BahnCard und erhielt einen Rabatt.",
    "correct":True,
    "explanation":"Richtig. Es wird ein 'BahnCard-Rabatt (10 %)' ausgewiesen."
  },
  {
    "id":423,"test":4,"teil":2,"type":"rf",
    "context":"Einladung zur Firmenfeier:\n\nLiebe Kolleginnen und Kollegen,\nwir laden Sie herzlich zum 25-jährigen Firmenjubiläum ein.\nWann: Freitag, 28. Juni, ab 18:00 Uhr\nWo: Eventlocation 'Alte Fabrik', Mainstraße 5\nDress-Code: Business Casual\nAnmeldung bis 15. Juni erforderlich.",
    "question":"Die Feier findet in der Firmenzentrale statt.",
    "correct":False,
    "explanation":"Falsch. Die Feier findet in der 'Alten Fabrik', Mainstraße 5, statt — nicht in der Zentrale."
  },
  {
    "id":424,"test":4,"teil":2,"type":"rf",
    "context":"(Gleiche Einladung wie Aufgabe 423)",
    "question":"Eine Anmeldung ist bis zum 15. Juni erforderlich.",
    "correct":True,
    "explanation":"Richtig. Die Einladung sagt ausdrücklich: 'Anmeldung bis 15. Juni erforderlich.'"
  },
  {
    "id":425,"test":4,"teil":2,"type":"rf",
    "context":"Produktbeschreibung:\n\nElektro-Fahrrad 'CityRide Pro'\n• Reichweite: bis zu 100 km\n• Ladezeit: ca. 4 Stunden\n• Gewicht: 22 kg\n• Wasserschutz: IP54-Standard\n• Preis: 2.499 Euro inkl. MwSt.\n• Garantie: 2 Jahre auf Akku und Rahmen",
    "question":"Das Fahrrad darf bei Regen nicht benutzt werden.",
    "correct":False,
    "explanation":"Falsch. Das Fahrrad ist nach IP54-Standard wassergeschützt und damit für Regen geeignet."
  },
  {
    "id":426,"test":4,"teil":2,"type":"rf",
    "context":"(Gleiche Produktbeschreibung wie Aufgabe 425)",
    "question":"Der Akku hat eine Garantie von zwei Jahren.",
    "correct":True,
    "explanation":"Richtig. Die Garantie gilt '2 Jahre auf Akku und Rahmen'."
  },
  {
    "id":427,"test":4,"teil":2,"type":"rf",
    "context":"Behördenbrief:\n\nSehr geehrter Herr Schmidt,\nIhre Ummeldung wurde erfolgreich bearbeitet. Bitte beachten Sie: Ihr Personalausweis ist abgelaufen. Sie müssen ihn innerhalb von 4 Wochen erneuern. Bringen Sie hierfür ein biometrisches Passfoto und 37 Euro mit.",
    "question":"Die Ummeldung von Herrn Schmidt war nicht erfolgreich.",
    "correct":False,
    "explanation":"Falsch. Der Brief bestätigt: 'Ihre Ummeldung wurde erfolgreich bearbeitet.'"
  },
  {
    "id":428,"test":4,"teil":2,"type":"rf",
    "context":"(Gleicher Behördenbrief wie Aufgabe 427)",
    "question":"Herr Schmidt muss für die Erneuerung des Ausweises ein Foto mitbringen.",
    "correct":True,
    "explanation":"Richtig. Der Brief nennt 'ein biometrisches Passfoto' als Voraussetzung."
  },
  {
    "id":429,"test":4,"teil":2,"type":"rf",
    "context":"Sportnachricht:\n\nDie deutschen Handballer haben das Halbfinale der Europameisterschaft gewonnen. Sie besiegten Frankreich 31:28 nach Verlängerung. Das Finale findet am Sonntag in Berlin statt.",
    "question":"Deutschland hat das Finale der Europameisterschaft bereits gewonnen.",
    "correct":False,
    "explanation":"Falsch. Deutschland hat das Halbfinale gewonnen. Das Finale steht noch aus."
  },
  {
    "id":430,"test":4,"teil":2,"type":"rf",
    "context":"(Gleiche Sportnachricht wie Aufgabe 429)",
    "question":"Das Spiel gegen Frankreich ging in die Verlängerung.",
    "correct":True,
    "explanation":"Richtig. Im Text steht: 'nach Verlängerung' — die reguläre Spielzeit reichte nicht."
  },

  # ── Teil 3: Leseverstehen / Textauswahl ──────────────────────────────────
  {
    "id":431,"test":4,"teil":3,"type":"text",
    "context":"TEXT A — Digitales Ehrenamt\nImmer mehr Menschen engagieren sich online, etwa als Wikipedia-Autoren, in Beratungsportalen, Sprachforen oder als digitale Nachhilfelehrer. Dieses Engagement ermöglicht Hilfe auch dann, wenn Ehrenamtliche und Hilfesuchende weit voneinander entfernt wohnen. Experten sehen darin eine sinnvolle Ergänzung zum klassischen Ehrenamt vor Ort. Gleichzeitig betonen sie, dass persönlicher Kontakt und lokale Projekte dadurch nicht vollständig ersetzt werden können.\n\nTEXT B — Integration durch Sport\nSportvereine leisten wichtige Integrationsarbeit, weil gemeinsames Training Menschen mit unterschiedlichem Hintergrund schnell in Kontakt bringt. Auf dem Spielfeld zählen oft Teamgeist, Regeln und gegenseitiger Respekt mehr als Sprache oder Herkunft. So entstehen Freundschaften, neue Netzwerke und ein Gefühl der Zugehörigkeit. Viele Städte fördern deshalb Sportprojekte gezielt, um Einheimische und Zugewanderte besser miteinander zu verbinden.\n\nTEXT C — Mehrgenerationenhäuser\nIn Mehrgenerationenhäusern leben oder begegnen sich Jung und Alt im Alltag bewusst häufiger. Ältere Menschen betreuen Kinder, teilen Erfahrungen oder unterstützen Familien, während Jüngere beim Einkaufen, bei digitalen Fragen oder im Haushalt helfen. Solche Projekte entlasten beide Seiten und schaffen Vertrauen zwischen verschiedenen Altersgruppen. Fachleute sehen darin ein wirksames Modell gegen Einsamkeit und für mehr gesellschaftlichen Zusammenhalt.",
    "question":"In welchem Text wird gemeinsamer Sport als soziale Brücke beschrieben?",
    "options":["Text A","Text B — Integration durch Sport","Text C"],
    "correct":1,
    "explanation":"Text B beschreibt, wie Sport Einheimische und Zugewanderte verbindet."
  },
  {
    "id":432,"test":4,"teil":3,"type":"text",
    "context":"(Gleiche Texte A, B, C wie Aufgabe 431)",
    "question":"Welcher Text beschreibt gegenseitige Hilfe zwischen verschiedenen Altersgruppen?",
    "options":["Text A","Text B","Text C — Mehrgenerationen"],
    "correct":2,
    "explanation":"Text C beschreibt, wie Alte und Junge sich in Mehrgenerationenhäusern gegenseitig helfen."
  },
  {
    "id":433,"test":4,"teil":3,"type":"text",
    "context":"(Gleiche Texte A, B, C wie Aufgabe 431)",
    "question":"In welchem Text wird eine neue Form des Helfens durch Technologie beschrieben?",
    "options":["Text A — Digitales Ehrenamt","Text B","Text C"],
    "correct":0,
    "explanation":"Text A beschreibt Online-Engagement als neue, technologiebasierte Form des Ehrenamts."
  },
  {
    "id":434,"test":4,"teil":3,"type":"text",
    "context":"TEXT D — Elektromobilität\nElektroautos werden in Deutschland immer beliebter, weil staatliche Förderungen, sinkende Akkupreise und neue Modelle den Einstieg erleichtern. Viele Fahrer schätzen zudem die geringeren lokalen Emissionen und die ruhige Fahrweise. Trotzdem bleibt die Ladeinfrastruktur ein großes Problem, besonders in ländlichen Regionen oder in Mehrfamilienhäusern ohne eigene Stellplätze. Ohne weitere Investitionen könnte der Ausbau der Elektromobilität langsamer verlaufen als geplant.\n\nTEXT E — Wasserstoffantrieb\nWasserstoff gilt als Energieträger der Zukunft, vor allem für Busse, Lastwagen und andere Fahrzeuge auf langen Strecken. Deutschland investiert Milliarden in Forschung, Produktion und Infrastruktur, um diese Technologie voranzubringen. Fachleute sehen darin große Chancen für den Güterverkehr und für Bereiche, in denen Batterien an Grenzen stoßen. Bis zur breiten Marktreife sind jedoch noch technische, wirtschaftliche und ökologische Fragen zu klären.\n\nTEXT F — Autonomes Fahren\nSelbstfahrende Autos werden in Deutschland intensiv erprobt, zum Beispiel auf Teststrecken, in Pilotprojekten oder in der Logistik. Die Technik verspricht mehr Sicherheit, weniger Staus und neue Mobilitätsangebote für ältere Menschen. Trotzdem bremsen Sicherheitsfragen, Haftungsprobleme und gesetzliche Hürden die breite Einführung. Viele Experten rechnen deshalb erst nach 2030 mit einer realistischen Marktreife für den Alltag.",
    "question":"Welcher Text beschreibt eine Technologie, die noch nicht marktreif ist?",
    "options":["Text D","Text E","Text F — Autonomes Fahren nach 2030"],
    "correct":2,
    "explanation":"Text F sagt ausdrücklich, dass autonomes Fahren erst nach 2030 marktreif sein wird."
  },
  {
    "id":435,"test":4,"teil":3,"type":"text",
    "context":"(Gleiche Texte D, E, F wie Aufgabe 434)",
    "question":"In welchem Text wird ein Infrastrukturproblem für ein Fahrzeug erwähnt?",
    "options":["Text D — fehlende Ladeinfrastruktur","Text E","Text F"],
    "correct":0,
    "explanation":"Text D: Die fehlende Ladeinfrastruktur auf dem Land ist ein Problem für Elektroautos."
  },
  {
    "id":436,"test":4,"teil":3,"type":"text",
    "context":"(Gleiche Texte D, E, F wie Aufgabe 434)",
    "question":"Welcher Text beschreibt eine Technologie, die vor allem für den Güterverkehr relevant ist?",
    "options":["Text D","Text E — Wasserstoff für Nutzfahrzeuge","Text F"],
    "correct":1,
    "explanation":"Text E beschreibt Wasserstoff als besonders geeignet für schwere Nutzfahrzeuge."
  },
  {
    "id":437,"test":4,"teil":3,"type":"text",
    "context":"TEXT G — Altersarmut in Deutschland\nTrotz einer starken Volkswirtschaft wächst die Altersarmut in Deutschland. Viele Rentnerinnen und Rentner müssen mit weniger als 1.000 Euro im Monat auskommen und können steigende Mieten oder Energiekosten kaum tragen. Besonders betroffen sind Frauen sowie Menschen mit unterbrochenen Erwerbsbiografien oder langen Phasen von Teilzeitarbeit. Sozialverbände fordern deshalb Reformen, um Armut im Alter wirksamer zu verhindern.\n\nTEXT H — Pflege im Alter\nMit der alternden Gesellschaft steigt auch der Pflegebedarf deutlich an. Pflegeheime sind vielerorts ausgelastet, Personal fehlt und die Kosten für einen Platz sind oft sehr hoch. Deshalb versorgen viele Familien ihre Angehörigen zu Hause, zusätzlich zu Beruf und eigenem Alltag. Diese Situation kann zu einer erheblichen Doppelbelastung führen und macht deutlich, wie groß der Druck im Pflegesystem bereits ist.\n\nTEXT I — Silver Economy\nÄltere Konsumenten werden für Wirtschaft und Dienstleistungssektor zu einer immer wichtigeren Zielgruppe. Die sogenannte Silver Economy umfasst Angebote rund um Reisen, Gesundheit, Freizeit, barrierefreies Wohnen und digitale Assistenzsysteme. Unternehmen entwickeln Produkte gezielt für Menschen ab 60, weil deren Kaufkraft wächst. Fachleute sehen darin nicht nur soziale Herausforderungen, sondern auch erhebliche wirtschaftliche Chancen für die kommenden Jahre.",
    "question":"Welcher Text beschreibt wirtschaftliche Chancen durch eine ältere Gesellschaft?",
    "options":["Text G","Text H","Text I — Silver Economy"],
    "correct":2,
    "explanation":"Text I beschreibt die wachsende Kaufkraft älterer Konsumenten als wirtschaftliche Chance."
  },
  {
    "id":438,"test":4,"teil":3,"type":"text",
    "context":"(Gleiche Texte G, H, I wie Aufgabe 437)",
    "question":"Welcher Text beschreibt finanzielle Not im Rentenalter?",
    "options":["Text G — Altersarmut","Text H","Text I"],
    "correct":0,
    "explanation":"Text G beschreibt, dass viele Rentner weniger als 1.000 Euro monatlich erhalten."
  },
  {
    "id":439,"test":4,"teil":3,"type":"text",
    "context":"(Gleiche Texte G, H, I wie Aufgabe 437)",
    "question":"In welchem Text wird die Belastung von Familien durch häusliche Pflege beschrieben?",
    "options":["Text G","Text H — Doppelbelastung","Text I"],
    "correct":1,
    "explanation":"Text H erwähnt die Doppelbelastung von Familien, die Angehörige zu Hause pflegen."
  },
  {
    "id":440,"test":4,"teil":3,"type":"text",
    "context":"TEXT J — Urban Gardening\nImmer mehr Stadtbewohner legen Gemüse- und Kräutergärten auf Balkonen, Dächern oder in Gemeinschaftsflächen an. Urban Gardening verbindet Nachhaltigkeit mit gesunder Ernährung und schafft Orte, an denen Nachbarn miteinander ins Gespräch kommen. Viele Projekte bieten Workshops für Kinder und Erwachsene an. Dadurch wird Gärtnern in der Stadt nicht nur zu einem Hobby, sondern auch zu einer sozialen Aktivität mit ökologischem Nutzen.\n\nTEXT K — Lebensmittelverschwendung\nIn Deutschland werden jedes Jahr rund 12 Millionen Tonnen Lebensmittel weggeworfen, obwohl vieles davon noch essbar wäre. Gründe sind unter anderem falsche Einkaufsplanung, große Verpackungen und strenge Schönheitsstandards im Handel. Initiativen wie 'Too Good To Go' oder Foodsharing versuchen, diese Entwicklung zu bremsen. Sie retten überschüssige Produkte und machen gleichzeitig auf das Problem der Verschwendung aufmerksam.\n\nTEXT L — Regionale Produkte\nDer Einkauf auf Bauernmärkten oder direkt beim Erzeuger liegt wieder im Trend. Viele Verbraucher möchten wissen, woher ihre Lebensmittel kommen, und legen Wert auf Frische, kurze Transportwege und persönliche Beratung. Regionale Produkte stärken außerdem die lokale Wirtschaft und kleinere Betriebe. Deshalb erleben Wochenmärkte in vielen Städten eine Renaissance und werden wieder zu beliebten Treffpunkten im Alltag.",
    "question":"Welcher Text beschreibt das Problem mit nicht genutzten Nahrungsmitteln?",
    "options":["Text J","Text K — Lebensmittelverschwendung","Text L"],
    "correct":1,
    "explanation":"Text K beschreibt die massive Lebensmittelverschwendung in Deutschland."
  },
  {
    "id":441,"test":4,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 440)",
    "question":"Welcher Text beschreibt einen Trend zum Einkauf direkt beim Erzeuger?",
    "options":["Text J","Text K","Text L — Bauernmarkt und Wochenmarkt"],
    "correct":2,
    "explanation":"Text L beschreibt den Trend zu Wochenmärkten und regionalen Produkten vom Erzeuger."
  },
  {
    "id":442,"test":4,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 440)",
    "question":"In welchem Text wird Gärtnern als soziale Aktivität beschrieben?",
    "options":["Text J — Urban Gardening und soziale Interaktion","Text K","Text L"],
    "correct":0,
    "explanation":"Text J erwähnt 'soziale Interaktion' ausdrücklich als Vorteil von Urban Gardening."
  },
  {
    "id":443,"test":4,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 440)",
    "question":"Welcher Text erwähnt eine Initiative oder App gegen Lebensmittelverschwendung?",
    "options":["Text J","Text K — Too Good To Go","Text L"],
    "correct":1,
    "explanation":"Text K erwähnt 'Too Good To Go' als Maßnahme gegen Lebensmittelverschwendung."
  },
  {
    "id":444,"test":4,"teil":3,"type":"text",
    "context":"(Alle Texte A bis L)",
    "question":"Welche zwei Texte thematisieren beide ältere Menschen in der Gesellschaft?",
    "options":["Texte A und B","Texte G und I","Texte J und L"],
    "correct":1,
    "explanation":"Text G (Altersarmut) und Text I (Silver Economy) thematisieren beide ältere Menschen."
  },
  {
    "id":445,"test":4,"teil":3,"type":"text",
    "context":"(Alle Texte A bis L)",
    "question":"Welcher Text ist am nützlichsten für jemanden, der ein umweltfreundliches Auto kaufen möchte?",
    "options":["Text D — Elektroautos mit Förderung","Text F — Autonomes Fahren","Text K — Lebensmittel"],
    "correct":0,
    "explanation":"Text D informiert über Elektroautos, staatliche Förderungen und sinkende Preise."
  },
]

# ───────────────────────────────────────────────────────────────────────────
# TEST 5 — Thema: Umwelt, Sprache & Wohlbefinden
# ───────────────────────────────────────────────────────────────────────────
TEST5 = [

  # ── Teil 1: Multiple Choice ──────────────────────────────────────────────
  {
    "id":501,"test":5,"teil":1,"type":"mc",
    "question":"Was bedeutet 'die Ausstellung'?",
    "options":["Eine Schulprüfung","Eine öffentliche Präsentation von Kunstwerken oder Objekten","Ein Konzert"],
    "correct":1,
    "explanation":"Eine Ausstellung präsentiert Kunstwerke, Exponate oder Themen für die Öffentlichkeit."
  },
  {
    "id":502,"test":5,"teil":1,"type":"mc",
    "question":"'Sie hat das Buch _____ ihrer Schwester gegeben.' Welches Pronomen?",
    "options":["ihr","sie","ihnen"],
    "correct":0,
    "explanation":"'Ihr' ist der Dativ des femininen Personalpronomens der 3. Person: 'Sie gab es ihr.'"
  },
  {
    "id":503,"test":5,"teil":1,"type":"mc",
    "question":"Was bedeutet 'beantragen'?",
    "options":["Etwas ablehnen","Etwas offiziell anfordern oder schriftlich stellen","Etwas kaufen"],
    "correct":1,
    "explanation":"'Beantragen' bedeutet, etwas offiziell zu beantragen, z. B. ein Visum oder eine Förderung."
  },
  {
    "id":504,"test":5,"teil":1,"type":"mc",
    "question":"'Er ist _____ guter Schüler.' Welcher Artikel?",
    "options":["ein","einen","einem"],
    "correct":0,
    "explanation":"'Schüler' ist maskulin. Nominativ nach 'sein': unbestimmter Artikel 'ein'."
  },
  {
    "id":505,"test":5,"teil":1,"type":"mc",
    "question":"Was ist 'die Bewerbung'?",
    "options":["Ein formeller Antrag auf eine Arbeitsstelle oder einen Studienplatz","Eine Urlaubsanfrage","Ein Kündigungsschreiben"],
    "correct":0,
    "explanation":"Eine Bewerbung ist ein formeller Antrag, bei dem man sich für eine Stelle oder einen Platz vorstellt."
  },
  {
    "id":506,"test":5,"teil":1,"type":"mc",
    "question":"'Ich hätte das Problem lösen _____.' Welche Form?",
    "options":["gelöst","lösen","zu lösen"],
    "correct":1,
    "explanation":"Modalverben im Konjunktiv II mit Infinitiv: 'hätte … lösen können'."
  },
  {
    "id":507,"test":5,"teil":1,"type":"mc",
    "question":"Was bedeutet 'selbstständig'?",
    "options":["Abhängig von anderen","Eigenständig und unabhängig handelnd","Sehr müde"],
    "correct":1,
    "explanation":"'Selbstständig' bedeutet, unabhängig und auf eigene Initiative zu handeln."
  },
  {
    "id":508,"test":5,"teil":1,"type":"mc",
    "question":"'Das Konzert findet _____ Samstag statt.' Welche Präposition?",
    "options":["am","an","im"],
    "correct":0,
    "explanation":"Bei Wochentagen: 'am' + Wochentag. 'Am Samstag' ist die korrekte Formulierung."
  },
  {
    "id":509,"test":5,"teil":1,"type":"mc",
    "question":"Was ist 'die Elternzeit'?",
    "options":["Urlaub für kranke Arbeitnehmer","Bezahlte Auszeit nach der Geburt eines Kindes","Urlaub für Großeltern"],
    "correct":1,
    "explanation":"Die Elternzeit ist eine gesetzlich geregelte, teilweise bezahlte Auszeit nach der Geburt."
  },
  {
    "id":510,"test":5,"teil":1,"type":"mc",
    "question":"'_____ des Regens gingen sie spazieren.' Welche Präposition?",
    "options":["Trotz","Wegen","Weil"],
    "correct":0,
    "explanation":"'Trotz' + Genitiv drückt einen Gegensatz aus: Spazieren trotz Regen."
  },
  {
    "id":511,"test":5,"teil":1,"type":"mc",
    "question":"Was bedeutet 'angespannt'?",
    "options":["Entspannt und gelassen","Nervös oder unter Druck stehend","Sehr hungrig"],
    "correct":1,
    "explanation":"'Angespannt' beschreibt einen Zustand von innerer Anspannung oder Nervosität."
  },
  {
    "id":512,"test":5,"teil":1,"type":"mc",
    "question":"'Er hat den ganzen Tag gearbeitet, _____ Pausen einzulegen.' Welche Konstruktion?",
    "options":["ohne","ohne zu","nicht zu"],
    "correct":1,
    "explanation":"'Ohne zu + Infinitiv' drückt aus, dass etwas nicht getan wird: 'ohne Pausen einzulegen'."
  },
  {
    "id":513,"test":5,"teil":1,"type":"mc",
    "question":"Was ist 'die Kaution'?",
    "options":["Eine monatliche Mietzahlung","Eine Sicherheitsleistung beim Mietvertrag","Eine Mahngebühr"],
    "correct":1,
    "explanation":"Die Kaution ist eine Sicherheitsleistung (meist 2–3 Monatsmieten), die bei Mietbeginn gezahlt wird."
  },
  {
    "id":514,"test":5,"teil":1,"type":"mc",
    "question":"'Er tut so, _____ ob er schliefe.' Welche Konstruktion?",
    "options":["als","als ob","wie ob"],
    "correct":1,
    "explanation":"'Als ob' + Konjunktiv II ist die korrekte Konstruktion für einen irrealen Vergleich."
  },
  {
    "id":515,"test":5,"teil":1,"type":"mc",
    "question":"Was bedeutet 'akzeptieren'?",
    "options":["Ablehnen und widersprechen","Etwas hinnehmen oder einverstanden sein","Protestieren"],
    "correct":1,
    "explanation":"'Akzeptieren' bedeutet, etwas anzunehmen oder mit etwas einverstanden zu sein."
  },
  {
    "id":516,"test":5,"teil":1,"type":"mc",
    "question":"'Ich bin _____ Meinung, dass…' Welcher Artikel?",
    "options":["der","in der","von der"],
    "correct":0,
    "explanation":"'Ich bin der Meinung, dass…' ist die feste idiomatische Redewendung im Deutschen."
  },
  {
    "id":517,"test":5,"teil":1,"type":"mc",
    "question":"Was ist 'das Ehrenamt'?",
    "options":["Ein bezahlter Nebenjob","Eine freiwillige, unbezahlte Tätigkeit für die Gemeinschaft","Ein staatliches Amt"],
    "correct":1,
    "explanation":"Das Ehrenamt ist eine freiwillige, unentgeltliche Tätigkeit zum Wohl der Gemeinschaft."
  },
  {
    "id":518,"test":5,"teil":1,"type":"mc",
    "question":"'Das Gerät wurde _____ repariert.' Welches Adverb passt am besten?",
    "options":["gestern","längst","morgen"],
    "correct":1,
    "explanation":"'Längst' bedeutet 'schon vor langer Zeit': 'Das Gerät wurde längst repariert.'"
  },
  {
    "id":519,"test":5,"teil":1,"type":"mc",
    "question":"Was bedeutet 'schlüssig'?",
    "options":["Widersprüchlich und verwirrend","Logisch, folgerichtig und überzeugend","Sehr langsam"],
    "correct":1,
    "explanation":"'Schlüssig' bedeutet, dass etwas logisch und in sich stimmig ist."
  },
  {
    "id":520,"test":5,"teil":1,"type":"mc",
    "question":"'Er hat sich _____ die Stelle beworben.' Welches Pronomen + Präposition?",
    "options":["ihm um","sich um","ihn für"],
    "correct":1,
    "explanation":"'Sich bewerben um' + Akkusativ ist die feste Verbindung: 'Er hat sich um die Stelle beworben.'"
  },

  # ── Teil 2: Richtig / Falsch ──────────────────────────────────────────────
  {
    "id":521,"test":5,"teil":2,"type":"rf",
    "context":"Veranstaltungshinweis:\n\nFotoausstellung 'Licht und Schatten'\nKünstlerin: Anna Bauer\nOrt: Galerie am Markt, Würzburg\nÖffnungszeiten: Di–So, 10–18 Uhr\nEintritt frei\nFinissage: Sonntag, 30. April, 17 Uhr (mit Künstlergespräch)",
    "question":"Die Ausstellung ist montags geöffnet.",
    "correct":False,
    "explanation":"Falsch. Die Galerie hat Dienstag bis Sonntag geöffnet — montags nicht."
  },
  {
    "id":522,"test":5,"teil":2,"type":"rf",
    "context":"(Gleiche Ausstellungsinfo wie Aufgabe 521)",
    "question":"Der Eintritt zur Ausstellung ist kostenlos.",
    "correct":True,
    "explanation":"Richtig. Im Hinweis steht ausdrücklich: 'Eintritt frei.'"
  },
  {
    "id":523,"test":5,"teil":2,"type":"rf",
    "context":"Reiserücktrittsversicherung:\n\nVersicherte Risiken: Krankheit, Unfall, Todesfall in der Familie. Nicht versichert: freiwillige Stornierung, Reiseunlust oder Jobverlust. Erstattung bis zu 100 % des Reisepreises. Meldung innerhalb von 24 Stunden nach Schadenseintritt erforderlich.",
    "question":"Wenn jemand keine Lust mehr auf die Reise hat, erstattet die Versicherung die Kosten.",
    "correct":False,
    "explanation":"Falsch. 'Reiseunlust' ist ausdrücklich nicht versichert."
  },
  {
    "id":524,"test":5,"teil":2,"type":"rf",
    "context":"(Gleiche Versicherungsbedingungen wie Aufgabe 523)",
    "question":"Im Todesfall eines Familienmitglieds wird der Reisepreis erstattet.",
    "correct":True,
    "explanation":"Richtig. 'Todesfall in der Familie' ist als versichertes Risiko aufgeführt."
  },
  {
    "id":525,"test":5,"teil":2,"type":"rf",
    "context":"Stadtbibliothek Würzburg — Neuerungen:\n\nAb sofort: Neue App für digitale Ausleihe. Bis zu 5 E-Books gleichzeitig ausleihbar. Ausleihdauer: 14 Tage, einmal verlängerbar. Physische Bücher weiterhin bis zu 4 Wochen ausleihbar. App-Registrierung kostenlos mit Bibliotheksausweis.",
    "question":"Mit der App können bis zu 10 E-Books gleichzeitig ausgeliehen werden.",
    "correct":False,
    "explanation":"Falsch. Es können nur bis zu 5 E-Books gleichzeitig ausgeliehen werden."
  },
  {
    "id":526,"test":5,"teil":2,"type":"rf",
    "context":"(Gleiche Bibliotheksinfo wie Aufgabe 525)",
    "question":"Physische Bücher dürfen länger ausgeliehen werden als E-Books.",
    "correct":True,
    "explanation":"Richtig. Physische Bücher: 4 Wochen; E-Books: 14 Tage. Physische Bücher also länger."
  },
  {
    "id":527,"test":5,"teil":2,"type":"rf",
    "context":"Pressemitteilung des Stadtrats:\n\nDer Stadtrat hat beschlossen, das alte Freibad zu renovieren statt es abzureißen. Die Kosten werden auf 4,2 Millionen Euro geschätzt. Die Bauarbeiten beginnen im Frühjahr. Das Freibad bleibt während der gesamten Bauzeit geschlossen.",
    "question":"Das Freibad wird abgerissen und durch einen Neubau ersetzt.",
    "correct":False,
    "explanation":"Falsch. Der Stadtrat hat beschlossen, das Freibad zu renovieren, nicht abzureißen."
  },
  {
    "id":528,"test":5,"teil":2,"type":"rf",
    "context":"(Gleiche Pressemitteilung wie Aufgabe 527)",
    "question":"Das Freibad ist während der Renovierung für die Öffentlichkeit geschlossen.",
    "correct":True,
    "explanation":"Richtig. Im Text steht: 'Das Freibad bleibt während der gesamten Bauzeit geschlossen.'"
  },
  {
    "id":529,"test":5,"teil":2,"type":"rf",
    "context":"Produktrückruf:\n\nDie Firma Gesund GmbH ruft den Salatdressing-Mix 'Kräutergarten 200 g' (Charge: A2204) freiwillig zurück. Grund: mögliche Verunreinigung mit nicht deklarierten Erdnussspuren. Betroffene Produkte bitte nicht verzehren und im Markt zurückgeben. Rückerstattung auch ohne Kassenbon möglich.",
    "question":"Das Produkt wird zurückgerufen, weil es verdorben ist.",
    "correct":False,
    "explanation":"Falsch. Der Rückruf erfolgt wegen nicht deklarierter Erdnussspuren — nicht wegen Verderbs."
  },
  {
    "id":530,"test":5,"teil":2,"type":"rf",
    "context":"(Gleicher Produktrückruf wie Aufgabe 529)",
    "question":"Das Produkt kann auch ohne Kassenbon zurückgegeben werden.",
    "correct":True,
    "explanation":"Richtig. 'Rückerstattung auch ohne Kassenbon möglich' steht ausdrücklich im Text."
  },

  # ── Teil 3: Leseverstehen / Textauswahl ──────────────────────────────────
  {
    "id":531,"test":5,"teil":3,"type":"text",
    "context":"TEXT A — Mehrsprachigkeit in Deutschland\nIn Deutschland spricht ein großer Teil der Bevölkerung zu Hause eine andere Sprache als Deutsch. Lange wurde das vor allem als Herausforderung gesehen, heute betrachten viele Fachleute Mehrsprachigkeit zunehmend als Ressource. Studien zeigen, dass mehrsprachige Kinder oft eine hohe kognitive Flexibilität entwickeln und leichter zwischen verschiedenen Denksystemen wechseln können. Entscheidend ist dabei, dass Schulen und Familien diese Fähigkeiten gezielt fördern.\n\nTEXT B — Deutsch als Fremdsprache\nDeutsch ist eine der wichtigsten Unterrichtssprachen in Europa und wird weltweit von Millionen Menschen gelernt. Besonders in Mittel- und Osteuropa sowie in Teilen Asiens ist das Interesse an Deutschkursen groß. Deutschland und Österreich investieren deshalb stark in Sprachförderung im Ausland, etwa durch Kulturinstitute, Austauschprogramme und digitale Lernangebote. Für viele Lernende ist Deutsch vor allem wegen Studium, Beruf und Migration attraktiv.\n\nTEXT C — Dialekte in Deutschland\nDeutschland hat eine reiche Dialektlandschaft mit regionalen Varianten wie Bairisch, Schwäbisch oder Plattdeutsch. Dialekte schaffen Identität, Verbundenheit und ein Gefühl kultureller Herkunft. Gleichzeitig werden sie im Berufsleben, in den Medien und im öffentlichen Raum seltener verwendet als früher. Vor allem jüngere Menschen sprechen häufiger Standarddeutsch, obwohl viele Familien und Regionen versuchen, ihre sprachlichen Traditionen bewusst zu bewahren.",
    "question":"In welchem Text wird Mehrsprachigkeit als Vorteil für Kinder beschrieben?",
    "options":["Text A — kognitive Vorteile","Text B","Text C"],
    "correct":0,
    "explanation":"Text A erwähnt, dass mehrsprachige Kinder bessere kognitive Flexibilität entwickeln."
  },
  {
    "id":532,"test":5,"teil":3,"type":"text",
    "context":"(Gleiche Texte A, B, C wie Aufgabe 531)",
    "question":"In welchem Text werden regionale Sprachvarianten behandelt?",
    "options":["Text A","Text B","Text C — Dialekte"],
    "correct":2,
    "explanation":"Text C beschreibt die verschiedenen deutschen Dialekte und ihren Rückgang."
  },
  {
    "id":533,"test":5,"teil":3,"type":"text",
    "context":"(Gleiche Texte A, B, C wie Aufgabe 531)",
    "question":"In welchem Text geht es um die globale Verbreitung der deutschen Sprache?",
    "options":["Text A","Text B — Deutsch weltweit","Text C"],
    "correct":1,
    "explanation":"Text B beschreibt, wie viele Menschen weltweit Deutsch lernen und wie es gefördert wird."
  },
  {
    "id":534,"test":5,"teil":3,"type":"text",
    "context":"TEXT D — Stadtplanung der Zukunft\nModerne Städte setzen zunehmend auf Schwammstadt-Konzepte, um sich besser an den Klimawandel anzupassen. Grünflächen, Bäume und durchlässige Böden speichern Regenwasser, kühlen die Umgebung und entlasten die Kanalisation bei Starkregen. So sollen Hitzewellen und Überschwemmungen besser bewältigt werden. Stadtplaner sehen darin eine wichtige Strategie, um dicht bebaute Räume lebenswerter und widerstandsfähiger zu machen.\n\nTEXT E — Smart City\nSmarte Städte nutzen Daten und Technologie, um Verkehr, Energieversorgung und Abfallwirtschaft effizienter zu steuern. Sensoren messen zum Beispiel Luftqualität, Verkehrsfluss oder Energieverbrauch in Echtzeit und liefern wichtige Informationen für die Planung. Dadurch lassen sich Probleme schneller erkennen und Ressourcen gezielter einsetzen. Gleichzeitig bleibt Datenschutz ein zentrales Thema, weil viele Bürger nicht möchten, dass zu viele Daten über ihren Alltag gesammelt werden.\n\nTEXT F — Neue Wohnformen\nCo-Living-Konzepte und Tiny Houses liegen im Trend, besonders in Städten mit hohen Mieten und wenig Wohnraum. Menschen teilen Gemeinschaftsflächen wie Küchen, Arbeitsräume oder Gärten und reduzieren bewusst ihren privaten Platzbedarf. Dadurch sinken Kosten, und soziale Kontakte entstehen oft leichter als in anonymen Wohnanlagen. Befürworter sehen darin eine flexible Antwort auf neue Lebensstile und veränderte Wohnbedürfnisse.",
    "question":"In welchem Text wird Technologie für ein besseres Stadtmanagement beschrieben?",
    "options":["Text D","Text E — Smart City","Text F"],
    "correct":1,
    "explanation":"Text E beschreibt, wie Daten und Technologie Städte effizienter und intelligenter machen."
  },
  {
    "id":535,"test":5,"teil":3,"type":"text",
    "context":"(Gleiche Texte D, E, F wie Aufgabe 534)",
    "question":"Welcher Text beschreibt Lösungen gegen extreme Wetterereignisse?",
    "options":["Text D — Schwammstadt","Text E","Text F"],
    "correct":0,
    "explanation":"Text D beschreibt das Schwammstadt-Konzept als Lösung gegen Hitzewellen und Überschwemmungen."
  },
  {
    "id":536,"test":5,"teil":3,"type":"text",
    "context":"(Gleiche Texte D, E, F wie Aufgabe 534)",
    "question":"In welchem Text wird günstigeres Wohnen durch Teilen beschrieben?",
    "options":["Text D","Text E","Text F — Co-Living und Tiny Houses"],
    "correct":2,
    "explanation":"Text F beschreibt Co-Living und Tiny Houses als kostensparende Wohnformen."
  },
  {
    "id":537,"test":5,"teil":3,"type":"text",
    "context":"TEXT G — Burnout und Erholung\nBurnout ist eine ernsthafte Folge von chronischem Stress, der über lange Zeit nicht ausreichend verarbeitet wird. Typische Symptome sind tiefe Erschöpfung, Motivationsverlust, Konzentrationsprobleme und eine zunehmend zynische Haltung gegenüber der Arbeit. Fachleute betonen, dass bloße Erholung am Wochenende oft nicht ausreicht. Therapie und Prävention erfordern meist Auszeiten, psychologische Unterstützung und langfristige Veränderungen im Lebensstil.\n\nTEXT H — Achtsamkeit und Meditation\nAchtsamkeitsübungen und Meditation gelten inzwischen als wirksame Mittel gegen Stress, innere Unruhe und Angst. Viele Menschen nutzen dafür Apps wie Headspace oder Calm, weil sie Übungen einfach in den Alltag integrieren können. Auch Unternehmen und Krankenkassen bieten zunehmend entsprechende Kurse an. Ziel ist es, Gedanken bewusster wahrzunehmen, besser mit Belastungen umzugehen und geistig schneller zur Ruhe zu kommen.\n\nTEXT I — Sport als Stressbewältigung\nKörperliche Aktivität hilft nachweislich dabei, Stresshormone abzubauen und die Stimmung zu verbessern. Schon etwa 30 Minuten moderater Bewegung pro Tag, etwa Spazierengehen, Radfahren oder Joggen, können positive Effekte auf die psychische Gesundheit haben. Sport stärkt außerdem das Körpergefühl und fördert besseren Schlaf. Deshalb empfehlen viele Ärzte Bewegung als wichtigen Baustein im Umgang mit Alltagsstress.",
    "question":"Welcher Text empfiehlt körperliche Aktivität als Mittel gegen Stress?",
    "options":["Text G","Text H","Text I — Sport gegen Stress"],
    "correct":2,
    "explanation":"Text I beschreibt, wie Sport Stresshormone abbaut und die Stimmung verbessert."
  },
  {
    "id":538,"test":5,"teil":3,"type":"text",
    "context":"(Gleiche Texte G, H, I wie Aufgabe 537)",
    "question":"In welchem Text werden digitale Hilfsmittel zur Entspannung erwähnt?",
    "options":["Text G","Text H — Meditations-Apps","Text I"],
    "correct":1,
    "explanation":"Text H erwähnt Apps wie Headspace und Calm als digitale Achtsamkeitshilfen."
  },
  {
    "id":539,"test":5,"teil":3,"type":"text",
    "context":"(Gleiche Texte G, H, I wie Aufgabe 537)",
    "question":"In welchem Text werden Symptome einer arbeitsbedingten Erkrankung beschrieben?",
    "options":["Text G — Burnout-Symptome","Text H","Text I"],
    "correct":0,
    "explanation":"Text G listet Burnout-Symptome auf: Erschöpfung, Motivationsverlust, Zynismus."
  },
  {
    "id":540,"test":5,"teil":3,"type":"text",
    "context":"TEXT J — Tierschutz in Deutschland\nDeutschland hat eines der strengsten Tierschutzgesetze der Welt, doch in der Praxis bestehen weiterhin große Probleme. Millionen Nutztiere leben unter Bedingungen, die von Tierschutzorganisationen seit Jahren kritisiert werden. Besonders in der industriellen Massentierhaltung sehen Experten erhebliche Missstände. Deshalb fordern Verbände strengere Kontrollen, härtere Strafen und bessere Standards für Haltung, Transport und Schlachtung.\n\nTEXT K — Haustiere und Einsamkeit\nStudien zeigen, dass Haustierbesitzer sich oft weniger einsam fühlen und emotional stabiler sind. Besonders Hunde und Katzen bieten vielen Menschen Nähe, Struktur im Alltag und das Gefühl, gebraucht zu werden. In Altenheimen oder Kliniken werden deshalb gezielt Therapietiere eingesetzt. Fachleute betonen, dass Tiere menschliche Beziehungen nicht ersetzen, aber eine wichtige emotionale Unterstützung sein können.\n\nTEXT L — Vegane Ernährung und Umwelt\nVegane Ernährung kann den CO₂-Fußabdruck deutlich reduzieren, weil pflanzliche Produkte meist weniger Wasser, Fläche und Energie benötigen als tierische. Deshalb sehen Umweltforscher in einer stärker pflanzlichen Ernährung großes Potenzial für den Klimaschutz. Kritiker weisen jedoch darauf hin, dass vegane Ernährung nicht für alle Menschen kulturell, finanziell oder praktisch gleich gut zugänglich ist. Auch hier spielen Bildung und soziale Bedingungen eine wichtige Rolle.",
    "question":"In welchem Text geht es um den emotionalen Nutzen von Tieren für Menschen?",
    "options":["Text J","Text K — Haustiere gegen Einsamkeit","Text L"],
    "correct":1,
    "explanation":"Text K beschreibt, wie Haustiere emotionale Unterstützung bieten und Einsamkeit reduzieren."
  },
  {
    "id":541,"test":5,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 540)",
    "question":"Welcher Text beschreibt den Zusammenhang zwischen Ernährung und Umweltschutz?",
    "options":["Text J","Text K","Text L — Vegane Ernährung und CO₂"],
    "correct":2,
    "explanation":"Text L beschreibt, wie vegane Ernährung den CO₂-Fußabdruck und Ressourcenverbrauch senkt."
  },
  {
    "id":542,"test":5,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 540)",
    "question":"Welcher Text kritisiert die Diskrepanz zwischen Tierschutzgesetz und Realität?",
    "options":["Text J — Gesetz vs. Praxis","Text K","Text L"],
    "correct":0,
    "explanation":"Text J: Trotz strengem Tierschutzgesetz leiden viele Tiere — Lücke zwischen Gesetz und Realität."
  },
  {
    "id":543,"test":5,"teil":3,"type":"text",
    "context":"(Gleiche Texte J, K, L wie Aufgabe 540)",
    "question":"In welchem Text werden auch Gegenargumente zu einer Lebensweise erwähnt?",
    "options":["Text J","Text K","Text L — Kritik an veganer Ernährung"],
    "correct":2,
    "explanation":"Text L erwähnt Kritiker, die sagen, vegane Ernährung sei nicht für alle zugänglich."
  },
  {
    "id":544,"test":5,"teil":3,"type":"text",
    "context":"(Alle Texte A bis L)",
    "question":"In welchen zwei Texten wird Einsamkeit als gesellschaftliches Problem angesprochen?",
    "options":["Texte A und B","Texte G und K","Texte D und F"],
    "correct":1,
    "explanation":"Text G (Burnout → soziale Isolation) und Text K (Haustiere gegen Einsamkeit) sprechen beide Einsamkeit an."
  },
  {
    "id":545,"test":5,"teil":3,"type":"text",
    "context":"(Alle Texte A bis L)",
    "question":"Welcher Text hilft jemandem am meisten, der lernen möchte, besser mit Stress umzugehen?",
    "options":["Text D — Stadtplanung","Text G oder Text H — Burnout und Achtsamkeit","Text J — Tierschutz"],
    "correct":1,
    "explanation":"Text G (Burnout-Prävention) und Text H (Achtsamkeits-Apps) bieten konkrete Hilfe bei Stress."
  },
]

# ═══════════════════════════════════════════════════════════════════════════
# COMBINED DICTIONARY
# ═══════════════════════════════════════════════════════════════════════════
ALL_TESTS = {
    1: TEST1,
    2: TEST2,
    3: TEST3,
    4: TEST4,
    5: TEST5,
}

def get_questions_for_test(test_number: int):
    return ALL_TESTS.get(test_number, [])

def get_all_questions():
    result = []
    for t in range(1, 6):
        result.extend(ALL_TESTS[t])
    return result

QUESTIONS = get_questions_for_test(1)  # backward compatibility

# ═══════════════════════════════════════════════════════════════════
# TEIL 4 — SCHREIBEN (Brief schreiben) — 1 Aufgabe pro Test
# Format entspricht dem echten Goethe B1-Prüfungsformat:
# - Situation beschreiben
# - 4 Leitpunkte bearbeiten
# - 150-200 Wörter
# ═══════════════════════════════════════════════════════════════════

SCHREIBEN_AUFGABEN = {
    1: {
        "test": 1,
        "teil": 4,
        "type": "schreiben",
        "thema": "Brief an einen Freund — Einladung zu einer Party absagen",
        "situation": (
            "Sie haben eine Einladung zu einer Geburtstagsparty von Ihrem Freund Max bekommen. "
            "Leider können Sie nicht kommen. Schreiben Sie Max einen Brief und erklären Sie, "
            "warum Sie nicht kommen können."
        ),
        "leitpunkte": [
            "Bedanken Sie sich für die Einladung.",
            "Erklären Sie, warum Sie nicht kommen können.",
            "Machen Sie einen anderen Vorschlag (wann Sie sich treffen können).",
            "Wünschen Sie ihm alles Gute für die Party.",
        ],
        "hinweise": "Schreiben Sie 150–200 Wörter. Vergessen Sie Anrede und Grußformel nicht.",
        "beispiel_anrede": "Lieber Max,",
        "beispiel_gruss": "Viele Grüße,\n[Ihr Name]",
        "bewertungskriterien": [
            "Wurden alle 4 Leitpunkte bearbeitet?",
            "Ist der Brief logisch aufgebaut?",
            "Ist die Sprache dem Anlass angemessen?",
            "Sind Grammatik und Rechtschreibung korrekt?",
        ],
        "woerter_min": 150,
        "woerter_max": 200,
    },
    2: {
        "test": 2,
        "teil": 4,
        "type": "schreiben",
        "thema": "Brief an einen Vermieter — Wohnungsprobleme melden",
        "situation": (
            "Sie wohnen seit drei Monaten in einer neuen Wohnung. "
            "Es gibt mehrere Probleme: Die Heizung funktioniert nicht richtig und "
            "im Bad gibt es einen Wasserschaden. Schreiben Sie einen Brief an Ihren Vermieter, "
            "Herrn Bauer."
        ),
        "leitpunkte": [
            "Stellen Sie sich kurz vor (Name, Wohnung).",
            "Beschreiben Sie die Probleme in der Wohnung.",
            "Bitten Sie um schnelle Hilfe.",
            "Geben Sie an, wann Sie erreichbar sind.",
        ],
        "hinweise": "Schreiben Sie 150–200 Wörter. Benutzen Sie eine formelle Anrede und Grußformel.",
        "beispiel_anrede": "Sehr geehrter Herr Bauer,",
        "beispiel_gruss": "Mit freundlichen Grüßen,\n[Ihr Name]",
        "bewertungskriterien": [
            "Wurden alle 4 Leitpunkte bearbeitet?",
            "Ist der Ton formell und angemessen?",
            "Ist der Brief logisch strukturiert?",
            "Sind Grammatik und Rechtschreibung korrekt?",
        ],
        "woerter_min": 150,
        "woerter_max": 200,
    },
    3: {
        "test": 3,
        "teil": 4,
        "type": "schreiben",
        "thema": "Brief an einen Arbeitgeber — Krankmeldung",
        "situation": (
            "Sie sind krank und können nicht zur Arbeit kommen. "
            "Schreiben Sie eine E-Mail / einen Brief an Ihre Chefin, Frau Schmidt, "
            "und informieren Sie sie über Ihre Situation."
        ),
        "leitpunkte": [
            "Erklären Sie, dass Sie krank sind und nicht kommen können.",
            "Beschreiben Sie kurz Ihre Symptome.",
            "Informieren Sie, ob Sie einen Arzt besucht haben.",
            "Geben Sie an, wann Sie voraussichtlich zurückkommen.",
        ],
        "hinweise": "Schreiben Sie 150–200 Wörter. Achten Sie auf einen formellen Ton.",
        "beispiel_anrede": "Sehr geehrte Frau Schmidt,",
        "beispiel_gruss": "Mit freundlichen Grüßen,\n[Ihr Name]",
        "bewertungskriterien": [
            "Wurden alle 4 Leitpunkte bearbeitet?",
            "Ist der Ton höflich und professionell?",
            "Ist der Brief klar und verständlich?",
            "Sind Grammatik und Rechtschreibung korrekt?",
        ],
        "woerter_min": 150,
        "woerter_max": 200,
    },
    4: {
        "test": 4,
        "teil": 4,
        "type": "schreiben",
        "thema": "Brief an einen Kurs-Anbieter — Kursanmeldung",
        "situation": (
            "Sie möchten einen Deutschkurs auf dem Niveau B2 an der Volkshochschule besuchen. "
            "Schreiben Sie einen Brief an die Volkshochschule und fragen Sie nach dem Kurs."
        ),
        "leitpunkte": [
            "Erklären Sie, warum Sie sich für den Kurs interessieren.",
            "Fragen Sie nach den Kurszeiten und Kosten.",
            "Fragen Sie, ob Vorkenntnisse erforderlich sind.",
            "Bitten Sie um Informationen zur Anmeldung.",
        ],
        "hinweise": "Schreiben Sie 150–200 Wörter. Verwenden Sie eine formelle Anrede.",
        "beispiel_anrede": "Sehr geehrte Damen und Herren,",
        "beispiel_gruss": "Mit freundlichen Grüßen,\n[Ihr Name]",
        "bewertungskriterien": [
            "Wurden alle 4 Leitpunkte bearbeitet?",
            "Ist der Brief formell und höflich?",
            "Sind alle relevanten Informationen enthalten?",
            "Sind Grammatik und Rechtschreibung korrekt?",
        ],
        "woerter_min": 150,
        "woerter_max": 200,
    },
    5: {
        "test": 5,
        "teil": 4,
        "type": "schreiben",
        "thema": "Brief an die Stadtverwaltung — Beschwerde über Lärm",
        "situation": (
            "In Ihrer Straße wird seit Wochen nachts sehr laut gefeiert. "
            "Sie können nicht schlafen. Schreiben Sie einen Beschwerdebrief "
            "an das Ordnungsamt Ihrer Stadt."
        ),
        "leitpunkte": [
            "Beschreiben Sie das Problem (Lärm, wann, wie oft).",
            "Erklären Sie, wie das Problem Ihren Alltag beeinflusst.",
            "Fragen Sie, was das Ordnungsamt dagegen tun kann.",
            "Bitten Sie um eine schnelle Reaktion.",
        ],
        "hinweise": "Schreiben Sie 150–200 Wörter. Bleiben Sie höflich, auch wenn Sie sich beschweren.",
        "beispiel_anrede": "Sehr geehrte Damen und Herren,",
        "beispiel_gruss": "Mit freundlichen Grüßen,\n[Ihr Name]",
        "bewertungskriterien": [
            "Wurden alle 4 Leitpunkte bearbeitet?",
            "Ist der Ton sachlich und höflich?",
            "Ist die Beschwerde klar formuliert?",
            "Sind Grammatik und Rechtschreibung korrekt?",
        ],
        "woerter_min": 150,
        "woerter_max": 200,
    },
}
