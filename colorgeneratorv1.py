import colorsys
import tkinter as tk

#creating the data
data = {
    "base_colour" : ""
}

dull_mute_colours = ["#A75051", "#B27D58", "#B3AF38", "#589A5D", "#4781A7", "#746198"]
bright_colours = ["#EE4C52", "#F9AF15", "#FAF057", "#B7D332", "#54B5D2", "#9369C6"]

dull = True

def convert(base_hex):
    base_hex = base_hex.lstrip("#")
    r = int(base_hex[:2], 16)
    g = int(base_hex[2:4], 16)
    b = int(base_hex[4:], 16)
    
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    return h, s, v

def store_colours(a_list):
    global data
    data["colour1"] = a_list[0]
    data["colour2"] = a_list[1]
    data["colour3"] = a_list[2]
    data["colour4"] = a_list[3]
    data["colour5"] = a_list[4]

def monochromatic(base_hex):
    h, s, v = convert(base_hex)

    scheme = []
    for i in range(2, 0, -1):
        new_v = max(0, v * (1 - 0.2 * i))
        new_r, new_g, new_b = colorsys.hsv_to_rgb(h, s, new_v)

        hex_colour = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
        scheme.append(hex_colour)
    
    scheme.append(base_hex)

    for i in range(1, 3):
        new_v = min(1, v * (1 + 0.2 * i))
        new_r, new_g, new_b = colorsys.hsv_to_rgb(h, s, new_v)

        hex_colour = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
        scheme.append(hex_colour)
    
    return scheme

def analogous(base_hex):
    scheme = monochromatic(base_hex)
    for i in range(0, 2):
        current = scheme[i]

        h, s, v = convert(current)

        if h >= 0.5:
            new_h = min(1, h * (1 + 0.1 * (i + 1)))
        else:
            new_h = max(0, h * (1 - 0.1 * (i + 1)))
        new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, s, v)

        hex_colour = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
        scheme[i] = hex_colour

    for i in range(3, 5):
        current = scheme[i]

        h, s, v = convert(current)

        if h >= 0.5:
            new_h = max(0, h * (1 - 0.05 * (i + 1)))
        else:
            new_h = min(1, h * (1 + 0.05 * (i + 1)))
        new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, s, v)

        hex_colour = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
        scheme[i] = hex_colour
    return scheme

def complementary(base_hex):
    scheme = monochromatic(base_hex)
    
    for i in range(0, 5):
        current = scheme[i]
        h, s, v = convert(current)

        if i == 0:
            if h >= 0.5:
                new_h = min(1, h * (1 + 0.1 * (i + 1)))
            else:
                new_h = max(0, h * (1 - 0.1 * (i + 1)))
            new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, s, v)

            hex_colour = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
            scheme[i] = hex_colour
        elif i == 1:
            if h >= 0.5:
                new_h = h - 0.5
            else:
                new_h = h + 0.5
            new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, s, v)

            hex_colour = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
            scheme[i] = hex_colour
        elif i == 3:
            if h >= 0.5:
                new_h = h - 0.5
            else:
                new_h = h + 0.5
            new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, s, v)

            hex_colour = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
            scheme[i] = hex_colour
        elif i == 4:
            if h >= 0.5:
                new_h = max(0, h * (1 - 0.05 * (i + 1)))
            else:
                new_h = min(1, h * (1 + 0.05 * (i + 1)))
            new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, s, v)

            hex_colour = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
            scheme[i] = hex_colour
        else:
            continue
    return scheme

def warmer_button_instructions():
    global data
    h, s, v = convert(data["adjusted_colour"])
    new_h = min(1, h * 1.05)
    new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, s, v)
    data["adjusted_colour"] = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
    adjusted_tile = tk.Label(colour_frame, bg = data["adjusted_colour"], width = 10, height = 5)
    adjusted_tile.grid(row = 0, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)
    colour_hex = tk.Label(colour_frame, text = data["adjusted_colour"], width = 10)
    colour_hex.grid(row = 2, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)

