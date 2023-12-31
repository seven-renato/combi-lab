# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XIfhk1cNf7we72E_iwplQ-zldBd_gta6
"""

!pip install rdkit
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw

#Sempre que adicionar descritor adicionar numa nova linha no final dos outros(*NÃO PODE MUDAR NENHUM DE ORDEM*) se mudar terar-se-ia que alterar a ordem da primeira linha do csv
def calculate_descriptors(mol):
    try:
        # Convert SMILES or MOL2 to RDKit molecule object
        if mol.endswith('.mol2'):
            mol = Chem.MolFromMol2File(mol, sanitize=False)
        else:
            mol = Chem.MolFromSmiles(mol)

        # Calculate descriptors
        descriptors = []
        descriptors.append(Descriptors.MolLogP(mol))
        descriptors.append(Descriptors.MolWt(mol))
        descriptors.append(Descriptors.NumRotatableBonds(mol))
        # GetNumAtoms(mol)
        descriptors.append(Descriptors.Chem.rdMolDescriptors.CalcMolFormula(mol))
        descriptors.append(Descriptors.NumHAcceptors(mol))
        descriptors.append(Descriptors.NumHDonors(mol))
        descriptors.append(Descriptors.TPSA(mol))

        # Add more descriptors as needed

    except Exception as e:
        print(f"Error processing molecule: {mol}")
        print(f"Error message: {str(e)}")
    string = ""
    for val in descriptors:
      string += str(val) + ";"
    return string[:-1]

#Apenas pressionar no botão de executar e salva o arquivo gerado
arq = open("./resultados_tratados_pt2.csv", "r") # Enviar o arquivo com os resultados anteriormente retirados, (ZINC_ID;MENOR_FEB;SMILE)
lista = arq.readlines()
arq.close()
lista_linhas = [val[:-1].split(";") for val in lista]
string = "ZINC_ID;MENOR_FEB;SMILE;MolLogP;MolWt;NumRotatableBonds;CalcMolFormula;NumHAcceptors;NumHDonors;TPSA\n" # Cada novo descritor adicionar um novo ";{nomedodescritor}"
for val in lista_linhas[1:]:
  try:
    string += (';').join(val) + calculate_descriptors(val[2]) + "\n"
  except:
    string += ""
arq2 = open("./resultados_tratados_pt3.csv", "w")
arq2.write(string)
arq2.close()