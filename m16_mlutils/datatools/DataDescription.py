import re


class DataDescription:

    def __init__(self, text):
        self.inner_dict = {}
        self.start_spaces = re.compile("^\s+")

        key = None
        for l in text.split("\n"):
            l_clean = l.strip()
            if l_clean:
                if self.start_spaces.search(l):
                    if "values" not in self.inner_dict[key]:
                        self.inner_dict[key]["values"] = {}
                    if key is not None:
                        values = l_clean.split("\t")
                        self.inner_dict[key]["values"][values[0]] = values[
                            1].strip()
                else:
                    parts = l_clean.split(":")
                    key = parts[0]
                    self.inner_dict[key] = {}
                    self.inner_dict[key]["description"] = parts[1].strip()

    def __getitem__(self, key):
        return self.inner_dict[key]

    def d(self, k, default=None):
        return self.get_description(k, default)

    def get_description(self, key, default=None):
        if not key in self.inner_dict:
            return default or key
        return self[key].get("description", key)

    def get_keys(self, key):
        if not key in self.inner_dict or "values" not in self.inner_dict[key]:
            return []
        return list(self.inner_dict[key]["values"].keys())

    def __str__(self):
        return '\n'.join(
            ["%15s: %s" % (k, self.inner_dict[k]["description"]) for k in
             self.inner_dict])
