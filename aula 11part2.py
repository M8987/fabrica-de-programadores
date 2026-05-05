import pandas as pd
import openpyxl

pessoa = {['marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos','marcos']
          "idade": [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
          "tamanho": [1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,1.89,]}

df = pd.DataFrame(pessoa)

df.to_excel("tabelexcel.x1sx", sheet_name="aula_Hebert",
            engine="openyx1", index=false)
print("arquivo salvo com sucesso")