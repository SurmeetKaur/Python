import os

class DirectorySearch:
    def find(self, path, dir):
            try:
                os.chdir(path)
            except OSError:
            # Doesn't process a file that isn't a directory.
                return

            current_dir = os.getcwd()
            print(current_dir)
            for entry in os.listdir():
                  if entry == dir:
                      print(os.getcwd() + "/" + dir)
                  self.find(current_dir + "/" + entry, dir)


directory_searcher = DirectorySearch()
directory_searcher.find("./my_first_directory", "my_third_directory")
