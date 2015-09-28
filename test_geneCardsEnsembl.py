import genecards, nose.tools

def testEnsemblGeneWithNoHgncAlias():
    """BRAF is the first genecards link, 
       and the genecards page is easily
       matched to BRAF."""
    gene = 'BRAF'
    ensemblSet = genecards.getEnsemblGene(gene)
    nose.tools.assert_true(len(ensemblSet) == 1)
    nose.tools.assert_true(list(ensemblSet)[0] == 'ENSG00000157764')

def testEnsemblGeneWithHgncAlias():
    """BOD1L is an old HGNC name for
       BOD1L1. An HGNC alias must be
       used to recognize input BOD1L as
       the BOD1L1 gene stored in genecards."""
    gene = 'BOD1L'
    ensemblSet = genecards.getEnsemblGene(gene)
    nose.tools.assert_true(len(ensemblSet) == 1)
    nose.tools.assert_true(list(ensemblSet)[0] == 'ENSG00000038219')

