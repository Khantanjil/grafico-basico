#!/usr/bin/python
# Grafico basico em python

# Importacoes
from bokeh.plotting import figure
from bokeh.io import show, output_file

# Preparar dados
x = [1,2,3,4,5]
y = [6,7,8,9,10]

# Preparar o ficheiro html
output_file("grafico.html")

# Criar objeto
f = figure()

# Criar a linha no grafico
f.line(x,y)

# Mostrar o grafico
show(f)