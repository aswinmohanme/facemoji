
import tkinter
import tkinter.font

def createGUI():
    root = tkinter.Tk()
    root.title("FaceMoji")

    default_font = tkinter.font.nametofont("TkDefaultFont")
    root.option_add("*Font", default_font)

    headerLabel = tkinter.Label(root, text="FaceMoji")
    headerLabel.config(font=(default_font, 24))
    headerLabel.place(x=16, y=16)

    descriptionLabel = tkinter.Label(root, text="Facial emotion recognition is the process of detecting human emotions from facial expressions.", wraplength=420, justify="left")
    descriptionLabel.config(font=(default_font, 12))
    descriptionLabel.place(x=16, y=52)

    dataPrepareLabel = tkinter.Label(root, text="Data Preparation")
    dataPrepareLabel.config(font=(default_font, 12))
    dataPrepareLabel.place(x=16, y=120)

    createDatasetButton = tkinter.Button(root, text="Create Dataset")
    createDatasetButton.place(x=16, y=148, width=160)

    startTrainingButton = tkinter.Button(root, text="Start Training")
    startTrainingButton.place(x=190, y=148)

    startRunningLabel = tkinter.Label(root, text="Execute Model")
    startRunningLabel.config(font=(default_font, 12))
    startRunningLabel.place(x=16, y=210)

    testWithData = tkinter.Button(root, text="Test with Data")
    testWithData.place(x=16, y=240)

    openWebcam = tkinter.Button(root, text="Open Webcam", width=40) 
    openWebcam.place(x=130, y=240)

    root.geometry("460x300")
    root.mainloop()


def main():
    createGUI()

if __name__ == "__main__":
    main()
