import requests, bs4, time

baseUrl = 'http://www.genecards.org/'

def getEnsemblGene(gene):
    """Find ENSG for this gene.
       Look in HGNC aliases for this gene name."""
    searchUrl = baseUrl + 'Search/Keyword?queryString=%s' % (gene, )
    response = requests.get(searchUrl)
    soup = bs4.BeautifulSoup(response.text)
    links = soup.find_all("td", class_="gc-gene-symbol")
    ensemblGeneSet = set()
    i = 0
    for link in links:
        for item in link:
            name = str(item).split('data-ga-label="')[1].split('"')[0]
            href = baseUrl + str(item).split('href="')[1].split('"')[0].split('&')[0]
            time.sleep(2)
            newHtml = requests.get(href)
            hgncAliasSet = getPreviousHGNC(newHtml)
            time.sleep(2)
            ensemblSet = mkEnsemblSet(newHtml)
            if name == gene or gene in hgncAliasSet:
                ensemblGeneSet |= ensemblSet
            if i:
                time.sleep(2)
            i += 1
    return ensemblGeneSet

def mkEnsemblSet(href_html):
    """Return ENSG ID in this gene cards page."""
    ensemblGeneSet = set()
    soup2 = bs4.BeautifulSoup(href_html.text)
    links2 = soup2.find_all("a", class_="gc-ga-link")
    for link2 in links2:
        if 'ensembl' in str(link2) and 'geneview' in str(link2):
            ensemblGene = str(link2).split('gene=')[1].split('"')[0]
            ensemblGeneSet.add(ensemblGene)
    return ensemblGeneSet

def getPreviousHGNC(geneUrl_html):
    """Return all HGNC aliases in this genecards page."""
    hgncAlias = set()
    soup = bs4.BeautifulSoup(geneUrl_html.text)
    links = soup.find_all("div", class_="gc-subsection")
    for link in links:
        links2 = link.find_all("h3")
        if 'Previous HGNC Symbols' in str(links2):
            links3 = link.find_all("li")
            for item in links3:
                hgncAlias.add( item.getText() )
    return hgncAlias

#gene = 'ADAM1'
#print getEnsemblGene(gene) #getPreviousHGNC('http://www.genecards.org/cgi-bin/carddisp.pl?gene=BOD1L1')
