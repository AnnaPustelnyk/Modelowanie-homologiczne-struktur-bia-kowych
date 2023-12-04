from modeller import *
from modeller.automodel import *

env = Environ()
a = AutoModel(env, alnfile='fasta.fa',
              knowns=('3J4Q', '4WIH', '6F14', '6Y05', ), sequence='seq')
a.starting_model = 1
a.ending_model = 4
a.make()
a.write('filepdb', format = 'PDB')
