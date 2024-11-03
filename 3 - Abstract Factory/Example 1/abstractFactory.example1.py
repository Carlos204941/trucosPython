from abc import ABC, abstractmethod

class IButton(ABC):
    @abstractmethod
    def render(self):
        pass

class IDropDown(ABC):    
    @abstractmethod
    def render(self):
        pass
     
class ITextBox(ABC):
    @abstractmethod
    def render(self):
        pass

class IThemeFactory(ABC):  
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_drop_down(self):
        pass

    @abstractmethod
    def create_text_box(self):
        pass

class LinuxButton(IButton):
    def render(self):
        print("Rendering Linux button")

class LinuxDropDown(IDropDown):
    def render(self):
        print("Rendering Linux dropdown")

class LinuxTextBox(ITextBox):
    def render(self):
        print("Rendering Linux textbox")   

class LinuxFactory(IThemeFactory):
    def create_button(self):
        return LinuxButton()

    def create_drop_down(self):
        return LinuxDropDown()
    
    def create_text_box(self):
        return LinuxTextBox()
    
class MacButton(IButton):
    def render(self):
        print("Rendering Mac button")

class MacDropDown(IDropDown):
    def render(self):
        print("Rendering Mac dropdown")

class MacTextBox(ITextBox):
    def render(self):
          print("Rendering Mac textbox")

class MacFactory(IThemeFactory):     
    def create_button(self):
        return MacButton()
    
    def create_drop_down(self):
        return MacDropDown()
    
    def create_text_box(self):
        return MacTextBox()

class WinButton(IButton):
    def render(self):
        print("Rendering Windows button")

class WinDropDown(IDropDown):
    def render(self):
        print("Rendering Windows dropdown")

class WinTextBox(ITextBox):
    def render(self):
        print("Rendering Windows textbox")

class WinFactory(IThemeFactory):        
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