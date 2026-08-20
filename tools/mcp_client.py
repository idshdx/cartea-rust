import json
import subprocess
import os

class MCPClient:
    def __init__(self, command, args, env):
        self.process = subprocess.Popen(
            [command] + args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            env=env,
            bufsize=0,
            shell=(os.name == 'nt')
        )

    def _send(self, method, params=None):
        message = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        self.process.stdin.write(json.dumps(message) + "\n")
        self.process.stdin.flush()
        line = self.process.stdout.readline()
        return json.loads(line)

    def initialize(self):
        return self._send("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "translate-py-client", "version": "1.0"}
        })

    def initialized(self):
        return self._send("notifications/initialized", {})

    def list_tools(self):
        return self._send("tools/list", {})

    def call_tool(self, name, arguments):
        return self._send("tools/call", {"name": name, "arguments": arguments})

    def close(self):
        self.process.terminate()
        self.process.wait()
