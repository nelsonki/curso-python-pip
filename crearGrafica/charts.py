import matplotlib.pyplot as plt

def generate_bar_chart(name,labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  # plt.show()se detiene en pantalla el programa y muestras la grafica
  plt.savefig(f'./image/{name}.png')
  plt.close()

def generate_pie_chart( labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  #plt.show() se detiene en pantalla el programa y muestras la grafica
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart( labels, values)