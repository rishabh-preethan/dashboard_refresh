# Use an official Alpine Linux as a parent image
FROM alpine:latest

# Install curl
RUN apk add --no-cache curl

# Set environment variable for the cookie
ENV COOKIE=""

# The command to run the curl request
CMD ["sh", "-c", "curl -X POST https://trustonic.thirdray.app/api/queries/307/results \
-H 'Accept: application/json' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Accept-Language: en-GB,en;q=0.5' \
-H 'Cache-Control: max-age=0' \
-H 'Connection: keep-alive' \
-H 'Cookie: $COOKIE' \
-H 'Host: trustonic.thirdray.app' \
-H 'Referer: https://trustonic.thirdray.app/login' \
-H 'Sec-Fetch-Dest: document' \
-H 'Sec-Fetch-Mode: navigate' \
-H 'Sec-Fetch-Site: same-origin' \
-H 'Sec-Fetch-User: ?1' \
-H 'Sec-GPC: 1' \
-H 'Upgrade-Insecure-Requests: 1' \
-H 'sec-ch-ua-platform: \"macOS\"', \"91\", \"Chromium\";v=\"91\", \";Not A Brand\";v=\"99\"' \
-o output.json"]

