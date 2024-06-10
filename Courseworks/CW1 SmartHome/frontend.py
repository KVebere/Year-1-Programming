from backend import *
from tkinter import *

validDevices = ["SmartPlug", "SmartSpeaker"]

def setupHome():
    mySmartHome = SmartHome()
    while True:
        deviceInput = input("Enter the device you wish to add or write 'exit' to leave: ").lower()
        if deviceInput == "smartplug":
            consumptionRate = input("Enter the consumption rate between 0-150: ")
            mySmartHome.addDevice(SmartPlug(consumptionRate))
        elif deviceInput == "smartspeaker":
            mySmartHome.addDevice(SmartSpeaker())
        elif deviceInput == "exit":
            break
        else:
            print(f"Invalid device, please enter a valid device from {', '.join(validDevices)}.")
    # mySmartHome.addDevice(SmartPlug(45))
    # mySmartHome.addDevice(SmartSpeaker())
    # mySmartHome.addDevice(SmartPlug(45))
    # mySmartHome.addDevice(SmartSpeaker())
    # mySmartHome.addDevice(SmartPlug(45))
    return mySmartHome

#setupHome()
    
class SmartHomeSystem:
    def __init__(self, mySmartHome):
        self.smartHomeSystem = mySmartHome

        self.win = Tk()
        self.win.title("Smart Home System")
        self.win.geometry("450x260")

        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(
            row=0,
            column=0,
            padx=10,  
            pady=10,
        )

        self.deviceWidgets = []
        self.newConsumptionRate = DoubleVar()
        self.newOption = StringVar()

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
            
        numOfDevices = self.smartHomeSystem.getDevices()
        for i in range(len(numOfDevices)):
            device = self.smartHomeSystem.getDeviceAt(i)
            labelText = f"{device.__class__.__name__}: {device.getSwitchedOn()},"
            if device.__class__.__name__ == "SmartPlug":
                labelText += f" Consumption Rate:{device.getConsumptionRate()}"
            else:
                labelText += f" Option:{device.getOption()}"
            deviceLabel = Label(
                self.mainFrame, 
                text=labelText)

            deviceLabel.grid(
                row=i+1,
                column=0,
                padx=5,
                pady=5,
            )
            self.deviceWidgets.append(deviceLabel)

            
            toggleSwitchButton = Button(
                self.mainFrame,
                text="Toggle",
                command=lambda index=i: self.toggleSwitch(index)
            )

            toggleSwitchButton.grid(
                row=i+1,
                column=5,
                padx=5,
                pady=5,
            )
            self.deviceWidgets.append(toggleSwitchButton)

            editDeviceButton = Button(
                self.mainFrame,
                text="Edit",
                command=lambda index = i: self.updateWin(index)
            )

            editDeviceButton.grid(
                row=i+1,
                column=6,
                padx=5,
                pady=5,
            )
            self.deviceWidgets.append(editDeviceButton)

            deleteDeviceButton = Button(
                self.mainFrame,
                text="Delete",
                command=lambda index=i: self.deleteDevice(index)
            )

            deleteDeviceButton.grid(
                row=i+1,
                column=7,
                padx=5,
                pady=5,
            )
            self.deviceWidgets.append(deleteDeviceButton)

        turnOnAllButton = Button(
            self.mainFrame,
            text="Turn on all",
            command=self.turnOnAll
        )

        turnOnAllButton.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )

        turnOffAllButton = Button(
            self.mainFrame,
            text="Turn off all",
            command=self.turnOffAll
        )

        turnOffAllButton.grid(
            row=0,
            column=5,
            padx=5,
            pady=5,
        )

        addDeviceButton = Button(
            self.mainFrame,
            text="Add",
            command=self.addDevice
        )
        addDeviceButton.grid(
            row= 15,
            column=0,
            padx=5,
            pady=5,
        )

    def updateWin(self, deviceIndex):

        newWin = Toplevel(self.win)
        newWin.title("Edit Device")

        device = self.smartHomeSystem.getDeviceAt(deviceIndex)
        if isinstance(device, SmartPlug):
            updateSmartPlug = Label(
                newWin, 
                text=f"Update SmartPlug:"
        )
            
            updateSmartPlug.grid(
                row=0,              
                column=0, 
                padx=5, 
                pady=5
            )

            newConsumptionRateEntry = Spinbox(
                newWin,
                from_=0,
                to=150,
                textvariable=self.newConsumptionRate
            )
            
            newConsumptionRateEntry.grid(
                row=0, 
                column=1, 
                padx=5,
                pady=5
            )

        else:
            smartSpeakerLabel = Label(
                newWin,
                text=f"Update SmartSpeaker:")
            
            smartSpeakerLabel.grid(
                row=0, 
                column=0, 
                padx=5, 
                pady=5)
            
            newOptionEntry = Entry(
                newWin, 
                textvariable=self.newOption
            )

            newOptionEntry.grid(
                row=0, 
                column=1, 
                padx=5, 
                pady=5
            )
        
        editButton = Button(
                newWin, 
                text="Edit", 
                command=lambda index=deviceIndex: (
                    self.updateDevice(
                        index, self.newConsumptionRate.get(), 
                        self.newOption.get()), 
                        newWin.destroy()
                    )
                )

            
        editButton.grid(
            row=1, 
            column=0, 
            padx=5, 
            pady=5
        )
    
    def addDevice(self):

            newWin = Toplevel(self.win)
            newWin.title("Add Device")

            self.deviceType = StringVar()

            def updateCreateButtonState():
                if self.deviceType.get():
                    createButton.config(state="normal")
                else:
                    createButton.config(state="disabled")


            smartPlugRadioButton = Radiobutton(
                newWin, 
                text="SmartPlug", 
                variable=self.deviceType, 
                value="SmartPlug", 
                command=lambda: [self.updateConsumptionRateEntry(), updateCreateButtonState()]
            )

            smartPlugRadioButton.grid(
                row=0, 
                column=0, 
                padx=5, 
                pady=5
            )

            smartSpeakerRadioButton = Radiobutton(
                newWin, 
                text="SmartSpeaker", 
                variable=self.deviceType, 
                value="SmartSpeaker", 
                command=lambda: [self.updateConsumptionRateEntry(), updateCreateButtonState()]
            )

            smartSpeakerRadioButton.grid(
                row=0, 
                column=1, 
                padx=5, 
                pady=5
            )

            consumptionRateLabel = Label(
                newWin, 
                text="Consumption Rate:"
            )

            consumptionRateLabel.grid(
                row=1, 
                column=0, 
                padx=5, 
                pady=5
            )

            self.consumptionRateEntry = Entry(newWin)

            self.consumptionRateEntry.grid(
                row=1, 
                column=1, 
                padx=5, 
                pady=5
            )

            createButton = Button(
                newWin, 
                text="Create", 
                command=lambda: (
                    self.createDevice(
                        self.deviceType.get(), 
                        self.consumptionRateEntry.get()
                    ), 
                    newWin.destroy()
                )
        )

            
            createButton.grid(
                row=2, 
                column=0, 
                padx=5, 
                pady=5
            )

    def updateConsumptionRateEntry(self):
        if self.deviceType.get() == "SmartSpeaker":
            self.consumptionRateEntry.config(state=DISABLED)
        else:
            self.consumptionRateEntry.config(state=NORMAL)
    
    
    def turnOnAll(self):
        self.smartHomeSystem.turnOnAll()
        for widget in self.deviceWidgets:
            widget.destroy()
    
        self.deviceWidgets = []
        self.createWidgets()

    def turnOffAll(self):
        self.smartHomeSystem.turnOffAll()
        for widget in self.deviceWidgets:
            widget.destroy()
        
        self.deviceWidgets = []
        self.createWidgets()
    
    def toggleSwitch(self, index):
        self.smartHomeSystem.toggleSwitch(index)
        for widget in self.deviceWidgets:
            widget.destroy()

        self.deviceWidgets = []
        self.createWidgets()

    def createDevice(self, deviceType, consumptionRate):
        if deviceType == "SmartPlug":
            if consumptionRate.isdigit() and 0 <= int(consumptionRate) <= 150:
                self.smartHomeSystem.addDevice(SmartPlug(consumptionRate))
            else:
                messagebox.showerror("Error", "Invalid consumption rate, please enter a number between 0-150.")
        elif deviceType == "SmartSpeaker":
            self.smartHomeSystem.addDevice(SmartSpeaker())

        for widget in self.deviceWidgets:
            widget.destroy()

        self.deviceWidgets = []
        self.createWidgets()

    def updateDevice(self, index, newConsumptionRate, newOption):
        device = self.smartHomeSystem.getDeviceAt(index)
        if isinstance(device, SmartPlug):
            device.setConsumptionRate(newConsumptionRate)
        else:
            device.setOption(newOption)

        for widget in self.deviceWidgets:
            widget.destroy()

        self.deviceWidgets = []
        self.createWidgets()
        

    def deleteDevice(self, index):
        self.smartHomeSystem.removeDeviceAt(index)

        for widget in self.deviceWidgets:
            widget.destroy()

        self.deviceWidgets = []
        self.createWidgets()


def main():
    smartHome = setupHome()
    app = SmartHomeSystem(smartHome)
    app.run()

main()
