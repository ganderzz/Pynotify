# Pynotify

Simple notification/observable implementation for Python.


**Usage:**

```python
from pynotify import NOTIFY, EventHandler


@EventHandler(event="on_file_list_update")
class FileList:
  def handle_on_file_list_update(self, *args, **kwargs):
    data = kwargs.get("data")
    print(f"File list updated. The payload is: {data.payload}")



if __name__ == "__main__":
  file_list = FileList()
  NOTIFY.trigger(event="on_file_list_update", data={ "payload": "hi" })
```
