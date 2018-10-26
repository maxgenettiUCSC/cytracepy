"""
Plotting function for branch trajectories
"""


import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def branchPlot(expression, branches, genes):
   """Plots branch distance and gene expression
   
   Note:  This function requires the RNA expression TSV file and the Branch
      distance TSV file.  Optionally a TSV containing the list of genes of
      interest can be added.

   Args:
      expression: file name of RNA expression data n_cells x n_genes
      branches: file name of the branch distance n_branches x n_cells
      genes: File name of the genes of interest, n_empty x n_genes

   Returns:
      png of each branch of relative gene expression vs psudeotime
   """

   #iterates through each branch
   for branch in branches:

      #merges tables where cells are the index, then drops rows with NaN
      currentBranch = branches.filter([branch]).merge(expression, how = 'left', left_index = True, right_index = True)
      currentBranch = currentBranch.dropna()
   
     #plots each gene expressed in a current branch based on cell association
      for gene in currentBranch:
         if gene != branch:
            if genes.empty:
               plt.plot( branch, gene, data = currentBranch, label = gene)
            else:
               if gene in genes.values:
                  plt.plot( branch, gene, data = currentBranch, label = gene)

      plt.legend(loc = 'upper left')
      plt.title(branch)
      plt.show()

def main():

   #imports tab file with relative expression data
   expression = pd.read_table(sys.argv[1], index_col=0)
   #transposes expression DataFrame to make it easier to handle
   expression = expression.transpose()

   #imports tab file with branch data
   branches = pd.read_table(sys.argv[2], index_col=0)

   #checks if third file was supplied, imports as genes data
   genes = pd.DataFrame({})
   if len(sys.argv) > 3:
      genes = pd.read_table(sys.argv[3], header = None)
   #calls branchPlot function
   branchPlot(expression, branches, genes)

if __name__ == "__main__":
   main()