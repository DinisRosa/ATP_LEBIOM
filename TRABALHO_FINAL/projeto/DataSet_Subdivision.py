# Subdivisão da base de dados para facilitar pesquisa
def all_DOI_path(base: list) -> list:
    DOI_path = []
    for i, pub in enumerate(base):
        if 'doi' in pub.keys():
            DOI_path.append((pub['doi'][29:], i))
    return sorted(DOI_path, key=lambda tuplo: int(tuplo[0]))


def all_PublishDates(base: list) -> list:
    Pub_Dates = []
    for i, pub in enumerate(base):
        if 'publish_date' in pub.keys():
            Pub_Dates.append((pub['publish_date'][:11], i))
            
    return sorted(Pub_Dates, key=lambda data: int(data[0].split('-')[0] + data[0].split('-')[1] + data[0].split('-')[2]))


def all_KeyWords(base: list) -> list:
    KeyWords = []
    for i, pub in enumerate(base):
        if 'keywords' in pub.keys():
                KeyWords.append(''.join(char for char in pub['keywords'] if char not in '!,?'))
                KeyWords.append((pub['keywords'].split(','), i))
    return KeyWords

def all_KeyWords2(base: list) -> dict:
    KeyWordsDict:dict = {}
    for i, pub in enumerate(base):
        if 'authors' in pub.keys():
            pubKeyWords = ''.join(char for char in pub['keywords'] if char not in '!,?').split(',')
    return KeyWordsDict


'''def all_Authors(base: list) -> list:
    Authors = []
    for i, pub in enumerate(base):
        if 'authors' in pub.keys():
            Authors.append(([nome['name'] for nome in pub['authors']], i))
    return Authors'''

def all_Authors(base: list) -> dict:
    AuthorsDict: dict = {}
    for i, pub in enumerate(base):
        if 'authors' in pub.keys():
            pubAuthors = [nome['name'] for nome in pub['authors']]
            for author in pubAuthors:
                if author not in AuthorsDict:
                    AuthorsDict[author] = [i]
                else:
                    AuthorsDict[author].append(i)
    return AuthorsDict