#!/bin/bash

# Function for auto-completion of file names
autocomplete() {
    local cur="${COMP_WORDS[COMP_CWORD]}"
    local files=$(ls *.mp4 *.mkv *.avi 2>/dev/null)
    COMPREPLY=($(compgen -W "${files}" -- ${cur}))
}

# Register auto-completion function
complete -F autocomplete converter

# Check if file name is provided as an argument
if [ $# -eq 0 ]; then
    echo "Please provide the file name."
    exit 1
fi

# Extract audio from video file using ffmpeg
input_file="$1"
output_file="${input_file%.*}_audio.mp3"
ff


