import module.Debug as DEBUG
import module.playerMoving as playerMoving
def bind(mainWindow,Amongus,buttonmap):
    mainWindow.bind("<KeyPress-Left>",lambda event:Amongus.move('left',5))
    mainWindow.bind("<KeyPress-Right>",lambda event:Amongus.move('right',5))
    mainWindow.bind("<KeyPress-Up>",lambda event:Amongus.move('up',5))
    mainWindow.bind("<KeyPress-Down>",lambda event:Amongus.move('down',5))
    mainWindow.bind("<KeyRelease-Left>",lambda event:Amongus.stand())
    mainWindow.bind("<KeyRelease-Right>",lambda event:Amongus.stand())
    mainWindow.bind("<KeyRelease-Up>",lambda event:Amongus.stand())
    mainWindow.bind("<KeyRelease-Down>",lambda event:Amongus.stand())
    mainWindow.bind("<Button-1>",lambda event:DEBUG.reportCoordinate(Amongus))
    
