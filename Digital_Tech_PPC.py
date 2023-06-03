from customtkinter import * 
from tkinter import *
from tkinter.messagebox import *
from subprocess import call
import pkg_resources

class Program(CTk):
    def __init__(self, *args, **kwargs) -> CTk:
        CTk.__init__(self, *args, **kwargs)
        
        deactivate_automatic_dpi_awareness()
        set_widget_scaling(1.251)
        set_default_color_theme("dark-blue")

        self.attributes("-toolwindow", True)
        self.title("Python Package Commander")

        self.main_screen_frame = CTkFrame(master=self, width=1450, height=792.565947242206275, corner_radius=0, fg_color="grey")
        self.main_screen_frame.grid(row=0, column=0, padx=42, sticky="NSEW")

        Grid.rowconfigure(self,0,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        
        Grid.columnconfigure(self.main_screen_frame,0,weight=1)

        self.main_screen_main_text_1 = CTkLabel(master=self.main_screen_frame, text="Python", font=CTkFont(family="Script", size=75), text_color="black")
        self.main_screen_main_text_1.grid(row=0, column=0, pady=0, sticky="N")

        self.main_screen_main_text_2 = CTkLabel(master=self.main_screen_frame, text="Package", font=CTkFont(family="Script", size=75), text_color="black")
        self.main_screen_main_text_2.grid(row=1, column=0, pady=0)

        self.main_screen_main_text_3 = CTkLabel(master=self.main_screen_frame, text="Commander", font=CTkFont(family="Script", size=75), text_color="black")
        self.main_screen_main_text_3.grid(row=2, column=0, pady=0)

        self.main_screen_update_button = CTkButton(master=self.main_screen_frame, text="Update", fg_color="green", font=CTkFont(family="Ubuntu", size=24), width=319, command=self.__update__)
        self.main_screen_update_button.grid(row=3, column=0, pady=0)

        self.main_screen_update_all_text = CTkLabel(master=self.main_screen_frame, text="Update all packages", text_color="green", font=CTkFont(family="Ubuntu", size=72))

        self.main_screen_update_all_button = CTkButton(master=self.main_screen_frame, text="Update all packages", fg_color="green", font=CTkFont(family="Ubuntu", size=24), width=319, command=self.__update_all__)

        self.main_screen_update_package_text = CTkLabel(master=self.main_screen_frame, text="Update package", text_color="green", font=CTkFont(family="Ubuntu", size=72))

        self.main_screen_update_package_entry = CTkEntry(master=self.main_screen_frame, placeholder_text="Package name", placeholder_text_color="white", text_color="white", fg_color="green", font=CTkFont(family="Ubuntu", size=24), width=219)

        self.main_screen_update_package_button = CTkButton(master=self.main_screen_frame, text="Update package", fg_color="green", font=CTkFont(family="Ubuntu", size=24), command=self.__update_package__)

        self.main_screen_install_button = CTkButton(master=self.main_screen_frame, text="Install", fg_color="green", font=CTkFont(family="Ubuntu", size=24), width=319, command=self.__install__)
        self.main_screen_install_button.grid(row=4, column=0, pady=0)

        self.main_screen_install_package_text = CTkLabel(master=self.main_screen_frame, text="Install package", text_color="green", font=CTkFont(family="Ubuntu", size=72))

        self.main_screen_install_package_entry = CTkEntry(master=self.main_screen_frame, placeholder_text="Package name", placeholder_text_color="white", text_color="white", fg_color="green", font=CTkFont(family="Ubuntu", size=24), width=219)

        self.main_screen_install_package_button = CTkButton(master=self.main_screen_frame, text="Install package", fg_color="green", font=CTkFont(family="Ubuntu", size=24), command=self.__install_package__)

        self.main_screen_delete_button = CTkButton(master=self.main_screen_frame, text="Delete", fg_color="green", font=CTkFont(family="Ubuntu", size=24), width=319, command=self.__delete__)
        self.main_screen_delete_button.grid(row=5, column=0, pady=0)

        self.main_screen_delete_package_text = CTkLabel(master=self.main_screen_frame, text="Delete package", text_color="green", font=CTkFont(family="Ubuntu", size=72))

        self.main_screen_delete_package_entry = CTkEntry(master=self.main_screen_frame, placeholder_text="Package name", placeholder_text_color="white", text_color="white", fg_color="green", font=CTkFont(family="Ubuntu", size=24), width=219)

        self.main_screen_delete_package_button = CTkButton(master=self.main_screen_frame, text="Delete package", fg_color="green", font=CTkFont(family="Ubuntu", size=24), command=self.__delete_package__)

        self.main_screen_show_packages_button = CTkButton(master=self.main_screen_frame, text="Show packages", fg_color="green", font=CTkFont(family="Ubuntu", size=24), width=319, command=lambda: call("pip list", shell=True))
        self.main_screen_show_packages_button.grid(row=6, column=0, pady=0)

        self.main_screen_exit_button = CTkButton(master=self.main_screen_frame, text="↵", fg_color="green", font=CTkFont(family="Ubuntu", size=24), height=20, width=20, command=self.__exit__)

    def __update__(self):
        self.main_screen_exit_button.place(x=3, y=3)
        self.main_screen_update_all_text.place(x=3, y=50)
        self.main_screen_update_all_button.place(x=3, y=135)
        self.main_screen_update_package_text.place(x=3, y=185)
        self.main_screen_update_package_entry.place(x=3, y=270)
        self.main_screen_update_package_button.place(x=225, y=270)

        self.main_screen_main_text_1.grid_forget()
        self.main_screen_main_text_2.grid_forget()
        self.main_screen_main_text_3.grid_forget()
        self.main_screen_update_button.grid_forget()
        self.main_screen_install_button.grid_forget()
        self.main_screen_delete_button.grid_forget()
        self.main_screen_show_packages_button.grid_forget()

    def __update_all__(self):
        self.packages = [dist.project_name for dist in pkg_resources.working_set]
        call("pip install --upgrade " + ' '.join(self.packages), shell=True)

    def __update_package__(self):
        self.package = self.main_screen_update_package_entry.get()
        if self.package == "":
           showwarning(message="enter name of the package")
        
        else:
            call("pip install --upgrade " + self.package, shell=True)
            self.main_screen_update_package_entry.delete("0", END)

    def __install__(self):
        self.main_screen_exit_button.place(x=3, y=3)
        self.main_screen_install_package_text.place(x=3, y=50)
        self.main_screen_install_package_entry.place(x=3, y=135)
        self.main_screen_install_package_button.place(x=225, y=135)

        self.main_screen_main_text_1.grid_forget()
        self.main_screen_main_text_2.grid_forget()
        self.main_screen_main_text_3.grid_forget()
        self.main_screen_update_button.grid_forget()
        self.main_screen_install_button.grid_forget()
        self.main_screen_delete_button.grid_forget()
        self.main_screen_show_packages_button.grid_forget()

    def __install_package__(self):
        self.package = self.main_screen_install_package_entry.get()
        if self.package == "":
           showwarning(message="enter name of the package")
        
        else:
            call("pip install " + self.package, shell=True)
            self.main_screen_install_package_entry.delete("0", END)

    def __delete__(self):
        self.main_screen_exit_button.place(x=3, y=3)
        self.main_screen_delete_package_text.place(x=3, y=50)
        self.main_screen_delete_package_entry.place(x=3, y=135)
        self.main_screen_delete_package_button.place(x=225, y=135)

        self.main_screen_main_text_1.grid_forget()
        self.main_screen_main_text_2.grid_forget()
        self.main_screen_main_text_3.grid_forget()
        self.main_screen_update_button.grid_forget()
        self.main_screen_install_button.grid_forget()
        self.main_screen_delete_button.grid_forget()
        self.main_screen_show_packages_button.grid_forget()

    def __delete_package__(self):
        self.package = self.main_screen_delete_package_entry.get()
        if self.package == "":
           showwarning(message="enter name of the package")
        
        else:
            call("pip uninstall " + self.package, shell=True)
            self.main_screen_delete_package_entry.delete("0", END)
         
    def __exit__(self):
        self.main_screen_main_text_1.grid(row=0, column=0)
        self.main_screen_main_text_2.grid(row=1, column=0)
        self.main_screen_main_text_3.grid(row=2, column=0)
        self.main_screen_update_button.grid(row=3, column=0)
        self.main_screen_install_button.grid(row=4, column=0)
        self.main_screen_delete_button.grid(row=5, column=0)
        self.main_screen_show_packages_button.grid(row=6, column=0)

        self.main_screen_exit_button.place_forget()
        self.main_screen_update_all_text.place_forget()
        self.main_screen_update_all_button.place_forget()                                         
        self.main_screen_update_package_text.place_forget()
        self.main_screen_update_package_entry.place_forget()
        self.main_screen_update_package_button.place_forget()

        self.main_screen_install_package_text.place_forget()
        self.main_screen_install_package_entry.place_forget()
        self.main_screen_install_package_button.place_forget()

        self.main_screen_delete_package_text.place_forget()
        self.main_screen_delete_package_entry.place_forget()
        self.main_screen_delete_package_button.place_forget()

if __name__ == "__main__":
    program = Program().mainloop()