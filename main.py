def pulsador_madrid():
    basic.show_string("13 champions :(")

def pulsador_barca():
    basic.show_string("Mi comandante pedri el papa se europa")


input.on_button_pressed(Button.A, pulsador_madrid)
input.on_button_pressed(Button.B, pulsador_barca)
