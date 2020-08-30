import os
import subprocess
from github import Github
from getpass import getpass

name = ""

def crepo():
  password = getpass('Password: ')
  user = Github("Force4760", password).get_user()
  repo = user.create_repo(name)
  subprocess.call('git init', shell=True)
  subprocess.call('copy NUL README.md', shell=True)
  subprocess.call('git add README.md', shell=True)
  subprocess.call('git remote add origin git@github.com:Force4760/{}.git' .format(name), shell=True)
  subprocess.call("git commit -m 'firstcommit'" , shell=True)
  subprocess.call("git push -u origin master" , shell=True)
  subprocess.call("code ." , shell=True)

  

if __name__ == "__main__":

  name = input('Name: ')

  while True:

    category = input('What project: ')

    if category == "design":
      try:
        path = os.path.join("F:\FORCE\_DESIGN\Projects", name)
        assets = os.path.join(path, "Assets")
        finals = os.path.join(path, "Finals")
        os.mkdir(path)
        os.mkdir(assets)
        os.mkdir(finals)
        subprocess.Popen(r'explorer /select, {}' .format(assets))
        break
      except:
        continue

    elif category == "web":
      try:
        path = os.path.join("F:\FORCE\_CODING\Web\Projects", name)
        images = os.path.join(path, "images")
        styles = os.path.join(path, "styles")
        os.mkdir(path)
        os.mkdir(images)
        os.mkdir(styles)
        os.chdir(path)
        crepo()
        break
      except:
        continue
      
    elif category == "flutter":
      try:
        path = os.path.join("F:\FORCE\_CODING\Flutter\Projects", name)
        images = os.path.join(path, "images")
        fonts = os.path.join(path, "fonts")
        os.mkdir(path)
        os.mkdir(images)
        os.mkdir(fonts)
        os.chdir(path)
        crepo()
        break
      except:
        continue

    elif category == "python":
      try:
        path = os.path.join("F:\FORCE\_CODING\Python\Projetos", name)
        os.mkdir(path)
        os.chdir(path)
        crepo()
        break
      except:
        continue

    elif category == "music":
      try:
        path = os.path.join("F:\FORCE\_MUSIC\Beats", name)
        samples = os.path.join(path, "Samples")
        stems = os.path.join(path, "Stems")
        os.mkdir(path)
        os.mkdir(samples)
        os.mkdir(stems)
        subprocess.Popen(r'explorer /select, {}' .format(samples))
        break
      except:
        continue
    else:
      continue
