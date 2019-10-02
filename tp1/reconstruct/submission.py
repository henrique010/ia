import shell
import util
import wordsegUtil

############################################################
# Problema 1: Segmentacao de Palavras com funcao de custo 'unigram'

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        # BEGIN_YOUR_CODE (solucao em 1 linha de codigo, mas utilize quantas linhas julgar necessario)
        return self.query

        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def isEnd(self, state):
        # BEGIN_YOUR_CODE (solucao em 2 linhas de codigo, mas utilize quantas linhas julgar necessario)
        return state == ''

        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (solucao em 7 linhas de codigo, mas utilize quantas linhas julgar necessario)
        aux = []
        i = 0
        while i < (len(state) + 1): 
            aux.append((state[0:i], state[i:], self.unigramCost(state[0:i])))
            i = i + 1
        return aux

        raise Exception("Not implemented yet")
        # END_YOUR_CODE

def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    # BEGIN_YOUR_CODE (solucao em 3 linhas de codigo, mas utilize quantas linhas julgar necessario)
    if (len(ucs.actions) > 0 ):
        return ' '.join(ucs.actions)
    else:
        return query

    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problema 2: Insercao de Vogais com custo 'bigram'

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (solucao em 1 linha de codigo, mas utilize quantas linhas julgar necessario)
        if ( len(self.queryWords) > 0 ) :
            return (0,(wordsegUtil.SENTENCE_BEGIN, self.queryWords[0]))
        else:
            return (0,(wordsegUtil.SENTENCE_BEGIN,))

        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def isEnd(self, state):
        # BEGIN_YOUR_CODE (solucao em 2 linhas de codigo, mas utilize quantas linhas julgar necessario)
        return state[0] == len(self.queryWords)

        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (solucao em 8 linhas de codigo, mas utilize quantas linhas julgar necessario)
        aux = []
        fills = self.possibleFills(state[1][1])
        newIndx = state[0]+1
        if newIndx >= len(self.queryWords):
            nextSegment = None
        else:
            nextSegment = self.queryWords[newIndx]
        if len(fills) == 0 :
            fills.add(state[1][1])

        for f in fills:
            filledState = (newIndx, (state[1][0],f))
            aux.append((f, (newIndx,(f,nextSegment)), self.bigramCost(state[1][0], f)))
        return aux

        raise Exception("Not implemented yet")
        # END_YOUR_CODE

def insertVowels(queryWords, bigramCost, possibleFills):
    ucs = util.UniformCostSearch()
    ucs.solve(VowelInsertionProblem(queryWords, bigramCost, possibleFills))
    # BEGIN_YOUR_CODE (solucao em 3 linhas de codigo, mas utilize quantas linhas julgar necessario)
    return ' '.join(ucs.actions)

    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problema 3: Programa Integrado com custo 'bigram'

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (solucao em 1 linha de codigo, mas utilize quantas linhas julgar necessario)
        return (0, wordsegUtil.SENTENCE_BEGIN)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def isEnd(self, state):
        # BEGIN_YOUR_CODE (solucao em 2 linhas de codigo, mas utilize quantas linhas julgar necessario)
        return state[0] == len(self.query)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (solucao em 14 linhas de codigo, mas utilize quantas linhas julgar necessario)
        aux = []
        indx = state[0]
        currentword = state[1]
        for i in range(indx+1, len(self.query)+1):
            pretext = self.query[indx:i]
            fills = self.possibleFills(pretext)
            for f in fills:
                aux.append((f, (i, f), self.bigramCost(currentword, f)))
        return aux

        raise Exception("Not implemented yet")
        # END_YOUR_CODE

def segmentAndInsert(query, bigramCost, possibleFills):
    if len(query) == 0:
        return ''

    # BEGIN_YOUR_CODE (solucao em 4 linhas de codigo, mas utilize quantas linhas julgar necessario)
    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(JointSegmentationInsertionProblem(query, bigramCost, possibleFills))
    if ( ucs.actions is not None ) :
        return ' '.join(ucs.actions)
    else: 
        return ''

    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################

if __name__ == '__main__':
    shell.main()