def cooler_button_instructions():
    global data
    h, s, v =convert(data["adjusted_colour"])
    new_h = max(0, h * 0.95)
    new_r, new_g, new_b = colorsys.hsv_to_rgb(new_h, s, v)
    data["adjusted_colour"] = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
    adjusted_tile = tk.Label(colour_frame, bg = data["adjusted_colour"], width = 10, height = 5)
    adjusted_tile.grid(row = 0, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)
    colour_hex = tk.Label(colour_frame, text = data["adjusted_colour"], width = 10)
    colour_hex.grid(row = 2, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)

def increase_button_instructions():
    global data
    h, s, v = convert(data["adjusted_colour"])
    new_s = min(1, s * 1.05)
    new_r, new_g, new_b = colorsys.hsv_to_rgb(h, new_s, v)
    data["adjusted_colour"] = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
    adjusted_tile = tk.Label(colour_frame, bg = data["adjusted_colour"], width = 10, height = 5)
    adjusted_tile.grid(row = 0, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)
    colour_hex = tk.Label(colour_frame, text = data["adjusted_colour"], width = 10)
    colour_hex.grid(row = 2, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)

def decrease_button_instructions():
    global data
    h, s, v = convert(data["adjusted_colour"])
    new_s = max(0, s * 0.95)
    new_r, new_g, new_b = colorsys.hsv_to_rgb(h, new_s, v)
    data["adjusted_colour"] = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
    adjusted_tile = tk.Label(colour_frame, bg = data["adjusted_colour"], width = 10, height = 5)
    adjusted_tile.grid(row = 0, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)
    colour_hex = tk.Label(colour_frame, text = data["adjusted_colour"], width = 10)
    colour_hex.grid(row = 2, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)

def brighter_button_instructions():
    global data
    h, s, v = convert(data["adjusted_colour"])
    new_v = min(1, v * 1.05)
    new_r, new_g, new_b = colorsys.hsv_to_rgb(h, s, new_v)
    data["adjusted_colour"] = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
    adjusted_tile = tk.Label(colour_frame, bg = data["adjusted_colour"], width = 10, height = 5)
    adjusted_tile.grid(row = 0, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)
    colour_hex = tk.Label(colour_frame, text = data["adjusted_colour"], width = 10)
    colour_hex.grid(row = 2, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)

def darker_button_instructions():
    global data
    h, s, v = convert(data["adjusted_colour"])
    new_v = max(0, v * 0.95)
    new_r, new_g, new_b = colorsys.hsv_to_rgb(h, s, new_v)
    data["adjusted_colour"] = "#{:02x}{:02x}{:02x}".format(int(new_r * 255), int(new_g * 255), int(new_b * 255))
    adjusted_tile = tk.Label(colour_frame, bg = data["adjusted_colour"], width = 10, height = 5)
    adjusted_tile.grid(row = 0, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)
    colour_hex = tk.Label(colour_frame, text = data["adjusted_colour"], width = 10)
    colour_hex.grid(row = 2, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)

root = tk.Tk()
root.title("color generator")
root.geometry("1000x600")
colour_frame = tk.Frame(root)
colour_frame.pack(pady = 10)
adjust_frame = tk.Frame(root)
adjust_frame.pack(pady = 10)

def exitbutton():
    def closeapp():
        root.destroy()
    close = tk.Button(root, text = "exit", command = closeapp)
    close.place(relx = 0.6, rely = 0.9, anchor = "center")

def revert_to_original():
    def revert_button_instructions():
        destroy_adjust_buttons()
        adjusted_tile = tk.Label(colour_frame, bg = data["original_colour"], width = 10, height = 5)
        adjusted_tile.grid(row = 0, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)
        colour_hex = tk.Label(colour_frame, text = data["original_colour"], width = 10)
        colour_hex.grid(row = 2, column = data["adjust_colour_num"] - 1, padx = 5, pady = 5)
    revert_button = tk.Button(colour_frame, text = "revert", command = revert_button_instructions)
    revert_button.grid(row = 6, column = 2, padx = 5, pady = 5)

