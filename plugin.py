# import os
# import sublime_plugin
# import sublime
try:
    from LSP.plugin.core.main import register_language_handler
    from LSP.plugin.core.settings import ClientConfig
except ImportError:
    register_plugin = None


class TSSLSPPlugin(object):
    def __init__(self, name, config):
        self.name = name
        self.config = config
        pass

    def get_config():
        print("get config")
        return ClientConfig()

    def on_enable(self):
        print("enabling")

    def on_initialize(self, client):
        print("initializing")


default_name = "tss"

# default_name,
# client_config.get("command", []),
# client_config.get("tcp_port", None),
# client_config.get("scopes", []),
# client_config.get("syntaxes", []),
# client_config.get("languageId", ""),
# client_config.get("enabled", True),
# client_config.get("initializationOptions", dict()),
# client_config.get("settings", dict()),
# client_config.get("env", dict())


def plugin_loaded():
    if register_language_handler is None:
        print("LSP-tss: client hook not available, skipping...")
    else:
        default_config = ClientConfig(
            name=default_name,
            binary_args=[
                "node",
                "/Users/tomv/Projects/tomv564/lsp-tsserver/server/build/src/server.js",
                "--traceToConsole", "true", "--logVerbosity", "terse"
            ],
            tcp_port=None,
            scopes=["source.ts", "source.tsx", "source.js", "source.jsx"],
            syntaxes=[
                "Packages/TypeScript-TmLanguage/TypeScript.tmLanguage",
                "Packages/TypeScript-TmLanguage/TypeScriptReact.tmLanguage",
                "Packages/Babel/JavaScript (Babel).sublime-syntax",
                "Packages/JavaScript/JavaScript.sublime-syntax"
            ],
            languageId='typescript',
            enabled=False,
            init_options=dict(),
            settings=dict(),
            env=dict())

        register_language_handler(TSSLSPPlugin(default_name, default_config))
        print("LSP-tss: registered with LSP")
        # register_client_initialization_listener('rls'
        # , lambda client: register_client(client))


def plugin_unloaded():
    pass
