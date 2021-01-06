import turtle          # importation du module turtle
turtle.color('blue')   # la tortue est bleue
turtle.down()          # tant que la tortue est “down”,
                       # elle tracera la ligne de ses déplacements
turtle.begin_fill()    # va remplir l’intérieur de ce qui est tracé entre
                       # maintenant et le turtle.end_fill() ultérieur
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.end_fill()

turtle.color('red')
turtle.begin_fill()
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()

turtle.color('black')
turtle.begin_fill()
turtle.left(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()

turtle.done()          # laisse l'utilisateur fermer la fenêtre