def destroy_adjust_buttons():
    for widget in adjust_frame.winfo_children():
        widget.destroy()

def how_to_start():
    start_text = tk.Label(colour_frame, text = "select option")
    start_text.pack(pady = 20)
    select_start = tk.StringVar(value = "colour in mind (in hex code)")
    start_options = tk.OptionMenu(colour_frame, select_start, "colour in mind (in hex code)", "no colour in mind")
    start_options.pack(pady = 10)

    def start_button_instructions():
        choosen_start = select_start.get()
        start_button.destroy()
        start_text.destroy()
        start_options.destroy()
        if choosen_start == "no colour in mind":
            no_idea_start()
        else:
            base_colour_start()
    start_button = tk.Button(colour_frame, text = "start", command = start_button_instructions)
    start_button.pack(pady = 10)

def no_idea_start():
    select_variation_text = tk.Label(colour_frame, text = "Select variation")
    select_variation_text.pack(pady = 20)
    select_variation = tk.StringVar(value = "dull/muted")
    variation = tk.OptionMenu(colour_frame, select_variation, "dull/muted", "bright")
    variation.pack(pady = 10)

    def next_button_instructions():
        choosen_variation = select_variation.get()
        next_button.destroy()
        select_variation_text.destroy()
        variation.destroy()
        if choosen_variation == "bright":
            global dull
            dull = False
        #print(dull)
        choose_base()
    next_button = tk.Button(colour_frame, text = "next", command = next_button_instructions)
    next_button.pack(pady = 10)

def choose_base():
    global dull
    if dull:
        global dull_mute_colours
        for i in range(0, 6):
            current = dull_mute_colours[i]
            colour_tile = tk.Label(colour_frame, bg = current, width = 10, height = 5)
            colour_tile.grid(row = 0, column = i, padx = 5, pady = 5)
            option_label = tk.Label(colour_frame, text = f"Option{i + 1}", width = 10)
            option_label.grid(row = 1, column = i, padx = 5, pady = 5)
        select_option = tk.StringVar(value = "Option 1")
        options = tk.OptionMenu(colour_frame, select_option, "option1", "option2", "option3", "option4", "option5", "option6")
        options.grid(row = 2, column = 2, padx = 5, pady = 5)

        def next2_button_instructions():
            choosen_option = select_option.get()
            global data
            global dull_mute_colours
            if choosen_option == "option2":
                data["base_colour"] = dull_mute_colours[1]
            elif choosen_option == "option3":
                data["base_colour"] = dull_mute_colours[2]
            elif choosen_option == "option4":
                data["base_colour"] = dull_mute_colours[3]
            elif choosen_option == "option5":
                data["base_colour"] = dull_mute_colours[4]
            elif choosen_option == "option6":
                data["base_colour"] = dull_mute_colours[5]
            else:
                data["base_colour"] = dull_mute_colours[0]
            for widget in colour_frame.winfo_children():
                widget.destroy()
            scheme_and_generate(data["base_colour"])
        next2_button = tk.Button(colour_frame, text = "next", command = next2_button_instructions)
        next2_button.grid(row = 2, column = 3, padx = 5,pady = 5)

    else:
        global bright_colours
        for i in range(0, 6):
            current = bright_colours[i]
            colour_tile = tk.Label(colour_frame, bg = current, width = 10, height = 5)
            colour_tile.grid(row = 0, column = i, padx = 5, pady = 5)
            option_label = tk.Label(colour_frame, text = f"Option{i + 1}", width = 10)
            option_label.grid(row = 1, column = i, padx = 5, pady = 5)
        select_option = tk.StringVar(value = "Option 1")
        options = tk.OptionMenu(colour_frame, select_option, "option1", "option2", "option3", "option4", "option5", "option6")
        options.grid(row = 2, column = 2, padx = 5, pady = 5)

        def next2_button_instructions():
            choosen_option = select_option.get()
            global data
            global bright_colours
            if choosen_option == "option2":
                data["base_colour"] = dull_mute_colours[1]
            elif choosen_option == "option3":
                data["base_colour"] = bright_colours[2]
            elif choosen_option == "option4":
                data["base_colour"] = bright_colours[3]
            elif choosen_option == "option5":
                data["base_colour"] = bright_colours[4]
            elif choosen_option == "option6":
                data["base_colour"] = bright_colours[5]
            else:
                data["base_colour"] = bright_colours[0]
            for widget in colour_frame.winfo_children():
                widget.destroy()
            scheme_and_generate(data["base_colour"])
        next2_button = tk.Button(colour_frame, text = "next", command = next2_button_instructions)
        next2_button.grid(row = 2, column = 3, padx = 5,pady = 5)

