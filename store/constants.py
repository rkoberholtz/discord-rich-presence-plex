import sys
import os

name = "Discord Rich Presence for Plex"
version = "2.0.1"
plexClientID = "discord-rich-presence-plex"
isUnix = sys.platform in ["linux", "darwin"]
processID = os.getpid()
