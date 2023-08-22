from customtkinter import *
from tkinter import *
from pickle import *
from math import *
from unicodedata import *
from tkinter.messagebox import *

with open("my_calculus_settings.pickle", "rb") as data:
    language_data: str = load(data)

class Program(CTk):

    WIDTH: int = 500
    HEIGHT: int = 565
    TITLE: str = "My Calculus"
    COLOR_THEME: str = "dark-blue"
    ICON: str = "my calculus icon.ico"
    WIDGET_SCALING: float = 1.251

    def __init__(self, *args, **kwargs) -> None:
        CTk.__init__(self, *args, **kwargs)

        set_widget_scaling(self.WIDGET_SCALING)
        set_default_color_theme(self.COLOR_THEME)
        deactivate_automatic_dpi_awareness()

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        self.resizable(False, False)
        self.title(self.TITLE)
        self.iconbitmap(self.ICON)

        self.main_screen_entry_frame: CTkFrame = CTkFrame(master=self, width=480, height=200, fg_color="black")
        self.main_screen_entry_frame.grid(column=0, row=0, columnspan=5000)

        self.main_screen_expression_entry: CTkEntry = CTkEntry(master=self.main_screen_entry_frame, width=475, height=120, fg_color="transparent", border_width=0, text_color="green", font=("Roman", 135))
        self.main_screen_expression_entry.place(x=2, y=2)

        self.main_screen_result_entry: CTkEntry = CTkEntry(master=self.main_screen_entry_frame, width=475, height=20, fg_color="transparent", border_width=0, text_color="green", font=("Roman", 25), state="disabled")
        self.main_screen_result_entry.place(x=2, y=165)

        self.main_screen_procent_button: CTkButton = CTkButton(master=self, text="%", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=self.__procent__)
        self.main_screen_procent_button.grid(column=0, row=1, sticky="w")

        self.main_screen_sqrt_button: CTkButton = CTkButton(master=self, text="\/", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("sqrt()"))
        self.main_screen_sqrt_button.grid(column=1, row=1, sticky="w")

        self.main_screen_one_divided_by_x_button: CTkButton = CTkButton(master=self, text="1/x", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("1/"))
        self.main_screen_one_divided_by_x_button.grid(column=2, row=1, sticky="w")

        self.main_screen_number_in_second_degree_button: CTkButton = CTkButton(master=self, text="x2", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("**2"))
        self.main_screen_number_in_second_degree_button.grid(column=3, row=1, sticky="w")

        self.main_screen_clear_button: CTkButton = CTkButton(master=self, text="C", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.main_screen_expression_entry.delete("0", END))
        self.main_screen_clear_button.grid(column=4, row=1, sticky="w")
        
        self.main_screen_clear_everything_button: CTkButton = CTkButton(master=self, text="CE", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=self.__clear_everything__)
        self.main_screen_clear_everything_button.grid(column=5, row=1, sticky="w")

        self.main_screen_clear_number_button: CTkButton = CTkButton(master=self, text="<-", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.main_screen_expression_entry.delete(len(self.main_screen_expression_entry.get()) - 1, END))
        self.main_screen_clear_number_button.grid(column=6, row=1, sticky="w")

        self.main_screen_plus_button: CTkButton = CTkButton(master=self, text="+", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("+"))
        self.main_screen_plus_button.grid(column=7, row=1, sticky="w")

        self.main_screen_minus_button: CTkButton = CTkButton(master=self, text="-", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("-"))
        self.main_screen_minus_button.grid(column=7, row=2, sticky="w")

        self.main_screen_multiply_button: CTkButton = CTkButton(master=self, text="*", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("*"))
        self.main_screen_multiply_button.grid(column=7, row=3, sticky="e")

        self.main_screen_divide_button: CTkButton = CTkButton(master=self, text="/", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("/"))
        self.main_screen_divide_button.grid(column=7, row=4, sticky="e")

        self.main_screen_equal_button: CTkButton = CTkButton(master=self, text="=", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=self.__equation__)
        self.main_screen_equal_button.grid(column=7, row=5, sticky="e")

        self.main_screen_number_one_button: CTkButton = CTkButton(master=self, text="1", height=67, width=100, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("1"))
        self.main_screen_number_one_button.place(x=0, y=250)
        
        self.main_screen_number_two_button: CTkButton = CTkButton(master=self, text="2", height=67, width=100, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("2"))
        self.main_screen_number_two_button.place(x=100, y=250)

        self.main_screen_number_three_button: CTkButton = CTkButton(master=self, text="3", height=67, width=100, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("3"))
        self.main_screen_number_three_button.place(x=200, y=250)

        self.main_screen_number_four_button: CTkButton = CTkButton(master=self, text="4", height=67, width=100, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("4"))
        self.main_screen_number_four_button.place(x=0, y=317.5)

        self.main_screen_number_five_button: CTkButton = CTkButton(master=self, text="5", height=67, width=100, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("5"))
        self.main_screen_number_five_button.place(x=100, y=317.5)

        self.main_screen_number_six_button: CTkButton = CTkButton(master=self, text="6", height=67, width=100, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("6"))
        self.main_screen_number_six_button.place(x=200, y=317.5)

        self.main_screen_number_seven_button: CTkButton = CTkButton(master=self, text="7", height=67, width=100, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("7"))
        self.main_screen_number_seven_button.place(x=0, y=385)

        self.main_screen_number_eight_button: CTkButton = CTkButton(master=self, text="8", height=67, width=100, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("8"))
        self.main_screen_number_eight_button.place(x=100, y=385)

        self.main_screen_number_nine_button: CTkButton = CTkButton(master=self, text="9", height=67, width=100, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("9"))
        self.main_screen_number_nine_button.place(x=200, y=385)

        self.main_screen_number_zero_button: CTkButton = CTkButton(master=self, text="0", height=50, width=119.902, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("0"))
        self.main_screen_number_zero_button.place(x=300, y=250)

        self.main_screen_negative_number_button: CTkButton = CTkButton(master=self, text="+/-", height=50, width=119.902, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("-"))
        self.main_screen_negative_number_button.place(x=300, y=300.5)

        self.main_screen_comma_button: CTkButton = CTkButton(master=self, text=".", height=50, width=119.902, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("."))
        self.main_screen_comma_button.place(x=300, y=351)

        self.main_screen_mode_button: CTkButton = CTkButton(master=self, text="режим", height=50, width=119.902, fg_color="green", text_color="white", font=("Roman", 25), command=self.__mode_option__)
        self.main_screen_mode_button.place(x=300, y=401)

        self.main_screen_pi_button: CTkButton = CTkButton(master=self, text=lookup("GREEK SMALL LETTER PI"), height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("pi"))

        self.main_screen_e_button: CTkButton = CTkButton(master=self, text="e", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("e"))

        self.main_screen_cbrt_button: CTkButton = CTkButton(master=self, text="3\/", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("cbrt()"))

        self.main_screen_number_in_third_degree_button: CTkButton = CTkButton(master=self, text="x3", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("**3"))

        self.main_screen_number_module_button: CTkButton = CTkButton(master=self, text="|x|", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("fabs()"))

        self.main_screen_factorial_button: CTkButton = CTkButton(master=self, text="!x", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("factorial()"))

        self.main_screen_left_bracket_button: CTkButton = CTkButton(master=self, text="(", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__("("))

        self.main_screen_right_bracket_button: CTkButton = CTkButton(master=self, text=")", height=50, width=60, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: self.__button_operation__(")"))   

        self.main_screen_base_option: CTkComboBox = CTkComboBox(master=self, values=["binary-octal", "binary-decimal", "binary-hexadecimal", "octal-binary", "octal-decimal", "octal-hexadecimal", "decimal-binary", "decimal-octal", "decimal-hexadecimal", "hexadecimal-binary", "hexadecimal-octal", "hexadecimal-decimal"], height=50, width=479.7,  fg_color="green", border_color="green", button_color="green", button_hover_color="green", dropdown_fg_color="green", text_color="white", dropdown_text_color="white", font=("Roman", 32), dropdown_font=("Roman", 32), command=self.__change_base__)  

        if language_data == "Српски":
            self.main_screen_mode_button.configure(text="режим")

        elif language_data == "English":
            self.main_screen_mode_button.configure(text="mode")

        else:
            self.main_screen_mode_button.configure(text="режим")

    def __classical__(self) -> None:
        self.minsize(width=self.WIDTH, height=self.HEIGHT)

        self.main_screen_number_zero_button.configure(width=119.902)
        self.main_screen_negative_number_button.configure(width=119.902)
        self.main_screen_comma_button.configure(width=119.902)
        self.main_screen_mode_button.configure(width=119.902)

        self.main_screen_procent_button.grid(column=0, row=1, sticky="w")
        self.main_screen_sqrt_button.grid(column=1, row=1, sticky="w")
        self.main_screen_one_divided_by_x_button.grid(column=2, row=1, sticky="w")
        self.main_screen_number_in_second_degree_button.grid(column=3, row=1, sticky="w")
        self.main_screen_clear_button.grid(column=4, row=1, sticky="w")
        self.main_screen_clear_everything_button.grid(column=5, row=1, sticky="w")
        self.main_screen_clear_number_button.grid(column=6, row=1, sticky="w")
        self.main_screen_plus_button.grid(column=7, row=1, sticky="w")
        self.main_screen_minus_button.grid(column=7, row=2, sticky="w")
        self.main_screen_multiply_button.grid(column=7, row=3, sticky="e")
        self.main_screen_divide_button.grid(column=7, row=4, sticky="e")
        self.main_screen_equal_button.grid(column=7, row=5, sticky="e")

        self.main_screen_number_one_button.place(x=0, y=250)
        self.main_screen_number_two_button.place(x=100, y=250)
        self.main_screen_number_three_button.place(x=200, y=250)
        self.main_screen_number_four_button.place(x=0, y=317.5)
        self.main_screen_number_five_button.place(x=100, y=317.5)
        self.main_screen_number_six_button.place(x=200, y=317.5)
        self.main_screen_number_seven_button.place(x=0, y=385)
        self.main_screen_number_eight_button.place(x=100, y=385)
        self.main_screen_number_nine_button.place(x=200, y=385)

        self.main_screen_number_zero_button.place(x=300, y=250)
        self.main_screen_negative_number_button.place(x=300, y=300.5)
        self.main_screen_comma_button.place(x=300, y=351)
        self.main_screen_mode_button.place(x=300, y=401)

        self.main_screen_pi_button.grid_forget()
        self.main_screen_e_button.grid_forget()
        self.main_screen_cbrt_button.grid_forget()
        self.main_screen_number_in_third_degree_button.grid_forget()
        self.main_screen_number_module_button.grid_forget()
        self.main_screen_factorial_button.grid_forget()
        self.main_screen_left_bracket_button.grid_forget()
        self.main_screen_right_bracket_button.grid_forget()

        try:
            self.main_screen_scientific_calculator_additional_layout.destroy()

        except AttributeError:
            pass

        self.main_screen_base_option.place_forget()

    def __scientific__(self) -> None:
        self.minsize(width=self.WIDTH, height=628)

        self.main_screen_number_zero_button.configure(width=119.902)
        self.main_screen_negative_number_button.configure(width=119.902)
        self.main_screen_comma_button.configure(width=119.902)
        self.main_screen_mode_button.configure(width=119.902)

        self.main_screen_pi_button.grid(column=0, row=1, sticky="w")
        self.main_screen_e_button.grid(column=1, row=1, sticky="w")
        self.main_screen_cbrt_button.grid(column=2, row=1, sticky="w")
        self.main_screen_number_in_third_degree_button.grid(column=3, row=1, sticky="w")
        self.main_screen_number_module_button.grid(column=4, row=1, sticky="w")
        self.main_screen_factorial_button.grid(column=5, row=1, sticky="w")
        self.main_screen_left_bracket_button.grid(column=6, row=1, sticky="w")
        self.main_screen_right_bracket_button.grid(column=7, row=1, sticky="w")

        self.main_screen_procent_button.grid(column=0, row=2, sticky="w")
        self.main_screen_sqrt_button.grid(column=1, row=2, sticky="w")
        self.main_screen_one_divided_by_x_button.grid(column=2, row=2, sticky="w")
        self.main_screen_number_in_second_degree_button.grid(column=3, row=2, sticky="w")
        self.main_screen_clear_button.grid(column=4, row=2, sticky="w")
        self.main_screen_clear_everything_button.grid(column=5, row=2, sticky="w")
        self.main_screen_clear_number_button.grid(column=6, row=2, sticky="w")
        self.main_screen_plus_button.grid(column=7, row=2, sticky="w")
        self.main_screen_minus_button.grid(column=7, row=3, sticky="w")
        self.main_screen_multiply_button.grid(column=7, row=4, sticky="e")
        self.main_screen_divide_button.grid(column=7, row=5, sticky="e")
        self.main_screen_equal_button.grid(column=7, row=6, sticky="e")

        self.main_screen_number_one_button.place(x=0, y=300)
        self.main_screen_number_two_button.place(x=100, y=300)
        self.main_screen_number_three_button.place(x=200, y=300)
        self.main_screen_number_four_button.place(x=0, y=367.5)
        self.main_screen_number_five_button.place(x=100, y=367.5)
        self.main_screen_number_six_button.place(x=200, y=367.5)
        self.main_screen_number_seven_button.place(x=0, y=436)
        self.main_screen_number_eight_button.place(x=100, y=436)
        self.main_screen_number_nine_button.place(x=200, y=436)

        self.main_screen_number_zero_button.place(x=300, y=300)
        self.main_screen_negative_number_button.place(x=300, y=350.5)
        self.main_screen_comma_button.place(x=300, y=401)
        self.main_screen_mode_button.place(x=300, y=452)

        self.main_screen_base_option.place_forget()

        self.main_screen_scientific_calculator_additional_layout: Scientific_calculator_additional_layout = Scientific_calculator_additional_layout()

    def __programming__(self) -> None:
        self.minsize(width=self.WIDTH, height=self.HEIGHT)

        self.main_screen_number_zero_button.configure(width=179.902)
        self.main_screen_negative_number_button.configure(width=179.902)
        self.main_screen_comma_button.configure(width=179.902)
        self.main_screen_mode_button.configure(width=179.902)

        self.main_screen_base_option.place(x=0, y=200)

        self.main_screen_number_one_button.place(x=0, y=250)
        self.main_screen_number_two_button.place(x=100, y=250)
        self.main_screen_number_three_button.place(x=200, y=250)
        self.main_screen_number_four_button.place(x=0, y=317.5)
        self.main_screen_number_five_button.place(x=100, y=317.5)
        self.main_screen_number_six_button.place(x=200, y=317.5)
        self.main_screen_number_seven_button.place(x=0, y=385)
        self.main_screen_number_eight_button.place(x=100, y=385)
        self.main_screen_number_nine_button.place(x=200, y=385)

        self.main_screen_number_zero_button.place(x=300, y=250)
        self.main_screen_negative_number_button.place(x=300, y=300.5)
        self.main_screen_comma_button.place(x=300, y=351)
        self.main_screen_mode_button.place(x=300, y=401)

        self.main_screen_pi_button.grid_forget()
        self.main_screen_e_button.grid_forget()
        self.main_screen_cbrt_button.grid_forget()
        self.main_screen_number_in_third_degree_button.grid_forget()
        self.main_screen_number_module_button.grid_forget()
        self.main_screen_factorial_button.grid_forget()
        self.main_screen_left_bracket_button.grid_forget()
        self.main_screen_right_bracket_button.grid_forget()

        self.main_screen_procent_button.grid_forget()
        self.main_screen_sqrt_button.grid_forget()
        self.main_screen_one_divided_by_x_button.grid_forget()
        self.main_screen_number_in_second_degree_button.grid_forget()
        self.main_screen_clear_button.grid_forget()
        self.main_screen_clear_everything_button.grid_forget()
        self.main_screen_clear_number_button.grid_forget()
        self.main_screen_plus_button.grid_forget()
        self.main_screen_minus_button.grid_forget()
        self.main_screen_multiply_button.grid_forget()
        self.main_screen_divide_button.grid_forget()
        self.main_screen_equal_button.grid_forget()

        try:
            self.main_screen_scientific_calculator_additional_layout.destroy()

        except AttributeError:
            pass

    def __button_operation__(self, button: str) -> None:
        self.button: str = button
        self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
        self.main_screen_expression_entry.delete("0", END)
        self.main_screen_expression_entry.insert("0", f"{self.main_screen_expression_entry_data + self.button}")
        
    def __equation__(self) -> None:
        self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
        self.main_screen_result: str = eval(f"{self.main_screen_expression_entry_data}")

        self.main_screen_result_entry.configure(state="normal")
        self.main_screen_result_entry.delete("0", END)
        self.main_screen_result_entry.insert("0", f"резултат је {self.main_screen_result}")
        self.main_screen_result_entry.configure(state="disabled")

    def __procent__(self) -> None:
        self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
        self.main_screen_result: str = eval(f"{self.main_screen_expression_entry_data} / 100")

        self.main_screen_result_entry.configure(state="normal")
        self.main_screen_result_entry.delete("0", END)
        self.main_screen_result_entry.insert("0", f"резултат је {self.main_screen_result}")
        self.main_screen_result_entry.configure(state="disabled")

    def __clear_everything__(self) -> None:
        self.main_screen_expression_entry.delete("0", END)

        self.main_screen_result_entry.configure(state="normal")
        self.main_screen_result_entry.delete("0", END)
        self.main_screen_result_entry.configure(state="disabled") 

    def __mode_option__(self) -> None:
        self.main_screen_mode_option: Menu_Option = Menu_Option()
                                                                                     
    def __change_base__(self, configure) -> None:
        self.main_screen_count_system_result: str
        self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
        self.main_screen_base_data: str = self.main_screen_base_option.get()
        if self.main_screen_base_data == "binary-octal":
           self.main_screen_count_system_result = oct(int(self.main_screen_expression_entry_data, 2))

        elif self.main_screen_base_data == "binary-decimal":
           self.main_screen_count_system_result = int(self.main_screen_expression_entry_data, 2)

        elif self.main_screen_base_data == "binary-hexadecimal":
           self.main_screen_count_system_result = hex(int(self.main_screen_expression_entry_data, 2))

        elif self.main_screen_base_data == "octal-binary":
           self.main_screen_count_system_result = bin(int(self.main_screen_expression_entry_data, 8))

        elif self.main_screen_base_data == "octal-decimal":
           self.main_screen_count_system_result = int(self.main_screen_expression_entry_data, 8)

        elif self.main_screen_base_data == "octal-hexadecimal":
           self.main_screen_count_system_result = hex(int(self.main_screen_expression_entry_data, 8))

        elif self.main_screen_base_data == "decimal-binary":
           self.main_screen_count_system_result = bin(int(self.main_screen_expression_entry_data))

        elif self.main_screen_base_data == "decimal-octal":
           self.main_screen_count_system_result = oct(int(self.main_screen_expression_entry_data))

        elif self.main_screen_base_data == "decimal-hexadecimal":
           self.main_screen_count_system_result = hex(int(self.main_screen_expression_entry_data))

        elif self.main_screen_base_data == "hexadecimal-binary":
           self.main_screen_count_system_result = bin(int(self.main_screen_expression_entry_data, 16))

        elif self.main_screen_base_data == "hexadecimal-octal":
           self.main_screen_count_system_result = oct(int(self.main_screen_expression_entry_data, 16))

        else:
           self.main_screen_count_system_result = int(self.main_screen_expression_entry_data, 16)

        self.main_screen_result_entry.configure(state="normal")
        self.main_screen_result_entry.delete("0", END)
        self.main_screen_result_entry.insert("0", f"резултат је {self.main_screen_count_system_result}")
        self.main_screen_result_entry.configure(state="disabled")

    def __settings__(self) -> None:
        self.main_screen_settings_window: Settings_window = Settings_window()