def base_colour_start():
    text = tk.Label(colour_frame, text = "Enter a colour in hex (include '#')")
    text.pack(pady = 20)
    input_colour = tk.Entry(colour_frame, width = 30)
    input_colour.pack(pady = 10)

    def enter_button_instructions():
    #def enter_button_instructions(chloe):
        global data
        data["base_colour"] = input_colour.get()
        #print(data["base_colour"])
        enter_button.destroy()
        text.destroy()
        input_colour.destroy()
        scheme_and_generate(data["base_colour"])
    #enter_button = tk.Button(colour_frame, text = "Enter", command = lambda : enter_button_instructions(base_colour))
    enter_button = tk.Button(colour_frame, text = "Enter", command = enter_button_instructions)
    enter_button.pack(pady = 10)

def scheme_and_generate(base_colour):
    text2 = tk.Label(colour_frame, text = "Select colour scheme")
    text2.pack(pady = 20)
    select_field = tk.StringVar(value = "monochromatic")
    select = tk.OptionMenu(colour_frame, select_field, "monochromatic", "analogous", "complementary")
    select.pack(pady = 10)

    def generate_button_instructions():
        choosen_scheme = select_field.get()
        if choosen_scheme == "analogous":
            colours = analogous(base_colour)
            store_colours(colours)
        elif choosen_scheme == "complementary":
            colours = complementary(base_colour)
            store_colours(colours)
        else:
            colours = monochromatic(base_colour)
            store_colours(colours)
        
        for widget in colour_frame.winfo_children():
            widget.destroy()
        
        for i in range(0, 5):
            current = colours[i]
            colour_tile = tk.Label(colour_frame, bg = current, width = 10, height = 5)
            colour_tile.grid(row = 0, column = i, padx = 5, pady = 5)
            colour_num = tk.Label(colour_frame, text = f"colour{i + 1}")
            colour_num.grid(row = 1, column = i, padx = 5, pady = 5)
        global data
        hex_label1 = tk.Label(colour_frame, text = data["colour1"], width = 10)
        hex_label1.grid(row = 2, column = 0, padx = 5, pady = 5)
        hex_label2 = tk.Label(colour_frame, text = data["colour2"], width = 10)
        hex_label2.grid(row = 2, column = 1, padx = 5, pady = 5)
        hex_label3 = tk.Label(colour_frame, text = data["colour3"], width = 10)
        hex_label3.grid(row = 2, column = 2, padx = 5, pady = 5)
        hex_label4 = tk.Label(colour_frame, text = data["colour4"], width = 10)
        hex_label4.grid(row = 2, column = 3, padx = 5, pady = 5)
        hex_label5 = tk.Label(colour_frame, text = data["colour5"], width = 10)
        hex_label5.grid(row = 2, column = 4, padx = 5, pady = 5)
        choose_adjust()
        #print(data)

    generate_button = tk.Button(colour_frame, text = "generate", command = generate_button_instructions)
    generate_button.pack(pady = 10)

