import genecards, nose.tools, time

'''
Testing gene symbol to ensembl gene ID conversion.
'''

def subEnsemblGeneTest(gene, ensemblID):
    ensemblSet = genecards.getEnsemblGene(gene)
    nose.tools.assert_true(len(ensemblSet) == 1)
    nose.tools.assert_true(list(ensemblSet)[0] == ensemblID)
    time.sleep(2)

def testEnsemblGeneWithNoHgncAlias():
    """BRAF is the first genecards link.
       The genecards page is easily
       matched to BRAF."""
    gene = 'BRAF'
    ensemblGene = 'ENSG00000157764'
    subEnsemblGeneTest(gene, ensemblGene)

def testEnsemblGeneWithHgncAliasV1():
    """BOD1L is an old HGNC name for BOD1L1.
       An HGNC alias must be
       used to recognize input BOD1L as
       the BOD1L1 gene stored in genecards."""
    gene = 'BOD1L'
    ensemblGene = 'ENSG00000038219'
    subEnsemblGeneTest(gene, ensemblGene)
    
def testEnsemblGeneWithHgncAliasV2():
    """ADAM1 is an old HGNC name"""
    gene = 'ADAM1'
    ensemblGene = 'ENSG00000229186'
    subEnsemblGeneTest(gene, ensemblGene)

def testEnsemblGeneWithAlias():
    """LUST is an alias not found in genecard's HGNC list.
       I must locate the ensembl ID using the HGNC REST API."""
    gene = 'LUST'
    ensemblGene = 'ENSG00000281691'
    subEnsemblGeneTest(gene, ensemblGene)
