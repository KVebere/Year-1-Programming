# Python Coursework 2: Smart Home
# Scenario
A fictional UK-Finnish company, Alikoti, develops eco-friendly smart home technologies. Since 2011 they have developed fully integrated Smart Home Solutions. Since 2022 they have begun selling standalone smart home devices, including smart lights and smart fridges, to be supported by third-party software. Last year, the company made the decision to build its own Smart Home App. They have asked you to develop a prototype GUI app. This prototype must provide a graphical user interface that interacts with a smart home object. The smart home object is responsible for managing data for all smart devices. The company will use this prototype to make a business case for a fully developed application.

# Task 1 — SmartPlug Class [15 marks]
In backend.py, create a class called SmartPlug. This class represents a smart plug object with the instance variables and methods described below:

The SmartPlug class should have two instance variables: switchedOn and consumptionRate. switchedOn represents the plug's operational status, while consumptionRate indicates the rate of consumption within the range of 0 to 150. The constructor should initialise switchedOn to False (representing off) and set consumptionRate to an initial value set from the supplied parameter. The SmartPlug class should include a toggleSwitch method to modify the operational status (from off to on, and on to off), an accessor method for retrieving the operational status, and both accessor and mutator methods for handling the consumption rate. Make sure that your accessor and mutator methods handle invalid parameters appropriately. Finally, add a __str__ method to provide a human-readable string representation of a SmartPlug object. 

# Testing
Test your SmartPlug class by writing a testSmartPlug function outside the SmartPlug class. The testSmartPlug function should:
-Create an instance of the SmartPlug class with a consumption rate of 45.
-Toggle the status of this plug by calling its toggleSwitch method.
-Print the value of switchedOn using the appropriate accessor method.
-Print the value of consumptionRate, set it to a new valid value (of your choice), and then print it again. 
-Print the SmartPlug object.


# Task 2 — CustomDevice Class [15 marks]
Start by looking at table 1 to find out which device you need to create a class for. You should add this class and its test function to backend.py. The diagram and description below are for a generic CustomDevice class that demonstrates the basic idea of what you will have to do from table 1. The class name and option instance variable should be replaced by the class name and instance variable for your custom class from table 1.

The CustomDevice class should have two instance variables: switchedOn, reflecting the switch state of the CustomDevice, and option, representing the CustomDevice's specific option as outlined in table 1. The constructor should initialise switchedOn to a default state of off and set option to its default value from table 1. The class should have a method for toggling the switch state and an accessor method for retrieving it. The class should also have both accessor and mutator methods for handling the CustomDevice’s option. Also, ensure your mutator method handles invalid parameters. When an object of your CustomDevice is printed, it should display information about its switch state and the current value of the option (so implement the __str__ method appropriately).

# Testing
Test your device by writing a testDevice function (this should be named to reflect your particular custom device), which should:
-Create an instance of your CustomDevice class.
-Toggle the status of this device using the toggleSwitch method.
-Print the switchedOn instance variable using the appropriate accessor method.
-Print the current value of the option instance variable (from table 1). Then set it to a new value (of your choice). Next, print it again.
-Print the CustomDevice object.

# Task 3 — SmartHome Class [15 marks]
In backend.py, add a SmartHome class that manages and controls a collection of devices.

The SmartHome class should include a single instance variable, devices, representing a collection of devices. Each element of this collection can either be a SmartPlug or a custom device. The constructor should ensure that devices is initially empty. The class should have methods that let the user access all devices, retrieve or delete a specific device, and add a device. The user should be able to toggle a specific device but also turn all of them on or off at once. Additionally, when a smart home is printed, it should display a well-formatted message describing all of its devices and their attributes. Ensure that your accessor and mutator methods handle invalid parameters. 

# Testing
Test your class by writing a testSmartHome function, which should:
-Create an instance of the SmartHome class and two instances of the SmartPlug class with consumption rates of 45. Additionally, create an instance of your custom device.
-Toggle the first plug, hence turning it on. Then set its consumption rate to 150. Then, set the consumptionRate of the second plug to 25. Lastly, set the option of the custom device to a value of your choice.
-Add both plugs and the custom device to the smart home object.
-Toggle the status of the second plug using the appropriate method of the smart home object.
-Print the smart home object.
-Turn on all devices in the smart home and print the smart home object again.
-Remove the first device and print the smart home.

