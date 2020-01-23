cat ~/bin/test_patch.py
#!/usr/bin/env python
 
import os
import os.path
import sys
 
 
# from: https://github.com/python/cpython/blob/master/Lib/unittest/mock.py#L1081-L1097
def _dot_lookup(thing, comp, import_path):
    try:
        return getattr(thing, comp)
    except AttributeError:
        __import__(import_path)
        return getattr(thing, comp)
 
 
def _importer(target):
    components = target.split('.')
    import_path = components.pop(0)
    thing = __import__(import_path)
 
    for comp in components:
        import_path += ".%s" % comp
        thing = _dot_lookup(thing, comp, import_path)
    return thing
 
 
if '__main__' in __name__:
    os.chdir(os.getcwd())
 
    if len(sys.argv) < 2:
        print(f'usage: {sys.argv[0]} "some.module.path"')
    else:
        obj = _importer(sys.argv[1])
        print(f'Patch importer returns:\n {obj}')
        print()
        print(f'Imported object has:\n {dir(obj)}')