class Menu_Option(CTkToplevel):

    WIDTH: int = 300
    HEIGHT: int = 250
    WINDOW: str = "-toolwindow"
    TITLE: str = "My Calculus menu option"

    def __init__(self, *args, **kwargs) -> None:
        CTkToplevel.__init__(self, *args, **kwargs)

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        self.resizable(False, False)
        self.title(self.TITLE)
        self.attributes(self.WINDOW, True)

        self.main_screen_classical_mode_button: CTkButton = CTkButton(master=self, text="класични", height=50, width=250, fg_color="green", text_color="white", font=("Roman", 25), command=program.__classical__)
        self.main_screen_classical_mode_button.grid(column=0, row=0)

        self.main_screen_scientific_mode_button: CTkButton = CTkButton(master=self, text="научни", height=50, width=250, fg_color="green", text_color="white", font=("Roman", 25), command=program.__scientific__)
        self.main_screen_scientific_mode_button.grid(column=0, row=1)

        self.main_screen_programming_mode_button: CTkButton = CTkButton(master=self, text="програмерски", height=50, width=250, fg_color="green", text_color="white", font=("Roman", 25), command=program.__programming__)
        self.main_screen_programming_mode_button.grid(column=0, row=2)

        self.main_screen_settings_button: CTkButton = CTkButton(master=self, text="подешавања", height=50, width=250, fg_color="green", text_color="white", font=("Roman", 25), command=program.__settings__)
        self.main_screen_settings_button.grid(column=0, row=3)

        if language_data == "Српски":
            self.main_screen_classical_mode_button.configure(text="класични")
            self.main_screen_scientific_mode_button.configure(text="научни")
            self.main_screen_programming_mode_button.configure(text="програмерски")
            self.main_screen_settings_button.configure(text="подешавања")

        elif language_data == "English":
            self.main_screen_classical_mode_button.configure(text="classic")
            self.main_screen_scientific_mode_button.configure(text="scientific")
            self.main_screen_programming_mode_button.configure(text="programming")
            self.main_screen_settings_button.configure(text="settings")

        else:
            self.main_screen_classical_mode_button.configure(text="классический")
            self.main_screen_scientific_mode_button.configure(text="научный")
            self.main_screen_programming_mode_button.configure(text="программный")
            self.main_screen_settings_button.configure(text="настройки")

