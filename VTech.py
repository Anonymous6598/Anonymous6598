from flet import *

def main(page: Page):
    def open_menu_bar(event):
        main_screen_menu_bar_divider.visible = True
        
        main_screen_menu_bar.visible = True
        main_screen_menu_button.visible = False        
        
        page.update()
        
    def close_menu_bar(event):
        main_screen_menu_button.visible = True
        
        main_screen_menu_bar_divider.visible = False
        main_screen_menu_bar.visible = False
        
        page.update()

    def menu_bar_select(event):
        if event.control.selected_index == 0:
           main_screen_menu_button.visible = True
           main_screen_menu_image.visible = True

           main_screen_menu_bar_divider.visible = False
           main_screen_menu_bar.visible = False
           main_screen_my_diary_image.visible = False
           main_screen_my_diary_text.visible = False
           main_screen_my_diary_download_button.visible = False
           main_screen_ppc_image.visible = False
           main_screen_ppc_text.visible = False
           main_screen_ppc_download_button.visible = False
           main_screen_about_us_text.visible = False
           
           page.update()

        elif event.control.selected_index == 1: 

           main_screen_menu_button.visible = True
           main_screen_my_diary_image.visible = True
           main_screen_my_diary_text.visible = True
           main_screen_my_diary_download_button.visible = True
           
           main_screen_menu_bar_divider.visible = False
           main_screen_menu_bar.visible = False
           main_screen_menu_image.visible = False
           main_screen_ppc_image.visible = False
           main_screen_ppc_text.visible = False
           main_screen_ppc_download_button.visible = False
           main_screen_about_us_text.visible = False
           
           page.update()

        elif event.control.selected_index == 2:
           main_screen_menu_button.visible = True
           main_screen_ppc_image.visible = True
           main_screen_ppc_text.visible = True
           main_screen_ppc_download_button.visible = True
            
           main_screen_menu_image.visible = False
           main_screen_menu_bar_divider.visible = False
           main_screen_menu_bar.visible = False
           main_screen_my_diary_image.visible = False
           main_screen_my_diary_text.visible = False
           main_screen_my_diary_download_button.visible = False
           main_screen_about_us_text.visible = False

           page.update()

        elif event.control.selected_index == 3:
           main_screen_menu_button.visible = True
           main_screen_about_us_text.visible = True

           main_screen_menu_image.visible = False
           main_screen_menu_bar_divider.visible = False
           main_screen_menu_bar.visible = False
           main_screen_my_diary_image.visible = False
           main_screen_my_diary_text.visible = False
           main_screen_my_diary_download_button.visible = False
           main_screen_ppc_image.visible = False
           main_screen_ppc_text.visible = False
           main_screen_ppc_download_button.visible = False
           
           page.update()

    page.title = "VTech store"

    main_screen_menu_image = Image(src=f"/asserts/VTechLogo.png", fit=ImageFit.NONE)

    main_screen_menu_button = IconButton(icon=icons.MENU_ROUNDED, bgcolor="Green", on_click=open_menu_bar)

    main_screen_menu_bar_divider = VerticalDivider(width=1)
    main_screen_menu_bar_divider.visible = False

    main_screen_menu_bar = NavigationRail(selected_index=0, label_type=NavigationRailLabelType.ALL, min_width=50, min_extended_width=50, leading=FloatingActionButton(icon=icons.EXIT_TO_APP, bgcolor="Green", on_click=close_menu_bar), group_alignment=-1, destinations=[NavigationDestination(icon=icons.MENU, selected_icon=icons.MENU, label="menu"), NavigationDestination(icon=icons.BOOK_OUTLINED, selected_icon=icons.BOOK_OUTLINED, label="My Diary"), NavigationDestination(icon=icons.DISC_FULL_OUTLINED, selected_icon=icons.DISC_FULL_OUTLINED, label="PPC"), NavigationDestination(icon=icons.INFO_OUTLINED, selected_icon=icons.INFO_OUTLINED, label="About us")], on_change=menu_bar_select)
    main_screen_menu_bar.visible = False

    main_screen_my_diary_image = Image(src=f"/asserts/MyDiary.png", fit=ImageFit.NONE)
    main_screen_my_diary_image.visible = False

    main_screen_my_diary_text = Text("This is My Diary - a whole lightweight text and code editor. It has features of word(text editor, file converterer) and hotepad(save and read in all formats (including json and toml)) We hope you'll enjoy it. Downloading link:", size=30)
    main_screen_my_diary_text.visible = False

    main_screen_my_diary_download_button = ElevatedButton(text="Download", color="White", bgcolor="Green", on_click=lambda event: page.launch_url("https://drive.google.com/uc?export=download&id=1gHw3VTjD4F3C94PT5pnBAddbOawOh-kY"))
    main_screen_my_diary_download_button.visible = False

    main_screen_ppc_image = Image(src=f"/asserts/PPC.png", fit=ImageFit.NONE)
    main_screen_ppc_image.visible = False

    main_screen_ppc_text = Text("This is PPC(Pyhton Package Commander) - a user friendly package commander for python. It Requiers python and pip to work otherwise you won't be able to use it. We hope you'll enjoy it. Downloading link:", size=30)
    main_screen_ppc_text.visible = False

    main_screen_ppc_download_button = ElevatedButton(text="Download", color="White", bgcolor="Green", on_click=lambda event: page.launch_url("https://drive.google.com/uc?export=download&id=1q_SPc1Yd7QDyf7XkfZLqirg3gpIhiA17"))
    main_screen_ppc_download_button.visible = False

    main_screen_about_us_text = Text("I'm 17 years old boy, who is keen in progamming. I wrote several programs. They have great and easy user interface. I hope, you'll like them.", size=30)
    main_screen_about_us_text.visible = False

    page.add(Row([main_screen_menu_button], alignment="right"), Row([main_screen_menu_bar, main_screen_menu_bar_divider, Column([main_screen_menu_image, main_screen_my_diary_image, main_screen_my_diary_text, main_screen_my_diary_download_button, main_screen_ppc_image, main_screen_ppc_text, main_screen_ppc_download_button, main_screen_about_us_text], alignment="right", expand=True)], alignment="right", expand=True))

if __name__ == "__main__":
    app(target=main, assets_dir="asserts", view=WEB_BROWSER)