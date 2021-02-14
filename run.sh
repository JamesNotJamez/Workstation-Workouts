
# Get your slack token
source .env

docker run -it --rm \
	-e SLACK_WORKSTATION_TOKEN="$SLACK_WORKSTATION_TOKEN" \
	-e SLACK_CHANNEL="#workout" \
	workstation_workout_bot:latest
