import flet as ft
from flet import *
from pages.my_music import _view_ as v1
from pages.playlists import _view_ as v2
from pages.contact import _view_ as v3
from pages.config import _view_ as v4
from pages.search import _view_ as v5
from func.play_music import _view_ as v6

from func.play_music import audio1

def main(page: Page):
    page.theme_mode = "dark"
    page.window_width = 450
    page.window_resizable = False
    page.title = 'Orbus Player'

    my_music = v1()
    playlists = v2()
    contact = v3()
    config = v4()
    search = v5()

    play_music = v6()
    
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