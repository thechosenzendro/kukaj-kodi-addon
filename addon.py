import xbmcaddon
import xbmcgui
addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
line1 = "Děcko letadlo test tomík"
xbmcgui.Dialog().ok("PlsWok", line1)
