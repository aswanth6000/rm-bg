import sys, os
from rembg import remove
# from win10toast import ToastNotifier

# toaster = ToastNotifier()

def process_image(input_path):
    output_path = os.path.splitext(input_path)[0] + '_no_bg.png'
    # toaster.show_toast("RemoveBG", "Removing background...", duration=3)
    with open(input_path, 'rb') as inp:
        with open(output_path, 'wb') as out:
            out.write(remove(inp.read()))
    # toaster.show_toast("RemoveBG", f"Saved: {os.path.basename(output_path)}", duration=3)
    return output_path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: remove_bg.exe <image_file>")
    else:
        process_image(sys.argv[1])
