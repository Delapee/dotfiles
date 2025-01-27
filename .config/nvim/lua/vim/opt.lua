-- Configure options
vim.opt.clipboard = "unnamedplus" -- Use the system clipboard
vim.opt.expandtab = true -- Use spaces instead of tabs
vim.opt.tabstop = 2 -- Number of spaces for a tab
vim.opt.softtabstop = 2 -- Spaces to remove when deleting a tab
vim.opt.shiftwidth = 2 -- Indentation level

-- Global variables
vim.g.mapleader = " " -- Maps the leader key to Space
vim.g.maplocalleader = "\\" -- Maps the local leader key to Backslash

-- Window-local options
vim.wo.number = true -- Enable line numbers
vim.wo.relativenumber = true -- Enable relative line numbers

-- Navigate vim panes with tmux
vim.keymap.set("n", "<c-k>", ":wincmd k<CR>")
vim.keymap.set("n", "<c-j>", ":wincmd j<CR>")
vim.keymap.set("n", "<c-h>", ":wincmd h<CR>")
vim.keymap.set("n", "<c-l>", ":wincmd l<CR>")
