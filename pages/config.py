import flet as ft
from flet import *

def _view_():
    return View(
        '/config',
        controls=[
            Column(
                controls=[
                    Row(
                        controls=[
                            IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=lambda e: e.page.go('/my_music'),
                                # tooltip='Config',
                            ),
                        ]
                    ),
                    # main content
                    Container(
                        width=450,
                        height=450,
                        bgcolor='yellow800',
                        alignment=alignment.center,
                        content=Text('Config'),
                    ),
                ]
            )
        ],
    )