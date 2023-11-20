from adn import seq_alea, comp_inv, BASE_COMP

sequenceAdnAlea: str = seq_alea(100)
print(sequenceAdnAlea)
compSequenceAdnAlea: str = comp_inv(sequenceAdnAlea)
print(BASE_COMP)
print(compSequenceAdnAlea)