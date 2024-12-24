# Subdivisão da base de dados para facilitar pesquisa
def all_DOI_path(base: list) -> dict:
    DoiPathDict: dict[str, list[int]] = {}
    for i, pub in enumerate(base):
        if 'doi' in pub.keys():
            doi_key: str = pub['doi'][29:]
            if doi_key not in DoiPathDict:
                DoiPathDict[doi_key] = [i]
            else:
                DoiPathDict[doi_key].append(i)
    return {k: DoiPathDict[k] for k in sorted(DoiPathDict)}


def all_PublishDates(base: list) -> dict:
    PubDatesDict: dict[str, list[int]] = {}
    for i, pub in enumerate(base):
        if 'publish_date' in pub.keys():
            date_key: str = pub['publish_date'][:11]
            if date_key not in PubDatesDict:
                PubDatesDict[date_key] = [i]
            else:
                PubDatesDict[date_key].append(i)
    return {k: PubDatesDict[k] for k in sorted(PubDatesDict)}


def all_KeyWords(base: list) -> dict:
    KeyWordsDict: dict[str, list[int]] = {}
    for i, pub in enumerate(base):
        if 'keywords' in pub.keys():
            pubKeyWords: list[str] = ''.join(char for char in pub['keywords'] if char not in '!.?').split(',')
            for key in pubKeyWords:
                if key[0] == ' ':
                    key = key[1:]
                if key not in KeyWordsDict:
                    KeyWordsDict[key] = [i]
                else:
                    KeyWordsDict[key].append(i)
    return {k: KeyWordsDict[k] for k in sorted(KeyWordsDict)}


def all_Authors(base: list) -> dict:
    AuthorsDict: dict[str, list[int]] = {}
    for i, pub in enumerate(base):
        if 'authors' in pub.keys():
            pubAuthors: list[str] = [nome['name'] for nome in pub['authors']]
            for author in pubAuthors:
                if author not in AuthorsDict:
                    AuthorsDict[author] = [i]
                else:
                    AuthorsDict[author].append(i)
    return {k: AuthorsDict[k] for k in sorted(AuthorsDict)}


def UpdateIndexes(base: list) -> tuple[dict, dict, dict, dict]:
    doiDict = all_DOI_path(base)
    pdDict = all_PublishDates(base)
    kwDict = all_KeyWords(base)
    autDict = all_Authors(base)
    return doiDict, pdDict, kwDict, autDict