# Muffinwoman: Discord Music Bot

This is a just a quick exercise for checking out discord.py and youtube-dl.  My friend had a music bot 2 years back that could play almost any link thrown at it. This is meant to emulate that. Enjoy.

### Design Choices

1. Minimize dependencies: A lot of music bots these days are using Lavalink to send audio. That brings in Java 11 as a dependency.  The dependencies here are youtube-dl, discord.py, and pynacl (along with their dependencies)

2. No volume controls: It's trendy for reactions to be used to control volume. While this is a neat feature, users in the server can adjust the volume of the bot themselves.  I don't want to write functionality that's already there.

3. Host it yourself: Self explanatory really. Keeps the code simple so I can work on features and bug fixes when updates come.

### Issues and Feature Requests

Fill out an issue

### TODO

* Fix disconnect when dragging bot
* Investigate slow play command
* Investigate ffmpeg crashing once in a while
* Flesh out logic on checking the user's channel before joining

