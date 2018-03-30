
Hear about and install LSP from Package Control
Search for "typescript" or "tss" and install LSP-contrib-tss


First plugin load:
contrib-tss calls register_plugin(config, initialize_handler, enable_handler)


LSP handles:
if initialize_handler:
  add_initialize_handler(config, initialize_handler)


Open a typescript file

First time:
LSP checks default configs (deprecated)
LSP checks a lookup: syntax -> LSPPlugin(config: ClientConfg, enable_handler: Callable, initialize_handler: Callable)
LSP presents list of available configs and if user chooses:

if enable_handler:
	enable_handler(window, config)
else:
	lsp_enable(window, config)

contrib-tss checks if server installed and installs if desired.
calls lsp_enable(window, config) when ready.


In the future:

LSP has a global config or project config enabled already - starts up
only initialize_handler if present is called.