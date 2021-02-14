
# Get your slack token
source .env

docker run -it --rm \
	-e SLACK_WORKSTATION_TOKEN="$SLACK_WORKSTATION_TOKEN" \
	workstation_workout_bot:latest
