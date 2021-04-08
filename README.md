# discord-bot
v1.0.0 - [view change log](.github/CHANGELOG.md)

A discord bot with a lot of cmds and functions

## Installation
Fork this repository.

This project is optimized for hosting on [Heroku](https://www.heroku.com/). So head over to their site and create an account. It's completely free.

After that please create a new application on [Heroku](https://www.heroku.com/) and deploy this project to your [Heroku](https://www.heroku.com/) app. To do so, head over to the deploy category and select the GitHub deploy method. Then select the repository you just forked and deploy the main branch. 

In the settings of the app you need to add a few env vars. Add the following env vars.
```
BOT_TOKEN = your bot token
MY_DISCORD_ID = your discord id
MY_DISCORD_TAG = your discord tag
```

To be able to host the discord bot you still need a few [Heroku](https://www.heroku.com/) buildpacks. So head over to your [Heroku](https://www.heroku.com/) app settings and add the following buildpacks.

- [ffmpeg buildpack](https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest): This is necessary to use the music commands
- [opus](https://github.com/xrisk/heroku-opus): This is also necessary for the music commands
- python: Just select this by clicking the add buildpack button

Make sure that the python buildpack is at the bottom of the buildpacks.

Now the discord bot is ready to host. Yaaaaay!! Head over to the resources tab and switch the worker from off to on.

## Contributing
[Contributing.md](.github/CONTRIBUTING.md)

Contact PolarBear4u#7025 (Discord) for more information.

## Contributors
- PolarBear4u
- Frozen0wl

## Acknowledgments
[Acknowledgments.md](.github/ACKNOWLEDGMENTS.md)

## Licence
[GNU v3.0](LICENSE)

