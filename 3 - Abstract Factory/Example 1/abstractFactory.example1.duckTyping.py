class LinuxButton:
    def render(self):
        print("Rendering Linux button")

class LinuxDropDown:
    def render(self):
        print("Rendering Linux dropdown")

class LinuxTextBox:
    def render(self):
        print("Rendering Linux textbox")   

class LinuxFactory:
    def create_button(self):
        return LinuxButton()

    def create_drop_down(self):
        return LinuxDropDown()
    
    def create_text_box(self):
        return LinuxTextBox()
    
class MacButton:
    def render(self):
        print("Rendering Mac button")

class MacDropDown:
    def render(self):
        print("Rendering Mac dropdown")

class MacTextBox:
    def render(self):
          print("Rendering Mac textbox")

class MacFactory:     
    def create_button(self):
        return MacButton()
    
    def create_drop_down(self):
        return MacDropDown()
    
    def create_text_box(self):
        return MacTextBox()

class WinButton:
    def render(self):
        print("Rendering Windows button")

class WinDropDown:
    def render(self):
        print("Rendering Windows dropdown")

class WinTextBox:
    def render(self):
        print("Rendering Windows textbox")

class WinFactory:        
    def create_button(self):
        return WinButton()
    
    def create_drop_down(self):
        return WinDropDown()
    
    def create_text_box(self):
        return WinTextBox()
    

linux_factory = LinuxFactory()
linux_button = linux_factory.create_button()
linux_button.render()

win_factory = WinFactory()
win_button = win_factory.create_button()
win_button.render()

mac_factory = MacFactory()
mac_button = mac_factory.create_button()
mac_button.render()