#!/bin/bash

# Check if the required arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 SEARCH_STRING REPLACE_STRING"
    exit 1
fi

SEARCH="$1"
REPLACE="$2"
FILE="observability/grafana/dashboard.json"

# Check the operating system
if [[ "$(uname)" == "Darwin" ]]; then
    # macOS
    sed -i '' "s/$SEARCH/$REPLACE/g" "$FILE"
elif [[ "$(uname)" == "Linux" ]]; then
    # Linux
    sed -i "s/$SEARCH/$REPLACE/g" "$FILE"
else
    echo "Unsupported operating system."
    exit 1
fi
