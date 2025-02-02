#!/bin/sh
# wait-for-mongo.sh

set -e

host="$1"
shift
cmd="$@"

until mongosh --host $host --eval "db.adminCommand({ ping: 1 })"; do
>&2 echo "MongoDB not ready - waiting..."
sleep 2
done

>&2 echo "MongoDB it's ready- running command"
exec $cmd