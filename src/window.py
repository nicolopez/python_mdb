#!/usr/bin/env python

from gi.repository import Gtk

def main():
    window = Gtk.Window()
    window.set_title('A Python Movie Database')
    window.set_default_size(1024, 768)
    window.set_position(Gtk.WindowPosition.CENTER)
    window.connect('destroy', destroy)
    window.show_all()
    Gtk.main()

def destroy(window):
    Gtk.main_quit()


if __name__ == '__main__':
    main()
