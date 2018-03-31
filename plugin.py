from LSP.plugin.core.handlers import LanguageHandler
from LSP.plugin.core.settings import ClientConfig

default_name = 'tss'

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


class TSSLSPPlugin(LanguageHandler):
    def __init__(self):
        self._name = default_name
        self._config = default_config
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def config(self) -> ClientConfig:
        return self._config

    def on_enable(self) -> None:
        print("enabling")

    def on_initialize(self, client) -> None:
        print("initializing")
