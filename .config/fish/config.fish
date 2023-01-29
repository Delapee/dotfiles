set fish_greeting

source $HOME/.config/fish/alias

set PATH $HOME/.cargo/bin $PATH

set PATH $HOME/.local/share/neovim/bin $PATH

set PATH $HOME/.node/bin $PATH

eval /home/delape/miniconda3/bin/conda "shell.fish" "hook" $argv | source

starship init fish | source