class Scientific_calculator_additional_layout(CTkToplevel):
     
    WIDTH: int = 655 
    HEIGHT: int = 411
    WINDOW: str = "-toolwindow"
    TITLE: str = "My Calculus scientific calculator additional layout"

    def __init__(self, *args, **kwargs) -> None:
        CTkToplevel.__init__(self, *args, **kwargs)

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        self.resizable(False, False)
        self.title(self.TITLE)
        self.attributes(self.WINDOW, True)

        self.main_screen_functions_text: CTkLabel = CTkLabel(master=self, text="Functions", font=("Roman", 55))
        self.main_screen_functions_text.place(x=2, y=2)

        self.main_screen_logarith_function_button: CTkButton = CTkButton(master=self, text="logyX", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("log(x,y)"))
        self.main_screen_logarith_function_button.place(x=2, y=55)
        
        self.main_screen_natural_logarith_function_button: CTkButton = CTkButton(master=self, text="ln", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("log()"))
        self.main_screen_natural_logarith_function_button.place(x=72, y=55)

        self.main_screen_e_function_button: CTkButton = CTkButton(master=self, text="eX", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("e**"))
        self.main_screen_e_function_button.place(x=142, y=55)

        self.main_screen_root_function_button: CTkButton = CTkButton(master=self, text="y\/X", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("xyrt(number, x, y)"))
        self.main_screen_root_function_button.place(x=212, y=55)

        self.main_screen_number_in_y_degree_function_button: CTkButton = CTkButton(master=self, text="xY", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("**"))
        self.main_screen_number_in_y_degree_function_button.place(x=282, y=55)

        self.main_screen_two_in_x_degree_function_button: CTkButton = CTkButton(master=self, text="2X", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("2**"))
        self.main_screen_two_in_x_degree_function_button.place(x=352, y=55)

        self.main_screen_ten_in_x_degree_function_button: CTkButton = CTkButton(master=self, text="10X", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("10**"))
        self.main_screen_ten_in_x_degree_function_button.place(x=422, y=55)

        self.main_screen_trigonomical_functions_text: CTkLabel = CTkLabel(master=self, text="Trigonomical functions", font=("Roman", 55))
        self.main_screen_trigonomical_functions_text.place(x=2, y=110)

        self.main_screen_sin_function_button: CTkButton = CTkButton(master=self, text="sin", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("sin()"))
        self.main_screen_sin_function_button.place(x=2, y=175)

        self.main_screen_cos_function_button: CTkButton = CTkButton(master=self, text="cos", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("cos()"))
        self.main_screen_cos_function_button.place(x=72, y=175)

        self.main_screen_tan_function_button: CTkButton = CTkButton(master=self, text="tan", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("tan()"))
        self.main_screen_tan_function_button.place(x=142, y=175)

        self.main_screen_cotan_function_button: CTkButton = CTkButton(master=self, text="cotan", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("cotan()"))
        self.main_screen_cotan_function_button.place(x=212, y=175)

        self.main_screen_asin_function_button: CTkButton = CTkButton(master=self, text="asin", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("asin()"))
        self.main_screen_asin_function_button.place(x=283, y=175)

        self.main_screen_acos_function_button: CTkButton = CTkButton(master=self, text="acos", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("acos()"))
        self.main_screen_acos_function_button.place(x=353, y=175)

        self.main_screen_atan_function_button: CTkButton = CTkButton(master=self, text="atan", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("atan()"))
        self.main_screen_atan_function_button.place(x=423, y=175)

        self.main_screen_acotan_function_button: CTkButton = CTkButton(master=self, text="acotan", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("acotan()"))
        self.main_screen_acotan_function_button.place(x=2, y=226)

        self.main_screen_sinh_function_button: CTkButton = CTkButton(master=self, text="sinh", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("sinh()"))
        self.main_screen_sinh_function_button.place(x=86, y=226)

        self.main_screen_cosh_function_button: CTkButton = CTkButton(master=self, text="cosh", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("cosh()"))
        self.main_screen_cosh_function_button.place(x=156, y=226)

        self.main_screen_tanh_function_button: CTkButton = CTkButton(master=self, text="tanh", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("cosh()"))
        self.main_screen_tanh_function_button.place(x=226, y=226)

        self.main_screen_cotanh_function_button: CTkButton = CTkButton(master=self, text="cotanh", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("cosh()"))
        self.main_screen_cotanh_function_button.place(x=296, y=226)

        self.main_screen_asinh_function_button: CTkButton = CTkButton(master=self, text="asinh", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("asinh()"))
        self.main_screen_asinh_function_button.place(x=380, y=226)

        self.main_screen_acosh_function_button: CTkButton = CTkButton(master=self, text="acosh", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("acosh()"))
        self.main_screen_acosh_function_button.place(x=450, y=226)

        self.main_screen_atanh_function_button: CTkButton = CTkButton(master=self, text="atanh", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("atanh()"))
        self.main_screen_atanh_function_button.place(x=2, y=277)

        self.main_screen_atanh_function_button: CTkButton = CTkButton(master=self, text="acotanh", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("acotanh()"))
        self.main_screen_atanh_function_button.place(x=75, y=277)

        self.main_screen_degree_function_button: CTkButton = CTkButton(master=self, text="deg", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("degrees()"))
        self.main_screen_degree_function_button.place(x=172, y=277)

        self.main_screen_radian_function_button: CTkButton = CTkButton(master=self, text="rad", height=50, width=70, fg_color="green", text_color="white", font=("Roman", 25), command=lambda: program.__button_operation__("radians()"))
        self.main_screen_radian_function_button.place(x=242, y=277)

        if language_data == "Српски":
            self.main_screen_functions_text.configure(text="Функције")
            self.main_screen_trigonomical_functions_text.configure(text="Тригонометричке функције")

        elif language_data == "English":
            self.main_screen_functions_text.configure(text="Functions")
            self.main_screen_trigonomical_functions_text.configure(text="Trigonometric functions")

        else:
            self.main_screen_functions_text.configure(text="Функции")
            self.main_screen_trigonomical_functions_text.configure(text="Тригонометрические функции")

