class Omnibus:
    _cnt = {}
    _map = {}

    def __setattr__(self, name, value):
        if str(name).startswith("_"):
            super().__setattr__(name, value)
            return
        self._map.setdefault(self, set())
        if name not in self._map[self]:
            self._map[self].add(name)
            self._cnt[name] = self._cnt.get(name, 0) + 1

    def __getattr__(self, name):
        return self._cnt.get(name, 0)

    def __delattr__(self, name):
        if name in self._map.get(self, set()):
            self._map[self].remove(name)
            self._cnt[name] -= 1
            if not self._cnt[name]:
                del self._cnt[name]
                
import sys
exec(sys.stdin.read())
