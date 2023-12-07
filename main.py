import tkinter as tk
from tkinter import ttk, colorchooser, messagebox, simpledialog
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

import opengl_part

class DrawingApp:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        pygame.display.set_mode((self.screen_width, self.screen_height), DOUBLEBUF | OPENGL)

        glViewport(0, 0, self.screen_width, self.screen_height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.screen_width, self.screen_height, 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)

        self.background_color = (0.2, 0.2, 0.2, 1.0)  # Initial background color
        self.object_color = (0.8, 0.8, 0.8, 1.0)  # Initial object color
        self.line_width = 1.0  # Initial line width
        self.line_style = GL_LINES  # Initial line style
        self.scale_factor = 1.0  # Initial scale factor


        # Create a button instance
        self.button1 = Button(300, 250, 200, 100, "Click Me")

        self.drawing_function = self.draw_line  # Initial drawing function

        self.set_background_color(self.background_color)  # Set initial background color

    def get_width(self):
        return float(self.line_width)

    def draw_line(self):
        glColor4fv(self.object_color)
        glLineWidth(self.line_width)
        glBegin(self.line_style)
        glVertex2f(100 * self.scale_factor, 100 * self.scale_factor)  # Starting point of the line
        glVertex2f(200 * self.scale_factor, 200 * self.scale_factor)  # Ending point of the line
        glEnd()

    def draw_rectangle(self):
        glColor4fv(self.object_color)
        glLineWidth(self.line_width)
        glBegin(GL_QUADS)
        glVertex2f(300 * self.scale_factor, 300 * self.scale_factor)  # Top-left vertex
        glVertex2f(500 * self.scale_factor, 300 * self.scale_factor)  # Top-right vertex
        glVertex2f(500 * self.scale_factor, 500 * self.scale_factor)  # Bottom-right vertex
        glVertex2f(300 * self.scale_factor, 500 * self.scale_factor)  # Bottom-left vertex
        glEnd()

    def draw_polygon(self):
        glColor4fv(self.object_color)
        glLineWidth(self.line_width)
        glBegin(GL_POLYGON)
        glVertex2f(600 * self.scale_factor, 400 * self.scale_factor)  # Vertex 1
        glVertex2f(700 * self.scale_factor, 300 * self.scale_factor)  # Vertex 2
        glVertex2f(750 * self.scale_factor, 350 * self.scale_factor)  # Vertex 3
        glVertex2f(700 * self.scale_factor, 400 * self.scale_factor)  # Vertex 4
        glVertex2f(650 * self.scale_factor, 450 * self.scale_factor)  # Vertex 5
        glVertex2f(300 * self.scale_factor, 350 * self.scale_factor)  # Vertex 6
        glVertex2f(250 * self.scale_factor, 150 * self.scale_factor)  # Vertex 7

        glEnd()

    def draw_triangle(self):
        glColor4fv(self.object_color)
        glLineWidth(self.line_width)
        glBegin(GL_TRIANGLES)
        glVertex2f(400 * self.scale_factor, 200 * self.scale_factor)  # Vertex 1
        glVertex2f(500 * self.scale_factor, 100 * self.scale_factor)  # Vertex 2
        glVertex2f(600 * self.scale_factor, 200 * self.scale_factor)  # Vertex 3
        glEnd()

    def set_background_color(self, color):
        self.background_color = color

    def set_object_color(self, color):
        self.object_color = color

    def set_line_width(self, width):
        self.line_width = width

    def set_line_style(self, style):
        self.line_style = style

    def set_scale_factor(self, factor):
        self.scale_factor = factor

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_1:
                        self.drawing_function = self.draw_line
                    elif event.key == K_2:
                        self.drawing_function = self.draw_rectangle
                    elif event.key == K_3:
                        self.drawing_function = self.draw_polygon
                    elif event.key == K_4:
                        self.drawing_function = self.draw_triangle
                    elif event.key == K_b:
                        self.set_background_color(self.choose_background_color())  # Set background color to white
                    elif event.key == K_f:
                        self.set_object_color(self.choose_fill_color())  # Set object color to green
                    elif event.key == K_w:
                        self.set_line_width(self.set_line_width())  # Set line width to 1.0g
                    elif event.key == K_6:
                        self.set_line_width(3.0)  # Set line width to 3.0
                    elif event.key == K_7:
                        self.set_line_style(GL_LINES)  # Set line style to GL_LINES
                    elif event.key == K_8:
                        self.set_line_style(GL_LINE_LOOP)  # Set line style to GL_LINE_LOOP
                    elif event.key == K_EQUALS and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        self.set_scale_factor(self.scale_factor * 1.1)  # Increase scale factor by 10%
                    elif event.key == K_MINUS:
                        self.set_scale_factor(self.scale_factor * 0.9)  # Decrease scale factor by 10%

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            glClearColor(*self.background_color)
            self.drawing_function()

            pygame.display.flip()
            pygame.time.wait(10)

        pygame.quit()
