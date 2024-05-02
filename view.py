import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page
    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        #row1
        self._lista1=ft.Dropdown(width=self.page.window_width,options=[ft.dropdown.Option("Italian"), ft.dropdown.Option("English"), ft.dropdown.Option("Spanish")],
                          label="Select language", alignment=ft.alignment.center)
        self._row1 = ft.Row([self._lista1])
        #row2
        self._lista2 = ft.Dropdown(width=self.page.window_width/4,
                            options=[ft.dropdown.Option("Linear"), ft.dropdown.Option("Default"), ft.dropdown.Option("Dicatomic")],
                            label="Search Modality", alignment=ft.alignment.center)
        self._txtIn=ft.TextField(label="insert the text",width=self.page.window_width*1/2)
        self._btn = ft.ElevatedButton(width=self.page.window_width * 1 / 4, text="Search", on_click=self.__controller.handleClick)
        self._row2 = ft.Row([self._lista2, self._txtIn, self._btn])

        #row3
        self.robasotto=ft.ListView(expand=1, spacing=10, padding=20)
        self._row3=ft.Row([self.robasotto])
        self.page.add(self._row1,self._row2, self._row3)


    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()


