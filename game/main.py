#Piedra papel y tijera
import random


def seleccionar():
  opciones = ("piedra", "papel", "tijera")

  jugada = input("piedra, papel o tijera: ")
  jugada = jugada.lower()
  compu = random.choice(opciones)
  return jugada, compu


def reglas(jugada, compu, win_user, win_compu):
  if jugada == compu:
    print("Empate!")
  elif jugada == "piedra":
    if compu == 'tijera':
      print("usuario gano!")
      win_user += 1
    else:
      print("compu gano!")
      win_compu += 1
  elif jugada == "papel":
    if compu == "piedra":
      print("usuario gana!")
      win_user += 1
    else:
      print("compu gana!")
      win_compu += 1
  elif jugada == 'tijera':
    if compu == 'papel':
      print("usuario gana!")
      win_user += 1
    else:
      print("compu gana!")
      win_compu += 1
  return win_user, win_compu


def run():
  round = 1
  win_compu = 0
  win_user = 0
  while True:
    print("***" * 10)
    print("ROUND =>", round)
    print("***" * 10)
    round += 1
    jugada, compu = seleccionar()
    win_user, win_compu = reglas(jugada, compu, win_user, win_compu)
    if (win_compu == 3):
      print("El ganador es COMPU")
      break
    elif win_user == 3:
      print("El ganador es el JUGADOR")
      break


run()
