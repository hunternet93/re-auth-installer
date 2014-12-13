#!/usr/bin/env python3
# Red Eclipse Auth Installer
# https://github.com/hunternet93/re-auth-installer

# ==============================
# Define colors to use in the UI
# ==============================

bgcolor = "#000000"
textcolor = "#B11000"
font = ('Trebuchet MS', 16, 'bold')

# ======================================
# Imports, with Python-version detection
# ======================================

import platform
import os

if platform.python_version_tuple()[0] == '2':
    from Tkinter import *
    import tkMessageBox as tkmessagebox
else:
    from tkinter import *
    import tkinter.messagebox as tkmessagebox


# ==================================
# Locate the config file based on OS
# ==================================

if platform.system() == 'Linux':
    path = os.path.expanduser('~/.redeclipse/config.cfg')
    
if platform.system() == 'Windows':
    # TODO: Check this code!
    path = os.path.join(
        os.path.expanduser('~'),
        'My Documents',
        'My Games',
        'Red Eclipse',
        'config.cfg'
    )
        
if platform.system() == 'Darwin':
    # Darwin is Mac OS X's kernel's name
    path = os.path.expanduser('~/Library/Application Support/redeclipse/config.cfg')
    

# ==================================
# Attempt to open the config file
# Display error if there's a problem
# ==================================

try:
    # Open file for reading and appending.
    targetfile = open(path, 'a+')
except FileNotFoundError or PermissionError or IOError:
    tkmessagebox.showerror(
        'Red Eclipse Auth Installer',
        "Couldn't open Red Eclipse's config file. Please ensure Red Eclipse is installed correctly."
    )
    quit()
    

# =========================================
# Installs the auth key
# Run when the Install Key button is pushed
# =========================================

def install():
    targetfile.seek(0)
    # Check if the config file already has an auth key.
    if 'accountpass' in targetfile.read():
        q = tkmessagebox.askyesno(
            'Auth Already Installed',
            'An auth key seems to already be installed. Replace the current auth key?'
        )
    
        if not q:
            # User pressed no, so do nothing.
            return
    
    # Get username/auth key from text boxes.
    username = usernamebox.get().strip()
    key = keybox.get().strip()
    
    # Verify that username/auth keys have been entered, show a warning if not.
    if len(username) < 1:
        tkmessagebox.showwarning('Enter Username', 'Please enter a username.')
        return
    if len(key) < 1:
        tkmessagebox.showwarning('Enter Auth Key', 'Please enter an auth key.')
        return

    # Add the username/auth key to the config file.
    targetfile.write(
        'accountname "' + username + '"\n' +
        'accountpass "' + key + '"\n'
    )
    
    # Show a success dialog, then quit.
    tkmessagebox.showinfo('Auth Key Installed', 'The auth key has been installed.')
    quit()


# ==========================
# Initialize the UI elements    
# ==========================
root = Tk()
root.title('Red Eclipse Auth Installer')
root.config(bg = bgcolor)
root.minsize(400,200)

frame = Frame(root, bg = bgcolor)
frame.pack(fill = BOTH, expand = 1, padx = 20, pady = 20)

Label(frame, text = 'Username:', bg = bgcolor, fg = textcolor, font = font).pack()
usernamebox = Entry(frame, fg = textcolor, font = font)
usernamebox.pack(fill = X)

Label(frame, text = 'Auth Key:', bg = bgcolor, fg = textcolor, font = font).pack()
keybox = Entry(frame, fg = textcolor, font = font)
keybox.pack(fill = X)

Button(frame, text = 'Install Key', command = install, fg = textcolor, font = font).pack(anchor = S, expand = 1)

# =========================
# Run the Tkinter main loop
# =========================
root.mainloop()