def choose_adjust():
    select_adjust = tk.StringVar(value = "colour1")
    adjust_options = tk.OptionMenu(colour_frame, select_adjust, "colour1", "colour2", "colour3", "colour4", "colour5")
    adjust_options.grid(row = 3, column = 1, padx = 5, pady = 5)

    def adjust_button_instructions():
        global data
        colour_to_adjust = select_adjust.get()
        data["choosen_colour_option"] = colour_to_adjust
        if colour_to_adjust == "colour2":
            data["original_colour"] = data["colour2"]
            data["adjust_colour_num"] = 2
        elif colour_to_adjust == "colour3":
            data["original_colour"] = data["colour3"]
            data["adjust_colour_num"] = 3
        elif colour_to_adjust == "colour4":
            data["original_colour"] = data["colour4"]
            data["adjust_colour_num"] = 4
        elif colour_to_adjust == "colour5":
            data["original_colour"] = data["colour5"]
            data["adjust_colour_num"] = 5
        else:
            data["original_colour"] = data["colour1"]
            data["adjust_colour_num"] = 1
        data["adjusted_colour"] = data["original_colour"]
        choose_hsv()
    adjust_button = tk.Button(colour_frame, text = "adjust", command = adjust_button_instructions)
    adjust_button.grid(row = 3, column = 3, padx = 5, pady = 5)
    
def choose_hsv():
    select_hsv = tk.StringVar(value = "hue")
    hsv_options = tk.OptionMenu(colour_frame, select_hsv, "hue", "saturation", "value")
    hsv_options.grid(row = 4, column = 1, padx = 5, pady = 5)

    def go_button_instructions():
        revert_to_original()
        destroy_adjust_buttons()
        choosen_hsv = select_hsv.get()
        if choosen_hsv == "saturation":
            increase_button = tk.Button(adjust_frame, text = "increase", command = increase_button_instructions)
            increase_button.grid(row = 5, column = 1, padx = 5, pady = 5)
            
            decrease_button = tk.Button(adjust_frame, text = "decrease", command = decrease_button_instructions)
            decrease_button.grid(row = 5, column = 3, padx = 5, pady = 5)

        elif choosen_hsv == "value":
            brighter_button = tk.Button(adjust_frame, text = "brighter", command = brighter_button_instructions)
            brighter_button.grid(row = 5, column = 1, padx = 5, pady = 5)

            darker_button = tk.Button(adjust_frame, text = "darker", command = darker_button_instructions)
            darker_button.grid(row = 5, column = 3, padx = 5, pady = 5)

        else:
            warmer_button = tk.Button(adjust_frame, text = "cooler", command = warmer_button_instructions)
            warmer_button.grid(row = 5, column = 1, padx = 5, pady = 5)

            cooler_button = tk.Button(adjust_frame, text = "warmer", command = cooler_button_instructions)
            cooler_button.grid(row = 5, column = 3, padx = 5, pady = 5)

    go_button = tk.Button(colour_frame, text = "go", command = go_button_instructions)
    go_button.grid(row = 4, column = 3, padx = 5, pady = 5)

def restart():
    def restart_button_instructions():
        for widget in colour_frame.winfo_children():
            widget.destroy()
        for widget in adjust_frame.winfo_children():
            widget.destroy()
        how_to_start()
        exitbutton()
        restart()
    restart_button = tk.Button(root, text = "restart", command = restart_button_instructions)
    restart_button.place(relx = 0.4, rely = 0.9, anchor = "center")
    

#base_colour_start()
#no_idea_start()
how_to_start()
restart()
exitbutton()
root.mainloop()

#print(monochromatic("#4caf50"))
#print(analogous("#4caf50"))
#print(complementary("#4caf50"))