# Task 4 — SmartHomeSystem GUI [15 marks]
In a file called frontend.py, import the class(es) that you have defined in backend.py. In a setUpHome function, create an instance of the SmartHome object. Allow the user to populate it with five devices of their choosing using the shell (i.e., the function needs to give appropriate prompts to the user). The user should be able to specify the consumption rate for each smart plug added.
Create a SmartHomeSystem class for the GUI of your smart home system that should look like the figure below, but with appropriate fonts, sizes, colours, and spacing to make the interface look pleasant. Note that at this stage, you only need to display the widgets for your GUI (none of the buttons needs to work for this task). Then, in a separate main function, create a SmartHomeSystem object and populate it with the SmartHome object created in setUpHome.

The example below assumes a student number ending with 0 (for example, “up2123410”). The user has also created three SmartLights and two SmartPlugs (with consumption rates of 150 and 45) at the beginning of program execution before the GUI is displayed: 


# Task 5 — GUI interactivity [15 marks]
Once you have successfully built your GUI, you should implement its functionality. For each of the buttons on the GUI, you need to write the code in the SmartHomeSystem class that implements the functionality of the button. For instance:
-When the user clicks on the “Turn on all” button, all devices should be turned on: the backend needs to update, and the GUI should reflect this change. The same goes for the “Turn off all” button.
-When a device's “Toggle” button is clicked, the details of the device should be updated. Clicking on an “Edit” button should result in a new window where the user can modify all attributes of that device. Finally, the “Delete” button should remove the device. Clicking on any of these buttons should result in both the backend and frontend being updated.
-When the user clicks on the “Add” button, a new window should appear where they are given the option of whether they want a smart plug or a custom smart device. For new smart plugs, the user should be able to choose a consumption rate. The device should then be created and added to the backend (and GUI). 

# Challenge features [23 marks]
Make sure to only attempt these challenges once you have completed all the above tasks. To ensure that your solution to the challenges does not impact your answer to tasks 1-5, copy your existing files and paste them in backendChallenge.py and frontendChallenge.py. Then make your changes to these copies. You are free to add as many of the following features/enhancements to your system. The following tasks are of varied difficulty. Refer to the documentation pages of Tkinter for challenges 2-6.
-Inheritance — Improve the code quality of the backend by making appropriate usage of inheritance. [4 marks]
-Advanced Tkinter Widgets — Tkinter provides other widgets such as CheckButton or SpinBox which we have not covered in the classes. Currently, the user can only toggle each device straight from the main window. Modify your GUI to allow the user to modify other attributes of the devices directly from the main window using the widgets of your choice. You may also want to use similar widgets in the secondary windows of your app. [4 marks]
-Custom Device Visualisation — Enhance the GUI to represent each plug/device visually based on its type. For example, display a graphic or icon that represents your plugs/devices. This visual representation should provide an intuitive way for users to identify and interact with plugs/devices. Hint: look at the Photoimage widget. [3 marks]
-Interface & Accessibility setting — Improve the accessibility of your app by providing an “Accessibility settings” button. This needs to open a new window offering similar functionality to Moodle’s “Interface & Accessibility settings” menu. The user should be able to alter text size, change between light and dark mode, and also define a custom colour scheme (consisting of a background and text colour). Hint: Visit the tkColorChooser module. [4 marks]
-Permanent Data Storage — Currently, the user needs to create the devices one by one in the shell and the smart home system does not have permanent storage (i.e., upon closing the smart home system, all data will be lost). Investigate the tkFileDialog module of Tkinter which allows the user to upload a file (e.g., a text or a CSV file) where each row represents a device. Your app should also allow the user to save the state of a smart home to a file. [4 marks]
-Device Scheduler — Add a clock with hour values 0-23 which increment every 3 seconds to simulate the passing of time; “minutes” do not need to be implemented or displayed. Include a scheduling feature for devices using this clock feature, allowing users to set specific times for devices to turn on or off automatically. The main GUI window should show the clock and users should be able to see the devices turn on and off at the set times. [4 marks]


