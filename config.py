#! python3

from appJar import gui

app = gui()

## Layout config ##
app.setTitle("Config Window")
app.setGeometry("fullscreen")

## Header ##
app.addLabel("header","Settings page of Syback. All informations will be saved on instalation directory.",0,0,3)

## Informations ##
app.addLabelEntry("Username: ")

## GRID VIEW ##
app.setLabelBg("header","red")
app.getLabelWidget("header").config(font="Helvetica 22")
app.setLabelBg("Username: ","blue")

app.go()