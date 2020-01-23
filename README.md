# unittest.Mock object explorer

Sample usage
`~/bin/test_patch.py nise.report.upload_to_azure_container`
Returns
```
Patch importer returns:
 <function upload_to_azure_container at 0x7fe2326410e0>
Imported object has:
 ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

If the module does not exist, this error will show:
```
~/bin/test_patch.py nise.report.upload_to_something_else
Traceback (most recent call last):
  File "/home/blentz/bin/test_patch.py", line 34, in <module>
    obj = _importer(sys.argv[1])
  File "/home/blentz/bin/test_patch.py", line 24, in _importer
    thing = _dot_lookup(thing, comp, import_path)
  File "/home/blentz/bin/test_patch.py", line 13, in _dot_lookup
    __import__(import_path)
ModuleNotFoundError: No module named 'nise.report.upload_to_something_else'; 'nise.report' is not a package
```
