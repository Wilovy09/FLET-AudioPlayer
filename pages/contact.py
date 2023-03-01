import flet as ft
from flet import *

def _view_():
    return View(
        '/contact',
        controls=[
            Column(
                controls=[
                    Row(
                        controls=[
                            IconButton(
                                icon=ft.icons.MENU,
                                on_click=lambda e: e.page.go('/config'),
                            ),
                            FilledButton(
                                text='My Music',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/my_music'),  
                            ),
                            FilledButton(
                                text='Playlists',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/playlists'),
                            ),
                            FilledButton(
                                text='Contact',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/contact'),
                            ),
                            IconButton(
                                icon=ft.icons.SEARCH,
                                on_click=lambda e: e.page.go('/search'),
                            ),
                        ]
                    ),
                    # main content
                    ft.Divider(thickness=1),
                    Container(
                        width=450,
                        height=450,
                        bgcolor='pink800',
                        alignment=alignment.center,
                        content=Text('Contact'),
                    ),
                ]
            )
        ],
    )