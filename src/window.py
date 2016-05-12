#!/usr/bin/env python

from gi.repository import Gtk

class Pymdb:
    def __init__(self):
        window = Gtk.Window()
        window.set_title('A Python Movie Database')
        window.set_default_size(1024, 768)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect('destroy', self.destroy)
        window.show_all()

    def destroy(self, window):
        Gtk.main_quit()

def main():
    app = Pymdb()
    Gtk.main()

if __name__ == '__main__':
    main()
