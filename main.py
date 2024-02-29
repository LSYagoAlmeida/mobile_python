import flet as ft
from flet import *
from view.login import * 
from view.teste import * 

if __name__ == "__main__":
    
    def main(page: Page):
        page.title = "Flet Trello clone"
        page.padding = 0
        app = StartLogin(page)
        page.add(app)
        page.update()