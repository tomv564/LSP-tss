import shutil
import os
import sublime
import sublime_plugin
from LSP.plugin.core.handlers import LanguageHandler
from LSP.plugin.core.settings import ClientConfig, LanguageConfig

default_name = 'tss'
server_pkg_name = 'lsp-tsserver'
npm_command = 'npm'
server_command = 'lsp-tsserver'
if os.name == 'nt':
    npm_command = 'npm.cmd'
    server_command = 'lsp-tsserver.cmd'

default_config = ClientConfig(
    name=default_name,
    binary_args=[
        server_command, "--traceToConsole", "true", "--logVerbosity", "terse"
    ],
    tcp_port=None,
    enabled=False,
    init_options=dict(),
    settings=dict(),
    env=dict(),
    languages=[
        LanguageConfig("javascript", ["source.js", "source.jsx"], [
            "JavaScript (Babel).sublime-syntax",
            "Packages/JavaScript/JavaScript.sublime-syntax"
        ]),
        LanguageConfig("typescript", ["source.ts", "source.tsx"], [
            "Packages/TypeScript-TmLanguage/TypeScript.tmLanguage"
        ])
    ])


def node_is_installed() -> bool:
    return shutil.which("node") is not None


def server_is_installed() -> bool:
    return shutil.which(server_pkg_name) is not None


class LspTssSetupCommand(sublime_plugin.WindowCommand):
    def run(self):
        if not node_is_installed():
            sublime.message_dialog(
                "Please install Node.js before running setup".format(
                    server_pkg_name))
        elif not server_is_installed():
            if sublime.ok_cancel_dialog(
                    "{} was not in the PATH\nInstall globally now?".format(
                        server_pkg_name)):
                self.window.run_command(
                    "exec", {
                        "cmd": [
                            npm_command, "install", "--verbose", "-g",
                            server_pkg_name
                        ],
                    })
        else:
            sublime.message_dialog(
                "{} is already installed".format(server_pkg_name))


class LspTssPlugin(LanguageHandler):
    def __init__(self):
        self._name = default_name
        self._config = default_config

    @property
    def name(self) -> str:
        return self._name

    @property
    def config(self) -> ClientConfig:
        return self._config

    def on_start(self, window) -> bool:
        if not node_is_installed():
            window.status_message(
                "Node.js must be installed to run {}".format(server_pkg_name))
            return False
        if not server_is_installed():
            window.status_message(
                "{} was not in the PATH. Run Setup {} to install".format(
                    server_pkg_name, server_pkg_name))
            return False
        return True

    def on_initialized(self, client) -> None:
        pass  # extra initialization here.
