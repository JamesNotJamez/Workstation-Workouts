# Workstation Workout Slack Bot

A bot that will send you regular, short workouts during the working day to keep you active and get you out of your chair.

> Here's a hard one, 18 Sit Ups

> Here's a easy one, 16 Squats

The Oauth token for your bot is a required environment variable. Here is a video tutorial for getting your bot account set up - [Setting up a slack bot](https://www.youtube.com/watch?v=KJ5bFv-IRFM&t)
```
-e SLACK_WORKSTATION_TOKEN=<your token>
```

You can also mount a custom exercise file or rep/time file, just make sure to follow the same format.
```
-v /your/file/path:/app/exercises.yml
-v /your/file/path:/app/reps.yml
```

I've provided a run script so that I don't have to worry about passing my slack token environment manually every time. It can be added to the `.env` file which is sourced by the run script. This `.env` file is in the gitignore spec so your token won't be persisted to git if you do make any commits.

Avaiable from DockerHub [here](https://hub.docker.com/repository/docker/jamesnotjamez/workstation_workout_bot)
```
docker pull docker.io/jamesnotjamez/workstation_workout_bot
```
