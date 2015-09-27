import requests, bs4

baseUrl = 'http://www.genecards.org/'

def getEnsemblGene(gene):
    searchUrl = baseUrl + 'Search/Keyword?queryString=%s' % (gene, )
    response = requests.get(searchUrl)
    soup = bs4.BeautifulSoup(response.text)
    links = soup.find_all("td", class_="gc-gene-symbol")
    ensemblGeneSet = set()
    for link in links:
        for item in link:
            name = str(item).split('data-ga-label="')[1].split('"')[0]
            href = baseUrl + str(item).split('href="')[1].split('"')[0].split('&')[0]
            if name == gene:
                response2 = requests.get(href)
                soup2 = bs4.BeautifulSoup(response2.text)
                links2 = soup2.find_all("a", class_="gc-ga-link")
                for link2 in links2:
                    if 'ensembl' in str(link2) and 'geneview' in str(link2):
                        ensemblGene = str(link2).split('gene=')[1].split('"')[0]
                        ensemblGeneSet.add(ensemblGene)
    return ensemblGeneSet
