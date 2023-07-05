import random
import tkinter as tk

def roll_dice():
    # Generate a random number between 1 and 6
    roll_result = random.randint(1, 6)
    return roll_result

def animate_dice():
    # Clear the result label
    result_label.config(text="")

    # Generate random numbers for the dice faces
    dice_faces = [random.randint(1, 6) for _ in range(10)]

    # Animate the dice rolling
    for dice_face in dice_faces:
        # Update the label with the current dice face
        dice_label.config(text=str(dice_face))
        window.update()
        window.after(100)

    # Roll the dice for the final result
    result = roll_dice()

    # Update the label with the final result
    result_label.config(text="The dice rolled: " + str(result))

    # Update the dice face label with the final result
    dice_label.config(text=str(result))



# Create the main window
window = tk.Tk()
window.title("Dice Roller")

# Create a label for the dice animation
dice_label = tk.Label(window, text="", font=("Arial", 72))
dice_label.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(window, text="Click the 'Roll' button to roll the dice!", font=("Arial", 16))
result_label.pack(pady=20)

# Create a button to roll the dice
roll_button = tk.Button(window, text="Roll", font=("Arial", 16), command=animate_dice)
roll_button.pack()

# Start the main loop
window.mainloop()
