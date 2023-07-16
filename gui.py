import math
import tkinter as tk
import tkinter.messagebox as messagebox

def toggle_more_info():
    if more_info_button.cget("text") == "자세히 보기":
        more_info_button.config(text="요약 보기")
        result_label3.grid()
        result_label4.grid()
        result_label5.grid()
        result_label6.grid()
        result_label7.grid()
    else:
        more_info_button.config(text="자세히 보기")
        result_label3.grid_remove()
        result_label4.grid_remove()
        result_label5.grid_remove()
        result_label6.grid_remove()
        result_label7.grid_remove()

def calculate_gravity():
    try:
        latitude = float(latitude_entry.get())
        h = float(height_entry.get())
        observed_gravity = float(gravity_entry.get())

        def sin(degree):
            return math.sin(math.radians(degree))

        def cos(degree):
            return math.cos(math.radians(degree))

        def tan(degree):
            return math.tan(math.radians(degree))

        standard_gravity = 978031.85 * (1 + 0.005278895 * sin(latitude) ** 2 + 0.000023462 * sin(latitude) ** 4)
        FAC = 0.3086 * h
        is_water = water_var.get()

        if is_water == 1:
            if water_density_entry.get():
                water_density = float(water_density_entry.get())
            else:
                water_density = 1.03
            if rock_density_entry.get():
                rock_density = float(rock_density_entry.get())
            else:
                rock_density = 2.57  # Set default value to 2.57 (Granite density)
            BC = 0.0419 * (water_density - rock_density) * h
        else:
            if rock_density_entry.get():
                rock_density = float(rock_density_entry.get())
            else:
                rock_density = 2.57  # Set default value to 2.57 (Granite density)
            BC = 0.0419 * rock_density * h

        air_correction = 0.87 - 0.0000965 * h
        TC = float(terrain_correction_entry.get())
        perfect_BC = standard_gravity + FAC - BC + air_correction + TC

        if gravity_unit_var.get() == 1:
            result_text.set(f"측정 지점에서의 중력은 {perfect_BC} mgal 입니다.")
            result_text2.set(f"측정 지점에서의 완전부게이상은 {perfect_BC - standard_gravity} mgal 입니다.")
            result_text3.set(f"측정 지점에서의 표준 중력은 {standard_gravity} mgal 입니다.")
            result_text4.set(f"측정 지점에서의 프리에어 보정값은 {FAC} mgal 입니다.")
            result_text5.set(f"측정 지점에서의 단순 부게 보정값은 {BC} mgal 입니다.")
            result_text6.set(f"측정 지점에서의 대기 보정값은 {air_correction} mgal 입니다.")
            result_text7.set(f"측정 지점에서의 지형 보정값은 {TC} mgal 입니다.")
        else:
            result_text.set(f"측정 지점에서의 중력은 {perfect_BC / 1000} gal 입니다.")
            result_text2.set(f"측정 지점에서의 완전부게이상은 {(perfect_BC - standard_gravity) / 1000} gal 입니다.")
            result_text3.set(f"측정 지점에서의 표준 중력은 {standard_gravity / 1000} gal 입니다.")
            result_text4.set(f"측정 지점에서의 프리에어 보정값은 {FAC / 1000} gal 입니다.")
            result_text5.set(f"측정 지점에서의 단순 부게 보정값은 {BC / 1000} gal 입니다.")
            result_text6.set(f"측정 지점에서의 대기 보정값은 {air_correction / 1000} gal 입니다.")
            result_text7.set(f"측정 지점에서의 지형 보정값은 {TC / 1000} gal 입니다.")

        if is_water == 1:
            water_density_entry.config(state="normal")
            water_density_label.config(state="normal")
            rock_density_entry.config(state="normal")
        else:
            water_density_entry.config(state="disabled")
            water_density_label.config(state="disabled")
            rock_density_entry.config(state="normal")

    except Exception as e:
        if "could not convert string to float" in str(e):
            messagebox.showerror("Error", "모든 필드를 입력했는지 확인해 주세요.")
        else:
            messagebox.showerror("Error", str(e))

def water_checkbutton_changed():
    is_water = water_var.get()
    if is_water == 1:
        water_density_entry.config(state="normal")
        water_density_label.config(state="normal")
        rock_density_entry.config(state="normal")
    else:
        water_density_entry.config(state="disabled")
        water_density_label.config(state="disabled")
        rock_density_entry.config(state="normal")

root = tk.Tk()
root.title("Gravity Correction Master v1.0")

