import genecards

def testEnsemblGene():
    gene = 'BRAF'
    ensemblSet = genecards.getEnsemblGene(gene)
    nosetools.assert_true(len(ensemblSet) == 1)
    nosetools.assert_true(list(ensemblSet)[0] == 'ENSG00000157764')
    
