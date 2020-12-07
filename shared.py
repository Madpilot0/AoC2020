def read_from_file(filename):
  return list(map(lambda x: x.rstrip('\n'), open(filename, 'r').readlines()))

def read_from_file_grouped(filename):
  return open(filename, 'r').read().split('\n\n')