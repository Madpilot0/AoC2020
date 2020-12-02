def read_from_file(filename):
  return list(map(lambda x: x.rstrip('\n'), open(filename, 'r').readlines()))