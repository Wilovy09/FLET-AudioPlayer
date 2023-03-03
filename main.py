import flet as ft
from flet import *
from pages.my_music import _view_ as v1
from pages.playlists import _view_ as v2
from pages.contact import _view_ as v3
from pages.config import _view_ as v4
from pages.search import _view_ as v5
# from func.play_music import _view_ as v6
# from func.play_music import audio1

url = r"..\music\FindeSemana.mp3"

def main(page: Page):
# ! PAGE ##################################
    page.theme_mode = "dark"
    page.window_width = 450
    page.window_resizable = False
    page.title = 'Orbus Player'


    # page.overlay.append(audio1)

    def audio1():
        Audio(
        src=url,
        autoplay=True,
        volume=1,
        balance=0
    )

    def volume_down(_):
        audio1.volume -= 0.1
        audio1.update()
        print(audio1.volume)

    def volume_up(_):
        audio1.volume += 0.1
        audio1.update()
        print(audio1.volume)

    def balance_left(_):
        audio1.balance -= 0.1
        audio1.update()
        print(audio1.balance)

    def balance_right(_):
        audio1.balance += 0.1
        audio1.update()
        print(audio1.balance)

    def _playmusic_():
        return View(
            '/play_music',
            controls=[
                Column(
                    controls=[
                        Row(
                            controls=[
                                IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    on_click=lambda e: e.page.go('/my_music'),
                                ),
                            ]
                        ),
                        # main content
                        ft.Divider(thickness=1),
                        Container(
                            Row([
                                Column([
                                    IconButton(
                                        icon=ft.icons.ADD,
                                        on_click=volume_up),
                                    IconButton(
                                        icon=ft.icons.REMOVE,
                                        on_click=volume_down),
                                    ]
                                ),
                                Row([
                                    IconButton(
                                        icon=ft.icons.PLAY_ARROW,
                                        on_click=lambda _: audio1.play(),
                                    ),
                                    IconButton(
                                        icon=ft.icons.PAUSE,
                                        on_click=lambda _: audio1.pause(),
                                    ),
                                    ]
                                ),                
                                Column([
                                    ElevatedButton("R", on_click=balance_right),
                                    ElevatedButton("L", on_click=balance_left),
                                    ]
                                ),

                            ])

                        ),

                    ]
                )
            ],
        )

# ! ROUTES ##################################
    my_music = v1()
    playlists = v2()
    contact = v3()
    config = v4()
    search = v5()

    play_music = _playmusic_()
    
    def route_change(route):
        page.views.clear()
        
        if page.route == '/play_music':
            page.views.append(play_music)
        if page.route == '/search':
            page.views.append(search)
        if page.route == '/config':
            page.views.append(config)
        if page.route == '/playlists':
            page.views.append(playlists)
        if page.route == '/contact':
            page.views.append(contact)
        if page.route == '/my_music':
            page.views.append(my_music)
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    # page.overlay.append(audio1)

    page.views.append(play_music)
    page.views.append(search)
    page.views.append(config)
    page.views.append(playlists)
    page.views.append(contact)
    page.views.append(my_music)
    
    page.update()

ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)