# Title Label
title_label = tk.Label(root, text="Gravity Correction Master v1.0", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Developed By Label
developed_by_label = tk.Label(root, text="Developed by JeongHoon Lim", font=("Arial", 10))
developed_by_label.grid(row=1, column=0, columnspan=2)

# Variables
result_text = tk.StringVar()
result_text2 = tk.StringVar()
result_text3 = tk.StringVar()
result_text4 = tk.StringVar()
result_text5 = tk.StringVar()
result_text6 = tk.StringVar()
result_text7 = tk.StringVar()

# Labels
latitude_label = tk.Label(root, text="위도를 입력하세요(소수 입력 가능): ")
latitude_label.grid(row=2, column=0, sticky="e")

height_label = tk.Label(root, text="측점의 고도(지오이드고)를 입력하세요(m): ")
height_label.grid(row=3, column=0, sticky="e")

gravity_label = tk.Label(root, text="관측중력값을 입력하세요(mgal): ")
gravity_label.grid(row=4, column=0, sticky="e")

water_label = tk.Label(root, text="바다에서 측정했나요?")
water_label.grid(row=5, column=0, sticky="e")

water_density_label = tk.Label(root, text="측정 지점에서의 물(액체)의 밀도(g/cm^3): ", state="disabled")
water_density_label.grid(row=6, column=0, sticky="e")

rock_density_label = tk.Label(root, text="측정 지점에서의 암석의 밀도(g/cm^3): ")
rock_density_label.grid(row=7, column=0, sticky="e")

rock_density_info_label = tk.Label(root, text="* 미입력시 화강암의 밀도인 2.57g/cm^3가 자동으로 적용됩니다.", font=("Arial", 11))
rock_density_info_label.grid(row=8, column=0, columnspan=2, sticky="e")

terrain_correction_label = tk.Label(root, text="지형 보정값을 입력해 주세요: ")
terrain_correction_label.grid(row=9, column=0, sticky="e")

gravity_unit_label = tk.Label(root, text="표시 단위를 선택하세요: ")
gravity_unit_label.grid(row=10, column=0, sticky="e")

result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=12, column=0, columnspan=2)

result_label2 = tk.Label(root, textvariable=result_text2)
result_label2.grid(row=13, column=0, columnspan=2)

result_label3 = tk.Label(root, textvariable=result_text3)
result_label3.grid(row=14, column=0, columnspan=2)
result_label3.grid_remove()

result_label4 = tk.Label(root, textvariable=result_text4)
result_label4.grid(row=15, column=0, columnspan=2)
result_label4.grid_remove()

result_label5 = tk.Label(root, textvariable=result_text5)
result_label5.grid(row=16, column=0, columnspan=2)
result_label5.grid_remove()

result_label6 = tk.Label(root, textvariable=result_text6)
result_label6.grid(row=17, column=0, columnspan=2)
result_label6.grid_remove()

result_label7 = tk.Label(root, textvariable=result_text7)
result_label7.grid(row=18, column=0, columnspan=2)
result_label7.grid_remove()

# Entry fields
latitude_entry = tk.Entry(root)
latitude_entry.grid(row=2, column=1)

height_entry = tk.Entry(root)
height_entry.grid(row=3, column=1)

gravity_entry = tk.Entry(root)
gravity_entry.grid(row=4, column=1)

water_var = tk.IntVar()
water_checkbutton = tk.Checkbutton(root, text="예", variable=water_var, command=water_checkbutton_changed)
water_checkbutton.grid(row=5, column=1, sticky="w")

water_density_entry = tk.Entry(root, state="disabled")
water_density_entry.grid(row=6, column=1)

rock_density_entry = tk.Entry(root)
rock_density_entry.grid(row=7, column=1)

terrain_correction_entry = tk.Entry(root)
terrain_correction_entry.grid(row=9, column=1)

gravity_unit_var = tk.IntVar()
gravity_unit_radiobutton1 = tk.Radiobutton(root, text="mgal", variable=gravity_unit_var, value=1)
gravity_unit_radiobutton1.grid(row=10, column=1, sticky="w")
gravity_unit_radiobutton2 = tk.Radiobutton(root, text="gal", variable=gravity_unit_var, value=0)
gravity_unit_radiobutton2.grid(row=11, column=1, sticky="w")

# Button
calculate_button = tk.Button(root, text="보정 계산하기", command=calculate_gravity)
calculate_button.grid(row=11, column=0, sticky="e")

more_info_button = tk.Button(root, text="자세히 보기", command=toggle_more_info)
more_info_button.grid(row=19, column=0, columnspan=2, pady=10)

root.mainloop()
