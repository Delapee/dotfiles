return {
	{ "mg979/vim-visual-multi" },
	{
		"kylechui/nvim-surround",
		event = "VeryLazy",
		version = "*",
		config = function()
			require("nvim-surround").setup({})
		end,
	},
	{ "numToStr/Comment.nvim" },
}