def run_app():
    app = DrawingApp()
    app.run()
class ImageEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.current_color = 'black'
        self.line_width = 1
        self.line_style = 'Solid'
        self.fill_color = 'black'
        self.fill_style = None
        self.fill_confirm = False

        self.create_menu()

    def choose_line_width(self):
        root = tk.Tk()
        root.withdraw()

        number = simpledialog.askfloat("Enter Float Number", "Please enter a float number:")

        return number
    def create_menu(self):
        menubar = tk.Menu(self.root)

        # Menu for choosing background color
        background_menu = tk.Menu(menubar, tearoff=0)
        background_menu.add_command(label="Choose background color", command=self.choose_background_color)
        menubar.add_cascade(label="Background color", menu=background_menu)

        # Menu for choosing object color
        object_menu = tk.Menu(menubar, tearoff=0)
        object_menu.add_command(label="Choose object color", command=self.choose_object_color)
        menubar.add_cascade(label="Object color", menu=object_menu)

        # Menu for choosing line style and width
        line_menu = tk.Menu(menubar, tearoff=0)
        line_menu.add_command(label="Line style", command=self.choose_line_style)
        menubar.add_cascade(label="Line style", menu=line_menu)

        # Menu for drawing shapes
        shape_menu = tk.Menu(menubar, tearoff=0)
        shape_menu.add_command(label="Draw straight lines", command=self.draw_straight_line)
        shape_menu.add_command(label="Draw rectangles", command=self.draw_rectangles)
        shape_menu.add_command(label="Draw triangles", command=self.draw_triangles)
        shape_menu.add_command(label="Draw polygons", command=self.draw_polygons)
        menubar.add_cascade(label="Shapes", menu=shape_menu)

        # Menu for scaling the image
        scale_menu = tk.Menu(menubar, tearoff=0)
        scale_menu.add_command(label="Scale canvas", command=self.scale_canvas)
        menubar.add_cascade(label="Scale", menu=scale_menu)

        # Menu for using OpenGL
        object_menu = tk.Menu(menubar, tearoff=0)
        object_menu.add_command(label="run app", command=run_app)
        object_menu.add_command(label="draw disk", command=opengl_part.run_disk)
        menubar.add_cascade(label="use OpenGL", menu=object_menu)

        self.root.config(menu=menubar)

    def choose_background_color(self):
        color = colorchooser.askcolor(title="Choose background color")
        background_color = [0.0, 0.0, 0.0, 1.0]
        for i in range(3):
            background_color[i] = color[0][i] / 255
        return tuple(background_color)

    def choose_fill_color(self):
        color = colorchooser.askcolor(title="Choose background color")
        fill_color = [0.0, 0.0, 0.0, 1.0]
        for i in range(3):
            fill_color[i] = color[0][i] / 255
        return tuple(fill_color)


    def choose_object_color(self):
        dialog = tk.Toplevel()
        dialog.title("Choose type of fill")

        # choose stipple option
        options = [
            "gray12",
            "gray25",
            "gray50",
            "gray75",
            "hourglass",
            "spiral",
            "shingle",
            "bricks",
            "checkerboard",
            "cross",
            "diamond",
            "dots",
            "target"
        ]

        combobox = ttk.Combobox(dialog, values=options)
        combobox.pack()

        submit_button = ttk.Button(dialog, text="Update Fill Style",
                                   command=lambda: self.update_fill_style(combobox.get()),
                                   width=23)
        submit_button.pack()

        # Choose fill color
        choose_fill_color_button = ttk.Button(dialog,
                                              text="Choose fill color",
                                              command=self.choose_fill_color,
                                              width=23)
        choose_fill_color_button.pack()

        # OK button
        ok_button = ttk.Button(dialog, text="OK", command=lambda: self.fill_confirmation(dialog))
        ok_button.pack(side="left")

        # Cancel button
        cancel_button = ttk.Button(dialog, text="Cancel", command=dialog.destroy)
        cancel_button.pack(side="right")

    def fill_confirmation(self, dialog):
        self.fill_confirm = True
        dialog.destroy()

    def update_fill_style(self, fill_style):
        self.fill_style = fill_style
        print(fill_style)

    def set_line_width(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Choose line style and width")

        thickness_label = ttk.Label(dialog, text="Line width:")
        thickness_label.grid(row=1, column=0)

        thickness_combo = ttk.Entry(dialog)
        thickness_combo.grid(row=1, column=1)

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=2, column=0, columnspan=2)

        ok_button = ttk.Button(button_frame, text="OK",
                               command=lambda: self.get_line_width(dialog, thickness_combo.get()))
        ok_button.grid(row=0, column=0)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
        cancel_button.grid(row=0, column=1)

    def get_line_width(self, dialog, line_width):
        dialog.destroy()
        return float(line_width)
    def choose_line_style(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Choose line style and width")

        style_label = tk.Label(dialog, text="Line style:")
        style_label.grid(row=0, column=0)

        style_combo = ttk.Combobox(dialog, values=["Solid", "Dashed", "Dotted"])
        style_combo.grid(row=0, column=1)

        thickness_label = ttk.Label(dialog, text="Line width:")
        thickness_label.grid(row=1, column=0)

        thickness_combo = ttk.Entry(dialog)
        thickness_combo.grid(row=1, column=1)

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=2, column=0, columnspan=2)

        ok_button = ttk.Button(button_frame, text="OK",
                               command=lambda: self.accept_line_style(dialog, style_combo.get(), thickness_combo.get()))
        ok_button.grid(row=0, column=0)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
        cancel_button.grid(row=0, column=1)

    def accept_line_style(self, dialog, style, thickness):
        # Handle the line style and thickness
        # You can add your logic for handling the line style and thickness here
        print("Line Style:", style)
        print("Line Thickness:", thickness)
        self.line_style = style
        self.line_width = thickness
        dialog.destroy()

    def get_coordinates(self, create_func, num_triangles):
        dialog = tk.Toplevel(self.root)
        dialog.title("Enter coordinates and draw straight lines")

        inputs = []
        labels = ["X", "Y"]

        for i in range(num_triangles):
            for j in range(2):
                label = ttk.Label(dialog, text=f"{labels[j]}{i + 1}:")
                label.grid(row=2 * i + j, column=0)

                entry = ttk.Entry(dialog)
                entry.grid(row=2 * i + j, column=1)

                inputs.append(entry)

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=2 * num_triangles, column=0, columnspan=2)

        ok_button = ttk.Button(button_frame, text="OK",
                               command=lambda: self.accept_figure(dialog, [entry.get() for entry in inputs],
                                                                  create_func))
        ok_button.grid(row=0, column=0)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
        cancel_button.grid(row=0, column=1)

    def draw_straight_line(self):
        self.get_coordinates(self.canvas.create_line, 2)

    def draw_rectangles(self):
        self.get_coordinates(self.canvas.create_rectangle, 2)

    def draw_triangles(self):
        self.get_coordinates(self.canvas.create_polygon, 3)

    def accept_figure(self, dialog, xy, create_func):
        if self.fill_confirm:
            print(self.fill_color[1])
            create_func(xy, width=self.line_width, fill=self.fill_color[1], stipple=self.fill_style)
            self.fill_confirm = False
        else:
            if self.line_style == 'Dotted':
                create_func(xy, dash=(2, 2), width=self.line_width)
            elif self.line_style == 'Dashed':
                create_func(xy, dash=(2, 4), width=self.line_width)
            else:
                create_func(xy, width=self.line_width)
        dialog.destroy()

    def draw_polygons(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Enter number of coordinates")

        label = ttk.Label(dialog, text="How many angles?")
        label.grid(row=0, column=0)

        entry = ttk.Entry(dialog)
        entry.grid(row=0, column=1)

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=1, columnspan=2)

        ok_button = ttk.Button(button_frame, text="OK",
                               command=lambda: self.get_polygon_coordinates(dialog, int(entry.get())))
        ok_button.grid(row=0, column=0)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
        cancel_button.grid(row=0, column=1)

    def get_polygon_coordinates(self, dialog, num_of_coordinates):
        dialog.destroy()
        self.get_coordinates(self.canvas.create_polygon, num_of_coordinates)

    def scale_canvas(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Enter scale factor")

        label = ttk.Label(dialog, text="scale factor")
        label.grid(row=0, column=0)

        entry = ttk.Entry(dialog)
        entry.grid(row=0, column=1)

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=1, columnspan=2)

        ok_button = ttk.Button(button_frame, text="OK",
                               command=lambda: self.canvas.scale("all", 0, 0, float(entry.get()), float(entry.get())))
        ok_button.grid(row=0, column=0)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=dialog.destroy)
        cancel_button.grid(row=0, column=1)

    def run(self):
        self.root.mainloop()


# Create an instance of the image editor and run it
# editor = ImageEditor()
# editor.run()

