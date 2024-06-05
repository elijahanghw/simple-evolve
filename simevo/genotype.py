import numpy as np
import numba as nb
from simevo.utils import linmap
from scipy.stats import qmc

def get_genotype(length):
        genotype = np.random.uniform(low=-1, high=1, size=length)
        return genotype
