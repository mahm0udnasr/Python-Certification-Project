test_settings = {
    'Theme': 'dark',
    'Volume': 'high'
}
def add_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, update_setting):
    key, value = update_setting
    key = key.lower()
    value = value.lower()
    if key in settings.keys():
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings.keys():
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return f"Setting not found!"

def view_settings(settings):
    if(len(settings) < 1):
        return "No settings available."
    print("Current User Settings:")
    for key, value in settings.items():
        print(f"{key.title()}: {value}")