class Settings_window(CTkToplevel):
     
    WIDTH: int = 655 
    HEIGHT: int = 411
    TITLE: str = "My Calculus settings window"
    WINDOW: str = "-toolwindow"

    def __init__(self, *args, **kwargs) -> None:
        CTkToplevel.__init__(self, *args, **kwargs)

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        self.resizable(False, False)
        self.title(self.TITLE)
        self.attributes(self.WINDOW, True)

        self.main_screen_settings_text: CTkLabel = CTkLabel(master=self, text="Подешавања", font=("Roman", 75))
        self.main_screen_settings_text.place(x=0, y=0)

        self.main_screen_language_text: CTkLabel = CTkLabel(master=self, text="Језици", font=("Roman", 50))
        self.main_screen_language_text.place(x=0, y=87)

        self.main_screen_settings_language_option: CTkSegmentedButton = CTkSegmentedButton(master=self, values=["Српски", "English", "Русский"], selected_color="green", command=self.__language_settings__)
        self.main_screen_settings_language_option.place(x=15, y=147)

        self.main_screen_settings_language_option.set(language_data)

        if language_data == "Српски":
            self.main_screen_settings_text.configure(text="Подешавања")
            self.main_screen_language_text.configure(text="Језици")

        elif language_data == "English":
            self.main_screen_settings_text.configure(text="Settings")
            self.main_screen_language_text.configure(text="Languages")

        else:
            self.main_screen_settings_text.configure(text="Настройки")
            self.main_screen_language_text.configure(text="Языки")

    def __language_settings__(self, pickle) -> None:
        self.main_screen_settings_language_option_data: str = self.main_screen_settings_language_option.get()
        with open("my_calculus_settings.pickle", "wb") as self.data:
            dump(self.main_screen_settings_language_option_data, self.data)

        if self.main_screen_settings_language_option_data == "Српски":
            showwarning(title="Пажња", message="Рестартуј програм")

        elif self.main_screen_settings_language_option_data == "English":
            showwarning(title="Warning", message="Restart program")

        else:
            showwarning(title="Внимание", message="Перезагрузите программу")

def xyrt(number: float, x: float, y: float) -> float:
    xyrt: float = number ** (x / y)
    return xyrt

def cotan(number: float) -> float:
    cotangent: float = 1 / tan(number)
    return cotangent

def acotan(number: float) -> float:
    acotangent: float = 1 / atan(number)
    return acotangent

def cotanh(number: float) -> float:
    cotangenthyper: float = 1 / tanh(number)
    return cotangenthyper

def acotanh(number: float) -> float:
    acotangenthyper: float = 1 / atanh(number)
    return acotangenthyper

if __name__ == "__main__":
    try:
        program: Program = Program()
        program.mainloop()
	
    except FileNotFoundError:
        showerror(message="error: missing data file")
    
    except TclError:
        showerror(message="error: missing icon file")

    except EOFError:
	    showerror(message="error: corrupted data file")

else:
	showwarning(title="not script file", message="this is not script file")