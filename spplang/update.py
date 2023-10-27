import os
import winreg as reg

def associate_custom_extension(custom_extension, icon_path, friendly_name):
    # Register the custom file extension and set the friendly name
    with reg.OpenKey(reg.HKEY_CLASSES_ROOT, "", 0, reg.KEY_WRITE) as root_key:
        with reg.CreateKey(root_key, custom_extension) as sub_key:
            reg.SetValue(sub_key, "", reg.REG_SZ, friendly_name)

    # Associate your custom icon with the file extension
    with reg.OpenKey(reg.HKEY_CLASSES_ROOT, custom_extension, 0, reg.KEY_WRITE) as key:
        with reg.CreateKey(key, "DefaultIcon") as icon_key:
            reg.SetValue(icon_key, "", reg.REG_SZ, icon_path)

    # Notify the shell to refresh icons (requires administrative privileges)
    os.system("taskkill /f /im explorer.exe")
    os.system("start explorer.exe")

if __name__ == "__main__":
    # Predefined custom extension
    custom_extension = ".spp"

    # Predefined icon path
    icon_path = r"C:\spplang\eagle.png"

    # Predefined friendly name
    friendly_name = "SPP File"

    associate_custom_extension(custom_extension, icon_path, friendly_name)
