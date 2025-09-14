CTF_TASKS = [
    {
        "id": 1,
        "title": "1974",
        "text": "Please enter the eight-digit code to activate launch:",
        "hint": None,
        "answer_text": "<eight-digit-code>",
        "answer": ["00000000", "OOOOOOOO"],
    },
    {
        "id": 2,
        "title": "Eternal",
        "text": "I 2017 frigjorde en hackergruppe en exploit i Windows-operativsystemet funnet av National Security Agency (NSA). Exploiten brukte en svakhet i Microsofts Server Message Block (SMB) protokoll og ble brukt av det man tror var nordkoreanske hackere til å utføre et stort cyberangrep. Hva var 'kill-switchen'?",
        "hint": "Kill switchen var et domene navn.",
        "answer_text": "<første-syv-tegn-i-kill-switchen>",
        "answer": ["iuqerfs", "iuqerfsodp9ifjaposdfjhgosurijfaewrwergwea.com"],
    },
    {
        "id": 3,
        "title": "ラベル",
        "text": "2018年、仮想通貨取引所コインチェックがハッキングされ、約580億円分のネムが盗まれました。盗まれたネムが送られたアドレスには、特別なラベルが付けられました。そのタグ名は何でしょうか？",
        "hint": None,
        "answer_text": "<eight-digit-code>",
        "answer": [
            "coincheck_stolen_funds_do_not_accept_trades : owner_of_this_account_is_hacker.",
            "coincheck_stolen_funds_do_not_accept_trades : owner_of_this_account_is_hacker",
            "coincheck_stolen_funds_do_not_accept_trades: owner_of_this_account_is_hacker.",
            "coincheck_stolen_funds_do_not_accept_trades: owner_of_this_account_is_hacker",
            "coincheck_stolen_funds_do_not_accept_trades:owner_of_this_account_is_hacker.",
            "coincheck_stolen_funds_do_not_accept_trades:owner_of_this_account_is_hacker",
            "coincheck_stolen_funds_do_not_accept_trades",
            "owner_of_this_account_is_hacker",
        ],
    },
    {
        "id": 4,
        "title": "Finn Sykkelen",
        "text": "Sykkelen min har blitt stjålet! Kan du hjelpe meg å finne den? Jeg mistet den da jeg var på ferie i USA i februar. Det var en rød FC-770.",
        "hint": None,
        "answer_text": "<navn-på-byen-med-sykkelen> ",
        "answer": ["portland"],
    },
    {
        "id": 5,
        "title": "Sha",
        "text": "97c10efe01d5c9c88704a12d361d8429b3a6aa2412290a0773109d5d2d603d5e",
        "hint": "Sha256",
        "answer_text": "<secret-password>",
        "answer": ["easy"],
    },
    {
        "id": 6,
        "title": "Strømmen på Slottet ",
        "text": "Kjerstin har vært på middag på Slottet, og etter for mange glass portvin, blitt enig om å dekke fjorårets strømregning. Hva var den på?",
        "hint": None,
        "answer_text": "<første-fire-siffer-i-strømregningen> ",
        "answer": ["6238", "6238985"],
    },
    {
        "id": 7,
        "title": "Pluss Én",
        "text": "Ryktene sier at tidligere finansdirektør Ida har kikket etter ny jobb en stund, men ingen vet når hun begynte å se seg om etter nye muligheter. En intern varsler har sendt deg en forkortet lenke som visstnok leder til LinkedIn-profilen hennes: https://bit.ly/4oHdfFy Når ble lenken laget?",
        "hint": None,
        "answer_text": "<dag-i-datoen>",
        "answer": ["15", "femten", "femtende"],
    },
]

CTF_ABOUT = """
Capture the Flag (CTF) er navnet på en generell type oppgave innen infromatikk der målet er å finne en kode, passord
eller liknende, som kalles "flagg". De fleste oppgavene i er innenfor kategorien "Open source intelligence" (OSINT),
som betyr at flaggene ligger blant offentlig tilgjengelig informasjon. Prøv å søke på internet med forskjellige
kombinasjoner av ord i tittelen og oppgaveteksten, og prøve å søke videre med spor dere finner underveis.
"""
