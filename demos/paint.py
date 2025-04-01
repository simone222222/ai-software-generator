'''
Certainly! Below is a simple paint application using Python with the `tkinter` library. This application allows the user to draw freehand on a canvas using the mouse.

You'll need to have Python installed on your system to run this code. If you don't have `tkinter` installed (though it typically comes with Python), you can install it using pip:

```bash
pip install tk
```

Here's the code for a simple paint application:
'''
import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint App")

        self.color = "black"
        self.pen_size = 5

        # Create a canvas
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack()

        # Binding mouse events to the canvas
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Create a color button
        self.color_button = tk.Button(self.root, text="Select Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)

        # Create a clear button
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - self.pen_size, y - self.pen_size, x + self.pen_size, y + self.pen_size, fill=self.color, outline=self.color)

    def reset(self, event):
        pass  # No action needed here

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]  # Get the color hex code

    def clear_canvas(self):
        self.canvas.delete("all")  # Clear the canvas

if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()

'''
### How to Run the Code:
1. Copy the code into a file named `paint_app.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the program using the command:

   ```bash
   python paint_app.py
   ```

### Features of the Paint Application:
- **Drawing**: You can draw on the canvas by clicking and dragging the mouse.
- **Color Picker**: Clicking the "Select Color" button will open a color chooser dialog to select a color.
- **Clear Canvas**: Clicking the "Clear" button will remove everything drawn on the canvas.

Feel free to modify the code to add more features, such as changing pen size, saving the canvas, or adding shapes!
'''