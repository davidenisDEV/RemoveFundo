import os
from removebg import RemoveBg
from tkinter import Tk, filedialog

def remove_background_from_folder(input_folder):
    
    rmbg = RemoveBg("R4CJbaMKgkYcEWvsFwHw2xPY", "error.log")
    
    
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)
            
            
            rmbg.remove_background_from_img_file(input_path)
            
            
            processed_image_path = input_path[:-4] + "_no_bg.png"
            
            
            if os.path.exists(processed_image_path):
               
                os.rename(processed_image_path, input_path)

def select_folder():
    root = Tk()
    root.withdraw()  
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        remove_background_from_folder(folder_selected)
    else:
        print("Nenhuma pasta selecionada.")

if __name__ == "__main__":
    select_folder()
